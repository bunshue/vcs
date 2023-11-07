import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import pandas as pd
import mpl_finance as mpf
import talib

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
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
high = all_df["最高價"].astype(float)
low = all_df["最低價"].astype(float)
volume = all_df["成交股數"].str.replace(',', '').astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax.set_title(stock_symbol+"  K 線圖 ( " + dates[0] + " ~ " + dates[1] + " )")

# step 3 plot 子圖(ax)
mpf.candlestick2_ochl(ax, openprice, close, high, low, width=0.5,
                      colorup='r', colordown='g', alpha=0.6)
ax.plot(talib.SMA(close, 10), label='10日均線')
ax.plot(talib.SMA(close, 30), label='30日均線')
ax.legend(loc="best", fontsize=20)
ax.grid(True)

# step 3 plot 子圖(ax2)
mpf.volume_overlay(ax2, openprice, close, volume, colorup='r',
                   colordown='g', width=0.5, alpha=0.8)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])
ax2.grid(True)

# step 4 show plot
plt.show()
