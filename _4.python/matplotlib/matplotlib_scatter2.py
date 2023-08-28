# scatter 集合

import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(num = 'scatter 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

x = np.linspace(0, 10, 51)
print(type(x))

y1 = np.sin(x) * 5 + 5
y2 = np.cos(x) * 5 + 5

plt.scatter(x, y1, c = 'r')       #畫出每個x-y對應點
plt.scatter(x, y2, c = 'g')       #畫出每個x-y對應點

#第二張圖
plt.subplot(232)

A = 10  #震幅
N = 10  #總點數
rng = np.random.RandomState(42) #固定random seed
#print(rng)
x = A * rng.rand(N)     #0~A取N個數出來
print(type(x))
y = A * rng.rand(N)     #0~A取N個數出來

print(x)
print(y)
plt.scatter(x, y)       #畫出每個x-y對應點

#第三張圖
plt.subplot(233)


#曲線資料加入雜訊
x = np.linspace(-5,5,51)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

plt.scatter(x,yn,c='blue',marker = '.')
plt.plot(x,y+0.75,'r')


#第四張圖
plt.subplot(234)

#蒙地卡羅模擬 Monte Carlo Simulation 使用亂數與機率來解決問題

import math
import random
import matplotlib.pyplot as plt

print('蒙地卡羅模擬 a')

L = 100
NUMBER_OF_TRIALS = 300
numberOfHits = 0

r = L / 2
cx = r
cy = r

numberOfHits = 0
for i in range(NUMBER_OF_TRIALS):
    x = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    y = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    #print(x, y)

    d = math.sqrt((x-cx)**2+(y-cy)**2)  #點與中心的距離
    if d <= r:
        numberOfHits += 1
        plt.scatter(x, y, marker = '.', c = 'r')
    else:
        plt.scatter(x, y, marker = '.', c = 'g')
        
#求圓周率
p = numberOfHits / NUMBER_OF_TRIALS
pi = p * 4
print('圓周率 = ', pi)

plt.axis('equal')


#第五張圖
plt.subplot(235)

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)

# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)

#第六張圖
plt.subplot(236)

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.sin(x) + 0.3*np.random.randn(200)

plt.plot(x, y1, 'r')

plt.scatter(x, y2)

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(num = 'scatter 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

print('計算迴歸直線')

import matplotlib.pyplot as plt
import numpy as np

# 資料
x = np.array([23,24,28,24,27,21,18,25,28,20])  # 氣溫
y = np.array([37,22,62,32,74,16,10,69,83,7])   # 果汁販賣數量

# 迴歸直線
a, b = np.polyfit(x, y, 1)
y2 = a * x + b
print('斜率: {0}, 截距:{1}'.format(a, b))

# 繪圖
plt.scatter(x, y)  # 散布圖
plt.plot(x, y2)    # 迴歸直線

# 預測在氣溫33度時的販賣數量
# a * 33 + b



#第二張圖
plt.subplot(232)

print('繪製散布圖')
import matplotlib.pyplot as plt
import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

# 讀入資料
dat = pd.read_csv(filename, encoding='UTF-8')

# 散布圖
plt.scatter(dat['數學'], dat['理科'])
plt.axis('equal')


#共變異數與相關係數
import numpy as np
correlation = np.corrcoef(dat['數學'], dat['理科']) # 計算相關係數
correlation[0,1]  # 顯示在畫面



#第三張圖
plt.subplot(233)


#連接2點的直線

import matplotlib.pyplot as plt
import numpy as np

# 資料
x = np.arange(1, 5.1, 0.1)
y = 1/2*x + (1/2)

# 繪圖
plt.scatter(x, y)
plt.grid(color='0.8')




#第四張圖
plt.subplot(234)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, s=250)

#畫不同顏色的scatter
cl = np.random.randint(1, 4, 100)
plt.scatter(x, y, s=100, c=cl, alpha=0.6, cmap="Paired")

#第五張圖
plt.subplot(235)

x = np.linspace(-5, 5, 500)
y = np.sinc(x)
plt.plot(x,y)

plt.scatter(x[y>0], y[y>0], c='r')





#第六張圖
plt.subplot(236)

print('蒙地卡羅模擬 b')
import random
import math

trials = 800
Hits = 0
radius = 50
for i in range(trials):
    x = random.randint(1, 100)                      # x軸座標
    y = random.randint(1, 100)                      # y軸座標
    if math.sqrt((x-50)**2 + (y-50)**2) < radius:   # 在圓內
        plt.scatter(x, y, marker='.', c='r')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')

'''
print('蒙地卡羅模擬 c')

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)
'''

plt.show()



