"""
3D plot 集合 3

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

from mpl_toolkits.mplot3d import axes3d

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

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.set_title('contour')

ax.clabel(cset, fontsize=9, inline=1)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.plot_surface(X, Y, Z, cmap="bwr")
#ax.plot_surface(X, Y, Z, cmap="seismic")

ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return (np.power(x,2) + np.power(y, 2))

ax = fig.add_subplot(233, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據

ax.plot_surface(X, Y, f(X,Y), cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

                 
ax = fig.add_subplot(234, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據

ax.plot_surface(X, Y, f(X,Y), cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return np.sin(np.sqrt(x ** 2 + y ** 2))

ax = fig.add_subplot(235, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據

ax.plot_surface(X, Y, f(X,Y), cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return (4 - x**2 - y**2)

                 
ax = fig.add_subplot(236, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據

ax.plot_surface(X, Y, f(X,Y), cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

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

ax = fig.add_subplot(231, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.plot_wireframe(X, Y, Z, color='g')
ax.set_title('plot_wireframe 3D線框圖')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
#ax.plot_wireframe(X, Y, Z, cstride=10, rstride=10)

ax.set_title('plot_wireframe 3D線框圖')

print("------------------------------------------------------------")  # 60個

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

ax = fig.add_subplot(233, projection='3d')
# 定義資料資料
x = np.linspace(0, 5, 20)
y = np.linspace(0, 5, 20)  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.plot_wireframe(X, Y, Z, color = 'm')
ax.set_title('plot_wireframe 3D線框圖')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.contour(X, Y, Z, cmap='jet')
ax.set_title('contour')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.contour3D(X, Y, Z, cmap='jet')
ax.set_title('contour3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.contourf(X, Y, Z, cmap='jet')
ax.set_title('contourf')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.contourf3D(X, Y, Z, cmap='jet')
ax.set_title('contourf3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)  # 取得測試資料

ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, alpha=0.3)
ax.set_title('plot_wireframe 3D線框圖')

# 測試數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='jet')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

ax.set_title('contourf')

ax.set_title('plot_wireframe 3D線框圖 + contourf')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

# 建立數據
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
c = np.random.rand(N, N)
Z = 10 * np.exp(-(0.5*X**2+0.5*Y**2))

ax.plot_wireframe(X,Y,Z,rstride=5,cstride=5,color='g')
ax.set_title('plot_wireframe 3D線框圖')

# 數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X,Y,Z,zdir='z',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='x',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='y',offset=10,cmap='cool')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_title('contourf')

ax.set_title('plot_wireframe 3D線框圖 + contourf')

print("------------------------------------------------------------")  # 60個

def f(x, y):                                # 曲面函數
    return np.sin(np.sqrt(x ** 2 + y ** 2))

ax = fig.add_subplot(234, projection='3d')

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立取樣數據

ax.plot_surface(X, Y, f(X,Y), cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

ax.view_init(60,45)                         # 設定 3D 視角

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

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
ax.set_title('quiver')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

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

fig = plt.figure(
    num="3D繪圖 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection='3d')

R = 5
x = np.arange(-R, R + 1, 0.5)
y = np.arange(-R, R + 1, 0.5)

print(x)
print(y)
X, Y = np.meshgrid(x, y)
#Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
Z = R * R - np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

#畫線框圖
surf = ax.plot_wireframe(X, Y, Z)
fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

#畫散佈圖
ax.scatter(X, Y, Z, c = 'r')

ax.set_title('線框圖 plot_wireframe + scatter')
#plt.title('線框圖 plot_wireframe + scatter')  same

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(232, projection='3d')

start = 0
end = np.pi * 20   
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x) 

ax.plot(x, y, z)

plt.title('3D Plot')

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(233, projection='3d')

#3D曲面

#建立一個figure
#创建3D轴对象

X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
#计算3维曲面分格线坐标
X,Y = np.meshgrid(X, Y)

#用于计算X/Y对应的Z值
def f(x,y):
    return (1 - y** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#plot_surface函数可绘制对应的曲面

#ax.plot_surface(X, Y, f(X,Y), rstride = 1, cstride = 1)
#修改曲面顏色, 使用cmap属性可指定曲面颜色
ax.plot_surface(X, Y, f(X, Y), rstride = 1, cstride = 1, cmap = plt.cm.hot)

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(234, projection='3d')

#3D散点图的绘制使用scatter() 函数来绘制出散点

xs = np.random.randint(30, 40, 100)
ys = np.random.randint(20, 30, 100)
zs = np.random.randint(10, 20, 100)
xs2 = np.random.randint(50, 60, 100)
ys2 = np.random.randint(30, 40, 100)
zs2 = np.random.randint(50, 70, 100)
xs3 = np.random.randint(10, 30, 100)
ys3 = np.random.randint(40, 50, 100)
zs3 = np.random.randint(40, 50, 100)

ax.scatter(xs, ys, zs)
ax.scatter(xs2, ys2, zs2, c = 'r', marker = '^')
ax.scatter(xs3, ys3, zs3, c = 'g', marker = '*')

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(235, projection='3d')

from matplotlib import cm

def f(x, y):
    n = np.sqrt(np.power(x, 2) + np.power(y, 2)) / 180 * np.pi
    return np.cos(n) + np.cos(3 * n)

width = 200
step = 10

x = np.arange(-width, width, step)
y = np.arange(-width, width, step)

X, Y = np.meshgrid(x, y) 
Z = f(X, Y)

#ax.plot_surface(X, Y, Z)   不分層著色
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)    #分層著色
#ax.plot_wireframe(X, Y, Z)  #畫線框圖

ax.set_box_aspect((1, 1, 0.5))  #調整各軸顯示比例
plt.title('3D Plot Surface')

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(236, projection='3d')

"""
3D表面（彩色地图）
演示如何绘制使用CoolWarm颜色映射着色的3D曲面。使用“抗锯齿=假”使表面不透明。
还演示了使用线性定位器和Z轴刻度标签的自定义格式。
"""

from matplotlib import cm
from matplotlib.ticker import LinearLocator

#fig, ax = plt.subplots(subplot_kw = {"projection" : "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

plt.show()

print('------------------------------------------------------------')	#60個

fig = plt.figure(
    num="3D繪圖 集合 5",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection='3d')

# 產生 3D 座標資料
z1 = np.random.randn(50)
x1 = np.random.randn(50)
y1 = np.random.randn(50)
z2 = np.random.randn(50)
x2 = np.random.randn(50)
y2 = np.random.randn(50)

# 繪製 3D 座標點
ax.scatter(x1, y1, z1, c=z1, cmap='Reds', marker='^', label='My Points 1')
ax.scatter(x2, y2, z2, c=z2, cmap='Blues', marker='o', label='My Points 2')

ax.legend()

print('------------------------------------------------------------')	#60個

# 線框圖

from mpl_toolkits.mplot3d import axes3d

ax = fig.add_subplot(232, projection='3d')

# 生成一系列的測試數據
N = 0.05
X, Y, Z = axes3d.get_test_data(N)  # (1/N*6) X (1/N*6)
print(1 / N * 6)
print(X.shape)
print(Y.shape)
print(Z.shape)
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

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

from math import floor
from matplotlib import cm


def blending(t):
    return 6 * (t**5) - 15 * (t**4) + 10 * (t**3)


def lerp(g1, g2, t):
    return g1 + t * (g2 - g1)


def grad2(hashvalue, dx, dy):
    return [dy, dx + dy, dx, dx - dy, -dy, -dx - dy, -dx, -dx + dy][hashvalue % 8]


rand_table = np.random.randint(255, size=256).tolist()


def _perlin2(x, y):
    xi = floor(x)
    yi = floor(y)

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

ax = fig.add_subplot(234, projection='3d')

# 三維散點圖

data = np.random.rand(50, 3) # 生成三維數據，每維50個

ax.scatter(data[:, 0], data[:, 1], data[:, 2])

print("------------------------------------------------------------")  # 60個

# 三維柱圖

ax = fig.add_subplot(235, projection='3d')

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y) # 生成網格點座標矩陣
x, y = _xx.ravel(), _yy.ravel() # 展開爲一維數組

top = x + y
bottom = np.zeros_like(top) # 與top數組形狀一樣，內容全部爲0
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

# 三維曲面圖和等高線圖

from matplotlib import cm

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
ax.contourf(X,Y,Z,zdir='z',offset=-2) # 把等高線向z軸投射
ax.set_zlim(-2,2) # 設置z軸範圍
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes(projection="3d")

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir="z", label="curve in (x, y)")

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ("r", "g", "b", "k")

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))

c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir="y", c=c_list, label="points in (x, z)")

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20.0, azim=-35)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
