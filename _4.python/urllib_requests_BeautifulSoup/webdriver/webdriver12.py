#PyAutoGUI，自動控制滑鼠與鍵盤

# 有問題

from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

import sys

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

#台灣證券交易所
url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
driver.get(url)
time.sleep(3)

auto.PAUSE = 3
auto.moveTo(1263, 438, 2)
auto.click()
auto.typewrite("2330")
auto.moveTo(1461, 438, 2)
auto.click()
time.sleep(5)

html = driver.page_source

data = pd.read_html(html)
print(data)

print('完成')
sys.exit()

from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

stocks = [
    {
        "name": "聯電",
        "id": "2303"
    },
    {
        "name": "台積電",
        "id": "2330"
    },
    {
        "name": "華碩",
        "id": "2357"
    }
]

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

#台灣證券交易所
url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
driver.get(url)

auto.PAUSE = 3
for stock in stocks:
    auto.moveTo(1263, 438, 2)
    auto.doubleClick()
    auto.typewrite(stock["id"])
    auto.moveTo(1461, 438, 2)
    auto.click()
    time.sleep(5)
    html = driver.page_source
    data = pd.read_html(html)
    print(stock["name"])
    print(data[0])


print('----------------------------------------------------------------------')	#70個
print('完成')

'''
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
'''


