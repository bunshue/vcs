"""
3D plot 集合

參考 使用Matplotlib繪制3D圖形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/

3D plot 集合 1 大整理

1.plot() / plot3D()  # 繪製 3D 折線
2.scatter() / scatter3D() # 3D 散佈圖/散點圖 
3.plot_wireframe()
4.plot_surface() 繪製曲線表面圖 曲面圖
5.contour() (contour, contour3D, contourf, contourf3D)
6.quiver()
其他

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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

from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.collections import PolyCollection
from matplotlib.cm import viridis as colormap


def show():
    # pass
    plt.tight_layout()
    plt.show()


print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8])

# x軸1~5, y軸6~8, 編織出來15個點 X, Y
X, Y = np.meshgrid(x, y)

print("X = \n", X)
print()
print("Y = \n", Y)

plt.scatter(X, Y, marker="o", c="m")
plt.title("畫出 meshgrid")
show()

# 數字拉平
XR = X.ravel()
YR = Y.ravel()
print(XR)
print()
print(YR)

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
z = np.c_[x.ravel(), y.ravel()]
print(z.shape)
print(z)

print()

x = np.arange(1, 5, 1)  # 1 2 3 4
y = np.arange(5, 9, 1)  # 5 6 7 8
X, Y = np.meshgrid(x, y)
Z = np.c_[X.ravel(), Y.ravel()]

print(X)
print(Y)
print(Z)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 建立影像和 3D 軸物件
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

# 從(x, y, z)指向(dx,dy,dz)
x, y, z = 0, 0, 0
dx, dy, dz = 1, 1, 1
ax.quiver(x, y, z, dx, dy, dz, color="r")

ax.set_xlim3d(0, 1.2)
ax.set_ylim3d(0, 1.2)
ax.set_zlim3d(0, 1.2)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.scatter(0, 0, 0, c="r", s=100)
ax.scatter(1, 1, 1, c="g", s=100)

elevation, azimuth = 10, 30  # 仰角 方位角
ax.view_init(elev=elevation, azim=azimuth)  # 仰角(elevation), 方位角(azimuth)
# 仰角(elevation), 看向原點, xy平面之夾角
# 方位角(azimuth), 看向原點, 與+y軸之夾角

ax.set_xlabel("X", color="r")
ax.set_ylabel("Y", color="g")
ax.set_zlabel("Z", color="b")

show()

"""
ax = plt.figure()
ax.add_subplot(projection='3d')

ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
ax.set_title('繪製曲線表面',fontsize=14,color='b')
ax.set_title('wireframe( )函數的實例',fontsize=16,color='b');

"""

print("------------------------------------------------------------")  # 60個

import cv2

filename = "mola_1024x512_200mp.jpg"
filename = "C:/_git/vcs/_1.data/______test_files1/_material/ims3.bmp"

IMG_GRAY = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.title("使用 matplotlib 顯示圖片, 需先BGR轉RGB")
plt.imshow(cv2.cvtColor(IMG_GRAY, cv2.COLOR_BGR2RGB))
show()

print("image.shape內容 :", IMG_GRAY.shape)

H, W = IMG_GRAY.shape

x = np.linspace(W - 1, 0, W)
y = np.linspace(0, H - 1, H)

X, Y = np.meshgrid(x, y)
Z = IMG_GRAY[0:H, 0:W]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(X, Y, Z, 50, cmap="gist_earth")  # 150為剖面採樣數
ax.auto_scale_xyz([W - 1, 0], [0, H - 1], [0, 300])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection="3d")

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))
"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

# I think this is different from plt12_contours
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""

ax.set_zlim(-2, 2)

show()

print("------------------------------------------------------------")  # 60個


def f1(x, y):  # 左邊曲面函數
    return np.power(x, 2) + np.power(y, 2)


def f2(x, y):  # 右邊曲面函數
    r = np.sqrt(np.power(x, 2) + np.power(y, 2))
    return np.sin(r)


X = np.arange(-3, 3, 0.1)  # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)  # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)  # 建立 XY 座標
# 建立子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={"projection": "3d"})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X, Y), cmap="hsv")  # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X, Y), cmap="hsv")  # 繪製 3D 圖
show()


print("------------------------------------------------------------")  # 60個


# 建立3D測試資料

# 此 figure 共用資料

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

# 1. Z = X^2 + Y^2
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
# np.add 兩個陣列相加
Z = np.add(np.power(X, 2), np.power(Y, 2))

# 2. Z = sin(sqrt(X^2 + Y^2))
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x = np.linspace(-2 * np.pi, 2 * np.pi, 30)
y = np.linspace(-2 * np.pi, 2 * np.pi, 30)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

"""
x = np.linspace(-5, 5, num=50)
y = np.linspace(-5, 5, num=50)
X, Y = np.meshgrid(x, y)
Z = X * Y
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 1.plot + 2.scatter 散點圖1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")

# 畫點連線
xs = np.array([0, -5, -5, 5, 5, -5, 5])
ys = np.array([0, 5, 5, 5, -5, -5, 5])
zs = np.array([-5, -5, 5, -5, -5, -5, 5])

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

ax.plot(xs, ys, zs, color="m", lw=2)
ax.scatter(xs, ys, zs, color="y", s=100)

plt.title("3D折線圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")

N = 150
# 建立折線用的 3D 座標資料
t = np.linspace(0, 1, N)
x = t * np.sin(30 * t)
y = t * np.cos(30 * t)
z = t

"""
t = np.linspace(0, 20, N)
x = np.cos(t)
y = np.sin(t)
z = t
"""
c = x + y
ax.scatter(x, y, z, c=c, cmap="hsv")  # 繪製 3D 散點圖

# 繪製 3D 折線
ax.plot(x, y, z, color="m", lw=2)
# ax.plot3D(x, y, z) #plot3D看起來和plot一樣

# 投影在xy平面
ax.plot(x, y, zs=0, zdir="z")

# 建立散點用的 3D 座標資料, z 則沿用
x2 = x + np.random.randn(N) * 0.1
y2 = y + np.random.randn(N) * 0.1
ax.scatter(x2, y2, z, c=c, cmap="hsv")  # 繪製 3D 散點圖

plt.title("3D折線圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")

ax.scatter(X, Y, Z)
ax.scatter(X, Y, Z, c="r")
# ax.scatter(X, Y, Z, c=Z, cmap="Reds", marker="^", label="My Points 1")
# ax.scatter(X, Y, Z, c=Z, cmap="Blues", marker="o", label="My Points 2")
# ax.scatter(x1,y1,z1,c=z1,cmap='Oranges',marker='d',label='A 資料組')
# ax.scatter(x2,y2,z2,c=z2,cmap='Blues',marker='*',label='B 資料組')
# ax.scatter(X, Y, Z + 0.7 * np.random.randn(10, 10))
# ax.scatter(X, Y, Z, color="y", s=3)
ax.scatter3D(X, Y, Z)
ax.scatter(X, Y, Z, marker="*", color="m")

c = X + Y
ax.scatter(X, Y, Z, c=c)
ax.scatter(X, Y, Z, c=c, cmap="hsv")

# sc = ax.scatter(X, Y, Z, c=c, marker="o", cmap="hsv")
# fig.colorbar(sc)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")

ax.plot_wireframe(X, Y, Z)
# ax.plot_wireframe(X, Y, Z, alpha=0.1)
# ax.plot_wireframe(X, Y, Z, color = "r")
# ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
# ax.plot_wireframe(X, Y, Z, cstride=10, rstride=10)

# ax.plot_surface(X, Y, Z)   不分層著色
# ax.plot_wireframe(X, Y, Z)  #畫線框圖

# 畫線框圖
# surf = ax.plot_wireframe(X, Y, Z)
# fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

# 畫線框圖
# ax.plot_wireframe(X, Y, Z)
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

# cstride column 每幾點畫一條線 x軸
# rstride row    每幾點畫一條線 y軸

"""
rstride 	Array row stride (step size), defaults to 1
cstride 	Array column stride (step size), defaults to 1
rcount 	Use at most this many rows, defaults to 50
ccount 	Use at most this many columns, defaults to 50
X,Y,Z：輸入資料
rstride:行步長
cstride:列步長
rcount:行數上限
ccount:列數上限
"""

ax.set_title("plot_wireframe 3D線框圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ("r", "g", "b", "k")

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))

c_list = []
for c in colors:
    c_list.extend([c] * 20)

# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir="y", c=c_list)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 4.plot_surface 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=colormap)
# ax.plot_surface(X, Y, Z, alpha=0.3)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
# ax.plot_surface(X, Y, Z, cmap=cm.hsv)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
# fig.colorbar(surf, shrink=0.5, aspect=5)

"""
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)
"""

# 畫出三軸資料所構成的曲面
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z, cmap="seismic")
ax.plot_surface(X, Y, Z, cmap="hsv")
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.plot_surface(X, Y, Z, cmap="bwr")

ax.set_title("plot_surface 3D曲線表面")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")

# 三維曲面圖和等高線圖

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
# fig.colorbar(surf, shrink=0.5, aspect=5)
ax.contourf(X, Y, Z, zdir="z", offset=-2)  # 把等高線向z軸投射
ax.set_zlim(-2, 2)  # 設置z軸範圍

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")

# 3D表面（彩色地圖）
# 演示如何繪制使用CoolWarm顏色映射著色的3D曲面。使用“抗鋸齒=假”使表面不透明。
# 還演示了使用線性定位器和Z軸刻度標簽的自定義格式。

from matplotlib.ticker import LinearLocator

# fig, ax = plt.subplots(subplot_kw = {"projection" : "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter("{x:.02f}")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")

# 2. 接下來給進 X 和 Y 值，並將 X 和 Y 編織成柵格。每一個（X, Y）點對應的高度值我們用下面這個函數來計算。
# 使用ax.plot_surface繪出網格表面圖形，並將一個 colormap rainbow 填充顏色。

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # x-y 平面的網格
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap("rainbow"))

# 3.將三維圖像投影到 XY 平面上做一個等高線圖。

ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))

# 其中，rstride 和 cstride 分別代表 row 和 column 的跨度。 可比較兩個圖分別是跨度為1 和 5 的效果。

# 3D基本操作

# fig = plt.figure()
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # x-y 平面的網格
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap("rainbow"))
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 4.plot_surface 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection="3d")

# ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1)
# 修改曲面顏色, 使用cmap屬性可指定曲面顏色
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)

# ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)    #分層著色

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")


def blending(t):
    return 6 * (t**5) - 15 * (t**4) + 10 * (t**3)


def lerp(g1, g2, t):
    return g1 + t * (g2 - g1)


def grad2(hashvalue, dx, dy):
    return [dy, dx + dy, dx, dx - dy, -dy, -dx - dy, -dx, -dx + dy][hashvalue % 8]


rand_table = np.random.randint(255, size=256).tolist()


def _perlin2(x, y):
    xi = math.floor(x)
    yi = math.floor(y)

    aa = rand_table[(rand_table[xi % 256] + yi) % 256]
    ba = rand_table[(rand_table[(xi + 1) % 256] + yi) % 256]
    ab = rand_table[(rand_table[xi % 256] + yi + 1) % 256]
    bb = rand_table[(rand_table[(xi + 1) % 256] + yi + 1) % 256]

    dx = x - xi
    dy = y - yi

    u = blending(dx)
    v = blending(dy)

    g1 = lerp(grad2(aa, dx, dy), grad2(ba, dx - 1, dy), u)
    g2 = lerp(grad2(ab, dx, dy - 1), grad2(bb, dx - 1, dy - 1), u)

    return lerp(g1, g2, v)


_perlin2 = np.frompyfunc(_perlin2, 2, 1)


def perlin2(x, y):
    cx, cy = np.meshgrid(x, y)
    return _perlin2(cx, cy).astype(float)


width = 100
x = np.arange(width)
y = np.arange(width)

X, Y = np.meshgrid(x, y)
Z = perlin2(x / 25, y / 25)

ax.plot_surface(X, Y, Z, cmap=cm.gist_earth)  # 用地形高度顏色來著色
ax.set_box_aspect((1, 1, 25 / width))
plt.title("Perlin noise")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")


# 正交曲線座標系統
# 球座標當中的三個曲面交出三條曲線，這三個曲線形成了廣義的正交曲線座標系統(generalized orthonormal curved coordinates)

# draw 3 surfaces
r = 1.0  # r=constant
f, t = np.mgrid[0 : 2 * np.pi : 40j, 0 : np.pi / 2 : 40j]
x = r * np.cos(f) * np.sin(t)
y = r * np.sin(f) * np.sin(t)
z = r * np.cos(t)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 2)
ax.plot_surface(x, y, z, alpha=0.5, color="r")

t = np.pi / 4.0  # theta=constant
r, f = np.mgrid[0:1.5:40j, 0 : 2.0 * np.pi : 40j]
x = r * np.sin(t) * np.cos(f)
y = r * np.sin(t) * np.sin(f)
z = r * np.cos(t)
ax.plot_surface(x, y, z, alpha=0.3, color="g")

f = np.pi / 4.0  # phi=constant
r, t = np.mgrid[0:1.2:40j, 0 : np.pi / 2.0 : 40j]
x = r * np.sin(t) * np.cos(f)
y = r * np.sin(t) * np.sin(f)
z = r * np.cos(t)
ax.plot_surface(x, y, z, alpha=0.5, color="b")

ax.set_title(r"3 surfaces $r=1, \theta=\pi/4, \phi=\pi/4$" " meet in 3 curves")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_title("正交曲線座標系統")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")

ax.contour(X, Y, Z)
# ax.contour(X, Y, Z, cmap='jet')
# ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)
ax.contour3D(X, Y, Z, cmap="jet")
ax.contourf(X, Y, Z)
ax.contourf(X, Y, Z, cmap="jet")
ax.contourf3D(X, Y, Z, cmap="jet")

"""
#多了ax.clabel 16, extend3d=True
cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.clabel(cset, fontsize=9, inline=1)
"""
ax.set_title("contour / contour3D\ncontourf / contourf3D")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")

ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, alpha=0.3)
# ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='g')

# 測試數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X, Y, Z, zdir="z", offset=-100, cmap="jet")
cset = ax.contourf(X, Y, Z, zdir="x", offset=-40, cmap="jet")
cset = ax.contourf(X, Y, Z, zdir="y", offset=40, cmap="jet")

# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

ax.set_title("測試數據投影到x,y,z平面")


show()

print("------------------------------------------------------------")  # 60個

# 此 figure 共用資料


def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


def f(x, y):  # 曲面函數
    return np.sin(np.sqrt(x**2 + y**2))


def f(x, y):  # 曲面函數
    return np.power(x, 2) + np.power(y, 2)


def f(x, y):  # 曲面函數
    r = np.sqrt(np.power(x, 2) + np.power(y, 2))
    return np.sin(r)


def f(x, y):  # 曲面函數
    return 4 - x**2 - y**2


x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

x = np.arange(-3, 3, 0.1)  # 曲面 X 區間
y = np.arange(-3, 3, 0.1)  # 曲面 Y 區間
X, Y = np.meshgrid(x, y)  # 建立取樣數據
Z = f(X, Y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 6.quiver",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")

# 從(x, y, z)指向(dx,dy,dz)
x, y, z = 0, 0, -1
dx, dy, dz = 0, 0, 1
ax.quiver(x, y, z, dx, dy, dz, color="r", arrow_length_ratio=0.1)

x, y, z = 0, 0, 0
dx, dy, dz = 1, 1, 1
ax.quiver(x, y, z, dx, dy, dz, color="g")

x, y, z = 1, 1, 1
dx, dy, dz = 0, -2, -2
ax.quiver(x, y, z, dx, dy, dz, color="b")

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")

v1 = np.array([2, 0, 0])
v2 = np.array([0, 4, 0])
v3 = np.array([0, 0, 3])
v12 = v1 + v2
v123 = v1 + v2 + v3
print("v12=", v12)
print("v123=", v123)
print("|v123|=", np.linalg.norm(v123))
phi = np.arctan(3 / np.linalg.norm(v123))
print("phi=", phi, np.degrees(phi))
# ax.grid(True)
ax.quiver(-4, 0, 0, 8, 0, 0, color="g", arrow_length_ratio=0.05)
ax.quiver(0, -4, 0, 0, 8, 0, color="g", arrow_length_ratio=0.05)
ax.quiver(0, 0, -4, 0, 0, 8, color="g", arrow_length_ratio=0.05)
ax.scatter(0, 0, 0, "o")
ax.scatter(v1[0], v1[1], v1[2], "o")
ax.scatter(v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2], "o")
ax.scatter(v1[0] + v2[0] + v3[0], v1[1] + v2[1] + v3[1], v1[2] + v2[2] + v3[2], "o")
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color="b")
ax.quiver(v1[0], v1[1], v1[2], v2[0], v2[1], v2[2], color="b")
ax.quiver(v12[0], v12[1], v12[2], v3[0], v3[1], v3[2], color="b")
ax.quiver(0, 0, 0, v12[0], v12[1], v12[2], color="r", arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, v123[0], v123[1], v123[2], color="r", arrow_length_ratio=0.1)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")

# 建立網格空間, 產生格點資料
x, y, z = np.meshgrid(
    np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.8)
)

# 產生向量場資料
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z)

# 繪製向量場
# ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, color="r")
ax.set_title("quiver 3D 向量場")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")

# 三維等位面與法線

x = np.linspace(2.0, 5.0, 10)
y = np.linspace(2.0, 5.0, 10)
X, Y = np.meshgrid(x, y)
Z1 = np.sqrt(X**2 + Y**2)
Z2 = np.sqrt(X**2 + Y**2 - 2.0)
Z3 = np.sqrt(X**2 + Y**2 - 3.0)
ax.scatter([3], [4], [5], color="k", s=40)

ax.plot_surface(X, Y, Z1, label="C=0")
ax.plot_surface(X, Y, Z2, label="C=6")
ax.plot_surface(X, Y, Z3, label="C=12")

ax.quiver(3.0, 4.0, 5.0, 6.0 / 5.0, 8.0 / 5.0, -10.0 / 5.0, color="r")

ax.set_title("$f(x,y,z)=x^2+y^2-z=C$")
# ax.plot_surface(X, Y, Z)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
# ax.legend()

# ax.set_title("三維等位面與法線dddd")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")


show()

print("------------------------------------------------------------")  # 60個
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

ax = fig.add_subplot(231, projection="3d")

# 定義長條的位置
xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ypos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 定自長條的外形
dx = np.ones(10)  # 寬度
dy = np.ones(10) * 0.5  # 深度
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="m", alpha=0.8)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")

# 定義長條的位置
xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ypos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 定自長條的外形
dx = np.ones(10)  # 寬度
dy = np.ones(10) * 0.5  # 深度
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="lightgreen", edgecolor="black")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")

# 定義長條的位置
xpos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ypos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
zpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 定自長條的外形
dx = np.ones(10)  # 寬度
dy = np.ones(10) * 0.5  # 深度
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 高度
ax.bar3d(
    xpos, ypos, zpos, dx, dy, dz, color="lightgreen", edgecolor="black", shade=False
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")

colors = ["m", "r", "g", "b"]  # 不同平面的顏色
yticks = [3, 2, 1, 0]  # y 座標平面
ax.set_yticks(yticks)  # 設定 y 軸刻度標記

# 依次在 y = 3, 2, 1, 0 平面繪製長條圖
for c, k in zip(colors, yticks):
    left = np.arange(12)  # 建立 x 軸座標
    height = np.random.rand(12)  # 建立長條高度
    ax.bar(left, height, zs=k, zdir="y", color=c, alpha=0.8)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")

# 定義 xpos, ypos, zpos 座標位置
x = list(range(1, 6))
y = list(range(1, 6))
xx, yy = np.meshgrid(x, y)
xpos = xx.ravel()
ypos = yy.ravel()
zpos = np.zeros(len(x) * len(y))
# 定義長條
dx = np.ones(len(x) * len(y)) * 0.6
dy = np.ones(len(x) * len(y)) * 0.6
z = np.linspace(1, 3, 25).reshape(len(x), len(y))
dz = z.ravel()
# 定義顏色
color = ["yellow", "aqua", "lightgreen", "orange", "blue"]
color_list = []
for i in range(len(x)):
    c = color[i]
    color_list.append([c] * len(y))
colors = np.asarray(color_list)
barcolors = colors.ravel()
# 繪製 3D 長條圖
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=barcolors)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")

# 三維柱圖
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)  # 生成網格點座標矩陣
x, y = _xx.ravel(), _yy.ravel()  # 展開爲一維數組
top = x + y
bottom = np.zeros_like(top)  # 與top數組形狀一樣，內容全部爲0
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)

show()

print("------------------------------------------------------------")  # 60個
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

ax = fig.add_subplot(231, projection="3d")

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
ax.bar3d(x, y, z, dx, dy, dz, shade=True, edgecolor="w", color="g")
ax.set_title("含陰影")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")

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
ax.bar3d(x, y, z, dx, dy, dz, shade=False, edgecolor="w", color="g")
ax.set_title("不含陰影")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")

xpos = np.arange(10)
ypos = np.arange(10)
zpos = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = np.arange(10) + 1

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)

ax.set_title("繪製 3D 長條圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")

# 建立 x, y, z
_x = np.linspace(0, 10, 10)
_y = np.linspace(1, 10, 3)
_xx, _yy = np.meshgrid(_x, _y)
_zz = np.exp(-_xx * (1.0 / _yy))
x = _xx.flatten()
y = _yy.flatten()
z = np.zeros(_zz.size)
# 建立 dx, dy, dz, 也就是定義長條
dx = 0.25 * np.ones(_zz.size)
dy = 0.25 * np.ones(_zz.size)
dz = _zz.flatten()
# 定義顏色
color = ["yellow", "aqua", "lightgreen"]
color_list = []
for i in range(len(_y)):
    c = color[i]
    color_list.append([c] * len(_x))
colors = np.asarray(color_list)
barcolors = colors.ravel()

# 建立 3D 長條圖
ax.bar3d(x, y, z, dx, dy, dz, color=barcolors, alpha=0.5)
ax.set_title("bar3d")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")

month = np.arange(0, 13)
years = [2016, 2017, 2018, 2019]

precipitation = []
for year in years:
    value = np.random.rand(len(month)) * 300
    value[0], value[-1] = 0, 0
    precipitation.append(list(zip(month, value)))

poly = PolyCollection(precipitation, facecolors=["b", "c", "r", "m"])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=years, zdir="y")
ax.set_xlabel("Month")
ax.set_xlim3d(0, 12)
ax.set_ylabel("Year")
ax.set_ylim3d(2015, 2020)
ax.set_zlabel("Precipitation")
ax.set_zlim3d(0, 300)
ax.set_title("多邊形")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")

month = np.arange(1, 12)
years = [2016, 2017, 2018, 2019]


def get_color(value_array):
    color = []
    for v in value_array:
        if v < 50:
            color.append("y")
        elif v < 100:
            color.append("g")
        elif v < 150:
            color.append("b")
        elif v < 200:
            color.append("c")
        elif v < 250:
            color.append("m")
        else:
            color.append("r")
    return color


for year, c in zip(years, ["b", "c", "r", "m"]):
    value = np.random.rand(len(month)) * 300
    ax.bar(month, value, year, zdir="y", color=get_color(value), alpha=0.7)
    for i in np.arange(0, 12):
        ax.bar

ax.set_xlabel("Month")
ax.set_xticks(np.arange(1, 13))
ax.set_ylabel("Year")
ax.set_yticks(np.arange(2016, 2020))
ax.set_zlabel("Precipitation")
ax.set_title("柱狀圖")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3D繪圖

# 使用mplot3D繪制的3D曲面圖
import mpl_toolkits.mplot3d

x, y = np.mgrid[-2:2:20j, -2:2:20j]
z = x * np.exp(-(x**2) - y**2)

fig = plt.figure(figsize=(8, 6))
ax = plt.subplot(111, projection="3d")
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.Blues_r)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_circles  # 圓形分佈的資料集

X, y = make_circles(10, noise=0.1)
print(X.shape)
print(y.shape)
print(X)
print(y)

from mpl_toolkits import mplot3d

r = np.exp(-(X**2).sum(1))  # e^(X[0]^2+X[1])^2) ，sum(1)中的1表示表示 axis=1,沿着行的方向求和

print(r)

elev = 30
azim = 30
ax = plt.subplot(projection="3d")
ax.scatter3D(X[:, 0], X[:, 1], r, c=y, s=50, cmap="autumn")
ax.view_init(elev=elev, azim=azim)  # 改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
ax.set_xlabel("X", color="r")
ax.set_ylabel("Y", color="g")
ax.set_zlabel("Z", color="b")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

ax.set_xlabel(r"$\phi_\mathrm{real}$")
ax.set_ylabel(r"$\phi_\mathrm{im}$")
ax.set_zlabel(r"$V(\phi)$")

"""
#製作動圖
for angle in np.arange(95, 180, 12):
    ax.set_zlabel("Angle: " + str(angle))
    ax.view_init(30, angle)  # 設定 3D 視角(仰角, 方位角)
    filename = "./" + str(angle) + ".png"
    plt.savefig(filename)
    print("Save " + filename + " finish")
"""

# Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2

# R = np.sqrt(X**2 + Y**2)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

print("------------------------------------------------------------")  # 60個

# 製作資料
π = np.pi
θ = np.linspace(-5 * π, 5 * π, 200)

x = np.cos(θ)
y = np.sin(θ)
z = θ / (5 * π)

start = 0
end = np.pi * 20
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x)

x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = np.cos(x)

x = np.linspace(0, 5, 10)
y = np.linspace(0, 5, 10)
X, Y = np.meshgrid(x, y)

Z = 2 * X + Y

t = np.linspace(0, 1, 300)
x = t * np.sin(30 * t)
y = t * np.cos(30 * t)
z = t

c = x + y

X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))


x = np.random.random(150) * 10  # 建立150個0 - 10的隨機數
y = np.random.random(150) * 15  # 建立150個0 - 15的隨機數
z = np.random.random(150) * 20  # 建立150個0 - 20的隨機數

ax.legend()  # 顯示圖例

"""
colors = x + y  # 色彩是沿 x + y 累增
ax[0].scatter(x, y, z, c=colors)  # 繪製左子圖
ax[1].scatter(x, y, z, c=colors, cmap="hsv")  # 繪製右子圖
"""

# 產生 3D 座標資料
z = np.linspace(0, 15, 100)
x = np.sin(z)
y = np.cos(z)

# 繪製 3D 曲線
ax.plot(x, y, z, color="gray")

# 繪製 3D 座標點
ax.scatter(x2, y2, z, c=z, cmap="jet")

x_heights = np.random.randint(120, 190, 50)
y_weights = np.random.randint(30, 100, 50)
z_ages = np.random.randint(low=10, high=35, size=50)

# 性別標籤 1 是男生, 0 是女生
gender = np.random.choice([0, 1], 50)

data = np.random.rand(50, 3)  # 生成三維數據，每維50個

# 產生 3D 座標資料
x1 = np.random.randn(50)
y1 = np.random.randn(50)
z1 = np.random.randn(50)

x2 = np.random.randn(50)
y2 = np.random.randn(50)
z2 = np.random.randn(50)

# 繪製 3D 座標點
ax.scatter(x1, y1, z1, c=z1, cmap="Reds", marker="^", label="My Points 1")
ax.scatter(x2, y2, z2, c=z2, cmap="Blues", marker="o", label="My Points 2")


# ax.set_aspect("equal")

ax.view_init(elev=20.0, azim=-35)  # 設定 3D 視角(仰角, 方位角)
ax.view_init(elev=30.0, azim=45)  # 設定 3D 視角(仰角, 方位角)
ax.view_init(60, 45)  # 設定 3D 視角(仰角, 方位角)
ax.set_title(f"仰角={ax.elev},方位角={ax.azim}")

ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(0, 2)

ax.set_axis_off()


# 3D散點圖的繪制使用scatter() 函數來繪制出散點
xs1 = np.random.randint(30, 40, 100)
ys1 = np.random.randint(20, 30, 100)
zs1 = np.random.randint(10, 20, 100)
"""
xs2 = np.random.randint(50, 60, 100)
ys2 = np.random.randint(30, 40, 100)
zs2 = np.random.randint(50, 70, 100)

xs3 = np.random.randint(10, 30, 100)
ys3 = np.random.randint(40, 50, 100)
zs3 = np.random.randint(40, 50, 100)
"""
ax.scatter(xs1, ys1, zs1, c="r")
# ax.scatter(xs2, ys2, zs2, c = 'g', marker = '^')
# ax.scatter(xs3, ys3, zs3, c = 'b', marker = '*')

# 建立數據, 製作3D資料 X Y Z
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
c = np.random.rand(N, N)
Z = 10 * np.exp(-(0.5 * X**2 + 0.5 * Y**2))

"""
R = 5
x = np.arange(-R, R + 1, 0.5)
y = np.arange(-R, R + 1, 0.5)
X, Y = np.meshgrid(x, y)

# np.add 兩個陣列相加
#Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
Z = R * R - np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
"""


"""
def f2(x, y):
    n = np.sqrt(np.power(x, 2) + np.power(y, 2)) / 180 * np.pi
    return np.cos(n) + np.cos(3 * n)

width = 200
step = 10

x = np.arange(-width, width, step)
y = np.arange(-width, width, step)

X, Y = np.meshgrid(x, y) 
Z = f2(X, Y)
"""


ax.set_box_aspect((1, 1, 0.5))  # 調整各軸顯示比例


# 建立3D測試資料

N = 0.05
X, Y, Z = axes3d.get_test_data(N)  # (1/N*6) X (1/N*6)  # 取得測試資料

print(1 / N * 6)
print(X.shape)
print(Y.shape)
print(Z.shape)

# 畫三維球
u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
X = np.cos(u) * np.sin(v)
Y = np.sin(u) * np.sin(v)
Z = np.cos(v)

"""
def f1(x, y):
    return np.exp(-(0.5 * X**2 + 0.5 * Y**2))

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)  # 建立 X 和 Y 資料
Z = f1(X, Y)  # 建立 Z 資料
c = np.random.rand(N, N)  # 取隨機色彩值
"""

"""
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)  # 建立 X 和 Y 資料
Z = np.exp(-(0.5*X**2+0.5*Y**2))  # 建立 Z 資料
Z = np.exp(-(0.1*X**2+0.1*Y**2))  # 建立 Z 資料
Z = np.exp(-(X**2+Y**2))  # 建立 Z 資料
c = np.random.rand(N, N)  # 取隨機色彩值
"""

"""
# Create supporting points in polar coordinates
r = np.linspace(0, 1.2, 50)
p = np.linspace(0, 2 * np.pi, 50)
R, P = np.meshgrid(r, p)
# Transform them to cartesian system
X, Y = R * np.cos(P), R * np.sin(P)
Z = (R**2 - 1) ** 2
"""

"""
#用于計算X/Y對應的Z值
def f3(x,y):
    return (1 - y** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#plot_surface函數可繪制對應的曲面

X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
#計算3維曲面分格線坐標
X, Y = np.meshgrid(X, Y)
Z = f3(X, Y)
"""

ax.set_title("線框圖 plot_wireframe + scatter")
# plt.title('線框圖 plot_wireframe + scatter')  same

# ax.set_zlim3d(0, 1)

# 存圖
plt.savefig("mat-3D-mv1.png")
plt.savefig("matplot-3D-1.png")
plt.savefig("3-vectors.png")
plt.savefig("3-surfaces-spherical-intersec-curves.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes(projection="3d")

# 3D plot

show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# 3D plot

show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_wireframe(X, Y, Z)

ax.scatter(0, 0, 0, c="r", s=100)
ax.scatter(5, 5, 5, c="g", s=100)
