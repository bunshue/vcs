# 新進測試03

import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from pylab import mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 

country = ["美國","澳洲","日本","歐洲","英國"]
pou = [10543, 2105, 1190, 3346, 980]
          
plt.pie(pou,labels=country,explode=(0,0,0.2,0,0),
        autopct="%1.2f%%")                          # 繪製圓餅圖

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='polar')
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖",fontsize=12)
ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title('一般座標 Sin 圖',fontsize=12)
ax2.set_aspect(2)
plt.tight_layout()                      # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return (np.power(x,2) + np.power(y, 2))
def f2(x, y):                                # 右邊曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X,Y), cmap='hsv')   # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X,Y), cmap='hsv')   # 繪製 3D 圖
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 50)

f1 = 3 * np.sin(x)                  # y陣列的變化
f2 = np.sin(x)
f3 = 0.2 * np.sin(x)

plt.plot(x, f1) 
plt.plot(x, f2, '-x')
plt.plot(x, f3)
plt.plot(x, f1, 'go')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(2*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 1, y, alpha=0.1)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

# 函數的係數
a = -1
b = 2
# 繪製區間圖形
x = np.linspace(-2, 4, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-2)&(x<=5),
                 facecolor='lightgreen')

plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 2, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 2, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 2, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 2, 4)
plt.plot(seq, data4, '-s')

plt.show()


print("------------------------------------------------------------")  # 60個


import csv
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

filename = '_data/TaipeiWeatherJan.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

seq = range(1,32)
plt.plot(seq,highTemps,seq,meanTemps,seq,lowTemps)

plt.title("2025年1月台北天氣報告", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = '_data/ST43_3479_202310.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    for _ in range(5):                              # 跳過前5列
        next(csvReader)
    all_rows = list(csvReader)
    data_without_last_row = all_rows[:-1]           # 跳過最後一列
    
    mydates, openPrices, highPrices, lowPrices, closePrices = [], [], [], [], []   
    
    for row in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            openPrice = eval(row[3])
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            openPrices.append(openPrice)            # 儲存開盤價
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, openPrices, '-p', label='開盤價')    # 繪製開盤價
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



