# Python 測試 yfinance / FinMind

# 方案一：抓台股首選 —— 使用 FinMind（台灣團隊開發，免申請 Key）
# 這是台灣金融資料開源團隊做的，直接對接台灣證交所，抓台股快又穩定，絕對不會有退市或時區錯誤。

# pip install yfinance
# pip install finmind

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from FinMind.data import DataLoader
import mplfinance as mpf

# ==========================================
# 步驟 1：抓取資料
# ==========================================
dl = DataLoader()  # 初始化資料載入器

# 抓取台積電 (2330) 2026年9月到10月的日線資料
df = dl.taiwan_stock_daily(
    stock_id="2330",
    start_date="2026-08-01",  # 稍微拉長時間，畫均線才不會斷掉
    end_date="2026-10-28"
)

print(df.head())

# ==========================================
# 步驟 2：數據分析 (資料處理與計算)
# ==========================================
# 1. 轉換欄位名稱以符合 mplfinance 的標準格式 (大小寫需相符)
# 1. 自動偵測並轉換欄位名稱 (相容 FinMind 不同版本的欄位名)

rename_dict = {
    'date': 'Date',
    'open': 'Open',
    'max': 'High',
    'min': 'Low',
    'close': 'Close'
}

# 判斷成交量欄位到底是叫 Trading_Volume 還是 volume
if 'Trading_Volume' in df.columns:
    rename_dict['Trading_Volume'] = 'Volume'
elif 'volume' in df.columns:
    rename_dict['volume'] = 'Volume'

df = df.rename(columns=rename_dict)

# [偵錯小幫手] 印出目前的欄位名稱，確保有成功換成 Open, High, Low, Close, Volume
print("目前資料表的欄位有：", df.columns.tolist()) 

# 2. 將 Date 轉為時間格式，並設定為索引 (Index)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 3. 計算均線與漲跌幅
df['MA5'] = df['Close'].rolling(window=5).mean()  # 移動平均線 (MA)
df['MA20'] = df['Close'].rolling(window=20).mean()  # 移動平均線 (MA)
df['Daily_Return'] = df['Close'].pct_change()  # 每日漲跌幅

print("--- 最新 5 筆數據分析結果 (含均線與漲跌幅) ---")
print(df[['Open', 'High', 'Low', 'Close', 'MA5', 'MA20', 'Daily_Return']].tail())

import mplfinance as mpf

# ==========================================
# 步驟 3：繪製 K 線圖
# ==========================================
# 設定 K 線圖的顏色風格 (binance 風格：綠漲紅跌，符合台灣習慣需特別設定)
# 台灣習慣：紅漲綠跌

# 1. 先設定台灣習慣的紅漲綠跌
my_color = mpf.make_marketcolors(
    up='red',          # 上漲為紅
    down='green',      # 下跌為綠
    edge='inherit',
    wick='inherit',
    volume='inherit'
)

# 2. 【核心修正】在 make_mpf_style 中直接指定內建中文字型！
# 這裡我們傳入一個字型清單，讓系統去抓微軟正黑體（Windows）或蘋方體（Mac）

# 僅有 marketcolors
# my_style = mpf.make_mpf_style(marketcolors=my_color, gridstyle='--')

# marketcolors + font
my_style = mpf.make_mpf_style(
    marketcolors=my_color, 
    gridstyle='--',
    rc={'font.family': ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']} 
)

# 繪製 K 線圖 (包含 5日/20日均線 與 下方的成交量) + 中文

mpf.plot(
    df, 
    type='candle',         # 類型為 K 線圖 (Candlestick)
    mav=(5, 20),           # 自動加上 5日、20日 移動平均線
    volume=True,           # 顯示成交量
    style=my_style,        # 套用台灣紅綠燈顏色 # 套用包含字型設定的樣式
    title="台積電 (2330) 歷史走勢圖",
    ylabel="股價 (元)",
    ylabel_lower="成交量"
)

sys.exit()


# 6060



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
# 127筆資料 7 欄位
df = pd.read_csv("data/alphabet_stock_data.csv")
print(df.shape)

start_date = pd.to_datetime("2020-4-1")
end_date = pd.to_datetime("2020-9-30")

df["Date"] = pd.to_datetime(df["Date"])
print(df["Date"].shape)
new_df = (df["Date"] >= start_date) & (df["Date"] <= end_date)
print(new_df.shape)

df1 = df.loc[new_df]
stock_data = df1.set_index("Date")
stock_data.plot(subplots=True, figsize=(8, 8))
plt.legend(loc="best")
plt.suptitle("Alphabet Inc.字母控股 股價")

plt.show()
'''
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

import yfinance as yf

# 下載 0050.TW 的歷史股價資料
df = yf.download('2330.TW', start='2026-01-01', end='2026-10-01')

# 顯示前 5 筆資料
print(df.head())


import yfinance as yf

# 方式 A：把時間範圍拉長（例如從 9 月開始抓）
start_date = "2026-09-01"
end_date = "2026-10-20"
interval = "1d"

ticker = "2330.TW"
stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

print("--- 方式 A 結果 ---")
print(stock_data.tail())

# 方式 B：用 period 參數直接抓最近一個月（最不容易出錯，強烈推薦）
print("\n--- 方式 B 結果 ---")
tsmc = yf.Ticker("2330.TW")
stock_data_b = tsmc.history(period="1mo")
print(stock_data_b.tail())

print("------------------------------------------------------------")  # 60個

import yfinance as yf

start_date = "2026-08-12"
end_date = "2026-09-20"
interval = "1d"

ticker = "2330.TW"
stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

print(stock_data)

# df = yf.download("2330.TW", start="2021-01-01", end="2022-12-31")

print("------------------------------------------------------------")  # 60個

# 設定參數
start_date = "2026-10-12"  # 設定開始日期
end_date = "2026-10-15"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘
interval = "1d"  # 設定時間週期為 15 分鐘

# 抓取 S&P 500 數據 # 標準普爾500指數，簡稱S&P 500 、標普500或史坦普500
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
sp500_data["date"] = sp500_data["Date"]  # 添加 'date' 欄位
sp500_data["tic"] = "^GSPC"  # 添加 'tic' 欄位，這裡 '^GSPC' 是 S&P 500 的代號

# 移除原本的 'Datetime' 欄位
sp500_data = sp500_data.drop(columns=["Date"])

# 將所有欄位名稱轉為小寫，以符合 FeatureEngineer 的預期格式
sp500_data.columns = [col.lower() for col in sp500_data.columns]

# 顯示處理後的數據
print(sp500_data.head())

print("------------------------------")  # 30個

"""
步驟 2: 使用 FeatureEngineer 進行特徵工程
現在我們可以使用 FeatureEngineer 來添加技術指標並進行特徵工程。
"""
""" NG
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

"""
特徵工程的輸出
經過特徵工程處理後，我們的數據集將包含原始的 OHLCV 資料以及計算出的技術指標。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 頻率轉換、合併多個表格

# 下載每日股價

# 台泥 1101

df_quote = yf.download("1101.TW", start="2025-01-01", end="2025-02-10")
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

# Yahoo Finance API抓取資料，FinRL特徵工程

"""
使用 yfinance 抓取 S&P 500 的 15 分鐘資料
下面是一個具體範例，從 Yahoo Finance 下載 S&P 500 指數在指定兩天內的每 15 分鐘的歷史資料。
這些數據將包括開盤價（Open）、最高價（High）、最低價（Low）、收盤價（Close）、調整後的收盤價（Adj Close）以及成交量（Volume）。

start_date 和 end_date: 我們選擇了 2 天的日期範圍，這適合使用 15m 這樣的高頻資料。
interval: 15m 代表每 15 分鐘抓取一次資料，適合短期交易分析。
intervals 參數
參考yf.download的定義註解

Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days

一開始嘗試抓取 2023-08-01 ~ 2023-08-02 被拒絕
YFPricesMissingError('$%ticker%: possibly delisted; no price data found (15m 2023-08-01 -> 2023-08-02) (Yahoo error = "15m data not available for startTime=1690862400 and endTime=1690948800. The requested range must be within the last 60 days.")')
"""
import yfinance as yf

# 設定參數
start_date = "2025-04-28"  # 設定開始日期
end_date = "2025-04-30"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘


# 抓取 S&P 500 數據
ticker = "^GSPC"  # Yahoo Finance 中 S&P 500 的代號
sp500_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

# 顯示數據
print(sp500_data.head())

print("------------------------------")  # 30個

# 使用 yfinance 一次抓取多隻股票的資料
import yfinance as yf

# 設定參數
start_date = "2025-04-28"  # 設定開始日期
end_date = "2025-04-30"  # 設定結束日期
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

# 錯在此
"""
# 添加必要的欄位
sp500_data = sp500_data.reset_index()  # 重設索引，將日期移到普通欄位
sp500_data['date'] = sp500_data['Datetime']  # 添加 'date' 欄位
sp500_data['tic'] = '^GSPC'  # 添加 'tic' 欄位，這裡 '^GSPC' 是 S&P 500 的代號

# 移除原本的 'Datetime' 欄位
sp500_data = sp500_data.drop(columns=['Datetime'])

# 將所有欄位名稱轉為小寫，以符合 FeatureEngineer 的預期格式
sp500_data.columns = [col.lower() for col in sp500_data.columns]

# 顯示處理後的數據
print(sp500_data.head())

print("------------------------------")  # 30個

# 步驟 2: 使用 FeatureEngineer 進行特徵工程
# 現在我們可以使用 FeatureEngineer 來添加技術指標並進行特徵工程。

from finrl.meta.preprocessor.preprocessors import FeatureEngineer

# 定義我們要使用的技術指標
INDICATORS = ['macd', 'rsi', 'cci', 'dx']

# 初始化 FeatureEngineer
fe = FeatureEngineer(use_technical_indicator=True, tech_indicator_list=INDICATORS)

# 將技術指標應用於 S&P 500 的數據
sp500_data_with_indicators = fe.preprocess_data(sp500_data)

# 顯示結果
print(sp500_data_with_indicators.head())

# 特徵工程的輸出
# 經過特徵工程處理後，我們的數據集將包含原始的 OHLCV 資料以及計算出的技術指標。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# mplfinance 的使用


"""
python用mplfinance中的candlestick_ohlc畫分時圖

matplotlib.finance獨立出來成爲mplfinance，而mplfinance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。
我需要分析分時圖，也就是一分鐘的行情，這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mplfinance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，
浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。
時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，導致在X軸上這4個時間段都重疊在一起，無法區分了。
要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。
那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），採用默認的格式化是亂碼。需要自定義x軸的格式化函數。

pip install mplfinance
pip install --upgrade mplfinance

"""

from pandas import DataFrame
import matplotlib.dates as dates
import mplfinance as mpf
from matplotlib.ticker import Formatter
from mplfinance.original_flavor import candlestick_ohlc

dfcvs = DataFrame(
    [
        #    時間            開盤, 最高 ,最低, 收盤
        ["2018/09/17-21:34", 3646, 3650, 3644, 3650],
        ["2018/09/17-21:35", 3650, 3650, 3648, 3648],
        ["2018/09/17-21:36", 3650, 3650, 3648, 3650],
        ["2018/09/17-21:37", 3652, 3654, 3648, 3652],
    ]
)

dfcvs.columns = ["時間", "開盤", "最高", "最低", "收盤"]
dfcvs["時間"] = pd.to_datetime(dfcvs["時間"], format="%Y/%m/%d-%H:%M")

# matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
# 因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
# 這樣就可以一分鐘就佔一個位置

dfcvs["時間"] = dfcvs["時間"].apply(lambda x: dates.date2num(x) * 1440)
data_mat = dfcvs.values

fig, ax = plt.subplots(figsize=(10, 6))

fig.subplots_adjust(bottom=0.1)
candlestick_ohlc(
    ax, data_mat, colordown="#53c156", colorup="#ff1717", width=0.2, alpha=1
)


# 將x軸的浮點數格式化成日期小時分鐘
# 默認的x軸格式化是日期被dates.date2num之後的浮點數，因爲在上面乘以了1440，所以默認是錯誤的
# 只能自己將浮點數格式化爲日期時間分鐘
# 參考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
    def __init__(self, dates, fmt="%Y%m%d %H:%M"):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        "Return the label for time x at position pos"
        ind = int(np.round(x))
        # ind就是x軸的刻度數值，不是日期的下標

        return dates.num2date(ind / 1440).strftime(self.fmt)


formatter = MyFormatter(data_mat[:, 0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    label.set_rotation(90)
    label.set_horizontalalignment("right")

show()

print("------------------------------------------------------------")  # 60個

# 加載取數與繪圖所需的函數包
import datetime
from hs_udata import set_token, stock_quote_daily
import matplotlib as mpl
import matplotlib.dates as mdates

# from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc

data_price = [1, 2, 3, 4, 5]

# 繪製圖片
fig = plt.figure(
    num="matplotlib 02",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

grid = plt.GridSpec(12, 10, wspace=0.5, hspace=0.5)

ax1 = fig.add_subplot(grid[0:8, 0:12])  # 設置K線圖的尺寸

# candlestick_ohlc(ax1, ohlc.values.tolist(), width = 0.7, colorup = 'red', colordown = 'green')

# （2）繪制均線
# ax1.plot(range(len(data_price)), data_price, color = 'red', lw = 2, label = 'MA (5)')

# 設置標注
plt.title("test", fontsize=14)  # 設置圖片標題
plt.ylabel("價 格（元）", fontsize=14)  # 設置縱軸標題
# plt.legend(loc = 'best')                    # 繪制圖例
ax1.set_xticks([])  # 日期標注在成交量中，故清空此處x軸刻度
ax1.set_xticklabels([])  # 日期標注在成交量中，故清空此處x軸

# （3）繪制成交量
# 成交量數據

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8:10, 0:12])  # 設置成交量圖形尺寸
# ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
# ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation=30)
plt.xlabel("日 期", fontsize=14)  # 設置橫軸標題
# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]  # ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))  # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)  # 生成橫軸標注位置列表
xticks_str = list(map(lambda x: date_list[int(x)], xticks_num))  # 生成正在標注日期列表
ax2.set_xticks(xticks_num)  # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)  # 設置橫軸標注日期

show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from io import StringIO


def get_setting():  # ←將「讀取設定檔」寫成函式, 可讓程式易讀易用
    result = []  # ←準備一個空串列來存放讀取及解析的結果
    try:  # 使用 try 來預防開檔或讀檔錯誤
        with open("data/stock.txt") as f:  # 用 with 以讀取模式開啟檔案
            slist = f.readlines()  # 以行為單位讀取所有資料
            print("讀入：", slist)  # 輸出讀到的資料以供確認
            a, b, c = slist[0].split(",")  # ←將股票字串以逗號切割為串列
            result = [a, b, c]
    except:
        print("data/stock.txt 讀取錯誤")
    return result  # ←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []


def get_data():
    data = get_setting()
    print(data)
    dates = []
    # print(data[1])
    start_date = datetime.datetime.strptime(data[1], "%Y%m%d")
    end_date = datetime.datetime.strptime(data[2], "%Y%m%d")
    for daynumber in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(days=daynumber)
        if date.weekday() < 6:
            dates.append(date.strftime("%Y%m%d"))
    return data[0], dates


def crawl_data(date, symbol):
    print("下載股價")
    url = (
        "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
        + date
        + "&type=ALL"
    )
    print(url)
    response = requests.get(url)

    r_text = [
        i for i in response.text.split("\n") if len(i.split('",')) == 17 and i[0] != "="
    ]
    df = pd.read_csv(StringIO("\n".join(r_text)), header=0)

    df = df.drop(columns=["Unnamed: 16"])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    df_columns = filter_df.columns
    return list(filter_df.iloc[0]), filter_df.columns


print("------------------------------------------------------------")  # 60個

all_list = []
stock_symbol, dates = get_data()

for date in dates:
    time.sleep(5)
    try:
        crawler_data = crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)
print(all_df)

# step 1 prepare data
day = all_df["日期"].astype(str)
close = all_df["收盤價"].astype(float)

# step 2 create plot
plt.figure(figsize=(12, 8), dpi=100)

# step 3 plot
plt.plot(day, close, "s-", color="r", label="Close Price")
plt.title("TSMC Line chart")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)

plt.show()

print("------------------------------------------------------------")  # 60個

all_list = []
stock_symbol, dates = get_data()

for date in dates:
    time.sleep(5)
    try:
        crawler_data = crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

# step 1 prepare data
day = all_df["日期"].astype(str)
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
ax.set_title(stock_symbol + "  開盤價、收盤價 ( " + dates[0] + " ~ " + dates[-1] + " )")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, "s-", color="r", label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, "o-", color="b", label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

# step 4 show plot
plt.show()

print("------------------------------------------------------------")  # 60個

import mplfinance as mpf

all_list = []
stock_symbol, dates = get_data()

for date in dates:
    time.sleep(5)
    try:
        crawler_data = crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

print(all_df)

# step 1 prepare data
day = all_df["日期"].astype(str)
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)
high = all_df["最高價"].astype(float)
low = all_df["最低價"].astype(float)
volume = all_df["成交股數"].str.replace(",", "").astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
ax.set_title(stock_symbol + "  K 線圖 ( " + dates[0] + " ~ " + dates[1] + " )")

# step 3 plot 子圖(ax)
mpf.candlestick2_ochl(
    ax, openprice, close, high, low, width=0.5, colorup="r", colordown="g", alpha=0.6
)

ax.plot(talib.SMA(close, 10), label="10日均線")
ax.plot(talib.SMA(close, 30), label="30日均線")
ax.legend(loc="best", fontsize=20)
ax.grid(True)

# step 3 plot 子圖(ax2)
mpf.volume_overlay(
    ax2, openprice, close, volume, colorup="r", colordown="g", width=0.5, alpha=0.8
)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)

# step 4 show plot
plt.show()




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------")  # 30個

