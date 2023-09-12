import os
import sys
import time
import random

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

'''
#plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'y:',seq,data4,'k.')   
#plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')   
#plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')

plt.savefig('out20_12.jpg')

import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread('out20_12.jpg')
plt.imshow(fig)
plt.show()
'''


'''
print('------------------------------------------------------------')	#60個

import numpy as np

x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

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

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

points = 30
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(points):                     # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1,11,points)          # 建立 x
y = np.random.randint(1,11,points)          # 建立 y
size =  (30 * np.random.rand(points))**2    # 散點大小數列
plt.scatter(x, y, s=size, c=colors)         # 繪製散點
plt.xticks(np.arange(0,12,step=1.0))        # x 軸刻度
plt.yticks(np.arange(0,12,step=1.0))        # y 軸刻度
plt.show()

print('------------------------------------------------------------')	#60個

# ch20_24.ipynb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=x,cmap='rainbow')  # 色彩隨 x 軸值變化
plt.show()



print('------------------------------------------------------------')	#60個


# ch20_25.ipynb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=y,cmap='rainbow')  # 色彩隨 y 軸值變化
plt.colorbar()                            # 色彩條
plt.show()




print('------------------------------------------------------------')	#60個

# ch20_26.py
import matplotlib.pyplot as plt
import random

def loc(index):
    #處理座標的移動
    x_mov = random.choice([-3, 3])          # 隨機x軸移動值
    xloc = x[index-1] + x_mov               # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])   # 隨機y軸移動值
    yloc = y[index-1] + y_mov               # 計算y軸新位置
    x.append(xloc)                          # x軸新位置加入串列
    y.append(yloc)                          # y軸新位置加入串列
    
num = 10000                                 # 設定隨機點的數量
x = [0]                                     # 設定第一次執行x座標
y = [0]                                     # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
plt.axis('off')                             # 隱藏座標
plt.show()


print('------------------------------------------------------------')	#60個

plt.plot(x1, y1, 'go-')
plt.plot(x2, y2, 'm.-')

plt.plot(seq, data1, '-*')
plt.plot(seq, data2, 'm-o')                      


plt.subplot(2,2,1)  #四格佔1格
plt.subplot(2,2,2)  #四格佔1格
plt.subplot(2,1,2)  #二格佔1格 = 四格佔2格
'''

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')

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

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
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

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
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

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
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

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('得票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
from random import randint

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)
         
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

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
from random import randint

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)
         
times = 10000                           # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
dice_generator(times, sides)            # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.8)     # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
from random import randint

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)
         
times = 10000                           # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
dice_generator(times, sides)            # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area)
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area,autopct="%1.2f%%")
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
exp = [0.0,0.0,0.0,0.0,0.0,0.1]
plt.pie(people,labels=area,explode=exp,autopct="%1.2f%%")
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')
plt.show()



print('------------------------------------------------------------')	#60個


# ch20_40.ipynb
import matplotlib.pyplot as plt  
import numpy as np  
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
ani.save('sin.gif', writer='pillow')        # 儲存 sin.gif 檔案
plt.show()

print('------------------------------------------------------------')	#60個


# ch20_41.ipynb
import matplotlib.pyplot as plt  
import numpy as np  
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
ani.save('sin2.gif', writer='pillow')       # 儲存 sin2.gif 檔案
plt.show()


print('------------------------------------------------------------')	#60個

# ch20_42.ipynb
import numpy as np
import matplotlib.pyplot as plt
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
ani.save('sinball.gif', writer='pillow')   # 儲存 sinball.gif 檔案

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
# 建立衰減數列.
x = np.linspace(0.0, 5.0, 50)
y = np.cos(3 * np.pi * x) * np.exp(-x)

plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)
plt.plot(x, y, 'go-')
plt.ylabel('衰減值')
plt.show()


print('------------------------------------------------------------')	#60個

# ch20_44.ipynb
import matplotlib.pyplot as plt

plt.title(r'$\frac{7}{9}+\sqrt{7}+\alpha\beta$',fontsize=20)
plt.show()
print('------------------------------------------------------------')	#60個


# ch20_45.ipynb
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(1,0,'bo')                  # 輸出藍點
plt.text(1,0,'sin(x)',fontsize=20)  # 輸出公式
plt.plot(x,y)
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib as mpl
import matplotlib.pyplot as plt 
from matplotlib.font_manager import fontManager
import numpy as np

fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
mpl.rc('font', family='Taipei Sans TC Beta')
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


print('------------------------------------------------------------')	#60個

