import re

from selenium import webdriver
from selenium.webdriver.common.by import By

import json
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')

driver.get("file:///C:/Users/jayram%20raut/Desktop/task%201/jayram/6.html")

table_head = driver.find_element(by=By.TAG_NAME, value='thead').text

titles = re.split('(?=[A-Z])',table_head)

# seller_names = driver.find_element(by=By.CLASS_NAME, value='b5ycib shntl').text

# details = driver.find_element(by=By.CLASS_NAME, value='SH30Lb yGibJf').text

item_prices = driver.find_element(by=By.TAG_NAME,value='span').text

# total_prices = driver.find_element(by=By.CLASS_NAME,value='drzWO')

print(titles)
# print(seller_names)
# print(details)
print(item_prices)
# print(total_prices)

# body = (driver.find_element(by=By.ID, value='sh-osd__online-sellers-cont')).text

# body1 = body.list(body)


df = pd.DataFrame(columns=[table_head, body])



# df_split = df.to_csv('1.csv')

# print(df)

# print(type(body))
print(titles)

# print(seller.text)

# print(body)
driver.close()
