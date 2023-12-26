# ch24_6.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.google.com'
browser.get(url)                        # 網頁下載至瀏覽器

txtBox = browser.find_element_by_name('q')
txtBox.send_keys('明志科技大學')        # 輸入表單資料
time.sleep(5)                           # 暫停5秒
txtBox.submit()                         # 送出表單









