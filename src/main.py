import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def main():
    driver = set_webdriver()
    get_web(driver)
    select_manufacturer(driver)
    click_search(driver)
    table = crwal_sold_info(driver)
    move_next_page(driver)
    # parse_text(table)
    time.sleep(10)


def set_webdriver():
    driver = webdriver.Chrome("driver/chromedriver")
    return driver


def get_web(driver):
    url = "http://www.encar.com/dc/dc_carsearchpop.do?method=soldoutCars&carType=for"
    driver.get(url)
    driver.implicitly_wait(3)


def select_manufacturer(driver):
    selected_manufacturer = Select(driver.find_element_by_id("companySearch"))
    selected_manufacturer.select_by_value("013")  # 벤츠


def click_search(driver):
    driver.find_element_by_class_name("sp.search").click()
    driver.implicitly_wait(3)


def crwal_sold_info(driver):
    table = driver.find_element_by_class_name("list.car_list").text
    return table


def move_next_page(driver):
    current_page = driver.find_element_by_class_name("current").text
    # next_page =
    # TODO: 이거 완성하기, 받아 오는 정보는 세달이 적당할 듯함
    # TODO: 가격과 판매 신고 가격의 차이점이 뭔지 물어보기


def parse_text(text):
    lines = text.splitlines()
    lines = lines[1:]

    for line in lines:
        front = line.split(" ")[:-6]
        # end = line.split("km")[1]
        # print(front)
        # print(end)
    # while True:
    #     line = text.readline()

    #     if not line:
    #         break
    #     else:
    #         front = line.split("km")[0]
    #         end = line.split("km")[1]
    #         print(front)
    #         print(end)


if __name__ == "__main__":
    main()
