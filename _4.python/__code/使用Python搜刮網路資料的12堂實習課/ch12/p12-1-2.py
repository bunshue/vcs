from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"

driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(60)
driver.get(url)

driver.maximize_window()    #���ù����

auto.PAUSE = 3
auto.moveTo(1263, 438, 2)
auto.click()
auto.typewrite("2330")
auto.moveTo(1461, 438, 2)
auto.click()
time.sleep(5)
html = driver.page_source

driver.quit()   #�����s�����åB�h�X�X�ʵ{��

data = pd.read_html(html)
print(data)

