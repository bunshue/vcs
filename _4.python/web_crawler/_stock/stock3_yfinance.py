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
import datetime
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

df = pd.read_csv("data/alphabet_stock_data.csv")
start_date = pd.to_datetime("2020-4-1")
end_date = pd.to_datetime("2020-9-30")
df["Date"] = pd.to_datetime(df["Date"])
new_df = (df["Date"] >= start_date) & (df["Date"] <= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index("Date")
stock_data.plot(subplots=True, figsize=(8, 8))
plt.legend(loc="best")
plt.suptitle(
    "Open,High,Low,Close,Adj Close prices & Volume of Alphabet Inc., From 01-04-2020 to 30-09-2020",
    fontsize=12,
    color="black",
)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
# Yahoo Finance API抓取資料，FinRL特徵工程
https://ithelp.ithome.com.tw/m/articles/10353034


使用 yfinance 抓取 S&P 500 的 15 分鐘資料
下面是一個具體範例，從 Yahoo Finance 下載 S&P 500 指數在指定兩天內的每 15 分鐘的歷史資料。
這些數據將包括開盤價（Open）、最高價（High）、最低價（Low）、收盤價（Close）、調整後的收盤價（Adj Close）以及成交量（Volume）。

start_date 和 end_date: 我們選擇了 2 天的日期範圍，這適合使用 15m 這樣的高頻資料。
interval: 15m 代表每 15 分鐘抓取一次資料，適合短期交易分析。
intervals 參數
參考yf.download的定義註解
Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days
"""

# 設定參數
start_date = "2025-02-12"  # 設定開始日期
end_date = "2025-02-13"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘

# 抓取 S&P 500 數據
ticker = "^GSPC"  # Yahoo Finance 中 S&P 500 的代號
sp500_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

# 顯示數據
print(sp500_data.head())

print("------------------------------")  # 30個

# 使用 yfinance 一次抓取多隻股票的資料

# 設定參數
start_date = "2025-02-12"  # 設定開始日期
end_date = "2025-02-13"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘

# 設定多支股票的代號
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # 股票代號

# 抓取多支股票的數據
data = yf.download(
    tickers, start=start_date, end=end_date, interval=interval, group_by="ticker"
)

# 顯示數據
for ticker in tickers:
    print(f"--- {ticker} ---")
    print(data[ticker].head())
    print("\n")

print("------------------------------")  # 30個

"""
使用 FinRL 進行特徵工程
股市中有很多常見的指標，這些技術指標像是移動平均收斂散度（MACD）、相對強弱指數（RSI）等等。因為很多人使用這些指標，導致股票的波動很多時候會對這些指標有反應，因此在訓練時，可以考慮將這些指標做為特徵丟給網路當作輸入；這邊使用FinRL的API可以很輕鬆地取得這些指標數值來做特徵工程。

步驟 1: 做特徵工程前對，數據格式做預處理
在應用特徵工程之前，我們需要對數據進行一些預處理步驟，包括添加必要的欄位並將欄位名稱轉換為小寫，以符合 FeatureEngineer 的預期格式。

在進行特徵工程之前，我們需要確保數據框包含 date 和 tic 欄位。date 欄位用來表示時間戳，而 tic 欄位用來表示股票的代號。
"""
# 添加必要的欄位
sp500_data = sp500_data.reset_index()  # 重設索引，將日期移到普通欄位
sp500_data["date"] = sp500_data["Datetime"]  # 添加 'date' 欄位
sp500_data["tic"] = "^GSPC"  # 添加 'tic' 欄位，這裡 '^GSPC' 是 S&P 500 的代號

# 移除原本的 'Datetime' 欄位
sp500_data = sp500_data.drop(columns=["Datetime"])

# 將所有欄位名稱轉為小寫，以符合 FeatureEngineer 的預期格式
sp500_data.columns = [col.lower() for col in sp500_data.columns]

# 顯示處理後的數據
print(sp500_data.head())

print("------------------------------")  # 30個

"""
步驟 2: 使用 FeatureEngineer 進行特徵工程
現在我們可以使用 FeatureEngineer 來添加技術指標並進行特徵工程。
"""

# 先安裝 finrl
# gymnasium
# stable_baselines3
from finrl.meta.preprocessor.preprocessors import FeatureEngineer

# 定義我們要使用的技術指標
INDICATORS = ["macd", "rsi", "cci", "dx"]

# 初始化 FeatureEngineer
fe = FeatureEngineer(use_technical_indicator=True, tech_indicator_list=INDICATORS)

# 將技術指標應用於 S&P 500 的數據
sp500_data_with_indicators = fe.preprocess_data(sp500_data)

# 顯示結果
print(sp500_data_with_indicators.head())

"""
特徵工程的輸出
經過特徵工程處理後，我們的數據集將包含原始的 OHLCV 資料以及計算出的技術指標。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

# 下載每日股價

df_quote = yf.download("1101.TW", start="2020-01-01", end="2022-11-30")
df_quote.tail()

print("轉換為月頻率")

df_quote_new = df_quote.resample("ME").mean()
print(df_quote_new)

print("讀取月營收資料")

df_monthly_sales = pd.read_csv("./data/stock_monthly_sales.csv")
cc = df_monthly_sales.head()
print(cc)

print("轉換日期格式")

df_quote_new = df_quote.reset_index()
df_quote_new.Date = df_quote_new.Date
df_quote_new.Date = df_quote_new.Date.map(lambda x: str(x)[:4] + str(x)[5:7])
print(df_quote_new)

print("合併2個表格")

# 轉換日期資料型態，讓2個表格的日期資料型態一致
df_monthly_sales["年月"] = df_monthly_sales["年月"].astype("str")

# 合併2個表格
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]

# 欄位改名
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
print(df)

print("計算股價與月營收關聯度")

# 相關係數
cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("營收公布日期晚一個月")

df_monthly_sales["單月營收"] = df_monthly_sales["單月營收"].shift(-1)
df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)
df = df[["Date", "單月營收", "Adj Close"]]
df.rename({"單月營收": "sales"}, axis=1, inplace=True)
df.dropna(inplace=True)

# 相關係數
cc = df[["sales", "Adj Close"]].corr()
print(cc)

print("------------------------------------------------------------")  # 60個
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

from pandas_datareader import data
from pandas_datareader import wb
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

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
