# Python 測試 twstock 1

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import twstock
import time

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
print("最新資料")
print(stock.price)
print("日期：", stock.date[-1])
print("開盤價：", stock.open[-1])
print("最高價：", stock.high[-1])
print("最低價：", stock.low[-1])
print("收盤價：", stock.price[-1])

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019, 12)
for s in stocklist:
    print(s.date.strftime("%Y-%m-%d"), end="\t")
    print(s.open, end="\t")
    print(s.high, end="\t")
    print(s.low, end="\t")
    print(s.close)


# 鴻海股票即時交易資訊
real = twstock.realtime.get("2317")
if real["success"]:  # 如果讀取成功
    print("即時股票資料：", real["info"]["name"])
    print("開盤價：", real["realtime"]["open"], end=", ")
    print("最高價：", real["realtime"]["high"], end=", ")
    print("最低價：", real["realtime"]["low"], end=", ")
    print("目前股價：", real["realtime"]["latest_trade_price"])
else:
    print("錯誤：" + real["rtmessage"])


# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019, 12)
listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime("%Y-%m-%d"))
    listy.append(s.close)

plt.figure(figsize=[10, 5])  # 圖像大小[英吋]
plt.title("鴻海2019年12月股價", fontsize=18)
plt.xlabel("日期", fontsize=14)
plt.ylabel("股價", fontsize=14)
plt.plot(listx, listy, "r:s")

plt.xticks(rotation=45)
plt.grid("k:", alpha=0.5)
plt.ylim(88, 93)
plt.yticks([88, 89, 90, 91, 92, 93])

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

plt.show()


companys = ["2330", "2912", "3293"]
plt.figure(figsize=[10, 5])  # 圖像大小[英吋]
for company in companys:
    stock = twstock.Stock(company)
    # 取得 2019 年 12 月的資料
    stocklist = stock.fetch(2019, 12)
    listx = []
    listy = []
    for s in stocklist:
        listx.append(s.date.strftime("%Y-%m-%d"))
        listy.append(s.close)

    plt.plot(listx, listy)
    plt.xticks(rotation=45)
plt.show()


# plt.figure(figsize=[12,30])	#圖像大小[英吋]
stock = twstock.Stock("2317")
slist = []
for i in range(1, 13):
    stocklist = stock.fetch(2019, i)
    [slist.append(s) for s in stocklist]
    #    listx = [s.date.strftime('%d') for s in stocklist]
    #    listy = [s.close for s in stocklist]
    #    plt.subplot('62{}'.format(i))
    #    plt.xticks(rotation=45)
    #    plt.title(label="{}月".format(i))

    #    plt.plot(listx, listy)
    print(len(slist))
    time.sleep(5)
    if i == 6:
        time.sleep(20)

# plt.show()

# lista = []
# list1 = [1,2,3,4,5]
# list2 = [7,8,9,10,11]
# list1.append(list2)
# list1
# %%


# 將資料寫出到csv檔
import csv

# 比較看看
# filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv'

with open("2019_2330.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(slist)

print("------------------------------------------------------------")  # 60個

# twstock 抓取股票資訊做分析

# 導入模組
import matplotlib.pyplot as plt
import twstock

# 股票代碼 stock_code

stock_code = str(2330)
stock = twstock.Stock(stock_code)  # 建立 Stock 物件

# 使用語法：（查詢某年某月的股票資料）
# stock.fetch(year, month)

stocklist1 = stock.fetch(2023, 1)  # 查詢 2023年1月的資料
stocklist2 = stock.fetch(2023, 2)  # 查詢 2023年2月的資料

stocklist = stocklist1 + stocklist2


# 建立 x, y 軸串列，x 軸為日期時間(date)，y 軸為收盤價(close)
# 印出 stock.data[0]，可以觀察到「close」就是收盤價的價位資料

print(stock.data[0])


listx = []
listy = []
for value in stocklist:
    listx.append(value.date.strftime("%Y-%m-%d"))
    listy.append(value.close)

plt.figure(num="股票分析", figsize=(10, 10))  # 設定圖表區寬高

plt.xlabel("日期", fontsize="16")  # 設定 x 軸標題內容及大小
plt.ylabel("股價", fontsize="16")  # 設定 y 軸標題標題內容及大小
plt.title("台積電(2330)", fontsize="18")  # 設定圖表標題內容及大小

plt.plot(listx, listy, color="red", markersize="16", marker=".")  # 紅色，實線，標記大小 16，標記為「點」

plt.xticks(rotation=45)  # 讓 x 坐標軸標題旋轉 45 度, 使得文字不會重疊

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

plt.show()  # 將圖表呈現出來

print("------------------------------------------------------------")  # 60個

import twstock
import pandas as p

stock_code = str(2330)
stock = twstock.realtime.get(stock_code)

# 檢查是不是即時資料 是:顯示True 不是:顯示False
print(stock["success"])

result = p.DataFrame(stock).T.iloc[1:3]
result.columns = [
    "股票代碼",
    "地區",
    "股票名稱",
    "公司全名",
    "現在時間",
    "最新成交價",
    "成交量",
    "累計成交量",
    "最佳5檔賣出價",
    "最佳5檔賣出量",
    "最佳5檔買進價",
    "最佳5檔買進量",
    "開盤價",
    "最高價",
    "最低價",
]
print(result)

print("------------------------------------------------------------")  # 60個

import twstock
import time
import requests

stock = twstock.Stock("2317")  # 鴻海
print("近31個收盤價：")
print(stock.price)  # 近31個收盤價
print("近6個收盤價：")
print(stock.price[-6:])  # 近6日之收盤價

realdata = twstock.realtime.get("2317")  # 即時資料
print(realdata)

if realdata["success"]:
    print("即時股票資料：")
    print(realdata)  # 即時資料
else:
    print("錯誤：" + realdata["rtmessage"])

realprice = realdata["realtime"]["latest_trade_price"]  # 目前股價
if realprice == "-":
    print("找不到資料")
else:
    print("鴻海目前股價：" + realprice)

print("-----------------------------------")

time.sleep(30)  # 等一下

print("每一分鐘抓一次資料")

while True:
    realdata = twstock.realtime.get("2317")  # 即時資料
    print(realdata)
    if realdata["success"]:
        realprice = realdata["realtime"]["latest_trade_price"]  # 目前股價
        if realprice == "-":
            print("找不到資料")
        else:
            print("鴻海目前股價：" + realprice)
        time.sleep(60)  # 每1分鐘讀一次
    else:
        print("twstock 讀取錯誤，錯誤原因：" + realdata["rtmessage"])
        time.sleep(60)  # 每1分鐘讀一次


print("------------------------------------------------------------")  # 60個

import twstock
import time
import requests

import matplotlib.pyplot as plt

from twstock import Stock

tsmc = Stock("2330")
print(tsmc.price)

print("------------------------------------------------------------")  # 60個

from twstock import Stock

tsmc = Stock("2330")
print(tsmc.moving_average(tsmc.price, 5))
print(tsmc.moving_average(tsmc.capacity, 5))

print("------------------------------------------------------------")  # 60個

from twstock import Stock

tsmc = Stock("2330")
data = tsmc.moving_average(tsmc.price, 5)
plt.plot(list(range(len(data))), data)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
