#%%
import pandas as pd

import common_functions as comm
import sold_item as sold
import equivalent_item as equal

#%%
# 팔린 매물 부분

today_30 = comm.get_dates(2)
driver = comm.open_sk_encar()

#%%
df_sold_main = pd.DataFrame()

search_condition = True
while search_condition:

    page_numbers = driver.find_elements_by_xpath(f'//*[@id="tabRival2"]/div/span[2]/a')

    for i in range(0, len(page_numbers)):
        driver.find_element_by_xpath(
            f'//*[@id="tabRival2"]/div/span[2]/a[{str(i+1)}]'
        ).click()

        df_sold = sold.get_list_page(driver)

        df_sold_main = pd.concat([df_sold_main, df_sold])

        search_condition = comm.get_search_condition(df_sold, today_30)

    df_sold_main.reset_index(drop=True, inplace=True)

    comm.click_next_page_list(driver)


#%%
# 동급 매물 부분

today_30 = comm.get_dates(2)
driver = comm.open_sk_encar()
equal.click_tab_equivalent_item(driver)
#%%
df_equal_main = pd.DataFrame()

search_condition = True
while search_condition:

    page_numbers = driver.find_elements_by_xpath(f'//*[@id="page_list"]/span')

    for i in range(0, len(page_numbers[:-2])):

        driver.find_element_by_xpath(f'//*[@id="page_list"]/span[{str(i+1)}]').click()

        df_equal = equal.get_list_page(driver)

        df_equal_main = pd.concat([df_equal_main, df_equal])

        search_condition = comm.get_search_condition(df_equal, today_30)

    df_equal_main.reset_index(drop=True, inplace=True)

    comm.click_next_page_list(driver)


# %%
