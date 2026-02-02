# ch7_12.py
from selenium import webdriver
import time

url = 'https://www.google.com'
email = input('請輸入你的Google Email的帳號 : ')
pwd = input('請輸入你的Google Email的密碼 : ')

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
browser.get(url)                    # 網頁下載至瀏覽器

browser.find_element_by_id('gb_70').click()











