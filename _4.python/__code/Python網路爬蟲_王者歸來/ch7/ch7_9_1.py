# ch7_9_1.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.mcut.edu.tw/?Lang=en'
browser.get(url)                    # 網頁下載至瀏覽器

txtBox = browser.find_element_by_name('SchKey')
txtBox.send_keys('王永慶')          # 輸入表單資料
time.sleep(5)                       # 暫停5秒
txtBox.submit()                     # 送出表單









