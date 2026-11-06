"""
Python 測試 FinMind

抓台股首選 —— 使用 FinMind（台灣團隊開發，免申請 Key）
這是台灣金融資料開源團隊做的，直接對接台灣證交所，抓台股快又穩定，絕對不會有退市或時區錯誤。

pip install finmind

print("------------------------------------------------------------")  # 60個

Python 測試 twstock

pip install twstock
pip install twstock --upgrade  # 更新套件

twstock 台灣股市股票價格擷取
https://pypi.org/project/twstock/

print("------------------------------------------------------------")  # 60個

Python 測試 twse

公開資訊觀測站
https://mops.twse.com.tw/mops/
https://mops.twse.com.tw/mops/#/web/home
"""
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

import csv
import json
import requests

from io import StringIO
from bs4 import BeautifulSoup

import mplfinance as mpf

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


stock_id1 = "2330"  # 2330台積電
stock_id2 = "2317"  # 2317鴻海
stock_id3 = "6869"  # 6869雲豹能源

import twstock

print("------------------------------------------------------------")  # 60個
print("使用 FinMind ST")
print("------------------------------------------------------------")  # 60個

from FinMind.data import DataLoader

api = DataLoader()

cc = help(api.taiwan_stock_dividend_result)
# print(cc)

"""
★ 台股總覽 TaiwanStockInfo
這張資料表主要是列出台灣所有，上市、上櫃、興櫃，的股票名稱，代碼和產業類別！
資料更新時間 每天 1:30，實際更新時間以 API 資料為主
"""

"""
api = DataLoader()
# api.login_by_token(api_token='token')
df = api.taiwan_stock_info()
print('台股總覽 TaiwanStockInfo')
print(df)
"""

"""
★ 台股總覽(含權證) TaiwanStockInfoWithWarrant
這張資料表主要是列出台灣所有，上市、上櫃、興櫃，的股票、權證名稱，代碼和產業類別！
資料量超過 5 萬筆
資料更新時間 每天 1:30，實際更新時間以 API 資料為主
"""
"""
api = DataLoader()
# api.login_by_token(api_token='token')
df = api.taiwan_stock_info_with_warrant()

print('台股總覽(含權證) TaiwanStockInfoWithWarrant')
print(df)
"""

"""
★ 台股交易日 TaiwanStockTradingDate
提供台股交易日。
資料更新時間-星期一至五 18:00，實際更新時間以 API 資料為主。
"""

"""
url = "https://api.finmindtrade.com/api/v4/data"
token = "" # 參考登入，獲取金鑰
headers = {"Authorization": f"Bearer {token}"}
parameter = {
    "dataset": "TaiwanStockTradingDate",
}
resp = requests.get(url, headers=headers, params=parameter)
data = resp.json()
data = pd.DataFrame(data["data"])
print(data)
"""

print("------------------------------")  # 30個

"""
★ 股價日成交資訊 TaiwanStockPrice
提供台股，上市、上櫃、興櫃，的股票日成交資訊！
"""
"""
api = DataLoader()
# api.login_by_token(api_token='token')
df = api.taiwan_stock_daily(
    stock_id="2330",
    start_date="2026-09-01",
    end_date="2026-10-01"
)
print('股價')
print(df)

print("------------------------------")  # 30個

★ 除權息, 一次只能查一天
div_df = api.taiwan_stock_dividend_result(
    stock_id="2330",
    start_date="2026-09-01"
)
print('除權息')
print(div_df)
print(div_df.columns)

print("檢視前幾行\n", div_df.head())
"""

import FinMind

print(FinMind.__file__)
print(FinMind.__version__)
print(dir(FinMind))
print(dir(FinMind.data))

print("------------------------------------------------------------")  # 60個


def get_stock_data(stock_id, start_date, end_date):
    # 取得網站資料, 日線資料
    dl = DataLoader()  # 初始化資料載入器
    df = dl.taiwan_stock_daily(
        stock_id=stock_id, start_date=start_date, end_date=end_date
    )  # 稍微拉長時間，畫均線才不會斷掉
    return df


"""
# 即時讀取網路資料
print("抓取台積電 (2330) 2026年8月到10月的日線資料")
start_date = "2026-08-01"
end_date = "2026-11-01"
stock_id = "2330"
df = get_stock_data(stock_id, start_date, end_date)
# 存檔
print("存檔, df轉pickle")
df.to_pickle("tmp_finmind_data1.pkl")
"""
# 讀取pickle檔案資料
df1 = pd.read_pickle("tmp_finmind_data1.pkl")
# print("比較df df1是否相同", df.equals(df1))
df = df1.tail(30)

# 取得資料內容
print("列印取得的日線資料, 前5筆")
print(df)

# print("檢視前幾行\n", df.head())
print("df的形狀 : ", df.shape)
print("df的欄位 : ", df.columns.tolist())

print("------------------------------")  # 30個

print("撈出一部分資料")

start_date = "2026-10-01"
end_date = "2026-10-05"
print(df["date"].shape)

new_df = (df["date"] >= start_date) & (df["date"] <= end_date)
print("new_df的形狀 : ", new_df.shape)

df1 = df.loc[new_df]

print(df1)

print("------------------------------")  # 30個

# df的10個欄位
# “日期”  、“股票代碼”、“成交股數”、“成交金額”、“開盤價”、
# “最高價”、“最低價”  、“收盤價”  、 "漲跌價差”、“成交筆數”
"""
個股日收盤行情（Daily Stock Trading Quotes）標準資料格式
date            （日期）    ：交易當天的日期（在台股資料中，通常呈現為民國紀年如 112/10/24 或西元紀年 20231024）。
stock_id        （證券代號）：股票的四碼或六碼代號
Trading_Volume  （成交股數）：當天這檔股票總共成交了多少股（注意：台股 1 張 = 1,000 股）。
Trading_money   （成交金額）：當天總成交的累計新台幣金額。
open            （開盤價）  ：當天早上 9:00 開盤的第一筆成交價格。
max             （最高價）  ：當天盤中成交的最高價格。
min             （最低價）  ：當天盤中成交的最低價格。
close           （收盤價）  ：當天下午 1:30 收盤時的最後一筆成交價格。
spread          （漲跌價差）：當天收盤價與前一個交易日收盤價的差額（有正負號或由其他欄位標示漲跌）。
Trading_turnover（成交筆數）：當天這檔股票總共撮合成功了多少筆交易。
"""
day = df["date"].astype(str)  # 日期
stock_id = df["stock_id"].astype(str)  # 股票代碼
volume = df["Trading_Volume"].astype(float)  # 成交量（Trading_Volume）, 成交股數
money = df["Trading_money"].astype(float)  # 成交金額（Trading_money）
_open = df["open"].astype(float)  # 開盤價 Open
_max = df["max"].astype(float)  # 最高價 High
_min = df["min"].astype(float)  # 最低價 Low
close = df["close"].astype(float)  # 收盤價 Close
spread = df["spread"].astype(float)  # 買賣價差（Spread）
turnover = df["Trading_turnover"].astype(float)  # 交易筆數（Trading_turnover）

df["ma5"] = df["close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["ma20"] = df["close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["ma60"] = df["close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

_ma5 = df["ma5"].astype(float)  # 開盤價 Open
_ma20 = df["ma20"].astype(float)  # 開盤價 Open

M, N = df.shape

plt.figure(figsize=(12, 14))

plt.subplot(311)
plt.plot(day, _open, "s-", color="r", label="開盤價  Open Price")
plt.plot(day, close, "s-", color="g", label="收盤價 Close Price")
plt.plot(day, _max, "s", color="r", label="最高價 Max")
plt.plot(day, _min, "s", color="g", label="最低價 Min")
plt.xticks(range(M), df["date"], rotation=30)

plt.subplot(312)
plt.plot(day, _ma5, "s-", color="r", label="週線MA5")
plt.plot(day, _ma20, "s-", color="g", label="月線MA20")
plt.xticks(range(M), df["date"], rotation=30)

plt.subplot(313)  # 畫成交量
plt.bar(range(M), df["Trading_Volume"] / 1000, facecolor="#99ccff")

plt.ylabel("成交量(張)")
plt.xticks(range(M), df["date"], rotation=30)

show()

plt.figure(figsize=(10, 8))
plt.plot(day, _open, "s-", color="r", label="開盤價  Open Price")
plt.plot(day, close, "s-", color="g", label="收盤價 Close Price")
# plt.plot(day, _max, "s", color="r", label="最高價 Max")
# plt.plot(day, _min, "s", color="g", label="最低價 Min")

print("df之大小")
M, N = df.shape
print(df.shape)
print("df之大小", M, "X", N)
for idx in range(M):
    y_max = df["max"].iloc[idx]
    y_min = df["min"].iloc[idx]
    plt.plot([idx, idx], [y_max, y_min], color="cyan", linewidth=1.5, zorder=5)
    # print(idx, y_max, y_min)
    plt.scatter(idx, y_max, color="r", marker="^", s=40, zorder=5)
    plt.scatter(idx, y_min, color="g", marker="v", s=40, zorder=5)

plt.legend(loc="best", fontsize=16)
plt.xlabel("日期", fontsize=12)
plt.ylabel("股價 (元)", fontsize=12)
plt.title("歷史走勢圖", fontsize=12)
plt.xticks(rotation=30)

show()

print("------------------------------------------------------------")  # 60個

# ==========================================
# 步驟 2：數據分析 (資料處理與計算)
# ==========================================

# 轉換欄位名稱以符合 mplfinance 的標準格式 (大小寫需相符)
# 自動偵測並轉換欄位名稱 (相容 FinMind 不同版本的欄位名)
# "date"改"Date", "open"改"Open", "max"改"High", "min"改"Low", "close"改"Close"

print("修改前 df的欄位 : ", df.columns.tolist())

rename_dict = {
    "date": "Date",
    "open": "Open",
    "max": "High",
    "min": "Low",
    "close": "Close",
}

# 判斷成交量欄位到底是叫 Trading_Volume 還是 volume
if "Trading_Volume" in df.columns:
    print("xxxxx111")
    rename_dict["Trading_Volume"] = "Volume"  # "Trading_Volume"改"Volume"
elif "volume" in df.columns:
    print("xxxxx222")
    rename_dict["volume"] = "Volume"  # "volume"改"Volume"

df = df.rename(columns=rename_dict)  # df修改欄位名稱

# 新增拷貝欄位資料
df["date"] = df["Date"]

print("修改後 df的欄位 : ", df.columns.tolist())

print("------------------------------")  # 30個

print("aaaa")
print("檢視前幾行\n", df.head())

# 2. 將 Date 轉為時間格式，並設定為索引 (Index)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

print("bbbb")
print("檢視前幾行\n", df.head())

print("--- 最新 5 筆數據 ---")
print(df[["Open", "High", "Low", "Close"]].tail())

# 3. 計算均線與漲跌幅

"""
# MA5（5日均線）與 MA20（20日均線，俗稱月線）是股市技術分析中最常用的移動平均線（Moving Average）組合，
# 分別代表短期與中短期的市場平均成本 與強弱趨勢

• MA5（5日均線 / 週線）：
	• 定義：過去 5 個交易日收盤價的平均值，代表市場「近一週」的短線平均成本。
	• 特點：對價格變化最敏感、貼近盤面，適合觀察短線動能與攻擊力道，但雜訊較多。
• MA20（20日均線 / 月線）：
	• 定義：過去 20 個交易日收盤價的平均值，代表市場「近一個月」的中短期平均成本。
	• 特點：相對平滑，能過濾掉短期的上下震盪，常用來判斷中短期趨勢是否維持健康。
"""
df["MA5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["Close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["MA60"] = df["Close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

df["Daily_Return"] = df["Close"].pct_change()  # 每日漲跌幅, pct_change() : 與前項差的百分比

print("------------------------------")  # 30個

print("計算每日漲跌幅 PCT")
my_pct = []  # pct
my_pct.append(0)
M, N = df.shape
for idx in range(M):
    if idx > 0:
        dd = df["Close"].iloc[idx] - df["Close"].iloc[idx - 1]
        pp = dd / df["Close"].iloc[idx]
        print(idx, df["Close"].iloc[idx], dd, pp)
        my_pct.append(pp)

# 將pct塞回 DataFrame 中，方便繪圖
df["PCT"] = my_pct

print("------------------------------")  # 30個

# 畫週線MA5, 月線MA20

df["ma5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["ma20"] = df["Close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["ma60"] = df["Close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

df["daily_return"] = df["Close"].pct_change()  # 每日漲跌幅, pct_change() : 與前項差的百分比

_daily_return = df["daily_return"].astype(float)  # 每日漲跌幅, 後來沒用到, 或許是 PCT

print("------------------------------")  # 30個

print("--- 最新 5 筆數據分析結果 (含均線與漲跌幅) ---")
# print(df[["Open", "High", "Low", "Close", "MA5", "MA20", "Daily_Return"]].tail())
# print(df[["Open", "High", "Low", "Close", "MA5", "MA20", "Daily_Return"]])
print(df[["Open", "High", "Low", "Close", "MA5", "MA20", "Daily_Return", "PCT"]])

# K線圖（Candlestick chart，又稱蠟燭線或陰陽燭）
# 是用來記錄與反應金融商品（如股票、期貨、外匯或加密貨幣）在特定時間內價格變動的技術分析圖表。

# ==========================================
# 步驟 3：繪製 K 線圖
# ==========================================
# 設定 K 線圖的顏色風格 (binance 風格：綠漲紅跌，符合台灣習慣需特別設定)
# 台灣習慣：紅漲綠跌

# 1. 先設定台灣習慣的紅漲綠跌
my_color = mpf.make_marketcolors(
    up="red",  # 上漲為紅
    down="green",  # 下跌為綠
    edge="inherit",
    wick="inherit",
    volume="inherit",
)

# 2. 【核心修正】在 make_mpf_style 中直接指定內建中文字型！
# 這裡我們傳入一個字型清單，讓系統去抓微軟正黑體

# 僅有 marketcolors
# my_style = mpf.make_mpf_style(marketcolors=my_color, gridstyle='--')

# marketcolors + font
my_style = mpf.make_mpf_style(
    marketcolors=my_color,
    gridstyle="--",
    rc={"font.family": ["Microsoft JhengHei", "Arial Unicode MS", "sans-serif"]},
)

# 繪製 K 線圖 (包含 5日/20日均線 與 下方的成交量) + 中文
mpf.plot(
    df,
    type="candle",  # 類型為 K 線圖 (Candlestick)
    mav=(5, 20),  # 自動加上 5日、20日 移動平均線
    volume=True,  # 顯示成交量
    style=my_style,  # 套用台灣紅綠燈顏色 # 套用包含字型設定的樣式
    title="歷史走勢圖",
    ylabel="股價 (元)",
    ylabel_lower="成交量",
)

print("------------------------------------------------------------")  # 60個

# 自動標記買賣訊號程式碼

"""
# 即時讀取網路資料
print("抓取2026年8月到10月的日線資料")
start_date = "2026-08-01"
end_date = "2026-11-01"
stock_id = "2330"
df = get_stock_data(stock_id, start_date, end_date)
"""
# 讀取pickle檔案資料
df1 = pd.read_pickle("tmp_finmind_data1.pkl")
# print("比較df df1是否相同", df.equals(df1))
df = df1.tail(30)

# ==========================================
# 步驟 2：數據分析 (資料處理與計算買賣訊號)
# ==========================================

# 轉換欄位名稱以符合 mplfinance 的標準格式 (大小寫需相符)
# 自動偵測並轉換欄位名稱 (相容 FinMind 不同版本的欄位名)
# "date"改"Date", "open"改"Open", "max"改"High", "min"改"Low", "close"改"Close"

print("df的欄位 : ", df.columns.tolist())

rename_dict = {
    "date": "Date",
    "open": "Open",
    "max": "High",
    "min": "Low",
    "close": "Close",
}

# 判斷成交量欄位到底是叫 Trading_Volume 還是 volume
if "Trading_Volume" in df.columns:
    print("xxxxx111")
    rename_dict["Trading_Volume"] = "Volume"  # "Trading_Volume"改"Volume"
elif "volume" in df.columns:
    print("xxxxx222")
    rename_dict["volume"] = "Volume"  # "volume"改"Volume"

df = df.rename(columns=rename_dict)  # df修改欄位名稱

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# 2. 計算 5日 與 20日 均線
df["MA5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["Close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["MA60"] = df["Close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

# 3. 判斷交叉訊號
# 建立一個訊號欄位：1 代表黃金交叉(買)，-1 代表死亡交叉(賣)
df["Signal"] = 0

# 找出 5MA 大於 20MA 的日子
# 這行會幫我們標示狀態。如果今天短均線在長均線上方就給 1，反之給 -1
df["Signal"] = np.where(df["MA5"] > df["MA20"], 1, -1)

# 透過與前一天的訊號做對比 (diff)，找出剛好「發生交叉」的那一天
# diff() 結果為 2 代表從 -1 變成 1 (黃金交叉)；-2 代表從 1 變成 -1 (死亡交叉)
# 這是找出「變盤日」的神奇函數。如果昨天是 -1（空頭），今天是 1（多頭），相減得到的差值就是 2。這代表趨勢反轉，今天就是黃金交叉買點。

df["Position_Change"] = df["Signal"].diff()

# 4. 建立繪圖專用的買賣點價格陣列 (如果沒訊號，就填上 NaN 否則會畫在 0 的位置)
# 我們故意把標記箭頭畫在 K 線的外面一點點（下方 2% 或上方 2%），這樣箭頭就不會跟 K 線重疊在一起，視覺上更清晰。
df["Buy_Price"] = np.where(
    df["Position_Change"] == 2, df["Low"] * 0.98, np.nan
)  # 畫在最低價下方 2% 處
df["Sell_Price"] = np.where(
    df["Position_Change"] == -2, df["High"] * 1.02, np.nan
)  # 畫在最高價上方 2% 處

print("--- 有觸發買賣訊號的日子 ---")
print(
    df[df["Position_Change"].isin([2, -2])][["Close", "MA5", "MA20", "Position_Change"]]
)

# ==========================================
# 步驟 3：繪製 K 線圖 (包含買賣訊號箭頭)
# ==========================================
# 1. 樣式與顏色設定
my_color = mpf.make_marketcolors(
    up="red", down="green", edge="inherit", wick="inherit", volume="inherit"
)
my_style = mpf.make_mpf_style(
    marketcolors=my_color,
    gridstyle="--",
    rc={"font.family": ["Microsoft JhengHei", "Arial Unicode MS", "sans-serif"]},
)

# 2. 【核心】建立額外的買賣點圖層 (addplot)
plots = [
    # 買點：紅色朝上箭頭 (scatter)
    mpf.make_addplot(
        df["Buy_Price"], type="scatter", markersize=100, marker="^", color="red"
    ),
    # 賣點：綠色朝下箭頭 (scatter)
    mpf.make_addplot(
        df["Sell_Price"], type="scatter", markersize=100, marker="v", color="green"
    ),
]

# 3. 繪製中文 K 線圖，並把 plots 傳進去
mpf.plot(
    df,
    type="candle",
    mav=(5, 20),
    volume=True,
    style=my_style,
    addplot=plots,  # 加入自訂的買賣箭頭圖層
    title="均線策略買賣訊號圖",
    ylabel="股價 (元)",
    ylabel_lower="成交量",
)

print("------------------------------------------------------------")  # 60個

# ==========================================
# 步驟 4：量化策略回測 (計算總報酬率)
# ==========================================

# 初始化帳戶參數
initial_capital = 1000000.0  # 初始資金 100 萬
cash = initial_capital  # 目前手頭現金
stock_shares = 0.0  # 目前持有股數
history_total_value = []  # 紀錄每天的帳戶總價值 (淨值走勢)
trade_log = []  # 紀錄交易明細

print("========== 交易明細紀錄 ==========")

# 逐日模擬交易
for date, row in df.iterrows():
    current_close = row["Close"]
    signal = row["Position_Change"]

    # 狀況一：觸發買進訊號 (黃金交叉) 且目前手上沒股票
    if signal == 2 and stock_shares == 0:
        stock_shares = cash / current_close
        cash = 0
        trade_log.append(
            f"【買進】{date.strftime('%Y-%m-%d')} | 價格: {current_close:.1f} 元 | 全額買入 {stock_shares:.1f} 股"
        )
        print(trade_log[-1])

    # 狀況二：觸發賣出訊號 (死亡交叉) 且目前手上有股票
    elif signal == -2 and stock_shares > 0:
        cash = stock_shares * current_close
        trade_log.append(
            f"【賣出】{date.strftime('%Y-%m-%d')} | 價格: {current_close:.1f} 元 | 賣出拿回現金: ${cash:,.0f} 元"
        )
        stock_shares = 0
        print(trade_log[-1])

    # 每日結算：計算當天帳戶總價值 (現金 + 股票市值)
    current_value = cash + (stock_shares * current_close)
    history_total_value.append(current_value)

print("==================================\n")

# 將資產歷史數據塞回 DataFrame 中，方便繪圖
df["Total_Value"] = history_total_value

# ==========================================
# 步驟 5：計算最終績效指標
# ==========================================
final_value = df["Total_Value"].iloc[-1]
total_return_rate = ((final_value - initial_capital) / initial_capital) * 100

# 計算同時期「買進持有的對照組報酬率」 (Buy and Hold)
buy_and_hold_return = (
    (df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[0]
) * 100

print("========== 策略績效結算 ==========")
print(f"💰 初始資金： ${initial_capital:,.0f} 元")
print(f"💰 期末資產： ${final_value:,.0f} 元")
print(f"📈 策略總報酬率： {total_return_rate:.2f} %")
print(f"📊 同期純持有的報酬率 (大盤對照組)： {buy_and_hold_return:.2f} %")
print("==================================")

# ==========================================
# 步驟 6：繪製資產淨值走勢圖 (產出成果圖)
# ==========================================
# 呼叫我們先前設定好的中文字型設定，確保圖片能顯示中文

plt.figure(figsize=(10, 8))
plt.plot(df.index, df["Total_Value"], label="均線策略資產淨值", color="blue", linewidth=2)
plt.axhline(y=initial_capital, color="red", linestyle="--", label="初始資金 (100萬)")

plt.title("均線交叉策略 - 帳戶資產淨值走勢圖 (Equity Curve)", fontsize=14)
plt.xlabel("日期", fontsize=12)
plt.ylabel("帳戶總價值 (元)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper left")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取pickle檔案資料
df = pd.read_pickle("tmp_finmind_data1.pkl")
print(df)

day = df["date"].astype(str)  # 日期
# print(day[::5])  # syntax
openprice = df["open"].astype(float)  # 開盤價 Open
close = df["close"].astype(float)  # 收盤價 Close
high = df["max"].astype(float)  # 最高價 High
low = df["min"].astype(float)  # 最低價 Low
volume = df["Trading_Volume"].astype(float)  # 成交量（Trading_Volume）, 成交股數


plt.figure(figsize=[12, 6])

plt.plot(day, openprice, "s-", color="r", label="開盤價")
plt.plot(day, close, "o-", color="g", label="收盤價")

plt.xticks(range(0, len(day), 5), fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.grid(True)
plt.legend(loc="best", fontsize=10)

plt.title("開盤價、收盤價")

show()

print("------------------------------------------------------------")  # 60個
# 6060

# 讀取pickle檔案資料
df = pd.read_pickle("tmp_finmind_data1.pkl")
# df = df.tail(5)

print("df的形狀 : ", df.shape)
print(df)

# 計算5天, 20天和60天移動平均線
df["MA5"] = df["close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["MA60"] = df["close"].rolling(window=40).mean()  # 移動平均線 (MA60) 連同過去N點平均

# 繪製收盤價和移動平均線
plt.figure(figsize=(10, 8))
plt.plot(df["close"], label="收盤價", color="r")
plt.plot(df["MA5"], label="週線", color="g")
plt.plot(df["MA20"], label="月線", color="b")
plt.plot(df["MA60"], label="半年線", color="c")

plt.title("股價 5 日, 20 日和 60日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()
plt.grid(True)

show()

print("------------------------------")  # 30個

# 移動平均生成交易信號
# 買入信號: 5日均線從下方突破20日均線
# 賣出信號: 5日均線從上方跌破20日均線
df["Signal"] = 0.0
df.iloc[5:, df.columns.get_loc("Signal")] = np.where(
    df["MA5"].iloc[5:] > df["MA20"].iloc[5:], 1.0, 0.0
)
df["Signal_change"] = df["Signal"].diff()

# 找出買入和賣出的日期
buy_dates = df[df["Signal_change"] == 1].index
sell_dates = df[df["Signal_change"] == -1].index

print(f"買入日期: {buy_dates.tolist()}")
print(f"賣出日期: {sell_dates.tolist()}")

print("------------------------------")  # 30個

print("df的第0筆資料")
print("開盤價：", df["open"].iloc[0])
print("收盤價：", df["close"].iloc[0])
print("最高價：", df["max"].iloc[0])
print("最低價：", df["min"].iloc[0])
print("交易量：", df["Trading_Volume"].iloc[0])

df = df.filter(["close"])  # 取出一欄資料

print()
print(df)

df = df.rename(columns={"close": "TT"})  # df修改欄位名稱

print()
print(df)

# 報酬率公式：(Pt−Pt−1)/Pt−1

r = df["TT"].diff() / df["TT"]
print()
print(r)


print("最後一百筆資料")

r[-100:].plot()  # df直接畫出
plt.title("報酬率 最後一百筆資料")

show()

# 原本股價圖波動的很厲害，現在我們想讓它變得平滑一點，改看每 20 天的平均

P = df["TT"]  # 取出一欄資料

print(P.rolling(window=20).mean())  # 移動平均線 (MA20) 連同過去N點平均

P.plot()
P.rolling(window=20).mean().plot()  # 移動平均線 (MA20) 連同過去N點平均
P.rolling(window=40).mean().plot()  # 移動平均線 (MA60) 連同過去N點平均

plt.title("all / MA20 / MA60")

show()

print("------------------------------------------------------------")  # 60個
print("使用 FinMind SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 分時圖 不知道是什麼意義
# mplfinance 的使用

"""
python 用 mplfinance 中的 candlestick_ohlc 畫分時圖

matplotlib.finance獨立出來成爲mplfinance，
而mplfinance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。

我需要分析分時圖，也就是一分鐘的行情，
這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mplfinance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，
浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。

時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，
導致在X軸上這4個時間段都重疊在一起，無法區分了。
要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。
那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，
將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），
採用默認的格式化是亂碼。需要自定義x軸的格式化函數。

pip install mplfinance
pip install --upgrade mplfinance
"""

import matplotlib.dates as dates
from matplotlib.ticker import Formatter
from mplfinance.original_flavor import candlestick_ohlc

df = pd.DataFrame(
    [
        #    時間            開盤, 最高 ,最低, 收盤
        ["2018/09/17-21:34", 3646, 3650, 3644, 3650],
        ["2018/09/17-21:35", 3650, 3650, 3648, 3648],
        ["2018/09/17-21:36", 3650, 3650, 3648, 3650],
        ["2018/09/17-21:37", 3652, 3654, 3648, 3652],
    ]
)

# df.plot()
# show()

print(df)

df.columns = ["時間", "開盤", "最高", "最低", "收盤"]

print("原時間")
print(df["時間"])

# 修改時間格式
df["時間"] = pd.to_datetime(df["時間"], format="%Y/%m/%d-%H:%M")

print()
print(df)

# matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
# 因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
# 這樣就可以一分鐘就佔一個位置

print("原時間")
print(df["時間"])

# 時間改成 1970/1/1至今的"分數"
df["時間"] = df["時間"].apply(lambda x: dates.date2num(x) * 1440)

print("新時間")
print(df["時間"])

data_mat = df.values
print("df.values")
print(df.values)

fig, ax = plt.subplots(figsize=(8, 5))

fig.subplots_adjust(bottom=0.1)
candlestick_ohlc(
    # ax, data_mat, colordown="#53c156", colorup="#ff1717", width=0.2, alpha=1
    ax,
    data_mat,
    colordown="green",
    colorup="red",
    width=0.2,
    alpha=1,
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


print()
print(data_mat[:, 0])
print()

formatter = MyFormatter(data_mat[:, 0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    label.set_rotation(20)
    label.set_horizontalalignment("right")
plt.title("畫分時圖")

show()

print("------------------------------------------------------------")  # 60個
print("使用 twstock ST")
print("------------------------------------------------------------")  # 60個

stock_id = "2330"  # 2330台積電
# stock_id = "2317"  # 2317鴻海

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

print("股票代號:", stock.sid)
print("個股資訊\n", twstock.codes[stock_id])

print("各日資料(近31日)")
print("各日收盤價:", stock.price)  # 近31個收盤價
print("各日最高價:", stock.high)
print("各日最低價:", stock.low)
print("各日成交股數:", stock.capacity)
print("各日的日期:", stock.date)

print("近6個收盤價：")
print(stock.price[-6:])  # 近6日之收盤價

print("------------------------------")  # 30個

print("最新資料")
print("日期：", stock.date[-1])
print("開盤價：", stock.open[-1])
print("最高價：", stock.high[-1])
print("最低價：", stock.low[-1])
print("收盤價：", stock.price[-1])

print("------------------------------")  # 30個
"""
# 使用語法：（查詢某年某月的股票資料）
# stock.fetch(year, month)  # 取得 year年month月 的資料

stocklist = stock.fetch(2019, 12)  # 取得 2019年12月 的資料
print(stocklist)
for s in stocklist:
    print(s)
    print(s.date.strftime("%Y-%m-%d"), end="\t")
    print(s.open, end="\t")
    print(s.high, end="\t")
    print(s.low, end="\t")
    print(s.close)

print("------------------------------")  # 30個
"""
# 股票即時交易資訊

print("即時資料, 1檔 / 3檔")

realdata = twstock.realtime.get(stock_id)  # 即時資料
# realdata = twstock.realtime.get([stock_id1, stock_id2, stock_id3])  # 即時資料
print(realdata)

print("是否讀取成功：", realdata["success"])

if realdata["success"]:  # 如果讀取成功
    print("timestamp", realdata["timestamp"])
    print("股票名稱：", realdata["info"]["name"])
    print("股票代碼：", realdata["info"]["code"])
    print("地區：", realdata["info"]["channel"])
    print("股票名稱：", realdata["info"]["name"])
    print("公司全名：", realdata["info"]["fullname"])
    print("現在時間：", realdata["info"]["time"])
    print("開盤價：", realdata["realtime"]["open"])
    print("最高價：", realdata["realtime"]["high"])
    print("最低價：", realdata["realtime"]["low"])
    print("最新成交價：", realdata["realtime"]["latest_trade_price"])
    print("成交量：", realdata["realtime"]["trade_volume"])
    print("累計成交量：", realdata["realtime"]["accumulate_trade_volume"])
    print("最佳5檔賣出價：", realdata["realtime"]["best_bid_price"])
    print("最佳5檔賣出量：", realdata["realtime"]["best_bid_volume"])
    print("最佳5檔買進價：", realdata["realtime"]["best_ask_price"])
    print("最佳5檔買進量：", realdata["realtime"]["best_ask_volume"])
else:
    print("錯誤：" + realdata["rtmessage"])

stock_id = "2330"  # 2330台積電

realdata = twstock.realtime.get(stock_id)  # 即時資料

print("realdata")
print(realdata)

result = pd.DataFrame(realdata).T.iloc[1:3]
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
print("result")
print(result.T)

print("------------------------------")  # 30個

stock_id = "2317"  # 2317鴻海

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

stocklist = stock.fetch(2019, 12)  # 取得 2019年12月 的資料

listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime("%Y-%m-%d"))
    listy.append(s.close)

plt.figure(figsize=[10, 8])

plt.title("2019年12月股價", fontsize=18)
plt.xlabel("日期", fontsize=14)
plt.ylabel("股價", fontsize=14)
plt.plot(listx, listy, "r:s")

plt.xticks(rotation=45)
plt.grid("k:", alpha=0.5)
plt.ylim(88, 93)
plt.yticks([88, 89, 90, 91, 92, 93])

show()

print("------------------------------")  # 30個

stock_ids = [stock_id1, stock_id2, stock_id3]
plt.figure(figsize=[10, 8])
for stock_id in stock_ids:
    stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件
    stocklist = stock.fetch(2019, 12)  # 取得 2019年12月 的資料
    listx = []
    listy = []
    for s in stocklist:
        listx.append(s.date.strftime("%Y-%m-%d"))
        listy.append(s.close)

    plt.plot(listx, listy)
    plt.xticks(rotation=45)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件
# 取得最近31筆資料

# 建立 x, y 軸串列，x 軸為日期時間(date)，y 軸為收盤價(close)
# 印出 stock.data[0]，可以觀察到「close」就是收盤價的價位資料

print(len(stock.data))
print(stock.data)  # 取得最近31筆資料
print()
print(stock.data[0])  # 第0筆資料

stocklist1 = stock.fetch(2023, 1)  # 取得 2023年1月 的資料
stocklist2 = stock.fetch(2023, 2)  # 取得 2023年2月 的資料

stocklist = stocklist1 + stocklist2

listx = []
listy = []
for value in stocklist:
    listx.append(value.date.strftime("%Y-%m-%d"))
    listy.append(value.close)

plt.figure(num="股票分析", figsize=(10, 10))

plt.xlabel("日期", fontsize="16")
plt.ylabel("股價", fontsize="16")
plt.title("股票分析", fontsize="18")

plt.plot(listx, listy, color="red", markersize="16", marker=".")

plt.xticks(rotation=45)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock_id = "2317"  # 2317鴻海

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

realdata = twstock.realtime.get(stock_id)  # 即時資料
print(realdata)

if realdata["success"]:
    print("即時股票資料：")
    print(realdata)  # 即時資料
    print("目前股價：")
    print(realdata["realtime"]["latest_trade_price"])  # 即時價格 最新成交價
    realprice = realdata["realtime"]["latest_trade_price"]  # 目前股價
    if realprice == "-":
        print("找不到資料")
    else:
        print("目前股價：" + realprice)
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
    print("目前股價：" + str(realprice))
    if mode == 1:
        message = "現在股價為 " + str(realprice) + "元，可以賣出股票了！"
    else:
        message = "現在股價為 " + str(realprice) + "元，可以買入股票了！"
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

stock_id = "2317"  # 2317鴻海

while True:
    realdata = twstock.realtime.get(stock_id)  # 即時資料
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
        print("錯誤：" + realdata["rtmessage"])
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

stock_id = "2317"  # 2317鴻海

while True:
    realdata = twstock.realtime.get(stock_id)  # 即時資料
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
        print("錯誤：" + realdata["rtmessage"])
        counterError = counterError + 1
        if counterError >= 3:  # 最多錯誤3次
            print("程式結束！")
            break
    for i in range(300):  # 每5分鐘讀一次
        time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# twstock 各個 API 比較

stock_id = "2317"  # 2317鴻海

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

data = stock.fetch(2026, 10)  # 取得 2020年1月 的資料
print("資料長度 :", len(data))

data = stock.fetch_31()
print("資料長度 :", len(data))

data = stock.fetch_from(2021, 9)
print("資料長度 :", len(data))

sys.exit()

print("------------------------------")  # 30個

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

data = stock.fetch(2020, 7)  # 取得 2020年7月 的資料
# data = stock.fetch_from(2020, 7) # ????

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

df[["close", "open", "high", "low"]].plot()  # df直接畫出
show()

print("------------------------------")  # 30個

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

data = stock.fetch_from(2019, 1)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

# 計算5天, 20天和60天移動平均線
df["MA5"] = df["close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["MA60"] = df["close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

df[["MA5", "MA20", "MA60"]].plot(figsize=(10, 5))  # df直接畫出 + 圖片大小
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

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

print("------------------------------")  # 30個

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

print(stock.moving_average(stock.price, 5))
print(stock.moving_average(stock.capacity, 5))

realdata = twstock.realtime.get(stock_id)  # 即時資料

data = stock.moving_average(stock.price, 5)

plt.plot(list(range(len(data))), data)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("判斷 四大買點、四大賣點")

from twstock import BestFourPoint

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

bfp = BestFourPoint(stock)

bfp_buy = bfp.best_four_point_to_buy()
print("是否為四大買點:", bfp_buy)
bfp_sell = bfp.best_four_point_to_sell()
print("是否為四大賣點:", bfp_sell)
bfp_result = bfp.best_four_point()
print("綜合判斷:", bfp_result)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

stock_id = "2317"  # 2317鴻海

# plt.figure(figsize=[12,30])
stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

slist = []

for i in range(1, 13):
    stocklist = stock.fetch(2019, i)  # 取得 2019年i月 的資料
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

show()

# lista = []
# list1 = [1,2,3,4,5]
# list2 = [7,8,9,10,11]
# list1.append(list2)
# list1

# 將資料寫出到csv檔
# 比較看看
filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(slist)

print("------------------------------------------------------------")  # 60個

print("讀取csv檔, 並畫出")

filename = "D:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv"

with open(filename, "r", newline="") as f:
    datas = csv.reader(f)
    listx = []
    listy = []
    # debug
    # for data in datas:
    #    print(data)
    for data in datas:
        listx.append(data[0])
        listy.append(data[5])

    # print(len(datas))
    # print(len(listx), len(listy))
    plt.figure(figsize=(20, 5))  # 圖像大小[英吋]
    plt.plot(listx, listy)
    plt.yticks(range(10, 200, 10))
    show()

# print([x[6] for x in datas])
# print(type(datas))

plt.figure(figsize=(20, 5))
plt.plot([x.close for x in slist])
show()

for data in datas:
    print(data)

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取資料存入資料庫")

import sqlite3

stock_id = "2330"  # 2330台積電

stock = twstock.Stock(stock_id)  # 以股票代號建立 Stock 物件

df = pd.DataFrame(stock.fetch_from(2026, 10))
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
print(df.head())
conn = sqlite3.connect("tmp_" + stock_id + ".db")
df.to_sql(stock_id, conn, if_exists="replace")
print("已經將股票資料存入SQLite資料庫...")

print("------------------------------------------------------------")  # 60個
print("使用 twstock SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("使用 twse ST")
print("------------------------------------------------------------")  # 60個

print("讀取上市公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_L.csv")
# r.encoding = "big5"
filename = "data/t187ap03_L.csv"

# df = pd.read_csv(filename, index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

# df.drop(df.index[len(df.index) - 1], inplace=True)

print(df)
print("---------------")  # 15個
print(df["公司代號"])
print("---------------")  # 15個
print(df[df["公司代號"] == 2330])

print("------------------------------")  # 30個

print("讀取上櫃公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_O.csv")
# r.encoding = "big5"
filename = "data/t187ap03_O.csv"

# df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
df = pd.read_csv(filename, index_col=False)

# df.drop(df.index[len(df.index)-1], inplace=True)

print(df)

print("------------------------------")  # 30個

print("讀取興櫃公司基本資料")

# r = requests.get("http://dts.twse.com.tw/opendata/t187ap03_R.csv")
# r.encoding = "big5"

# df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)

filename = "data/t187ap03_R.csv"

df = pd.read_csv(filename, index_col=False, skiprows=1)

df.drop(df.index[len(df.index) - 1], inplace=True)
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("下載月營收")


def monthly_report(year, month):
    # 假如是西元，轉成民國
    if year > 1911:
        year -= 1911

    url = (
        "https://mops.twse.com.tw/nas/t21/sii/t21sc03_"
        + str(year)
        + "_"
        + str(month)
        + "_0.html"
    )
    if year <= 98:
        url = (
            "https://mops.twse.com.tw/nas/t21/sii/t21sc03_"
            + str(year)
            + "_"
            + str(month)
            + ".html"
        )

    # 偽瀏覽器
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }

    print(url)

    # 下載該年月的網站，並用pandas轉換成 dataframe
    r = requests.get(url, headers)
    r.encoding = "big5"
    html_df = pd.read_html(StringIO(r.text))

    print(html_df)

    # 處理一下資料
    if html_df[0].shape[0] > 500:
        df = html_df[0].copy()
    else:
        df = pd.concat([df for df in html_df if df.shape[1] <= 11])

    print(df)

    # df = df[list(range(0,10))]
    # column_index = df.index[(df[0] == '公司代號')][0]
    # df.columns = df.iloc[column_index]
    # df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    # df = df[~df['當月營收'].isnull()]
    # df = df[df['公司代號'] != '合計']

    return df


df = monthly_report(2017, 1)

print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("下載財報")


def financial_statement(year, season, exchange="sii", type="綜合損益表"):
    if year > 1911:
        year -= 1911

    if type == "綜合損益表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb04"
    elif type == "資產負債表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb05"
    elif type == "營益分析查詢彙總表":
        url = "http://mops.twse.com.tw/mops/web/ajax_t163sb06"
    else:
        print("type does not match")

    print(url)

    # 一些參數：
    # TYPEK => 市場別
    # sii>上市
    # otc>上櫃
    # rotc>興櫃
    # pub>公開發行

    # year => 年度
    # season => 季別
    r = requests.post(
        url,
        {
            "encodeURIComponent": 1,
            "step": 1,
            "firstin": 1,
            "off": 1,
            "TYPEK": exchange,
            "year": year,
            "season": season,
        },
    )

    r.encoding = "utf8"
    dfs = pd.read_html(r.text)

    print(dfs)

    for i, df in enumerate(dfs):
        df.columns = df.iloc[0]
        dfs[i] = df.iloc[1:]

    df = pd.concat(dfs).applymap(lambda x: x if x != "--" else np.nan)
    df = df[df["公司代號"] != "公司代號"]
    df = df[~df["公司代號"].isnull()]
    if any(df.columns.str.contains("合計：")):
        df = df.loc[:, ~df.columns.str.contains("合計：")]
    return df


""" fail
df = financial_statement(2017, 2, type='營益分析查詢彙總表')
print(df[df['公司名稱']=='台泥'])
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("國內主要金融指標")

# 政府開放資料平台 - 國內主要金融指標
# https://data.gov.tw/dataset/30815

url_by_month = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000037-51i"
print(url_by_month)

r = requests.get(url_by_month)
df = pd.read_csv(StringIO(r.text))

print(df.set_index("月別"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
print('證券商分公司基本資料')

# 讀取證券商分公司基本資料

r = requests.get("http://www.twse.com.tw/brokerService/branchList.csv")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
print('讀取證券商總公司基本資料')

r = requests.get("http://www.twse.com.tw/brokerService/brokerList.csv?lang=zh")
r.encoding = "big5"
df = pd.read_csv(StringIO(r.text), index_col=False, skiprows=1)
print(df)
"""

print("------------------------------------------------------------")  # 60個

""" NG 資料抓不下來
print('讀取 Nasdaq 的股價歷史資料')

symbol = 'GOOG'.lower()

url_template = "https://www.nasdaq.com/symbol/{symbol}/historical"
url = url_template.format(symbol=symbol)
print(url)

rs = requests.session()
r = rs.get(url)
soup = BeautifulSoup(r.text, 'lxml')
params = soup.select('#getFile input')
# 時間長短：5d, 1m, 3m, 6m, 1y, 18m, 2y, 3y, 4y, 5y, 6y, 7y, 8y, 9y, 10y
timeframe = '{timestr}|true|{symbol}'.format(timestr='3m', symbol=symbol.upper())
payload = {}

for tag in params:
    if tag['name'] != 'ctl00$quotes_content_left$submitString':
        payload[tag['name']] = tag['value']
    else:
        payload[tag['name']] = timeframe

#r = rs.post(url, data=payload)
r = rs.post(url, data=payload, verify=False)
print(r.text)
"""

print("------------------------------------------------------------")  # 60個

""" NG 資料抓不下來
print('讀取 NASDAQ, NYSE, AMEX 公司資料')

url_template = "https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange={}&render=download"

url = url_template.format('NASDAQ')

df = pd.read_csv(url)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)
"""

print("------------------------------------------------------------")  # 60個

print("讀取景氣對策信號")

"""
網址：政府開放資料 - 國發會 景氣指標及燈號
https://www.ndc.gov.tw/News_Content.aspx?n=9D32B61B1E56E558&sms=9D3CAFD318C60877&s=C367F13BF38C5711
應用：
可以利用景氣對策信號判斷 ETF 的進入點。
"""

""" NG 無檔案
from io import BytesIO

# 讀取 .xlsx 檔

r = requests.get('https://ws.ndc.gov.tw/Download.ashx?u=LzAwMS9hZG1pbmlzdHJhdG9yLzEwL3JlbGZpbGUvNTc4MS82MzkyL2VmMWQ4ZjliLTMxOGMtNDFmZC1hNzgzLWVjNGY5MTMwMjRmOC54bHN4&n=5paw6IGe56i%2f6ZmE5Lu25pW45YiXLnhsc3g%3d&icon=..xlsx')
df = pd.read_excel(BytesIO(r.content))

df = df.set_index('DATE')

df['2010-01-01':]['景氣對策信號綜合分數'].plot()

show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直接取得csv檔資料

datestr = "20240716"

url = (
    "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
    + datestr
    + "&type=ALLBUT0999"
)
print(url)

# 下載股價
response = requests.get(url)
# print(response.text)  # HTML網頁內容, 即csv檔的內容

r_text = response.text.split("\n")

r_text = [i for i in r_text if len(i.split('",')) == 17 and i[0] != "="]

data = "\n".join(r_text)

df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=["Unnamed: 16"])

stock_symbol = "2330"  # 台積電
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("下載台股單日股價行情")

datestr = "20180131"

r = requests.get(
    "http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
    + datestr
    + "&type=ALL"
)

# pandas 會自動把字串裡的單一引號 (") 去除

df = pd.read_csv(
    StringIO(
        "\n".join(
            [
                i.translate({" ": None})
                for i in r.text.split("\n")
                if len(i.split('",')) == 17 and i[0] != "="
            ]
        )
    ),
    header=0,
    thousands=",",
)

df = df.loc[:, ~df.columns.str.contains("Unnamed")]

print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台股股價歷史資料")

print("讀取台股股價資料")

url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY"
params = {}
params["stockNo"] = "2330"
params["date"] = "20160101"
params["response"] = "csv"

r = requests.get(url, params=params)

import datetime

df = pd.read_csv(
    StringIO(r.text), engine="python", skiprows=1, skipfooter=4, thousands=","
)


def DateConvert(twdate):
    x = twdate.split("/")
    return datetime.date(int(x[0]) + 1911, int(x[1]), int(x[2]))


df["日期"] = df["日期"].map(DateConvert)
df = df.loc[:, ~df.columns.str.contains("Unnamed")]
print(df)

print("------------------------------------------------------------")  # 60個
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
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("110年8月股市趨勢圖")
"""
plt.grid(True)

# 存成圖片, 要放在show()之前
# plt.savefig("matplotlib_chart.png")

show()

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 4.5 台灣證券交易所API
# 這個API長得大概像這樣:
# http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20160501&stockNo=2330
# 比較重要的地方是date這個參數, 基本上你給的值一定要是yyyyMMdd的形式, 但是真正作用的只有yyyy與MM, 因為他會把這段request解讀成你想要看stockNo股票在yyyy年MM月的紀錄, 所以dd基本上沒有太大意義, 但卻是不可少的部分.

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

# 臺灣證券交易所-基本市況報導網站 MIS
# https://mis.twse.com.tw/stock/

# 元大寶來台灣卓越50證券投資信託基金
# TPE: 0050

url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw"
response = requests.get(url)
json_data = json.loads(response.text)

print(type(json_data))
print(json_data)

print("全名 :", json_data["msgArray"][0]["nf"])
print("簡稱 :", json_data["msgArray"][0]["n"])
print("最高 :", json_data["msgArray"][0]["h"])
print("最低 :", json_data["msgArray"][0]["l"])
print("昨收 :", json_data["msgArray"][0]["y"])
print("開盤 :", json_data["msgArray"][0]["o"])
print("成交 :", json_data["msgArray"][0]["z"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台股即時股價資料")

# 取得需要的 URL
SESSION_URL = "http://mis.twse.com.tw/stock/index.jsp"
STOCKINFO_URL = (
    "http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_id}&_={time}"
)


def get_realtime_quote(stockNo, ex="tse"):
    req = requests.Session()
    req.get(SESSION_URL)

    stock_id = "{}_{}.tw".format(ex, stockNo)

    r = req.get(STOCKINFO_URL.format(stock_id=stock_id, time=int(time.time()) * 1000))

    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {"rtmessage": "json decode error", "rtcode": "5000"}


print(get_realtime_quote("2330"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# yearurl.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
for i in range(1, 13):  # 取1到12數字
    url_twse = urlbase + twodigit(i) + urltail  # 組合網址
    print(url_twse)


# stockmonth.py
def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

filepath = "stockmonth01.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    url_twse = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2317&_=1521363562193"
    res = requests.get(url_twse)  # 回傳為json資料
    jdata = json.loads(res.text)  # json解析

    outputfile = open(filepath, "w", newline="", encoding="utf-8")  # 開啟儲存檔案
    outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
    outputwriter.writerow(jdata["fields"])
    for dataline in jdata["data"]:  # 寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear.py
def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:108/01/01->20190101
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

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
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


# stockyear_plotly.py
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


from plotly.graph_objs import Scatter, Layout
from plotly.offline import plot

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2019"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "stockyear2019.csv"

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
data = [
    Scatter(x=pdstock["日期"], y=pdstock["收盤價"], name="收盤價"),
    Scatter(x=pdstock["日期"], y=pdstock["最低價"], name="最低價"),
    Scatter(x=pdstock["日期"], y=pdstock["最高價"], name="最高價"),
]
plot({"data": data, "layout": Layout(title="2019年個股統計圖")}, auto_open=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉換民國日期為西元:106/03/02->20170302
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
filepath = "tmp_stockyear2017a.csv"

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
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉換民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

url_twse = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20170101&stockNo=2317&_=1521363562193"
filepath = "tmp_stockmonth01.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    res = requests.get(url_twse)  # 回傳為json資料
    jdata = json.loads(res.text)  # json解析

    outputfile = open(filepath, "w", newline="", encoding="utf-8")  # 開啟儲存檔案
    outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
    outputwriter.writerow(jdata["fields"])
    for dataline in jdata["data"]:  # 寫入資料
        outputwriter.writerow(dataline)
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
pdstock.plot(kind="line", figsize=(12, 6), x="日期", y=["收盤價", "最低價", "最高價"])  # 繪製統計圖


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base_url = "https://www.twse.com.tw"
url = base_url + "/zh/brokerService/brokerServiceAudit"
# https://www.twse.com.tw/brokerService/brokerServiceAudit?showType=list&stkNo=1020&focus=6

csvfile = "tmp_BrokerBranchs.csv"

items = []
print("爬取總公司: ", url)
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one(".grid")  # 找到<table>
rows = tag_table.find_all("tr")  # 找出所有<tr>
for row in rows:
    item = []
    for cell in row.find_all(["td"]):
        txt = cell.text.replace("\n", "").replace("\r", "").strip()
        if txt == "明細":
            new_url = base_url + cell.find("a").get("href")
            print("爬取分公司: ", new_url)
            r2 = requests.get(new_url)
            r2.encoding = "utf8"
            soup2 = BeautifulSoup(r2.text, "lxml")
            tag_table2 = soup2.select_one(".grid.links")  # 找到<table>
            rows2 = tag_table2.find_all("tr")  # 找出所有<tr>
            for row2 in rows2:
                item_branch = []
                for cell2 in row2.find_all("td"):
                    txt = cell2.text.replace("\n", "").replace("\r", "").strip()
                    item_branch.append(txt)
                if item_branch and len(item_branch) == 5:
                    items.append(item_branch)  # 新增分公司
        else:
            item.append(txt)
    if item and len(item) == 5:
        items.append(item)  # 新增總公司
    time.sleep(1)

print("券商總數(總公司+分公司):", len(items))
# 開啟CSV檔案寫入截取的資料
with open(csvfile, "w+", newline="", encoding="utf8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["證券商代號", "證券商名稱", "開業日", "地址", "電話"])
    for item in items:
        writer.writerow(item)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import datetime
import pandas_datareader as pdr

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
""" NG
df = pdr.DataReader("2330.TW", "yahoo", start, end)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major1.json", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=csv&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major2.csv", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
if r.status_code == requests.codes.ok:
    print("成功爬取資料...")
    """# NG
    data = r.json() 
    df = pd.read_json(json.dumps(data["data"]))
    df.columns = data["fields"]
    print(df.head())
    df.to_csv("tmp_three_major3.csv", index=False)
    """
else:
    print("HTTP請求錯誤...")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dates = [20250601, 20250701, 20250801]
stockNo = 2330

url = (
    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
)

for date in dates:
    print(date, stockNo)
    # data = pd.read_html(r.text)[0]  # old
    data = pd.read_html(url.format(date, stockNo))[0]

    data.columns = data.columns.droplevel(0)

    csvfile = "tmp_stock_{}_{}.csv".format(stockNo, date)
    data.to_csv(csvfile, index=False)
    time.sleep(5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("使用 twse SP")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("使用 其他 金融匯率股票相關 ST")
print("------------------------------------------------------------")  # 60個

print("google-currency：不同幣值換算")

from google_currency import convert

print(convert("USD", "JPY", 230))

from google_currency import convert

samount = 100  # @param {type:'integer'}
damount = convert("USD", "JPY", samount)
retdict = json.loads(damount)
print("{} 元美金 = 日幣 {} 元".format(samount, retdict["amount"]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

msg = "這是 LINE Notify 發送的訊息。"
token = "你的 LINE Notify 權杖"  # 權杖
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("TWCB：中央銀行資料庫")

import TWCB

print(TWCB.get_info())

df1 = TWCB.get("BP01D01.px")
print(df1)

df1.to_csv("匯率日報表.csv")

data_list = TWCB.get_by_search("美元之匯率")

TWCB.get_all()

with open("download_TWCB.json", "r", encoding="utf-8") as f:
    test_data = json.load(f)

if not os.path.isdir("twcb"):
    os.mkdir("twcb")

for key in test_data.keys():
    data = pd.read_json(test_data[key])
    data.to_csv("twcb/" + key + ".csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

API_KEY = "fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    print(url)
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None


print("轉換匯率")

base = "USD"

data = convert_currency(base)

del data[base]

for ticker, value in data.items():
    print(f"{ticker}: {value}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
查詢歷史資料 範例
https://rate.bot.com.tw/xrt/all/2023-03-20

https://rate.bot.com.tw/

(台銀牌告匯率)
https://rate.bot.com.tw/xrt?Lang=zh-TW
"""


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------")  # 30個

i = 0
for cell in cells:
    print(i)
    print(cell.text.strip())
    i = i + 1

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

prices = list()
for price in buyingrate:
    prices.append(price.text.strip())
print(prices)

print("------------------------------")  # 30個

print(names)
print(prices)
rates = zip(names, prices)
for rate in rates:
    print(rate)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from lxml import html

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
response = requests.get(url)
tree = html.fromstring(response.text)

print(
    "美金："
    + str(
        tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()")[0]
    )
)
print(
    "日圓："
    + str(
        tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()")[0]
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台灣銀行 匯率查詢")

url = "https://rate.bot.com.tw/xrt/flcsv/0/day"  # 牌告匯率 CSV 網址

response = requests.get(url)  # 爬取網址內容
response.encoding = "utf-8"  # 網頁編碼模式  # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = response.text  # 以文字模式讀取內容
rts = rt.split("\n")  # 使用「換行」將內容拆分成串列
for i in rts:  # 讀取串列的每個項目
    try:  # 使用 try 避開最後一行的空白行
        a = i.split(",")  # 每個項目用逗號拆分成子串列
        print(a[0] + ": " + a[12])  # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
    except:
        break

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#ie11andabove > div > table")
rows = tag_table.find_all("tr")
with open(csvfile, "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n", "").replace("\r", ""))
        writer.writerow(lst)

print("------------------------------")  # 30個


def split_name(name):
    pos = name.find(")")
    return pd.Series({'"幣別"': name[0:pos].strip() + ")"})


df = pd.read_csv("tmp_xrt.csv", encoding="big5")
df = df.drop(df.index[[0, 1]])
df = df.iloc[:, 0:5]
df.columns = ["幣別", "現金(買)", "現金(賣)", "即期(買)", "即期(賣)"]
df["幣別"] = df["幣別"].apply(split_name)
df.to_csv("tmp_xrt2.csv", index=False, encoding="big5")
print(df.head())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

base_url = "https://www.cbc.gov.tw/tw/"
url = base_url + "lp-645-1.html"
csvfile = "tmp_USxrt.csv"
items = []
next_page = True

while next_page:
    print(url)
    r = requests.get(url)
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_table = soup.find("table", class_="rwd-table")  # 找到<table>
    rows = tag_table.find_all("tr")  # 找出所有<tr>
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n", "").replace("\r", ""))
        items.append(lst)
    # 找尋下一頁按鈕的<a>標籤
    tag_li = soup.find("li", class_="next")
    if tag_li:
        next_page = True
        url = base_url + tag_li.find("a").get("href")
        time.sleep(2)
    else:
        next_page = False

with open(csvfile, "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in items:
        writer.writerow(item)

print("------------------------------")  # 30個

csvfile = "tmp_USxrt.csv"
df = pd.read_csv(csvfile)
df.drop_duplicates(keep=False, inplace=True)
df.to_csv("tmp_USxrt2.csv", index=False, encoding="utf8")
print(df.head(5))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查詢台銀牌告匯率")

from time import localtime
from time import strftime
from os.path import exists  # 台銀匯率網站

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")  # 回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml")  # 解析網頁，建立bs物件
for single_tr in (
    bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr")
):  # 針對匯率表格分析
    cell = single_tr.findAll("td")  # 找到每一個表格
    currency_name = (
        cell[0].find("div", {"class": "visible-phone"}).contents[0]
    )  # 找到表格中幣別
    currency_name = currency_name.replace("\r", "")  # 取代不需要的字元
    currency_name = currency_name.replace("\n", "")
    currency_name = currency_name.replace(" ", "")
    currency_rate = cell[2].contents[0]  # 找到幣別匯率
    print(currency_name, currency_rate)
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())  # 記錄目前時間
    data = [["時間", "匯率"], [now_time, currency_rate]]  # 準備寫入檔案資料
    print("寫入資料 :", data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#ie11andabove > div > table")
rows = tag_table.find_all("tr")
with open(csvfile, "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n", "").replace("\r", "").strip())
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("使用 其他 金融匯率股票相關 SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個

"""
股票資料彙整_YahooFinance
股票資料彙整_Yahoo股市

#使用 pandas_datareader.data.DataReader 抓取 2356.TW, 1566.TWO 最近一個月的股價資料

#股票資料彙整_YahooFinance

import timeit
from pandas_datareader import data, wb


def getWebData(name, 
               start = datetime.date(1970, 1, 1), 
               end = datetime.date.today(), 
               data_source = 'yahoo', 
               retry_count=3, 
               pause=0.001):
    
    df = data.DataReader(name = name, 
                         data_source = data_source,
                         start = start,
                         end = end,
                         retry_count = retry_count,
                         pause = pause
                        ) 

    df = df.to_frame()
    df.index.names = ['Date', 'Name'] 
    
    return df

def fetchAndStoreStockData(stocks):
    
#     start = datetime.datetime(1965, 1, 1)
#     end = datetime.datetime(2013, 1, 1)    
    df = getWebData(stocks)     

    # Write to files __________________________    
    df.to_excel('Yahoo Finance{0}.xlsx'.format(''))

fetchAndStoreStockData(stocks = ['2356.TW', '1566.TWO'])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 練習 - 股票資料彙整_Yahoo股市 - 問題

page = 1
url = "https://tw.stock.yahoo.com/s/list.php?c=tse&pid=" + str(page)
url

"""
目標:

使用 Pandas，抓取上述 url 網頁中的股價資料
將股票代號與名稱區隔為不同的欄位
將資料儲存為 Excel 檔案
須注意個欄位的格式，數字欄位的儲存格式應該為數字
重排欄位順序為:
'市場別', '股票代號', '股票名稱', '日期', '時間', 
'成交', '買進', '賣出', '漲跌', '張數',
'昨收', '開盤', '最高', '最低'

匯集 Yahoo 股市 page 1~ 5 的資料 (pd.concat)
依據股票代號的前兩碼，做 GroupBy 操作
merge ../data/個股_類別.xls(先解壓縮 個股_類別.rar) 中的資料之後，做 GroupBy 操作
"""
# 股票資料彙整_Yahoo股市

# 目標資料來源:
# https://tw.stock.yahoo.com/s/list.php?c=tse&pid=1

# 抓取網頁資料


def get_yahoo_page_html(url):
    html = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
        },
    )
    return html.text


def getDataOnePage(html):
    targetTableIndex = 0
    table = pd.read_html(
        html,
        attrs={
            "border": "1",
            "cellspacing": "0",
            "cellpadding": "2",
            "bgcolor": "#ffffff",
        },
        header=0,
    )[targetTableIndex]

    return table


def getDataOnePageTSE(page):
    url = "https://tw.stock.yahoo.com/s/list.php?c=tse&pid=" + str(page)
    return getDataOnePage(html=get_yahoo_page_html(url))


# 抓第一頁的資料
df = getDataOnePageTSE(1)

cc = df.tail()
print(cc)

df.to_excel("tmp_stock.xlsx")

# 修整 DataFrame中的資料


def fixTable(marketType, table, theDate=datetime.date.today()):
    fixedTable = table

    # Drop
    fixedTable.drop(["選擇", "凱基證券下單"], axis=1, inplace=True)
    fixedTable.dropna(axis=0, how="all", inplace=True)

    # fill missing data
    fixedTable["股票代號名稱"] = fixedTable["股票代號"]
    fixedTable["股票代號"] = fixedTable["股票代號名稱"].map(lambda x: x.split()[0])
    fixedTable["股票名稱"] = fixedTable["股票代號名稱"].map(lambda x: x.split()[1])
    fixedTable["日期"] = theDate
    fixedTable["市場別"] = marketType

    # data type
    fixedTable.replace("－", np.nan, inplace=True)

    fixedTable["股票代號"] = fixedTable["股票代號"].astype(str)
    fixedTable["時間"] = fixedTable["時間"].astype(datetime.time)
    fixedTable[["成交", "買進", "賣出", "張數", "昨收", "開盤", "最高", "最低"]] = fixedTable[
        ["成交", "買進", "賣出", "張數", "昨收", "開盤", "最高", "最低"]
    ].astype(float)

    fixedTable["漲跌"] = fixedTable["成交"] - fixedTable["昨收"]
    fixedTable["漲跌"] = fixedTable["漲跌"].map(lambda x: round(x, 2))

    # sort
    #     fixedTable.sort_values(by = '股票代號', inplace = True)

    # indexing
    fixedTable.index = pd.Series(range(len(fixedTable)))
    fixedTable.index.name = "項次"
    fixedTable = fixedTable.reindex(
        columns=[
            "市場別",
            "股票代號",
            "股票名稱",
            "日期",
            "時間",
            "成交",
            "買進",
            "賣出",
            "漲跌",
            "張數",
            "昨收",
            "開盤",
            "最高",
            "最低",
        ]
    )

    return fixedTable


df1 = fixTable("TSE", df)

cc = df1.tail()
print(cc)

# 彙整 Yahoo 股市 page 1~ 5 的資料

# 抓第一頁~第五頁的資料
dfs = map(lambda p: fixTable("TSE", getDataOnePageTSE(p)), range(1, 6))

# Append 在一起
df = pd.concat(dfs)
len(df)

# 1000

df.index = pd.Index(range(len(df)))  # 重新編排 row index 編號
df = df[df["股票代號"].str.len() <= 4]  # 濾除 權證 資料

cc = df.tail()
print(cc)

# 抓取 類股 資料

df_類股 = pd.read_excel("..\\data\個股_類別.xls")  # 需先解壓縮 個股_類別.rar

cc = df_類股.tail()
print(cc)

# Merge

mdf = df.merge(df_類股, left_on="股票代號", right_on="個股_代號", how="left")  # merge
mdf = mdf.drop(["市場別_ID", "個股_代號", "個股_名稱"], axis=1)  # drop 多於的欄位

cc = mdf.tail()
print(cc)

# GroupBy

# 各類股有多少支個股
mdf.groupby(["類股_名稱"]).size().sort_index()


# 各類股 平均股價
mdf.groupby(["類股_名稱"])["成交"].mean().sort_index()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# syntax sort_values
price_df = price_df.sort_values("date")

# 建立欄位
price_df["adj_factor"] = 1.0

# syntax
# 添加必要的欄位
sp500_data = sp500_data.reset_index()  # 重設索引，將日期移到普通欄位
sp500_data["date"] = sp500_data["Date"]  # 添加 'date' 欄位

# 移除原本的 'Datetime' 欄位
sp500_data = sp500_data.drop(columns=["Date"])

# 將所有欄位名稱轉為小寫，以符合 FeatureEngineer 的預期格式
sp500_data.columns = [col.lower() for col in sp500_data.columns]

print("------------------------------")  # 30個

# 頻率轉換、合併多個表格

# 下載每日股價

# 台泥 1101

print("轉換為月頻率")
df_quote_new = df_quote.resample("ME").mean()
print(df_quote_new)


print("讀取月營收資料")
df_monthly_sales = pd.read_csv("./data/stock_monthly_sales.csv")

print("檢視前幾行\n", df_monthly_sales.head())

print("轉換日期格式")
df_quote_new = df_quote.reset_index()

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

# 欄位改名
df.rename({"單月營收": "sales"}, axis=1, inplace=True)  # df修改欄位名稱
print(df)

print("計算股價與月營收關聯度")

cc = df[["sales", "Adj Close"]].corr()  # 相關係數
cc = df[["sales", "Adj Close"]].corr()  # 相關係數
print(cc)
print(cc)

df = pd.merge(
    left=df_monthly_sales,
    right=df_quote_new,
    left_on="年月",
    right_on="Date",
    how="inner",
)

syntax
df = df[["Date", "單月營收", "Adj Close"]]  # 取出部分欄位

df.rename({"單月營收": "sales"}, axis=1, inplace=True)  # df修改欄位名稱

print("------------------------------------------------------------")  # 60個

# 添加必要的欄位
sp500_data = sp500_data.reset_index()  # 重設索引，將日期移到普通欄位
sp500_data["date"] = sp500_data["Datetime"]  # 添加 'date' 欄位
sp500_data["tic"] = "^GSPC"  # 添加 'tic' 欄位，這裡 '^GSPC' 是 S&P 500 的代號

# 移除原本的 'Datetime' 欄位
sp500_data = sp500_data.drop(columns=["Datetime"])

# 將所有欄位名稱轉為小寫，以符合 FeatureEngineer 的預期格式
sp500_data.columns = [col.lower() for col in sp500_data.columns]

# 顯示處理後的數據
print("檢視前幾行\n", sp500_data.head())

print("------------------------------------------------------------")  # 60個


# 從台灣證券交易所 下載股價資料


def crawl_data(date, symbol):
    print("下載股價, 從台灣證券交易所")
    url = (
        "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="
        + date
        + "&type=ALL"
    )
    print(url)
    response = requests.get(url)

    df = df.drop(columns=["Unnamed: 16"])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    df_columns = filter_df.columns
    return list(filter_df.iloc[0]), filter_df.columns


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("df語法 與 畫圖 ST")
print("------------------------------------------------------------")  # 60個

# 做不等大的子圖 ST

fig = plt.figure(num="matplotlib 02", figsize=(8, 8))

grid = plt.GridSpec(12, 10, wspace=0.5, hspace=0.5)

ax1 = fig.add_subplot(grid[0:8, 0:12])  # 設置K線圖的尺寸

data = [1, 2, 3, 4, 5]
ax1.plot(range(len(data)), data, color="red", lw=2, label="資料1")

plt.title("做不等大的子圖", fontsize=14)
plt.ylabel("y縱軸標題", fontsize=14)
plt.legend(loc="best")
ax1.set_xticks([])  # 日期標注在下圖中，故清空此處x軸刻度
ax1.set_xticklabels([])  # 日期標注在下圖中，故清空此處x軸

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8:10, 0:12])  # 設置成交量圖形尺寸
# ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
# ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation=30)
plt.xlabel("日 期", fontsize=14)

# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]  # ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))  # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)  # 生成橫軸標注位置列表
xticks_str = list(map(lambda x: date_list[int(x)], xticks_num))  # 生成正在標注日期列表
ax2.set_xticks(xticks_num)  # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)  # 設置橫軸標注日期

show()

# 做不等大的子圖 SP

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 開始時間 為 60天前
start = datetime.datetime.now() - datetime.timedelta(days=60)

# 結束時間 為 現在
end = datetime.date.today()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8), dpi=100)

# ax1.set_title("開盤價、收盤價 ( " + df["date"][0] + " ~ " + df["date"][-1] + " )")
ax1.set_title("開盤價、收盤價")
# ax1.set_title("K 線圖")

# 畫子圖(ax1)
ax1.plot(day, openprice, "s-", color="r", label="開盤價")
ax1.legend(loc="best", fontsize=10)
ax1.grid(True)

# 畫子圖(ax2)
ax2.plot(day, close, "o-", color="g", label="收盤價")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)

show()

print("------------------------------------------------------------")  # 60個
print("df語法 與 畫圖 SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.rcParams["font.sans-serif"] = "mingliu"  # 設定中文字型

