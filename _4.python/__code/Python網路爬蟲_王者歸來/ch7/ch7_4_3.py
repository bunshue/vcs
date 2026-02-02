# ch7_4_3.py
from selenium import webdriver
import time

urls = ['http://aaa.24ht.com.tw',
        'http://www.mcut.edu.tw',
        'http://www.siliconstone.com']

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)

for url in urls:
    browser.get(url)                # 網頁下載至瀏覽器
    time.sleep(5)

browser.quit()






            

