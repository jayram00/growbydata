import driver as driver
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import csv
import json

from selenium.webdriver.remote.webelement import WebElement

driver: WebDriver = webdriver.Chrome(executable_path=r"C:\Users\jayram raut\Desktop\growbydata\chromedriver.exe")
driver.get("https://www.flipkart.com/realme-c11-2021-cool-grey-32-gb/p/itmbd856acb97c38?pid=MOBG4BEGX8QYNKGZ&lid=LSTMOBG4BEGX8QYNKGZ7GS1KS&marketplace=FLIPKART&q=mobiles&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&fm=organic&iid=5374b3ad-31d7-4463-9954-9445c177dfc4.MOBG4BEGX8QYNKGZ.SEARCH&ppt=hp&ppn=homepage&ssid=ibkdsmdtcw0000001652768054218&qH=eb4af0bf07c16429")

title = driver.find_element(by=By.XPATH,value='//h1')

current_price = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')

image = driver.find_element(by=By.XPATH,value='//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img')

product_data = {
	'title': title.text,
	'current_price': current_price.text,
	'image_url': image.get_attribute('src')
}

df = pd.DataFrame.from_dict(product_data)

df.to_csv(r'realme.csv',header=True,index = True)
driver.quit()