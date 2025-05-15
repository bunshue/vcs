"""

"""

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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

N = 100
index = np.arange(N)
bar_width = 0.8
figsize = (8, 8)

woe_fig = plt.figure(figsize=figsize)

plt.title("Number of Observations and WoE per bucket")
ax = woe_fig.add_subplot(111)
ax.set_ylabel("Observations")
# plt.xticks(index + bar_width / 2, self.bins["labels"])
# plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
ax2 = ax.twinx()
ax2.set_ylabel("Weight of Evidence")
ax2.plot(
    index + bar_width / 2,
    # self.bins["woe"],
    "bo-",
    linewidth=4.0,
    color="r",
    label="WoE",
)
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
plt.legend(handles, labels)
woe_fig.autofmt_xdate()

show()

print("------------------------------------------------------------")  # 60個

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
import pandas as pd

# 設定參數
start_date = "2025-04-28"  # 設定開始日期
end_date = "2025-04-30"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘


# 抓取 S&P 500 數據
ticker = "^GSPC"  # Yahoo Finance 中 S&P 500 的代號
sp500_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

# 顯示數據
print(sp500_data.head())


# 使用 yfinance 一次抓取多隻股票的資料
import yfinance as yf
import pandas as pd

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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
