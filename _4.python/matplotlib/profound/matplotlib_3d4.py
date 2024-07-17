"""
3D 曲面與輪廓設計
"""

from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import Axes3D

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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.clabel(cset, fontsize=9, inline=1)
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 繪製曲線表面
ax.plot_surface(X, Y, Z, cmap="bwr")
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
ax.set_title('繪製曲線表面',fontsize=14,color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return (np.power(x,2) + np.power(y, 2))

fig = plt.figure()                  
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

fig = plt.figure()                  
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='hsv')   # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure()                  
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='seismic') # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return (4 - x**2 - y**2)

fig = plt.figure()                  
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='seismic') # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 用 3D 線框繪製曲線表面
ax.plot_wireframe(X, Y, Z, color='g')
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 用 3D 線框繪製曲線表面
ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 定義資料資料
x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 用 3D 線框繪製曲線表面
ax.plot_wireframe(X, Y, Z, color = 'm')
ax.set_title('wireframe( )函數的實例',fontsize=16,color='b');
plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contour(X, Y, Z, cmap='jet')
plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contour3D(X, Y, Z, cmap='jet')

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contourf(X, Y, Z, cmap='jet')
plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.contourf3D(X, Y, Z, cmap='jet')
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# matplotlib 官方測試數據
X, Y, Z = axes3d.get_test_data(0.05)
# 繪製 3D 框線圖
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, alpha=0.3)
# 測試數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='jet')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 建立數據
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
c = np.random.rand(N, N)
Z = 10 * np.exp(-(0.5*X**2+0.5*Y**2))
# 繪製 3D 框線圖
ax.plot_wireframe(X,Y,Z,rstride=5,cstride=5,color='g')
# 數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X,Y,Z,zdir='z',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='x',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='y',offset=10,cmap='cool')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return np.sin(np.sqrt(x ** 2 + y ** 2))

fig = plt.figure()                  
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據
ax.plot_surface(X, Y, f(X,Y), cmap='seismic') # 繪製 3D 圖
ax.set_xlabel('x', color='b')
ax.set_ylabel('y', color='b')
ax.set_zlabel('z', color='b')
ax.view_init(60,45)                         # 設定 3D 視角
plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.figure().add_subplot(projection='3d')
# 建立網格空間
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
# 建立箭頭方向
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w,length=0.1,normalize=True,color='r')
plt.show()

print("------------------------------------------------------------")  # 60個

# 建立影像和 3D 軸物件
fig = plt.figure()
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
# 顯示座標軸
ax.set_xlabel('x',color='b')
ax.set_ylabel('y',color='b')
ax.set_zlabel('z',color='b')
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

