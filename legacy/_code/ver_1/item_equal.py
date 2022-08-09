import pandas as pd
from datetime import datetime


def get_list_model(driver):
    list_model = driver.find_elements_by_class_name("mod")

    ser_model = pd.Series()
    for model in list_model:
        ser_model = ser_model.append(pd.Series(model.text))

    ser_model = ser_model[2:]
    ser_model.reset_index(drop=True, inplace=True)

    return ser_model


def get_list_year(driver):
    list_year = driver.find_elements_by_class_name("yer")

    ser_year = pd.Series()
    for year in list_year:
        ser_year = ser_year.append(pd.Series(year.text))

    ser_year.reset_index(drop=True, inplace=True)

    return ser_year


def get_list_distance(driver):
    list_distance = driver.find_elements_by_class_name("dts")

    ser_distance = pd.Series()
    for distance in list_distance:
        ser_distance = ser_distance.append(pd.Series(distance.text))

    ser_distance = ser_distance[1:]
    ser_distance.reset_index(drop=True, inplace=True)

    return ser_distance


def get_list_price(driver):
    list_price = driver.find_elements_by_class_name("prc")

    ser_price = pd.Series()
    for price in list_price:
        ser_price = ser_price.append(pd.Series(price.text))

    ser_price = ser_price[2::2]
    ser_price.reset_index(drop=True, inplace=True)

    return ser_price


def get_list_date(driver):
    list_date = driver.find_elements_by_class_name("fdt.end")

    ser_date = pd.Series()
    for date in list_date:
        ser_date = ser_date.append(pd.Series(date.text))

    ser_date.reset_index(drop=True, inplace=True)
    ser_date = pd.to_datetime(ser_date, format="%m/%d")
    ser_date = ser_date.apply(lambda x: x.replace(year=datetime.today().year))

    return ser_date


def get_list_page(driver):

    ser_model = get_list_model(driver)
    ser_year = get_list_year(driver)
    ser_distance = get_list_distance(driver)
    ser_price = get_list_price(driver)
    ser_date = get_list_date(driver)

    df_page = pd.DataFrame()
    df_page["model"] = ser_model
    df_page["year"] = ser_year
    df_page["distance"] = ser_distance
    df_page["price"] = ser_price
    df_page["date"] = ser_date
    df_page["condition"] = "equal"

    return df_page
