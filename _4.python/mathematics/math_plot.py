"""
把 math 畫出來

"""

import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt

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

print('蒙地卡羅模擬 a')

L = 100
NUMBER_OF_TRIALS = 300
numberOfHits = 0

radius = L / 2
cx = radius
cy = radius

for i in range(NUMBER_OF_TRIALS):
    x = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    y = random.randint(0, L) # 0 ~ L (含前後) 之間的任意整數
    #x = np.random.randint(0, L) #使用numpy               # x軸座標
    #y = np.random.randint(0, L) #使用numpy               # y軸座標
    #print(x, y)

    d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)    #點與中心的距離
    #d = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)      #點與中心的距離
    if d <= radius:   # 在圓內
        numberOfHits += 1
        plt.scatter(x, y, marker = '.', c = 'r')
    else:
        plt.scatter(x, y, marker = '.', c = 'g')
plt.axis('equal')

#求圓周率
pi = numberOfHits / NUMBER_OF_TRIALS * 4
print('圓周率 = ', pi)

#第二張圖
plt.subplot(232)

print('蒙地卡羅模擬 b')
       
L = 2
NUMBER_OF_TRIALS = 300
numberOfHits = 0

radius = L / 2

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    #x = np.random.random() * 2 - 1 #使用numpy  # x軸座標
    #y = np.random.random() * 2 - 1 #使用numpy  # y軸座標
    #print(x, y)

    d = math.sqrt(x * x + y * y)  #點與中心的距離
    if d <= radius:   # 在圓內
        numberOfHits += 1
        plt.scatter(x, y, marker = '.', c = 'r')
    else:
        plt.scatter(x, y, marker = '.', c = 'g')
plt.axis('equal')

#求圓周率
pi = numberOfHits / NUMBER_OF_TRIALS * 4
print('圓周率 = ', pi)

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

x = np.linspace(0, 2 * np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數

plt.plot(x, y1, label = 'Sin')                    
plt.plot(x, y2, label = 'Cos')
plt.legend()

plt.grid(c = 'y', linestyle = '--', lw = 1) # 顯示虛線格線

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

plt.scatter(x, y, s = 50, color = 'r')#s是大小

#rand 隨機取值
x = np.random.rand(N)
y = np.random.rand(N)
print('max :', x.max())
print('min :', x.mean())
print('avg :', x.min())
print('std :', x.std())

plt.scatter(x, y, s = 50, color = 'g')          #s是大小
plt.scatter(x, y, s = 50, color = (0, 1, 0))    #s是大小 # 綠色

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
print("bins的y軸 ", h[0])
print("bins的x軸 ", h[1])
plt.ylabel('頻率')
plt.title('測試 10000 次')

plt.show()


print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'math 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

#衰減函數
def f1(t):
    return np.exp(-t) * np.sin(2 * np.pi * t)

x = np.linspace(0.0, np.pi, 100)

plt.plot(x, f1(x), 'r-')
plt.plot(x, f1(x), 'go')

plt.ylabel('衰減值')
plt.title('畫 f(x), 衰減數列')

#第二張圖
plt.subplot(232)

x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x**2)



#第三張圖
plt.subplot(233)


N = 1000000
#plt.plot(np.random.randn(N))
#plt.plot(range(N), np.random.randn(N))
#plt.scatter(range(N), np.random.randn(N))

# 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
normal_samples = np.random.normal(size = N)

normal_samples = np.random.randn(N)  #same

print(range(N))
print(type(normal_samples))
#print(normal_samples)
small_numbers = 0
big_numbers = 0
for i in range(N):
    if normal_samples[i] < -3.0:
        small_numbers += 1
    elif normal_samples[i] > 3.0:
        big_numbers += 1

print('big = ', big_numbers)
print('small = ', small_numbers)

normal_array = np.zeros(600)
for i in range(N):
    z = int(normal_samples[i] * 100 + 300)
    #print(z, end = ' ')
    if (z >= 0) & (z < 600):
        normal_array[z] += 1

plt.plot(normal_array)
plt.title('常態分佈')


#第四張圖
plt.subplot(234)

mu = 0                                                  # 平均值
sigma = 1                                               # 標準差
s = np.random.randn(10000)                              # 隨機數
print(s)

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

#第五張圖
plt.subplot(235)

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')



#第六張圖
plt.subplot(236)

import seaborn as sns #海生, 自動把圖畫得比較好看

mu = 0                                                  # 均值
sigma = 1                                               # 標準差
s = np.random.normal(mu, sigma, 10000)                  # 隨機數

count, bins, ignored = plt.hist(s, 30, density=True)    # 直方圖
# 繪製曲線圖
sns.kdeplot(s)

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'math 集合 3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

s = np.random.uniform(0.0,5.0,size=250)     # 隨機數
plt.hist(s, 5)                              # 直方圖


#第二張圖
plt.subplot(232)

import seaborn as sns #海生, 自動把圖畫得比較好看

s = np.random.uniform(size=10000)           # 隨機數

plt.hist(s, 30, density=True)               # 直方圖

# 繪製曲線圖
sns.kdeplot(s)


#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_x = 1500
pt_y = a * pt_x + b
print('f(1500) = {}'.format(pt_y))
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x, pt_y, '-o')              # 繪點 f(1500)
plt.text(pt_x-150, pt_y+3, 'f(1500)')   # 輸出文字f(1500)
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線


#第五張圖
plt.subplot(235)

a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03 
print('獲利48萬需有 {} 來客數'.format(int(pt_x)))
plt.plot(x, y)                                      # 繪函數直線
plt.plot(pt_x, pt_y, '-o')                          # 繪點
plt.text(pt_x-150, pt_y+3, '('+str(int(pt_x))+','+str(pt_y)+')')   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                                          # 加格線


#第六張圖
plt.subplot(236)

plt.plot([0, 0], [20, 0])              # 繪函數直線公式 1
plt.plot([0, 0], [0, 20])              # 繪函數直線公式 2
                                
line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * y) for y in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * y) for y in line4_x]

lineobj_x = np.linspace(0, 20, 20)
lineobj_y = [10 - y for y in lineobj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)              # 繪函數直線公式 3
plt.plot(line4_x, line4_y)              # 繪函數直線公式 4
plt.plot(lineobj_x, lineobj_y)          # 繪目標函數直線公式

plt.plot(5, 5, '-o')                    # 繪交叉點
plt.text(4.5, 5.5, '(5, 5)')            # 輸出(5, 5)
plt.xlabel("Research")
plt.ylabel("UI")
plt.grid()                              # 加格線



plt.show()

print('------------------------------------------------------------')	#60個


