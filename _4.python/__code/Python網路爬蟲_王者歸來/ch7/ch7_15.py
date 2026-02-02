# ch7_15.py
from selenium import webdriver
import time

url = 'https://www.google.com'
email = input('請輸入你的Google Email的帳號 : ')
pwd = input('請輸入你的Google Email的密碼 : ')

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)                    # 網頁下載至瀏覽器

browser.find_element_by_id('gb_70').click()                 # 按登入鈕
browser.find_element_by_id('identifierId').send_keys(email) # 輸入帳號
time.sleep(3)

# 按繼續鈕
browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
browser.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)
















