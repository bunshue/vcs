"""
bar3d : 3D 長條圖

"""

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


fig = plt.figure(
    num="3D繪圖 集合 bar3d 3D長條圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection='3d')

colors = ['m', 'r', 'g', 'b']   # 不同平面的顏色
yticks = [3, 2, 1, 0]           # y 座標平面
ax.set_yticks(yticks)           # 設定 y 軸刻度標記
# 依次在 y = 3, 2, 1, 0 平面繪製長條圖
for c, k in zip(colors, yticks):
    left = np.arange(12)        # 建立 x 軸座標 
    height = np.random.rand(12) # 建立長條高度
    ax.bar(left, height, zs=k, zdir='y', color=c, alpha=0.8) 



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

# 定義長條的位置
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [1,2,3,4,5,6,7,8,9,10]
zpos = [0,0,0,0,0,0,0,0,0,0]
# 定自長條的外形
dx = np.ones(10)                # 寬度
dy = np.ones(10) * 0.5          # 深度
dz = [1,2,3,4,5,6,7,8,9,10]     # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='m',alpha=0.8)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

# 定義長條的位置
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [1,2,3,4,5,6,7,8,9,10]
zpos = [0,0,0,0,0,0,0,0,0,0]
# 定自長條的外形
dx = np.ones(10)                # 寬度
dy = np.ones(10) * 0.5          # 深度
dz = [1,2,3,4,5,6,7,8,9,10]     # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,
         color='lightgreen',
         edgecolor='black')


print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

# 定義長條的位置
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [1,2,3,4,5,6,7,8,9,10]
zpos = [0,0,0,0,0,0,0,0,0,0]
# 定自長條的外形
dx = np.ones(10)                # 寬度
dy = np.ones(10) * 0.5          # 深度
dz = [1,2,3,4,5,6,7,8,9,10]     # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,
         color='lightgreen',
         edgecolor='black',shade=False)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

# 定義 xpos, ypos, zpos 座標位置
x = list(range(1,6))
y = list(range(1,6))
xx, yy = np.meshgrid(x, y)
xpos = xx.ravel()
ypos = yy.ravel()
zpos = np.zeros(len(x)*len(y))
# 定義長條
dx = np.ones(len(x)*len(y)) * 0.6
dy = np.ones(len(x)*len(y)) * 0.6
z = np.linspace(1,3,25).reshape(len(x),len(y))
dz = z.ravel()
# 定義顏色
color = ["yellow","aqua","lightgreen","orange","blue"]
color_list = []
for i in range(len(x)):
    c = color[i]
    color_list.append([c] * len(y))
colors = np.asarray(color_list)
barcolors = colors.ravel()
# 繪製 3D 長條圖
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=barcolors)  


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

# 三維柱圖
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y) # 生成網格點座標矩陣
x, y = _xx.ravel(), _yy.ravel() # 展開爲一維數組
top = x + y
bottom = np.zeros_like(top) # 與top數組形狀一樣，內容全部爲0
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)


plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

# 建立影像和 3D 軸物件
fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
# 建立 x, y, z
_x = np.arange(3)
_y = np.arange(6)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros(len(_x) * len(_y))
# 建立 dx, dy, dz
dx = np.ones(len(x))
dy = dx
dz = x + y
# 建立 3D 長條圖
ax1.bar3d(x,y,z,dx,dy,dz,shade=True,edgecolor='w',color='g')
ax1.set_title('含陰影',fontsize=16,color='m')

ax2.bar3d(x,y,z,dx,dy,dz,shade=False,edgecolor='w',color='g')
ax2.set_title('不含陰影',fontsize=16,color='m')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection='3d')

# 建立 x, y, z
_x = np.linspace(0, 10, 10)
_y = np.linspace(1, 10, 3)
_xx, _yy = np.meshgrid(_x, _y)
_zz = np.exp(-_xx * (1. / _yy))
x = _xx.flatten()
y = _yy.flatten()
z = np.zeros(_zz.size)
# 建立 dx, dy, dz, 也就是定義長條
dx = .25 * np.ones(_zz.size)
dy = .25 * np.ones(_zz.size)
dz = _zz.flatten()
# 定義顏色
color = ["yellow","aqua","lightgreen"]
color_list = []
for i in range(len(_y)):
    c = color[i]
    color_list.append([c] * len(_x))
colors = np.asarray(color_list)
barcolors = colors.ravel()

# 建立 3D 長條圖
ax.bar3d(x, y, z, dx, dy, dz, color=barcolors, alpha=0.5)
ax.set_title('bar3d')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection='3d')



# 繪製 3D 長條圖
# fig = plt.figure(figsize=(12, 8))

xpos = np.arange(10)
ypos = np.arange(10)
zpos = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10) + 1

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)

ax.set_title("繪製 3D 長條圖")



plt.show()

print("------------------------------------------------------------")  # 60個




sys.exit()

ax1.set_xlabel('X',color='b')
ax1.set_ylabel('Y',color='b')
ax1.set_zlabel('Z',color='b')

