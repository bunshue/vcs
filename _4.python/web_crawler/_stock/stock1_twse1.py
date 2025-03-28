# Python 測試 twse 1

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

import json
from bs4 import BeautifulSoup

print("------------------------------------------------------------")  # 60個

# 台灣證券交易所，個股日成交資訊
search_date = "20220101"
search_stock = "2330"
url = (
    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="
    + search_date
    + "&stockNo="
    + search_stock
)

# 取得股票資料json字串
html_data = requests.get(url)
# print(html_data.text)

# 從json字串轉為python的字典格式
json_data = json.loads(html_data.text)
datas = json_data["data"]
fields = json_data["fields"]
print(datas)  # 由List組成的二維陣列
print(fields)

# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)

# Pandas匯出
# 轉成csv檔
df.to_csv("./month_stock.csv", encoding="big5")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx", encoding="big5")
# 轉成html檔
df.to_html("./month_stock.html")

# 抓一整年的資料 2022年
year_df = pd.DataFrame()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
search_year = "2022"
search_stock = "2330"
# url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+search_date+'&stockNo='+search_stock

# 從1到12月
for m in range(1, 13):
    print(m)
    url = (
        "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="
        + search_year
        + "{0:02d}01&stockNo="
        + search_stock
    ).format(m)
    print(url)

    # 取得股票資料json字串
    html_data = requests.get(url, headers=headers)
    # print(html_data.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(html_data.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    # 存成Pandas的Dataframe
    month_df = pd.DataFrame(datas, columns=fields)
    # print(month_df)

    # 合併於整年的Dataframe
    year_df = year_df.append(month_df, ignore_index=True)

# print(year_df)
# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")

print("------------------------------------------------------------")  # 60個

# 讀取csv
df = pd.read_csv("./month_stock.csv", encoding="big5")
# print(df)

"""
# 讀取excel
df2 = pd.read_excel("./month_stock.xlsx")
print(df2)

# 讀取html
df3 = pd.read_html("./month_stock.html", encoding="utf8")
print(df3)
"""

# 使用 Matplotlib 畫圖

# 篩選我們要的資料
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# 繪圖
# plt.plot(date, high_price)
# plt.plot(date, low_price)
# plt.plot(date, end_price)

plt.plot(date, high_price, color="#ff2121")
plt.plot(date, low_price, color="#00bd42", linewidth=5)
plt.plot(date, end_price, color="#005de0", linestyle="dashed")

"""
plt.xlabel("日期")    # x軸標籤
plt.ylabel("價格")    # y軸標籤
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("110年8月股市趨勢圖")    # 主標題
"""
plt.grid(True)  # 是否有網格?

# 存成圖片, 要放在show()之前
# plt.savefig("matplotlib_chart.png")

# 顯示圖片
plt.show()

# 使用 Pandas 畫圖

# 篩選我們要的資料
chart_df = df[["日期", "最高價", "最低價", "收盤價"]]
# 將日期設為x軸
chart_df.set_index("日期", inplace=True)
print(chart_df)


# 繪圖
chart = chart_df.plot(xlabel="日期", ylabel="價格", title="110年8月股市趨勢圖", legend=True)
# chart = chart_df.plot(xlabel="日期", ylabel="價格", title="109年股市趨勢圖", legend=True)
plt.grid()


# 存成圖片, 要放在show()之前
# plt.savefig("pandas_chart.png")
# 顯示圖片

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

plt.show()

print("------------------------------------------------------------")  # 60個

# 4.5 台灣證券交易所API
# 這個API長得大概像這樣:
# http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20160501&stockNo=2330
# 比較重要的地方是date這個參數, 基本上你給的值一定要是yyyyMMdd的形式, 但是真正作用的只有yyyy與MM, 因為他會把這段request解讀成你想要看stockNo股票在yyyy年MM月的紀錄, 所以dd基本上沒有太大意義, 但卻是不可少的部分.
import time

TWSE_URL = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json"


def get_web_content(search_stock, current_date):
    resp = requests.get(TWSE_URL + "&date=" + current_date + "&stockNo=" + search_stock)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()


def get_data(search_stock, current_date):
    info = list()
    resp = get_web_content(search_stock, current_date)
    if resp is None:
        return None
    else:
        if resp["data"]:
            for data in resp["data"]:
                record = {
                    "日期": data[0],
                    "開盤價": data[3],
                    "收盤價": data[6],
                    "成交筆數": data[8],
                }
                info.append(record)
        return info


def get_stock_data_twse(search_stock):
    current_date = time.strftime("%Y%m%d")
    current_year = time.strftime("%Y")
    current_month = time.strftime("%m")
    print("Processing data for %s %s..." % (current_year, current_month))
    get_data(search_stock, current_date)
    collected_info = get_data(search_stock, current_date)
    for info in collected_info:
        print(info)


search_stock = "2330"
get_stock_data_twse(search_stock)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
