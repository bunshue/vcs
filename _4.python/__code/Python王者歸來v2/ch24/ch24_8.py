# ch24_8.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.deepmind.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text('深智數位緣起')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 







