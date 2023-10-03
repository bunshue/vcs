'''
plt之基本設定

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'math 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

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


#第二張圖
plt.subplot(232)


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

#第三張圖
plt.subplot(233)

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


#第四張圖
plt.subplot(234)

import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數

plt.plot(x, y1, label='Sin')                    
plt.plot(x, y2, label='Cos')
plt.legend()

plt.grid(c='y',linestyle='--',lw=1) # 顯示虛線格線



#第五張圖
plt.subplot(235)

N = 500

#randn 由標準常態分布隨機取值
#還可以取好高級的亂數, 從平均數 0, 標準差 1 的常態分佈中取出 n 個數字。

x = np.random.randn(N)
y = np.random.randn(N)
print('max :', x.max())
print('min :', x.mean())
print('avg :', x.min())
print('std :', x.std())

plt.scatter(x, y, s=50, color='r')#s是大小

#rand 隨機取值
x = np.random.rand(N)
y = np.random.rand(N)
print('max :', x.max())
print('min :', x.mean())
print('avg :', x.min())
print('std :', x.std())

plt.scatter(x, y, s=50, color='g')#s是大小
plt.scatter(x, y, s=50, color=(0, 1, 0))  #s是大小 # 綠色


#第六張圖
plt.subplot(236)

from random import randint

def dice_generator(times, sides):
    #處理隨機數
    for i in range(times):              
        ranNum = randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)
          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列

h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('頻率')
plt.title('測試 10000 次')


plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'math 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)

plt.plot(x, f(x))
plt.title('畫 f(x)')



#第二張圖
plt.subplot(232)


def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)

plt.plot(x, f(x))


#第三張圖
plt.subplot(233)

import matplotlib.pyplot as plt
import numpy as np

# 建立衰減數列.
x = np.linspace(0.0, 5.0, 50)
y = np.cos(3 * np.pi * x) * np.exp(-x)


plt.title('衰減數列')
plt.plot(x, y, 'go-')
plt.ylabel('衰減值')


#第四張圖
plt.subplot(234)





#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個

