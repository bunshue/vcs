# ch7_4_2.py
from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器
print('瀏覽器名稱 = ', browser.name)             # 列印瀏覽器名稱
print('網頁url    = ', browser.current_url)      # 列印網頁url
print('網頁連線id = ', browser.session_id)       # 網頁連線id
print('瀏覽器功能 = \n',browser.capabilities)    # 瀏覽器功能設定訊息



            

