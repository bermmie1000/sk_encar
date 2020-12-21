import time
import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import item_sold, item_equal


# 날짜
period = datetime.today() - timedelta(days=60)

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

# 팔린 매물 데이터 프레임 생성
df_upper_item_sold = pd.DataFrame()

isPeriod = True
while isPeriod:

    page_numbers = driver.find_elements_by_xpath(f'//*[@id="tabRival2"]/div/span[2]/a')
    for i in range(0, len(page_numbers)):
        # 다음 페이지 이동
        time.sleep(1)
        driver.find_element_by_xpath(f'//*[@id="tabRival2"]/div/span[2]/a[{str(i+1)}]').click()
        # 크롤링 및 데이터 프레임 저장
        df_lower_item_sold = item_sold.get_list_page(driver)
        df_upper_item_sold = pd.concat([df_upper_item_sold, df_lower_item_sold])

    counting_date = df_lower_item_sold["date"].min()
    isPeriod = counting_date > period

    # 다음 10장으로 이동
    driver.find_element_by_class_name("next").click()

df_upper_item_sold.reset_index(drop=True, inplace=True)
df_upper_item_sold.to_csv("data\\item_sold\\sold_items.csv", index=False, encoding="euc-kr")




#======================================
# # 팔린 매물 데이터 프레임 저장



# # 동급 매물 탭으로 전환
# driver.find_element_by_xpath('//*[@id="tabRival"]/li[1]/a').click()
# time.sleep(3)


# driver.close()
