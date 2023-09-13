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




plt.show()

print('------------------------------------------------------------')	#60個



