"""
查詢歷史資料 範例
https://rate.bot.com.tw/xrt/all/2023-03-20

"""

import requests
from bs4 import BeautifulSoup


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("查詢中央銀行匯率")

url = "https://rate.bot.com.tw/xrt/all/day"
# https://rate.bot.com.tw/xrt?Lang=zh-TW  另一個網址
html_data = get_html_data1(url)

soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())  # prettify()這個函數可以將DOM tree以比較美觀的方式印出。

# print('多重條件選擇')
cells = soup.select("table tr td")  # 尋找talbe標籤裡面的tr標籤裡面的td標籤 三者都要符合的抓出來
print(type(cells))
print("符合條件的資料", len(cells), "筆")
print(cells)
print("--------------------------------------------------------")
i = 0
for cell in cells:
    print(i)
    print(cell.text.strip())
    i = i + 1

print("--------------------------------------------------------")

print("顯示 幣別")
print("多重條件選擇")
dnames = soup.select("table tr td[data-table=幣別] div.visible-phone")
# print(type(dnames))
print("符合條件的資料", len(dnames), "筆")
# print(dnames)
names = list()
for dname in dnames:
    names.append(dname.text.strip())
print(names)

print("--------------------------------------------------------")

print("顯示 本行即期買入")
print("多重條件選擇")
buyingrate = soup.select("table tr td[data-table=本行即期買入]")
print(type(buyingrate))
print("符合條件的資料", len(buyingrate), "筆")
print(buyingrate)
i = 0
for price in buyingrate:
    print(i)
    print(price.text.strip())
    i = i + 1

print("--------------------------------------------------------")

prices = list()
for price in buyingrate:
    prices.append(price.text.strip())
print(prices)

print("--------------------------------------------------------")

print(names)
print(prices)
rates = zip(names, prices)
for rate in rates:
    print(rate)

print("--------------------------------------------------------")
