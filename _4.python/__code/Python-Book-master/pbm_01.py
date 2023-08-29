import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

'''
#lambda: 臨時要使用的函數
currency = 32.1357851   # 1美元 = 32.13台幣    台灣銀行 現金賣出價

price = [100, 500, 1000] #美元

ll = list(map(lambda x:currency*x, price))
print('換算成台幣 :', ll)

usb2twd = lambda x:currency*x

print(usb2twd(1000))


#print(f"1 美元合台幣 {c:.2f} 元。")
#print(f"1 美元合台幣 {c:10.2f} 元。")

print('------------------------------------------------------------')	#60個


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, s, r):
        self.suit = s
        self.rank = r
        
    def show(self):
        print(self.SUITS[self.suit] + self.RANKS[self.rank])


card01 = Card(2, 3)
card01.show()

        


print('------------------------------------------------------------')	#60個



animal = {'mouse':'老鼠',
          'panda':'貓熊',
          'penguin':'企鵝',
          'lion':'獅子',
          'tiger':'老虎',
          'zebra':'斑馬',
          'koala':'無尾熊',
          'hippo':'河馬'}
              
print(animal.keys())

for eng in animal.keys():
    print(f"{eng},{animal[eng]}")

print('用pickle來存取一個字典檔案, 讀寫接用 wb/rb binary')

import pickle

f = open("animal.pickle", 'wb')

pickle.dump(animal, f)

f.close()

f = open("animal.pickle", 'rb')

pickledict = pickle.load(f)
f.close()
print(pickledict)

'''

print('------------------------------------------------------------')	#60個


import matplotlib as mpl
import matplotlib.font_manager as fm




'''
for f in mpl.font_manager.fontManager.ttflist:
    print(f.name)

#[f.name for f in mpl.font_manager.fontManager.ttflist]
'''

'''
print('matplotlib 真的「看到的」字型')
for f in fm.fontManager.ttflist:
    print(f.name)
'''

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import yfinance as yf

#讀入台積電的股價，比如我們想看 2021-2022 這兩年的股價。
df = yf.download("2330.TW", start="2021-01-01", end="2022-12-31")

#有最高最低點、開盤收盤價、調整收盤價以及成交量的資訊。
print(df.head())


#只取調整收盤價
P = df["Adj Close"]
print(P.head())


P.plot()

plt.show()


#我們看一下大家最關心的報酬率，報酬率公式：(Pt−Pt_1)/Pt_1

r = P.diff()/P
r.plot()
plt.show()

print('最後一百筆資料')

r[-100:].plot()
plt.show()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





