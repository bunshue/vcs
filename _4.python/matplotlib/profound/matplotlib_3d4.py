"""
3D plot 集合 4

共用資料 大整理用

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

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import axes3d
from matplotlib.cm import viridis as colormap

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

# 此 figure 共用資料

# 1. Z = X^2 + Y^2
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

# 2. Z = sin(sqrt(X^2 + Y^2))
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x = np.linspace(-2 * np.pi, 2 * np.pi)
y = np.linspace(-2 * np.pi, 2 * np.pi)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

"""
x = np.linspace(-5, 5, num=50)
y = np.linspace(-5, 5, num=50)
X, Y = np.meshgrid(x, y)
Z = X * Y
"""

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

ax.plot_wireframe(X, Y, Z)
ax.set_title('plot_wireframe 3D線框圖')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

ax.plot_wireframe(X, Y, Z, alpha=0.1)
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)
#ax.set_title("等高線")
ax.set_title('plot_wireframe 3D線框圖 + 等高線')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)

"""
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)
"""
ax.set_title("plot_surface")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

ax.plot_surface(X, Y, Z, cmap=cm.hsv)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
# fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_title("曲面圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖


plt.tight_layout()
plt.show()



print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

ax.plot_surface(X, Y, Z)
ax.set_title("曲面 surface")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

plt.contour(X, Y, Z)
ax.set_title("曲面 contour")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

plt.contourf(X, Y, Z)
ax.set_title("曲面 contourf")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

ax.plot_surface(X, Y, Z)  # 畫出三軸資料所構成的曲面
ax.set_title("plot_surface")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

ax.plot_surface(X, Y, Z)
ax.set_title("繪製曲面 plot_surface")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("給曲面套上顏色")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 1 使用共同測試數據",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

# 此 figure 共用資料
X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

print("------------------------------------------------------------")  # 60個
ax = fig.add_subplot(231, projection='3d')

#ax.contour(X, Y, Z, cmap='jet')

#多了ax.clabel 16, extend3d=True
cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.clabel(cset, fontsize=9, inline=1)
ax.set_title('contour')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

ax.contour3D(X, Y, Z, cmap='jet')
ax.set_title('contour3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

ax.contourf(X, Y, Z, cmap='jet')
ax.set_title('contourf')

print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

ax.contourf3D(X, Y, Z, cmap='jet')
ax.set_title('contourf3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

ax.plot_surface(X, Y, Z, cmap="bwr")
#ax.plot_surface(X, Y, Z, cmap="seismic")
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

ax.plot_wireframe(X, Y, Z, color='g')
#ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
#ax.plot_wireframe(X, Y, Z, cstride=10, rstride=10)
ax.set_title('plot_wireframe 3D線框圖')

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

# 此 figure 共用資料

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

def f(x, y):                                # 曲面函數
    return np.sin(np.sqrt(x ** 2 + y ** 2))

def f(x, y):                                # 曲面函數
    return (np.power(x,2) + np.power(y, 2))

def f(x, y):                                # 曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

def f(x, y):                                # 曲面函數
    return (4 - x**2 - y**2)

x = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(x, y)                    # 建立取樣數據
Z = f(X, Y)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

ax.plot_wireframe(X, Y, Z, color = 'm')
ax.set_title('plot_wireframe 3D線框圖')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

ax.view_init(60,45)                         # 設定 3D 視角

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

ax.plot_surface(X, Y, Z, cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

ax.plot_surface(X, Y, Z, cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')


plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection='3d')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection='3d')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')


plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


