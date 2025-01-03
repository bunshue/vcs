# Python 測試 yfinance

# pip install yfinance

import yfinance as yf

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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

# df = yf.Ticker('TSLA')                   # 美股 Tesla
df = yf.Ticker("0005.HK").history(period="10y")

df = df.filter(["Close"])
df = df.rename(columns={"Close": "GT"})

# plt.style.use("seaborn-darkgrid")
plt.xlabel("Date")
plt.ylabel("Price")
plt.plot(df["GT"], linewidth=1)

plt.show()

print("------------------------------------------------------------")  # 60個

print(type(yf.Ticker))
# <class 'type'>
tsla = yf.Ticker("TSLA")  # 美股 Tesla
print(type(tsla))
# <class 'yfinance.ticker.Ticker'>
tw2330 = yf.Ticker("2330.TW")  # 台積電
print(type(tw2330))
# <class 'yfinance.ticker.Ticker'>

print("------------------------------------------------------------")  # 60個

tw2330 = yf.Ticker("2330.TW")
tsla = yf.Ticker("TSLA")

# print(tw2330.info)
print(tsla.get_info())

print("------------------------------------------------------------")  # 60個

pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data, wb
import pandas_datareader.data as web

yf.pdr_override()

# 蘋果股票 AAPL
# 台積電 2330.TW
# 中國銀行 601988.SS
# 恆生銀行 0011.HK

df = web.get_data_yahoo("AAPL", start="2018-01-01", end="2018-12-02")  # 下載股價
print(df.head())

print("------------------------------------------------------------")  # 60個

# 讀入台積電的股價，比如我們想看 2021-2022 這兩年的股價。
df = yf.download("2330.TW", start="2021-01-01", end="2022-12-31")

print("最高最低點、開盤收盤價、調整收盤價以及成交量的資訊")
print(df.head())

print("只取調整收盤價")

P = df["Adj Close"]
print(P.head())


P.plot()

plt.show()


# 我們看一下大家最關心的報酬率，報酬率公式：(Pt−Pt−1)/Pt−1

r = P.diff() / P
r.plot()
plt.show()

print("最後一百筆資料")

r[-100:].plot()

plt.show()


# 原本股價圖波動的很厲害，現在我們想讓它變得平滑一點，改看每 20 天的平均

print(P.rolling(window=20).mean())

P.rolling(window=20).mean().plot()
plt.show()


# 和原本的股價圖比較

P.plot()
P.rolling(window=20).mean().plot()
plt.show()


# 當然也可以算更多天的平均，會變得更平滑

P.plot()
P.rolling(window=20).mean().plot()
P.rolling(window=60).mean().plot()
plt.show()

print("------------------------------------------------------------")  # 60個

df = yf.download("2330.TW")
print(df.shape)
print(df.head())

print("------------------------------------------------------------")  # 60個

import datetime

# 開始時間 為 60天前
start = datetime.datetime.now() - datetime.timedelta(days=60)

# 結束時間 為 現在
end = datetime.date.today()
df = yf.download("2330.TW", start, end)
print(df.shape)
print(df.head())

print("------------------------------------------------------------")  # 60個

apple = yf.Ticker("AAPL")  # 建立Apple物件
print("Apple公司財務報表")
financials = apple.financials  # 獲取財務報表
print(financials)
quarterly_financials = apple.quarterly_financials  # 獲取季度財務報表
print(quarterly_financials)

tsmc = yf.Ticker("2330.TW")  # 建立Apple物件
print("台積電財務報表")
financials = tsmc.financials  # 獲取財務報表
print(financials)
quarterly_financials = tsmc.quarterly_financials  # 獲取季度財務報表
print(quarterly_financials)

print("------------------------------------------------------------")  # 60個


def fetch_apple_stock_price():
    # 獲取Apple股票資料
    apple = yf.Ticker("AAPL")

    # 獲取即時股價
    apple_stock_info = apple.history(period="1d")

    # 輸出股價
    print("Apple公司的股價(目前或最近交易日) : ")
    print("開盤價：", apple_stock_info["Open"].iloc[0])
    print("收盤價：", apple_stock_info["Close"].iloc[0])
    print("最高價：", apple_stock_info["High"].iloc[0])
    print("最低價：", apple_stock_info["Low"].iloc[0])
    print("交易量：", apple_stock_info["Volume"].iloc[0])


fetch_apple_stock_price()

print("------------------------------------------------------------")  # 60個

# 下載蘋果公司最近三個月的股價數據
apple = yf.Ticker("AAPL")
data = apple.history(period="3mo")

# 計算5天和20天移動平均線
data["MA5"] = data["Close"].rolling(window=5).mean()
data["MA20"] = data["Close"].rolling(window=20).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data["Close"], label="AAPL Close", color="blue")
plt.plot(data["MA5"], label="5-Day MA", color="green")
plt.plot(data["MA20"], label="20-Day MA", color="red")

# 標題和圖例
plt.title("Apple公司股價 5 日和 20 日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()

# 顯示圖表
plt.show()

print("------------------------------------------------------------")  # 60個

# 下載台積電最近三個月的股價數據
tsmc = yf.Ticker("2330.TW")
data = tsmc.history(period="1y")

# 計算5日和20日的簡單移動平均
data["SMA5"] = data["Close"].rolling(window=5).mean()
data["SMA20"] = data["Close"].rolling(window=20).mean()

# 繪製收盤價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data["Close"], label="Close Price", alpha=0.5)
plt.plot(data["SMA5"], label="5-Day SMA", alpha=0.8)
plt.plot(data["SMA20"], label="20-Day SMA", alpha=0.8)
plt.title("台積電股價 5 日和 20 日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()
plt.grid(True)
plt.show()

# 移動平均生成交易信號
# 買入信號: 5日均線從下方突破20日均線
# 賣出信號: 5日均線從上方跌破20日均線
data["Signal"] = 0.0
data.iloc[5:, data.columns.get_loc("Signal")] = np.where(
    data["SMA5"].iloc[5:] > data["SMA20"].iloc[5:], 1.0, 0.0
)
data["Signal_change"] = data["Signal"].diff()

# 找出買入和賣出的日期
buy_dates = data[data["Signal_change"] == 1].index
sell_dates = data[data["Signal_change"] == -1].index

print(f"買入日期: {buy_dates.tolist()}")
print(f"賣出日期: {sell_dates.tolist()}")

print("------------------------------------------------------------")  # 60個

# 下載蘋果公司最近 6 個月的股價數據
tsm = yf.Ticker("TSM")
data = tsm.history(period="6mo")

# 計算5天, 20天和60天移動平均線
data["MA5"] = data["Close"].rolling(window=5).mean()
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA60"] = data["Close"].rolling(window=60).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data["Close"], label="TSMC Close", color="blue")
plt.plot(data["MA5"], label="5-Day MA", color="green")
plt.plot(data["MA20"], label="20-Day MA", color="red")
plt.plot(data["MA60"], label="60-Day MA", color="magenta")

# 標題和圖例
plt.title("台積電美國股價 5 日, 20 日和 60日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()

# 顯示圖表
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
