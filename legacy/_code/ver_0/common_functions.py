#%%
import pandas as pd
from datetime import datetime
from datetime import timedelta
from selenium import webdriver

#%% path directory
dir_result = "..\\_result\\"

# %%
def open_sk_encar():
    dir_driver = "..\\_driver\\chromedriver.exe"
    url_sk_encar = (
        "http://www.encar.com/dc/dc_carsearchpop.do?method=soldoutCars&carType=kor"
    )
    driver = webdriver.Chrome(dir_driver)
    driver.get(url_sk_encar)
    return driver


#%%
def click_next_page_list(driver):
    driver.find_element_by_class_name("next").click()


#%%
def get_dates(days=31):
    today = datetime.today()
    today_30 = today - timedelta(days)

    return today_30


#%%
def get_search_condition(df_page, today_30):

    day_to_search = df_page["date"].min()

    search_condition = day_to_search > today_30

    return search_condition

