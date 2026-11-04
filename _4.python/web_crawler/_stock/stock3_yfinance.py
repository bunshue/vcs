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

print("------------------------------------------------------------")  # 60個
print("使用 FinMind ST")
print("------------------------------------------------------------")  # 60個
'''
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
print(div_df.head())
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
# print(df.head())
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
print(df.head())

# 2. 將 Date 轉為時間格式，並設定為索引 (Index)
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

print('bbbb')
print(df.head())

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
df["MA5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA) 連同過去N點平均
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

df["ma5"] = df["Close"].rolling(window=5).mean()  # 移動平均線 (MA) 連同過去N點平均
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
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA20"] = df["Close"].rolling(window=20).mean()

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
'''

# 讀取pickle檔案資料
df = pd.read_pickle("tmp_df_data1.pkl")
# df = df.tail(5)

print("df的形狀 : ", df.shape)
print(df)

# 計算5天和20天的移動平均線
df["MA5"] = df["close"].rolling(window=5).mean()
df["MA20"] = df["close"].rolling(window=20).mean()

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
    df["SMA5"].iloc[5:] > df["SMA20"].iloc[5:], 1.0, 0.0
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
df["MA5"] = df["close"].rolling(window=5).mean()
df["MA20"] = df["close"].rolling(window=20).mean()
df["MA60"] = df["close"].rolling(window=60).mean()

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
from hs_udata import set_token, stock_quote_daily
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

plt.figure(figsize=(12, 8), dpi=100)
# plt.figure(figsize=(10, 8))
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

plt.show()

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
cc = df_monthly_sales.head()
print(cc)

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
print(sp500_data.head())

print("------------------------------------------------------------")  # 60個
