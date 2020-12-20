import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import item_sold, item_equal

# 오프닝
driver = webdriver.Chrome("driver\\chromedriver")
driver.get("http://www.encar.com/dc/dc_carsearchpop.do?method=soldoutCars&carType=for")
driver.implicitly_wait(3)

# 제조사 필터링
selectorCompany = Select(driver.find_element_by_id("companySearch"))
selectorCompany.select_by_value("012")
driver.implicitly_wait(3)

# 모델 필터링
selectorModel = Select(driver.find_element_by_id("modelgroupSearch"))
selectorModel.select_by_value("011")

# 검색
driver.find_element_by_class_name("sp.search").click()
time.sleep(3)

# 팔린 매물 데이터 프레임 저장


# 동급 매물 탭으로 전환
driver.find_element_by_xpath('//*[@id="tabRival"]/li[1]/a').click()
time.sleep(3)


# driver.close()
