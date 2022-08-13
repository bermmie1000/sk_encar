import time
import io
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def main():
    driver = set_webdriver()
    get_web(driver)
    select_manufacturer(driver)

    appended = ""
    for _ in range(25):
        sold_info = crwal_sold_info(driver)
        appended = append_sold_info(appended, sold_info)
        move_next_page(driver)

    sold_info = crwal_sold_info(driver)
    appended = append_sold_info(appended, sold_info)

    dataset = parse_text(appended)
    dataset = preprocess(dataset)
    plot_sales(dataset)

    driver.close()


def set_webdriver():
    driver = webdriver.Chrome("driver/chromedriver")
    return driver


def get_web(driver):
    url = "http://www.encar.com/dc/dc_carsearchpop.do?method=soldoutCars&carType=for"
    driver.get(url)
    driver.implicitly_wait(10)


def select_manufacturer(driver):
    selected_manufacturer = Select(driver.find_element_by_id("companySearch"))
    selected_manufacturer.select_by_value("013")  # 벤츠
    __click_search(driver)


def __click_search(driver):
    driver.find_element_by_class_name("sp.search").click()
    driver.implicitly_wait(10)


def crwal_sold_info(driver):
    sold_info = driver.find_element_by_class_name("list.car_list").text
    return sold_info


def append_sold_info(table, sold_info):
    appended = "\n".join([table, sold_info])
    return appended


def move_next_page(driver):
    current_page = driver.find_element_by_class_name("current").text
    current_page = int(current_page)
    rescaled = current_page % 10
    next_page = rescaled + 1

    if rescaled == 0:
        __next_page_list(driver)
    else:
        __next_page(driver, next_page)


def __next_page_list(driver):
    driver.find_element_by_class_name("next").click()
    driver.implicitly_wait(10)


def __next_page(driver, next_page: int):
    driver.find_element_by_xpath(
        f'//*[@id="tabRival2"]/div/span[2]/a[{next_page}]'
    ).click()
    driver.implicitly_wait(10)


def __convert_text(table):
    liner = io.StringIO(table)
    return liner


def parse_text(table):
    liner = __convert_text(table)

    name = []
    info = []

    for line in liner.readlines():
        if "차량정보" not in line:
            line = line.strip()
            vehicle_name = line.split(" ")[:-6]
            vehicle_info = line.split(" ")[-6:]

            name.append(vehicle_name)
            info.append(vehicle_info)

    dataset = pd.DataFrame(data={"name": name, "info": info})

    return dataset


def preprocess(dataset):
    dataset["name"] = dataset["name"].apply(lambda x: " ".join(x[:]))
    dataset["info"] = dataset["info"].apply(lambda x: " ".join(x[:]))
    dataset.replace("", np.nan, inplace=True)
    dataset.dropna(axis=0, inplace=True)
    dataset.reset_index(drop=True, inplace=True)

    dataset = pd.concat(
        [dataset["name"], dataset["info"].str.split(" ", expand=True)], axis=1
    )
    dataset.columns = ["name", "year", "distance", "price", "_", "_", "date"]
    dataset.drop(columns={"_"}, inplace=True)

    # dataset["date"] = pd.to_datetime(dataset["date"], format="%Y/%m/%d")
    dataset.sort_values(by=["date"], inplace=True)

    dataset["distance"].replace(",", "", regex=True, inplace=True)
    dataset["distance"].replace("km", "", regex=True, inplace=True)
    dataset["distance"] = dataset["distance"].astype(int)

    dataset["price"].replace(",", "", regex=True, inplace=True)
    dataset["price"].replace("만원", "", regex=True, inplace=True)
    dataset["price"] = dataset["price"].astype(int)

    return dataset


def plot_sales(dataset):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataset["date"], y=dataset["price"], mode="markers"))
    fig.show()


if __name__ == "__main__":
    main()
