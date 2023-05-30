from selenium import webdriver
import pyautogui as auto
import pandas as pd
import time

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"

driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(60)
driver.get(url)

driver.maximize_window()    #全螢幕顯示

auto.PAUSE = 3
auto.moveTo(1263, 438, 2)
auto.click()
auto.typewrite("2330")
auto.moveTo(1461, 438, 2)
auto.click()
time.sleep(5)
html = driver.page_source

driver.quit()   #關閉瀏覽器並且退出驅動程序

data = pd.read_html(html)
print(data)





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

url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"

driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(60)
driver.get(url)

driver.maximize_window()    #全螢幕顯示

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

driver.quit()   #關閉瀏覽器並且退出驅動程序



