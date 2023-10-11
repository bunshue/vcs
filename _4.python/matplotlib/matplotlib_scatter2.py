# scatter 集合

import sys
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






#第六張圖
plt.subplot(236)

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)

# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)

plt.show()


print('------------------------------------------------------------')	#60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(num = 'scatter 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

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

#第二張圖
plt.subplot(232)

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                     # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1,11,N)          # 建立 x
y = np.random.randint(1,11,N)          # 建立 y
size =  (30 * np.random.rand(N))**2    # 散點大小數列
plt.scatter(x, y, s=size, c=colors)         # 繪製散點
plt.xticks(np.arange(0,12,step=1.0))        # x 軸刻度
plt.yticks(np.arange(0,12,step=1.0))        # y 軸刻度

#第三張圖
plt.subplot(233)

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=x,cmap='rainbow')  # 色彩隨 x 軸值變化

#第四張圖
plt.subplot(234)

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=y,cmap='rainbow')  # 色彩隨 y 軸值變化
plt.colorbar()                            # 色彩條


#第五張圖
plt.subplot(235)

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


#第六張圖
plt.subplot(236)


x = np.linspace(0, 10, 51)
print(type(x))

y1 = np.sin(x) * 5 + 5
y2 = np.cos(x) * 5 + 5

plt.scatter(x, y1, c = 'r')       #畫出每個x-y對應點
plt.scatter(x, y2, c = 'g')       #畫出每個x-y對應點


plt.show()

print('------------------------------------------------------------')	#60個





