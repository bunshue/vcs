# ch7_10.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.mcut.edu.tw'
browser.get(url)                    # 網頁下載至瀏覽器

ele = browser.find_element_by_tag_name('body')
time.sleep(3)
ele.send_keys(Keys.PAGE_DOWN)       # 網頁捲動到下一頁
time.sleep(3)
ele.send_keys(Keys.END)             # 網頁捲動到最底端
time.sleep(3)
ele.send_keys(Keys.PAGE_UP)         # 網頁捲動到上一頁
time.sleep(3)
ele.send_keys(Keys.HOME)            # 網頁捲動到最上端








