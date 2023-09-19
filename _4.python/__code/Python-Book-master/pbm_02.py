import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個
'''

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pip install yfinance

import yfinance as yf

df = yf.download("2330.TW", start="2021-01-01", end="2022-12-31")

print('最高最低點、開盤收盤價、調整收盤價以及成交量的資訊')
print(df.head())

print('只取調整收盤價')

P = df["Adj Close"]
print(P.head())

P.plot()

plt.show()


#我們看一下大家最關心的報酬率，報酬率公式：(Pt−Pt−1)/Pt−1

r = P.diff()/P
r.plot()
plt.show()

#最後一百筆資料

r[-100:].plot()

plt.show()


#原本股價圖波動的很厲害，現在我們想讓它變得平滑一點，改看每 20 天的平均

print(P.rolling(window=20).mean())

P.rolling(window=20).mean().plot()
plt.show()


#和原本的股價圖比較

P.plot()
P.rolling(window=20).mean().plot()
plt.show()


#當然也可以算更多天的平均，會變得更平滑

P.plot()
P.rolling(window=20).mean().plot()
P.rolling(window=60).mean().plot()
plt.show()
'''

print('------------------------------------------------------------')	#60個

chatbot = '🐶' + ": "

print(chatbot + 'good')

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





