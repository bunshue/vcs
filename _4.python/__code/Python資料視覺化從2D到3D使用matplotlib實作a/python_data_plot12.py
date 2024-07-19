
print("------------------------------------------------------------")  # 60個

# 共同
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
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

img = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 18],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35]])               
plt.imshow(img, cmap='Blues')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

img = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 18],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35]])               
plt.imshow(img, cmap='Blues', origin='lower')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
data = np.random.random((10, 10))
plt.imshow(data)
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
data = np.random.random((80, 80))
plt.imshow(data, cmap='cool')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

top = mpl.cm.get_cmap('OrRd_r', 128)        # OrRd_r色彩反轉
bottom = mpl.cm.get_cmap('Blues', 128)      # Blues色彩
# 組合OrRd_r和Blues色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
OrRdBlue = mpl.colors.ListedColormap(newcolors)

np.random.seed(10)
plt.subplot(211)                            # 上方子圖
data1 = np.random.random((80, 80))
plt.imshow(data1, cmap=OrRdBlue)

plt.subplot(212)                            # 下方子圖
data2 = np.random.random((80, 80))
plt.imshow(data2, cmap=OrRdBlue)
plt.subplots_adjust(left=0.2, right=0.6, bottom=0.1, top=0.9)
# 建立子圖表axes物件
ax = plt.axes([0.7, 0.1, 0.05, 0.8])        # 設定色彩條大小和位置
plt.colorbar(mpl.cm.ScalarMappable(cmap=OrRdBlue),cax=ax)
plt.show()

print("------------------------------------------------------------")  # 60個

N = 5
data = np.reshape(np.linspace(0,1,N**2), (N,N)) # 建立 N x N 陣列
plt.figure()
# 使用預設顏色繪製
plt.subplot(131)
plt.imshow(data)
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks(range(N))                            # 繪製 y 軸刻度
plt.title('使用預設插值',fontsize=12,color='b')
# 相同陣列使用不同的插值法
plt.subplot(132)
plt.imshow(data,interpolation='bicubic')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 bicubic 插值',fontsize=12,color='b')
plt.subplot(133)
plt.imshow(data,interpolation='hamming')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 hamming 插值',fontsize=12,color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

N = 5
np.random.seed(10)                  # 設定種子顏色值
src = np.random.random((N,N,3))     # 隨機產生影像圖陣列資料
plt.figure()

plt.subplot(141)
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks(range(N))    # 繪製 y 軸刻度
plt.title('RGB色彩')
plt.imshow(src)

plt.subplot(142)
r = src.copy()          # 複製影像色彩陣列
r[:,:,[1,2]] = 0        # 保留紅色元素, 設定綠色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Red元素')
plt.imshow(r)

plt.subplot(143)
g = src.copy()          # 複製影像色彩陣列
g[:,:,[0,2]] = 0        # 保留綠色元素, 設定紅色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Green元素')
plt.imshow(g)

plt.subplot(144)
b = src.copy()          # 複製影像色彩陣列
b[:,:,[0,1]] = 0        # 保留藍色元素, 設定紅色和綠色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Blue元素')
plt.imshow(b)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.array([1,2,3,4,5])
y = np.array([6,7,8])

#x軸1~5, y軸6~8, 編織出來15個點 xx, yy
xx, yy = np.meshgrid(x,y)

print('xx = \n', xx)
print('yy = \n', yy)

plt.scatter(xx,yy,marker='o',c='m')

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
xx, yy = np.meshgrid(x, y)

#z = np.sin(xx) + np.cos(yy)   # 建立影像
#z = np.sin(xx) + np.cos(yy)   # 建立影像
z = np.sin(xx) + np.sin(yy)   # 建立影像

plt.imshow(z)
#plt.imshow(z,cmap='hsv')
plt.show()

print("------------------------------------------------------------")  # 60個

x1 = [1,2,3]
y1 = [4,5,6,7,8]
z1 = np.add.outer(x1, y1)
print(f"z1 = \n{z1}")

x2 = range(8)
y2 = range(8)
z2 = np.add.outer(x2, y2)
print(f"z2 = \n{z2}")

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
z = np.add.outer(range(8), range(8)) % 2

im1 = plt.imshow(z, cmap='gray')

plt.show()

print("------------------------------------------------------------")  # 60個

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
xx, yy = np.meshgrid(x, y)
# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

fig = plt.figure()
z1 = np.add.outer(range(8), range(8)) % 2           # 棋盤
plt.imshow(z1, cmap='gray',extent=extent)           # 影像 1

z2 = np.sin(xx) + np.cos(yy)                        # 影像 2 公式
plt.imshow(z2, cmap='jet', alpha=0.8,
           interpolation='bilinear',extent=extent)  # 影像 2
plt.show()

print("------------------------------------------------------------")  # 60個

farmers = ["張三","李四","大成","陳王", "李曉.","林邊"]
fruits = ["釋迦","番茄","鳳梨","蓮霧","香蕉","芭樂"]
# 建立收成表
harvest = np.array([[0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
                    [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
                    [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
                    [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
                    [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
                    [0.3, 2.2, 0.0, 1.3, 0.0, 1.5]])

fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap='YlGn')
ax.figure.colorbar(im, ax=ax)
# 依據農夫姓名建立 x 軸刻度標記和刻度標籤
ax.set_xticks(np.arange(len(farmers)))
ax.set_xticklabels(farmers)
# 依據水果名稱建立 y 軸刻度標記和刻度標籤
ax.set_yticks(np.arange(len(fruits)))
ax.set_yticklabels(fruits)
# 炫轉 x 軸刻度標籤
plt.setp(ax.get_xticklabels(), rotation=45)
# 使用雙層迴圈註記收成數量
for i in range(len(fruits)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i,j],
                        ha="center", va="center", color="b")
ax.set_title("農夫收成(噸 / 年)",fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")
fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

farmers = ["張三","李四","大成","陳王", "李曉.","林邊"]
fruits = ["釋迦","番茄","鳳梨","蓮霧","香蕉","芭樂"]
# 建立收成表
harvest = np.array([[0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
                    [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
                    [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
                    [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
                    [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
                    [0.3, 2.2, 0.0, 1.3, 0.0, 1.5]])

fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap='YlGn')
ax.figure.colorbar(im, ax=ax)
# 依據農夫姓名建立 x 軸刻度標記和刻度標籤
ax.set_xticks(np.arange(len(farmers)))
ax.set_xticklabels(farmers)
# 依據水果名稱建立 y 軸刻度標記和刻度標籤
ax.set_yticks(np.arange(len(fruits)))
ax.set_yticklabels(fruits)
# 炫轉 x 軸刻度標籤
plt.setp(ax.get_xticklabels(), rotation=45)
# 使用雙層迴圈註記收成數量
for i in range(len(fruits)):
    for j in range(len(farmers)):
        if harvest[i,j] < 3.0:
            text = ax.text(j, i, harvest[i,j],
                           ha="center", va="center", color="b")
        else:
            text = ax.text(j, i, harvest[i,j],
                           ha="center", va="center", color="w")
ax.set_title("農夫收成(噸 / 年)",fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")
fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


