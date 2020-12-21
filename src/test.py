import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import item_sold, item_equal
import padnas as pd

# 오프닝
driver = webdriver.Chrome("driver\\chromedriver")
driver.get("http://www.encar.com/dc/dc_carsearchpop.do?method=soldoutCars&carType=for")

