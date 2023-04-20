#import pandas_datareader as stock

'''
data = stock.DataReader("2330.TW", "yahoo", "2022-03-01", "2023-03-01")
print(data)
'''
'''
import datetime
import time
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

#data = web.DataReader("F", 'yahoo', start, end)
data = web.DataReader('F', 'morningstar', start, end)

'''
'''
import pandas_datareader.data as web

#讀取yahoo財經
df = web.DataReader('0050.tw', 'yahoo', '2020-07-01')

#顯示最新10筆盤後交易資料
df.tail(5)
'''
'''

import pandas_datareader as web

stock = web.DataReader('ALB', data_source="yahoo", start="01.01.2021", end="30.10.2021")

'''



import numpy as np
import matplotlib.pyplot as plt

#熊貓是python的excel
import pandas as pd

#於終端機試著安裝pandas_datareader之後才可繼續進行後續的教學
#建議先更新看看: conda update pandas-datareader
#之前沒安裝過的話，就直接安裝吧: conda install pandas-datareader

#pandas_datareader可以直接到網路上跟合作的廠商抓資料
import pandas_datareader.data as web

#pandas_datareader可以直接到網路上跟合作的廠商抓資料
#無須輸入任何API網址，只要輸入 
#1.要什麼資料, 2.從哪個來源來, 3.從什麼時候的資料開始 即可
#ex:從yahoo取得apple的股價資料
#yahoo已經不提供資料了, 隨便改用一個morningstar提供的資料吧
#df = web.DataReader("AAPL","morningstar",start="2012-09-01")


'''
#取出data frame其中一個欄位:關盤價
P = df["Close"]

#計算每一期之間的報酬率
P.diff()

#計算每一期之間的報酬率(跟第一期的資料相比）
r = P.diff() / P
r.plot()

#看前一百天開始的紀錄(只要設定index=-100就是一百天前，是不是很神奇！？)
r[-100:].plot()

#移動平均:透過window=20參數可以將前20天的累計值計算出來
P.rolling(window=20).mean()

#當然也可以把移動平均畫成圖表
P.rolling(window=20).mean().plot()

#而且還可以將兩個曲線同時顯示在一個表，方便作比較
P.plot()
P.rolling(window=20).mean().plot()
P.rolling(window=60).mean().plot()

'''
