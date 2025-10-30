"""
Python 測試 twstock
pip install twstock
twstock 台灣股市股票價格擷取
https://pypi.org/project/twstock/
"""

import twstock

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import csv
import json
import requests

print("------------------------------------------------------------")  # 60個

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
print(stock.price)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
print("日期：", stock.date[-1])
print("開盤價：", stock.open[-1])
print("最高價：", stock.high[-1])
print("最低價：", stock.low[-1])
print("收盤價：", stock.price[-1])

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
realdata = twstock.realtime.get("2317")
if realdata["success"]:  # 如果讀取成功
    print("即時股票資料：", realdata["info"]["name"])
    print("開盤價：", realdata["realtime"]["open"], end=", ")
    print("最高價：", realdata["realtime"]["high"], end=", ")
    print("最低價：", realdata["realtime"]["low"], end=", ")
    print("目前股價：", realdata["realtime"]["latest_trade_price"])
else:
    print("錯誤：" + realdata["rtmessage"])


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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lista = []
# list1 = [1,2,3,4,5]
# list2 = [7,8,9,10,11]
# list1.append(list2)
# list1

# 將資料寫出到csv檔
# 比較看看
# filename = 'D:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv'

with open("2019_2330.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(slist)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock_code = "2330"
stock = twstock.realtime.get(stock_code)

# 檢查是不是即時資料 是:顯示True 不是:顯示False
print(stock["success"])

result = pd.DataFrame(stock).T.iloc[1:3]
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
print("------------------------------------------------------------")  # 60個

# twstock 抓取股票資訊做分析

# 股票代碼 stock_code

stock_code = "2330"
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
print("------------------------------------------------------------")  # 60個

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
    print("目前股價：")
    print(realdata["realtime"]["latest_trade_price"])  # 即時價格
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

print("------------------------------")  # 30個

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
    print("目前股價：")
    print(realdata["realtime"]["latest_trade_price"])  # 即時價格
else:
    print("錯誤：" + realdata["rtmessage"])


msg = "這是 LINE Notify 發送的訊息。"
token = "你的 LINE ifNoty 權杖"  # 權杖
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded",
}
payload = {"message": msg}
notify = requests.post(
    "https://notify-api.line.me/api/notify", headers=headers, params=payload
)
if notify.status_code == 200:
    print("發送 LINE Notify 成功！")
else:
    print("發送 LINE Notify 失敗！")


def lineNotify(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {"message": msg}
    notify = requests.post(
        "https://notify-api.line.me/api/notify", headers=headers, params=payload
    )
    return notify.status_code


def sendline(mode, realprice, counterLine, token):
    print("鴻海目前股價：" + str(realprice))
    if mode == 1:
        message = "現在鴻海股價為 " + str(realprice) + "元，可以賣出股票了！"
    else:
        message = "現在鴻海股價為 " + str(realprice) + "元，可以買入股票了！"
    code = lineNotify(token, message)
    if code == 200:
        counterLine = counterLine + 1
        print("第 " + str(counterLine) + " 次發送 LINE 訊息。")
    else:
        print("發送 LINE 訊息失敗！")
    return counterLine


token = "你的 LINE ifNoty 權杖"  # 權杖
counterLine = 0  # 儲存發送次數
counterError = 0  # 儲存錯誤次數

print("程式開始執行！")
while True:
    realdata = twstock.realtime.get("2317")  # 即時資料
    if realdata["success"]:
        realprice = realdata["realtime"]["latest_trade_price"]  # 目前股價
        if float(realprice) >= 80:
            counterLine = sendline(1, realprice, counterLine, token)
        elif float(realprice) <= 60:
            counterLine = sendline(2, realprice, counterLine, token)
        if counterLine >= 3:  # 最多發送3次就結束程式
            print("程式結束！")
            break
    else:
        print("twstock 讀取錯誤，錯誤原因：" + realdata["rtmessage"])
        counterError = counterError + 1
        if counterError >= 3:  # 最多錯誤3次
            print("程式結束！")
            break
    for i in range(300):  # 每5分鐘讀一次
        time.sleep(1)

print("------------------------------------------------------------")  # 60個

print("應用：使用LINE監控即時股價")

token = "你的 LINE Notify 權杖"  # 權杖
counterLine = 0  # 儲存發送次數
counterError = 0  # 儲存錯誤次數

print("程式開始執行！")
while True:
    realdata = twstock.realtime.get("2317")  # 即時資料
    if realdata["success"]:
        realprice = realdata["realtime"]["latest_trade_price"]  # 目前股價
        if realprice != "-":
            if float(realprice) >= 40:
                counterLine = sendline(1, realprice, counterLine, token)
            elif float(realprice) <= 20:
                counterLine = sendline(2, realprice, counterLine, token)
            if counterLine >= 3:  # 最多發送3次就結束程式
                print("程式結束！")
                break
    else:
        print("twstock 讀取錯誤，錯誤原因：" + realdata["rtmessage"])
        counterError = counterError + 1
        if counterError >= 3:  # 最多錯誤3次
            print("程式結束！")
            break
    for i in range(300):  # 每5分鐘讀一次
        time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")

print("price :", stock.price)

print(stock.moving_average(stock.price, 5))
print(stock.moving_average(stock.capacity, 5))

realdata = twstock.realtime.get("2330")

data = stock.moving_average(stock.price, 5)

plt.plot(list(range(len(data))), data)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print(twstock.codes["2330"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")
print("股票代號:", stock.sid)
print("各日收盤價:", stock.price)
print("各日最高價:", stock.high)
print("各日最低價:", stock.low)
print("各日成交股數:", stock.capacity)
print("各日的日期:", stock.date)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")
data = stock.fetch(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df[["close", "open", "high", "low"]].plot()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")
data = stock.fetch_from(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df[["close", "open", "high", "low"]].plot()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = twstock.realtime.get("2330")
print(data)
print("----------------------------")
data = twstock.realtime.get(["2330", "2337", "2409"])
print(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")
data = stock.fetch_from(2019, 1)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

df["5_Day_Mean"] = df["close"].rolling(window=5).mean()
df["20_Day_Mean"] = df["close"].rolling(window=20).mean()
df["60_Day_Mean"] = df["close"].rolling(window=60).mean()

df[["5_Day_Mean", "20_Day_Mean", "60_Day_Mean"]].plot(figsize=(10, 5))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock = twstock.Stock("2330")
ma_p = stock.moving_average(stock.price, 5)
print("五日均價:", ma_p)
ma_c = stock.moving_average(stock.capacity, 5)
print("五日均量:", ma_c)
ma_p_cont = stock.continuous(ma_p)
print("五日均價持續天數:", ma_p_cont)
ma_br = stock.ma_bias_ratio(5, 10)
print("五日、十日乖離率:", ma_br)
ma_brp = stock.ma_bias_ratio_pivot(stock.price, 5, True)
print("正乖離率轉折位置:", ma_brp)
ma_brp2 = stock.ma_bias_ratio_pivot(stock.price, 5, False)
print("負乖離率轉折位置:", ma_brp2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from twstock import BestFourPoint

stock = twstock.Stock("2330")
bfp = BestFourPoint(stock)

bfp_buy = bfp.best_four_point_to_buy()
print("是否為四大買點:", bfp_buy)
bfp_sell = bfp.best_four_point_to_sell()
print("是否為四大賣點:", bfp_sell)
bfp_result = bfp.best_four_point()
print("綜合判斷:", bfp_result)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 鴻海股票即時交易資訊
realdata = twstock.realtime.get("2317")
if realdata["success"]:  # 如果讀取成功
    print("即時股票資料：", realdata["info"]["name"])
    print("開盤價：", realdata["realtime"]["open"], end=", ")
    print("最高價：", realdata["realtime"]["high"], end=", ")
    print("最低價：", realdata["realtime"]["low"], end=", ")
    print("目前股價：", realdata["realtime"]["latest_trade_price"])
else:
    print("錯誤：" + realdata["rtmessage"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019, 12)
listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime("%Y-%m-%d"))
    listy.append(s.close)

plt.figure(figsize=[10, 5])
plt.title("鴻海2019年12月股價", fontsize=18)
plt.xlabel("日期", fontsize=14)
plt.ylabel("股價", fontsize=14)
plt.plot(listx, listy, "r:s")
plt.xticks(rotation=45)
plt.grid("k:", alpha=0.5)
plt.ylim(88, 93)
plt.yticks([88, 89, 90, 91, 92, 93])
plt.rcParams["font.sans-serif"] = "mingliu"
# plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
plt.rcParams["axes.unicode_minus"] = False

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# plt.figure(figsize=[12,30])
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
    #    plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
    #    plt.rcParams["axes.unicode_minus"] = False
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

filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(slist)
# %%

print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"

with open(filename, "r", newline="") as f:
    datas = csv.reader(f)
    listx = []
    listy = []
    for data in datas:
        listx.append(data[0])
        listy.append(data[5])

    #    print(len(datas))
    #    print(len(listx), len(listy))
    plt.figure(figsize=(20, 5))
    plt.plot(listx, listy)
    plt.yticks(range(10, 200, 10))
    plt.show()
#    print([x[6] for x in datas])

#    print(type(datas))
# %%
plt.figure(figsize=(20, 5))
plt.plot([x.close for x in slist])
plt.show()

# %%
for data in datas:
    print(data)

# %%
lsit1 = [1, 2, 3, 4]
list1[0]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "tmp_stockyear2017.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from datetime import datetime


def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split("/"))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"


filename = "data/ST43_3479_202310.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for _ in range(5):  # 跳過前 5 列
        next(csv_reader)
    list_data = list(csv_reader)
    data_without_last_row = list_data[:-1]  # 跳過最後一列

    mydates, highPrices, lowPrices, closePrices = [], [], [], []

    for line in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(line[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d")  # 轉換後日期
            highPrice = eval(line[4])  # 設定最高價
            lowPrice = eval(line[5])  # 設定最低價
            closePrice = eval(line[6])  # 設定收盤價
        except Exception:
            print(f"有缺值 {line}")
        else:
            highPrices.append(highPrice)  # 儲存最高價
            lowPrices.append(lowPrice)  # 儲存最低價
            closePrices.append(closePrice)  # 儲存收盤價
            mydates.append(currentDate)  # 儲存日期

fig = plt.figure(figsize=(12, 8))  # 設定繪圖區大小
plt.plot(mydates, highPrices, "-*", label="最高價")  # 繪製最高價
plt.plot(mydates, lowPrices, "-o", label="最低價")  # 繪製最低價
plt.plot(mydates, closePrices, "-^", label="收盤價")  # 繪製收盤價
plt.legend()
fig.autofmt_xdate()  # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel("價格", fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("twstock：台灣股票")

stock = twstock.Stock("2317")
print(stock.price)

print("日期：", stock.date[-1])
print("開盤價：", stock.open[-1])
print("最高價：", stock.high[-1])
print("最低價：", stock.low[-1])
print("收盤價：", stock.price[-1])

stock.fetch(2020, 1)
stock.fetch_31()

stock.fetch_from(2021, 9)
realdata = twstock.realtime.get("2317")
print(realdata)

if realdata["success"]:
    print("股票名稱、即時股票資料：")
    print("股票名稱：", realdata["info"]["name"])
    print("開盤價：", realdata["realtime"]["open"])
    print("最高價：", realdata["realtime"]["high"])
    print("最低價：", realdata["realtime"]["low"])
    print("目前股價：", realdata["realtime"]["latest_trade_price"])
else:
    print("錯誤：" + realdata["rtmessage"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取資料存入資料庫")

import sqlite3

stock_code = "2330"
stock = twstock.Stock(stock_code)
df = pd.DataFrame(stock.fetch_from(2020, 1))
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
print(df.head())
conn = sqlite3.connect("tmp_" + stock_code + ".db")
df.to_sql(stock_code, conn, if_exists="replace")
print("已經將股票資料存入SQLite資料庫...")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# 3030
print("------------------------------")  # 30個
