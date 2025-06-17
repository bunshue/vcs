import sys

print("------------------------------------------------------------")  # 60個

import twstock

stock = twstock.Stock("2330")
cc = stock.price
print("price")
print(cc)

real = twstock.realtime.get("2330")

print("------------------------------------------------------------")  # 60個

import twstock

stock = twstock.Stock("2317")  # 鴻海
print("近31個收盤價：")
print(stock.price)  # 近31個收盤價
print("近6個收盤價：")
print(stock.price[-6:])  # 近6日之收盤價

real = twstock.realtime.get("2317")
if real["success"]:
    print("即時股票資料：")
    print(real)  # 即時資料
    print("目前股價：")
    print(real["realtime"]["latest_trade_price"])  # 即時價格
else:
    print("錯誤：" + real["rtmessage"])

print("------------------------------------------------------------")  # 60個

import twstock

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
print(stock.price)

print("------------------------------------------------------------")  # 60個

import twstock

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock("2317")
print("日期：", stock.date[-1])
print("開盤價：", stock.open[-1])
print("最高價：", stock.high[-1])
print("最低價：", stock.low[-1])
print("收盤價：", stock.price[-1])

print("------------------------------------------------------------")  # 60個

import twstock

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

print("------------------------------------------------------------")  # 60個

import twstock

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

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import twstock

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

import matplotlib.pyplot as plt
import twstock

companys = ["2330", "2912", "3293"]
plt.figure(figsize=[10, 5])
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

import matplotlib.pyplot as plt
import twstock
import time

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

import csv

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(slist)
# %%

import matplotlib.pyplot as plt
import csv

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"
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


import twstock
import time
import requests


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

import twstock

print(twstock.codes["2330"])

print("------------------------------------------------------------")  # 60個

import twstock

stock = twstock.Stock("2330")
print("股票代號:", stock.sid)
print("各日收盤價:", stock.price)
print("各日最高價:", stock.high)
print("各日最低價:", stock.low)
print("各日成交股數:", stock.capacity)
print("各日的日期:", stock.date)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twstock

stock = twstock.Stock("2330")
data = stock.fetch(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df[["close", "open", "high", "low"]].plot()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twstock

stock = twstock.Stock("2330")
data = stock.fetch_from(2020, 7)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
df[["close", "open", "high", "low"]].plot()

print("------------------------------------------------------------")  # 60個

import twstock

data = twstock.realtime.get("2330")
print(data)
print("----------------------------")
data = twstock.realtime.get(["2330", "2337", "2409"])
print(data)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twstock

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

import twstock

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

import twstock
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

# twstock1.py
import twstock

stock = twstock.Stock("2317")  # 鴻海
print("近31個收盤價：")
print(stock.price)  # 近31個收盤價
print("近6個收盤價：")
print(stock.price[-6:])  # 近6日之收盤價

real = twstock.realtime.get("2317")
if real["success"]:
    print("即時股票資料：")
    print(real)  # 即時資料
    print("目前股價：")
    print(real["realtime"]["latest_trade_price"])  # 即時價格
else:
    print("錯誤：" + real["rtmessage"])

# linenotify.py
import requests

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


# linestock.py
import twstock
import time
import requests


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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
