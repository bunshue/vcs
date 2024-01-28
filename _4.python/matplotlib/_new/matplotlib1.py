# matplotlib_新進測試 all

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

'''
#產生兩個串列
x = [x for x in range(9)]       # 產生0, 1, ... 8串列
y = [0, 1, 4, 9, 16, 25, 36, 49, 64]

plt.plot(x, y, lw = 2)
plt.show()

         
data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'y:',seq,data4,'k.')   
plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')   

plt.show()

"""
seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend()
plt.legend(loc='best')
plt.legend(loc=0)
plt.legend(loc='upper right')
plt.legend(loc=6)
plt.legend(loc='best')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.show()
"""
print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import matplotlib.image as img

fig = img.imread(filename)
plt.imshow(fig)
plt.show()

print("------------------------------------------------------------")  # 60個

'''

xpt = [1,2,3,4,5]
ypt = [1,4,9,16,25]
plt.scatter(xpt, ypt)
plt.show()

print("------------------------------------------------------------")  # 60個

xpt = list(range(1,101))    # 建立1-100序列x座標點
ypt = [x**2 for x in xpt]   # 以x平方方式建立y座標點
plt.scatter(xpt, ypt, color='y')

plt.show()

print("------------------------------------------------------------")  # 60個

x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

print("------------------------------------------------------------")  # 60個

xpt = np.linspace(0, 10, 500)   # 建立含500個元素的陣列
ypt1 = np.sin(xpt)              # y陣列的變化
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1)          # 用預設顏色
plt.scatter(xpt, ypt2)          # 用預設顏色
plt.show()

print("------------------------------------------------------------")  # 60個

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x, y1, c=colors, marker='*')    # 繪製 sine 
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker='s')    # 繪製 cos 
plt.show()

print("------------------------------------------------------------")  # 60個

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 100)
f1 = 2 * np.sin(x)              # 波形 1
f2 = np.sin(2*x)                # 波形 2
f3 = 0.5 * np.sin(x)            # 波形 3
plt.plot(x, f1) 
plt.plot(x, f2)
plt.plot(x, f3)
plt.show()

print("------------------------------------------------------------")  # 60個

points = 30
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(points):                     # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1,11,points)          # 建立 x
y = np.random.randint(1,11,points)          # 建立 y
size = (points * np.random.rand(points))**2 # 散點大小數列
plt.scatter(x, y, s=size, c=colors)         # 繪製散點
plt.xticks(np.arange(0,12,step=1.0))        # x 軸刻度
plt.yticks(np.arange(0,12,step=1.0))        # y 軸刻度
plt.show()

print("------------------------------------------------------------")  # 60個

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 0, y, color='green', alpha=0.1)
plt.show()

print("------------------------------------------------------------")  # 60個

# 函數f(x)的係數
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1*x**2 + c1
plt.plot(x, y1, color='b')      # 藍色是 f(x)

# 函數g(x)的係數
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2*x**2 + b2*x + c2
plt.plot(x, y2, color='g')      # 綠色是 g(x)

# 繪製區間
plt.fill_between(x, y1=y1, y2=y2, where=(x>=-1)&(x<=2),
                 facecolor='yellow')

plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=x,cmap='rainbow')  # 色彩隨 x 軸值變化
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=y,cmap='rainbow')  # 色彩隨 y 軸值變化
plt.colorbar()                            # 色彩條
plt.show()

print("------------------------------------------------------------")  # 60個

num = 100
while True:
    x = np.random.random(100)           # 建立x軸100個隨機數字
    y = np.random.random(100)           # 建立y軸100個隨機數字
    plt.scatter(x,y,s=100,c=x,cmap='brg')   # 繪製散點圖
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")    # 詢問是否繼續
    if yORn == 'n' or yORn == 'N':      # 輸入n或N則程式結束
        break

print("------------------------------------------------------------")  # 60個

def loc(index):
    ''' 處理座標的移動 '''
    x_mov = random.choice([-3, 3])              # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])       # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標
while True:
    for i in range(1, num):                     # 建立點的座標
        loc(i)
    t = x                                       # 色彩隨x軸變化
    plt.scatter(x, y, s=2, c=t, cmap='brg')
    plt.axis('off')                             # 隱藏座標
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")            # 詢問是否繼續
    if yORn == 'n' or yORn == 'N':              # 輸入n或N則程式結束
        break
    else:
        x[0] = x[num-1]                 # 上次結束x座標成新的起點x座標
        y[0] = y[num-1]                 # 上次結束y座標成新的起點y座標
        del x[1:]                               # 刪除舊串列x座標元素
        del y[1:]                               # 刪除舊串列y座標元素
  
print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立衰減數列.
x1 = np.linspace(0.0, 5.0, 50)
y1 = np.cos(3 * np.pi * x1) * np.exp(-x1)
# 建立非衰減數列
x2 = np.linspace(0.0, 2.0, 50)
y2 = np.cos(3 * np.pi * x2)

plt.subplot(2,1,1)
plt.title('衰減數列')
plt.plot(x1, y1, 'go-')
plt.ylabel('衰減值')

plt.subplot(2,1,2)
plt.plot(x2, y2, 'm.-')
plt.xlabel('時間(秒)')
plt.ylabel('非衰減值')

plt.show()

print("------------------------------------------------------------")  # 60個

data1 = [1, 2, 3, 4, 5, 6, 7, 8]        # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]   # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.subplot(1, 2, 1)                    # 子圖1
plt.plot(seq, data1, '-*')
plt.subplot(1, 2, 2)                    # 子圖2
plt.plot(seq, data2, 'm-o')                      

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0.0, np.pi, 100)
plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(2,2,3)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0.0, np.pi, 100)
plt.subplot(221)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(222)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(223)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0.0, np.pi, 100)
plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(2,1,2)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplot(1,2,1)      # 建立子圖表 1,2,1
plt.text(0.15,0.5,'subplot(1,2,1)',fontsize='16',c='b')
plt.subplot(2,2,2)      # 建立子圖表 2,2,2
plt.text(0.15,0.5,'subplot(2,2,2)',fontsize='16',c='m')
plt.subplot(2,2,4)      # 建立子圖表 2,2,4
plt.text(0.15,0.5,'subplot(2,2,4)',fontsize='16',c='m')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y = np.sin(x)
fig = plt.figure()                          # 建立畫布物件
ax = fig.add_subplot()                      # 建立子圖(或稱軸物件)ax
ax.scatter(x, y, c=colors, marker='*')      # 繪製 sin
ax.set_title("建立畫布與軸物件,使用OO API繪圖", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]') 
fig.suptitle("4個子圖的實作",fontsize=16) # 圖表主標題
plt.tight_layout()                      # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect('equal', 'box')
ax[1, 1].set_title('設定寬高比相同')
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect(2)
ax[1, 1].set_title('設定寬高比是2')
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('得票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton')) # x 軸刻度
plt.yticks(np.arange(0, 450, 30))           # y 軸刻度
plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = random.randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)
def dice_count(sides):
    '''計算1-6個出現次數'''
    for i in range(1, sides+1):
        frequency = dice.count(i)       # 計算i出現在dice串列的次數
        frequencies.append(frequency)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 600                             # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
frequencies = []                        # 儲存每一面骰子出現次數串列
dice_generator(times, sides)            # 產生擲骰子的串列
dice_count(sides)                       # 將骰子串列轉成次數串列                          
x = np.arange(6)                        # 長條圖x軸座標
width = 0.35                            # 長條圖寬度
plt.bar(x, frequencies, width, color='g')   # 繪製長條圖
plt.ylabel('次數')
plt.xlabel('骰子點數')
plt.title('測試 600 次')
plt.xticks(x, ('1', '2', '3', '4', '5', '6'))
plt.yticks(np.arange(0, 150, 15))

plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = random.randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 10000                           # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
dice_generator(times, sides)            # 產生擲骰子的串列
h = plt.hist(dice,sides)                # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.8)             # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area)
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area,autopct="%1.2f%%")
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
exp = [0.0,0.0,0.0,0.0,0.0,0.1]
plt.pie(people,labels=area,explode=exp,autopct="%1.2f%%")
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.animation import FuncAnimation  

# 建立最初化的 line 資料 (x, y)  
def init():  
    line.set_data([], [])  
    return line,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):        
    x = np.linspace(0, 2*np.pi, 500)        # 建立 sin 的 x 值 
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 建立 sin 的 y 值  
    line.set_data(x, y)                     # 更新波形的資料
    return line,

# 建立動畫需要的 Figure 物件
fig = plt.figure()   
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-2, 2))    
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = ax.plot([], [], lw=3, color='g')  
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫  
ani = FuncAnimation(fig, animate,
                    frames = 200,          
                    init_func = init,                        
                    interval = 20)          # interval是控制速度
ani.save('tmp_sin.gif', writer='pillow')        # 儲存 tmp_sin.gif 檔案

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.animation import FuncAnimation  

# 建立最初化的 line 資料 (x, y)  
def init():  
    line.set_data([], [])  
    return line,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):        
    x = np.linspace(0, 2*np.pi, 10)         # 建立 sin 的 x 值 
    y = np.sin(2 * np.pi * (x - 0.01 * i))  # 建立 sin 的 y 值  
    line.set_data(x, y)                     # 更新波形的資料
    return line,

# 建立動畫需要的 Figure 物件
fig = plt.figure()   
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-2, 2))    
# 最初化線條 line, 變數, 須留意變數 line 右邊的逗號','是必須的  
line, = ax.plot([], [], lw=3, color='g')  
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫  
ani = FuncAnimation(fig, animate,
                    frames = 200,          
                    init_func = init,                        
                    interval = 20)          # interval是控制速度
ani.save('tmp_sin2.gif', writer='pillow')       # 儲存 tmp_sin2.gif 檔案

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.animation import FuncAnimation

# 建立最初化點的位置 
def init():
    dot.set_data(x[0], y[0])        # 更新紅色點的資料
    return dot,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):    
    dot.set_data(x[i], y[i])        # 更新紅色點的資料
    return dot,

# 建立動畫需要的 Figure 物件
fig = plt.figure()
N = 200
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))
# 建立和繪製 sin 波形
x = np.linspace(0, 2*np.pi, N)
y = np.sin(x)
line, = ax.plot(x, y, color='g',linestyle='-',linewidth=3)
# 建立和繪製紅點
dot, = ax.plot([],[],color='red',marker='o',
               markersize=15,linestyle='')
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫
ani = FuncAnimation(fig=fig, func=animate,
                    frames=N,
                    init_func=init,
                    interval=20,
                    blit=True,
                    repeat=True)
plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.animation import FuncAnimation

# 建立最初化點的位置 
def init():
    dot.set_data(x[0], y[0])        # 更新紅色點的資料
    return dot,
# 繪製 sin 波形, 這個函數將被重複調用
def animate(i):    
    dot.set_data(x[i], y[i])        # 更新紅色點的資料
    return dot,

# 建立動畫需要的 Figure 物件
fig = plt.figure()
N = 200
# 建立軸物件與設定大小
ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))
# 建立和繪製 sin 波形
x = np.linspace(0, 2*np.pi, N)
y = np.sin(x)
#line, = ax.plot(x, y, color='g',linestyle='-',linewidth=3)
# 建立和繪製紅點
dot, = ax.plot([],[],color='red',marker='o',
               markersize=15,linestyle='')
# interval = 20, 相當於每隔 20 毫秒執行 animate()動畫
ani = FuncAnimation(fig=fig, func=animate,
                    frames=N,
                    init_func=init,
                    interval=20,
                    blit=True,
                    repeat=True)
plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立衰減數列.
x = np.linspace(0.0, 5.0, 50)
y = np.cos(3 * np.pi * x) * np.exp(-x)

plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)
plt.plot(x, y, 'go-')
plt.ylabel('衰減值')
plt.show()

print("------------------------------------------------------------")  # 60個

plt.title(r'$\frac{7}{9}+\sqrt{7}+\alpha\beta$',fontsize=20)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(1,0,'bo')                  # 輸出藍點
plt.text(1,0,'sin(x)',fontsize=20)  # 輸出公式
plt.plot(x,y)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(arrowstyle='->',
                            facecolor='black'))
plt.annotate('局部極小值',
            xy=(1.5, -1),
            xytext=(2.0, -1.25),           
            arrowprops=dict(arrowstyle='-'))
plt.text(0.8,1.2,'Annotate的應用',fontsize=20,color='b')
plt.ylim(-1.5, 1.5)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
ax = plt.subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
ax.plot(theta, r, 'm', lw=3)
plt.title("極座標圖表",fontsize=16)
plt.tight_layout()      # 圖表標題可以緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):
    return (1.2-x**2+y**5)*np.exp(-x**2-y**2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 建立 2 個子圖
fig, ax = plt.subplots(1,2, figsize=(8,4))
# 繪製左圖 level 是預設
con = ax[0].contourf(X,Y,Z,cmap='Greens') # 填充輪廓圖
plt.colorbar(con,ax=ax[0])
oval = ax[0].contour(X,Y,Z,colors='b')    # 輪廓圖
ax[0].clabel(oval,colors='b')             # 增加高度標記
ax[0].set_title('指數函數等高圖level是預設',fontsize=16,color='b')
# 繪製右圖 level=12
ax[1].contourf(X,Y,Z,12,cmap='Greens')    # 填充輪廓圖
oval = ax[1].contour(X,Y,Z,12,colors='b') # 輪廓圖
ax[1].clabel(oval,colors='b')             # 增加高度標記
ax[1].set_title('指數函數等高圖level=12',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import axes3d

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")
ax[0].set_title('繪製曲線表面圖',fontsize=16,color='b')

# 繪製曲線框面圖
#ax = fig.add_subplot(111, projection='3d')
ax[1].plot_wireframe(X, Y, Z, color='g')
ax[1].set_title('繪製曲線框線圖',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0,1,300)        # z 軸值
x = z * np.sin(30*z)            # x 軸值
y = z * np.cos(30*z)            # y 軸值
colors = x + y                  # 色彩是沿 x + y 累增

# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
ax[0].scatter(x, y, z, c = colors)                  # 繪製左子圖
ax[1].scatter(x, y, z, c = colors, cmap='hsv')      # 繪製右子圖
ax[1].set_axis_off()            # 關閉軸

plt.show()

print("------------------------------------------------------------")  # 60個

def f1(x, y):                                # 左邊曲面函數
    return np.exp(-(0.5*X**2+0.5*Y**2))
def f2(x, y):                                # 右邊曲面函數
    return np.exp(-(0.1*X**2+0.1*Y**2))

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
np.random.seed(10)
c = np.random.rand(N, N)            # 取隨機色彩值
# 建立子圖
fig,ax = plt.subplots(1,3,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
sc = ax[0].scatter(X, Y, f1(X,Y), c=c, marker='o', cmap='hsv')
# 中間子圖乎叫 f2
sc = ax[1].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[1].set_axis_off()
# 右邊子圖乎叫 f2, 但是用不同的仰角和方位角
sc = ax[2].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[2].set_axis_off()
ax[2].view_init(60,-30)
ax[2].set_title(f"仰角={ax[2].elev},方位角={ax[2].azim}",color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.animation import FuncAnimation

def f(x, y):                                # 左邊曲面函數
    return (4 - x**2 - y**2)
def animate(i):
    ax.view_init(60,i)

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖
ax.set_axis_off()

ani = FuncAnimation(fig,func=animate,frames=np.arange(0,360,3),
                    interval=60)
plt.show()


      

print("------------------------------------------------------------")  # 60個


""" 共同抽出
plt.savefig('tmp_pic.jpg')



"""

