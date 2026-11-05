# Python 測試 FinMind

# 方案一：抓台股首選 —— 使用 FinMind（台灣團隊開發，免申請 Key）
# 這是台灣金融資料開源團隊做的，直接對接台灣證交所，抓台股快又穩定，絕對不會有退市或時區錯誤。

# pip install finmind

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


print("------------------------------------------------------------")  # 60個
print("使用 FinMind ST")
print("------------------------------------------------------------")  # 60個

from FinMind.data import DataLoader

api = DataLoader()

cc = help(api.taiwan_stock_dividend_result)
# print(cc)


"""
台股總覽 TaiwanStockInfo
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
台股總覽(含權證) TaiwanStockInfoWithWarrant
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
台股交易日 TaiwanStockTradingDate
提供台股交易日。
資料更新時間-星期一至五 18:00，實際更新時間以 API 資料為主。
"""

"""
import requests
import pandas as pd
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
股價日成交資訊 TaiwanStockPrice
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

# 除權息, 一次只能查一天
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
df.to_pickle("tmp_df_data1.pkl")
"""
# 讀取pickle檔案資料
df1 = pd.read_pickle("tmp_df_data1.pkl")
# print("比較df df1是否相同", df.equals(df1))
df = df1.tail(30)

# 取得資料內容
print("列印取得的日線資料, 前5筆")
print(df)

# print("檢視前幾行\n", df.head())
print("df的形狀 : ", df.shape)
print("df的欄位 : ", df.columns.tolist())

print("------------------------------")  # 30個

print('撈出一部分資料')

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
stock_id        （證券代號）：股票的四碼或六碼代號（例如 2330 代表台積電）。
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
volume = df["Trading_Volume"].astype(float)  # 成交量（Trading_Volume）
money = df["Trading_money"].astype(float)  # 成交金額（Trading_money）
_open = df["open"].astype(float)  # 開盤價 Open
_max = df["max"].astype(float)  # 最高價 High
_min = df["min"].astype(float)  # 最低價 Low
close = df["close"].astype(float)  # 收盤價 Close
spread = df["spread"].astype(float)  # 買賣價差（Spread）
turnover = df["Trading_turnover"].astype(float)  # 交易筆數（Trading_turnover）

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
plt.title("台積電 (2330) 歷史走勢圖", fontsize=12)
plt.xticks(rotation=30)

plt.show()

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

print('aaaa')
print("檢視前幾行\n", df.head())

# 2. 將 Date 轉為時間格式，並設定為索引 (Index)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

print('bbbb')
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

df["Daily_Return"] = df["Close"].pct_change()  # 每日漲跌幅, pct_change() : 與前項差的百分比

print("------------------------------")  # 30個

print('計算每日漲跌幅 PCT')
my_pct = []  # pct
my_pct.append(0)
M, N = df.shape
for idx in range(M):
    if idx>0:
        dd = df["Close"].iloc[idx]-df["Close"].iloc[idx-1]
        pp = dd/df["Close"].iloc[idx]
        print(idx, df["Close"].iloc[idx], dd, pp)
        my_pct.append(pp)

# 將pct塞回 DataFrame 中，方便繪圖
df["PCT"] = my_pct

print("------------------------------")  # 30個

# 畫週線MA5, 月線MA20

df["ma5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["ma20"] = df["Close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均

df["daily_return"] = df["Close"].pct_change()  # 每日漲跌幅, pct_change() : 與前項差的百分比

_ma5 = df["ma5"].astype(float)  # 開盤價 Open
_ma20 = df["ma20"].astype(float)  # 開盤價 Open
_daily_return = df["daily_return"].astype(float)  # 開盤價 Open

print(_ma5)

M, N = df.shape

day = df["date"].astype(str)  # 日期

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
plt.bar(range(M), df["Volume"]/1000, facecolor="#99ccff")
plt.ylabel("成交量(張)")
plt.xticks(range(M), df["date"], rotation=30)

plt.show()

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
# 這裡我們傳入一個字型清單，讓系統去抓微軟正黑體（Windows）或蘋方體（Mac）

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
    title="台積電 (2330) 歷史走勢圖",
    ylabel="股價 (元)",
    ylabel_lower="成交量",
)

print("------------------------------------------------------------")  # 60個

# 自動標記買賣訊號程式碼

"""
# 即時讀取網路資料
print("抓取台積電 (2330) 2026年8月到10月的日線資料")
start_date = "2026-08-01"
end_date = "2026-11-01"
stock_id = "2330"
df = get_stock_data(stock_id, start_date, end_date)
"""
# 讀取pickle檔案資料
df1 = pd.read_pickle("tmp_df_data1.pkl")
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
    title="台積電 (2330) 均線策略買賣訊號圖",
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

plt.show()

print("------------------------------------------------------------")  # 60個
print("使用 FinMind SP")
print("------------------------------------------------------------")  # 60個

# 讀取pickle檔案資料
df = pd.read_pickle("tmp_df_data1.pkl")
# df = df.tail(5)

print("df的形狀 : ", df.shape)
print(df)

# 計算5天和20天的移動平均線
df["MA5"] = df["close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均

# 繪製收盤價和移動平均線
# plt.figure(figsize=(10, 6))
plt.figure(figsize=(10, 8))
plt.plot(df["close"], label="收盤價", color="r")
plt.plot(df["MA5"], label="週線", color="g")
plt.plot(df["MA20"], label="月線", color="b")
plt.title("TSMC股價 5 日和 20 日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()
plt.grid(True)

plt.show()


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

print("------------------------------------------------------------")  # 60個

# 讀取pickle檔案資料
df = pd.read_pickle("tmp_df_data1.pkl")

# 計算5天, 20天和60天移動平均線
df["MA5"] = df["close"].rolling(window=5).mean()  # 移動平均線 (MA5) 連同過去N點平均
df["MA20"] = df["close"].rolling(window=20).mean()  # 移動平均線 (MA20) 連同過去N點平均
df["MA60"] = df["close"].rolling(window=60).mean()  # 移動平均線 (MA60) 連同過去N點平均

# 繪製股價和移動平均線
# plt.figure(figsize=(10, 6))
plt.figure(figsize=(10, 8))
plt.plot(df["close"], label="收盤價", color="r")
plt.plot(df["MA5"], label="週線", color="g")
plt.plot(df["MA20"], label="月線", color="b")
plt.plot(df["MA60"], label="半年線", color="c")

# 標題和圖例
plt.title("TSMC股價 5 日, 20 日和 60日移動平均線")
plt.xlabel("日期")
plt.ylabel("價格")
plt.legend()

plt.show()

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

r[-100:].plot()

plt.show()


# 原本股價圖波動的很厲害，現在我們想讓它變得平滑一點，改看每 20 天的平均

P = df["TT"]  # 取出一欄資料

print(P.rolling(window=20).mean())  # 移動平均線 (MA20) 連同過去N點平均

P.rolling(window=20).mean().plot()  # 移動平均線 (MA20) 連同過去N點平均

plt.show()

# 和原本的股價圖比較

P.plot()
P.rolling(window=20).mean().plot()  # 移動平均線 (MA20) 連同過去N點平均

plt.show()

# 當然也可以算更多天的平均，會變得更平滑

P.plot()
P.rolling(window=20).mean().plot()  # 移動平均線 (MA20) 連同過去N點平均
P.rolling(window=60).mean().plot()  # 移動平均線 (MA60) 連同過去N點平均

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 開始時間 為 60天前
start = datetime.datetime.now() - datetime.timedelta(days=60)

# 結束時間 為 現在
end = datetime.date.today()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
import matplotlib as mpl
import matplotlib.dates as mdates

# from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc

data_price = [1, 2, 3, 4, 5]

# 繪製圖片
# plt.figure(figsize=(10, 8))
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

# 讀取pickle檔案資料
all_df = pd.read_pickle("tmp_df_data1.pkl")
print(all_df)

day = all_df["date"].astype(str)
close = all_df["close"].astype(float)

plt.figure(figsize=(12, 8), dpi=100)
# plt.figure(figsize=(10, 8))
plt.plot(day, close, "s-", color="r", label="收盤價")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)
plt.show()

# 3030

# 讀取pickle檔案資料
all_df = pd.read_pickle("tmp_df_data1.pkl")
print(all_df)

# step 1 prepare data
day = all_df["date"].astype(str)
openprice = all_df["open"].astype(float)
close = all_df["close"].astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
#ax.set_title("開盤價、收盤價 ( " + all_df["date"][0] + " ~ " + all_df["date"][-1] + " )")
ax.set_title("開盤價、收盤價")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, "s-", color="r", label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, "o-", color="b", label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

plt.show()

# 3030

# 讀取pickle檔案資料
all_df = pd.read_pickle("tmp_df_data1.pkl")
print(all_df)

# step 1 prepare data
day = all_df["date"].astype(str)
openprice = all_df["open"].astype(float)
close = all_df["close"].astype(float)
high = all_df["max"].astype(float)
low = all_df["min"].astype(float)
volume = all_df["Trading_Volume"].astype(float)  # 成交股數

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
ax.set_title("K 線圖")

# step 3 plot 子圖(ax)
# NG

ax.grid(True)

# step 3 plot 子圖(ax2)
# NG

ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Python 測試 twstock
pip install twstock
twstock 台灣股市股票價格擷取
https://pypi.org/project/twstock/
"""

import twstock

print("------------------------------------------------------------")  # 60個
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

# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個

"""
股票資料彙整_YahooFinance
股票資料彙整_Yahoo股市

#使用 pandas_datareader.data.DataReader 抓取 2356.TW, 1566.TWO 最近一個月的股價資料

#股票資料彙整_YahooFinance

from pandas import Series, DataFrame
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
    重排欄位順序為:'市場別', '股票代號', '股票名稱', '日期', '時間', '成交', '買進', '賣出', '漲跌', '張數', '昨收', '開盤', '最高', '最低'
    Extra:
        匯集 Yahoo 股市 page 1~ 5 的資料 (pd.concat)
        依據股票代號的前兩碼，做 GroupBy 操作
            merge ../data/個股_類別.xls(先解壓縮 個股_類別.rar) 中的資料之後，做 GroupBy 操作

"""
# 股票資料彙整_Yahoo股市

from pandas import Series, DataFrame

# 目標資料來源:
# https://tw.stock.yahoo.com/s/list.php?c=tse&pid=1

# 抓取網頁資料

import requests


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
    fixedTable.index = Series(range(len(fixedTable)))
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

df1.tail(5)

# 彙整 Yahoo 股市 page 1~ 5 的資料

# 抓第一頁~第五頁的資料
dfs = map(lambda p: fixTable("TSE", getDataOnePageTSE(p)), range(1, 6))

# Append 在一起
df = pd.concat(dfs)
len(df)

# 1000

df.index = pd.Index(range(len(df)))  # 重新編排 row index 編號
df = df[df["股票代號"].str.len() <= 4]  # 濾除 權證 資料
df.tail()

# 抓取 類股 資料

df_類股 = pd.read_excel("..\\data\個股_類別.xls")  # 需先解壓縮 個股_類別.rar
df_類股.tail()

# Merge

mdf = df.merge(df_類股, left_on="股票代號", right_on="個股_代號", how="left")  # merge
mdf = mdf.drop(["市場別_ID", "個股_代號", "個股_名稱"], axis=1)  # drop 多於的欄位
mdf.tail()

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



