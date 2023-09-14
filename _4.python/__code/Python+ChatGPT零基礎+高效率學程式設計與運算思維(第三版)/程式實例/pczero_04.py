import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2025':
            total2025 += int(row[5])
        if row[1] == '2026':
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

# ex20_2.ipynb
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

print('------------------------------------------------------------')	#60個

# ex20_4.py
import matplotlib.pyplot as plt
import numpy as np

trials = 2000
Hits = 0
radius = 50
for i in range(trials):
    x = np.random.randint(1, 100)               # x軸座標
    y = np.random.randint(1, 100)               # y軸座標
    if np.sqrt((x-50)**2 + (y-50)**2) < radius: # 在圓內
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')
plt.show()

print('------------------------------------------------------------')	#60個


# ex20_6.ipynb
import matplotlib.pyplot as plt
import random

def loc(index):
    ''' 處理座標的移動 '''
    x_mov = random.choice([-3,-2,-1,1,2,3])     # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5,-3,-1,1,3,5])     # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
plt.axis('off')
plt.show()

print('------------------------------------------------------------')	#60個

# ex20_8.ipynb
import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條
data5 = [1, 6, 11, 16, 21, 26, 31, 36]          # data5線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 3, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 3, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 3, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 3, 4)
plt.plot(seq, data4, '-s')

plt.subplot(2, 3, 6)
plt.plot(seq, data5, '-v')

plt.show()


print('------------------------------------------------------------')	#60個
# ex20_10.ipynb

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np
from random import randint

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum1 = randint(1, sides)             # 產生1-6隨機數
        ranNum2 = randint(1, sides)             # 產生1-6隨機數
        dice.append(ranNum1+ranNum2)
def dice_count(sides):
    '''計算2-11個出現次數'''
    for i in range(2, 13):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)       
times = 1000                                    # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
frequencies = []                                # 儲存每一面骰子出現次數串列
dice_generator(times, sides)                    # 產生擲骰子的串列
dice_count(sides)                               # 將骰子串列轉成次數串列
N = len(frequencies)
x = np.arange(N)                                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, frequencies, width, color='g')       # 繪製長條圖
plt.ylabel('出現次數')
plt.title('測試 1000 次', fontsize=16)
plt.xticks(x, ('2','3','4','5','6','7','8','9','10','11','12'))
plt.yticks(np.arange(0, 150, 15))
plt.show()


print('------------------------------------------------------------')	#60個
# ex20_12.ipynb
import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

country = ["美國","澳洲","日本","歐洲","英國"]
pou = [10543, 2105, 1190, 3346, 980]
          
plt.pie(pou,labels=country,explode=(0,0,0.2,0,0),
        autopct="%1.2f%%")                          # 繪製圓餅圖
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





