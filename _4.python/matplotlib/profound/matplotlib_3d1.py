"""

參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/

3D plot 集合 1 大整理

1.plot()
2.scatter()
3.plot_wireframe()
4.plot_surface()
5.contour() (contour, contour3D, contourf, contourf3D)

其他

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

# 此 figure 共用資料

# 1. Z = X^2 + Y^2
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)

# np.add 兩個一維陣列組成一個二維陣列
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

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

fig = plt.figure(
    num="3D繪圖 集合 1.plot",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
# np.add 兩個一維陣列組成一個二維陣列
z = np.add(x, y)

ax.plot(x, y, z, color="r")
ax.plot(x, y, z, color='m', lw=3)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

# 圓環與直線
p = np.mgrid[0 : 2.0 * np.pi : 20j]

x = 3.0 * np.cos(p) * np.sin(np.pi / 6.0)
y = 3.0 * np.sin(p) * np.sin(np.pi / 6.0)
z = 3.0 * np.cos(np.pi / 6.0)

ax.plot(x, y, z, color="r")
ax.plot(p / 3.0, p / 3.0, p / 3.0, color="g")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir="z", label="curve in (x, y)")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

ax.plot(x, y, z)
ax.set_title("plot")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

ax.plot3D(x, y, z)
ax.set_title("plot3D")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

# intersection curves
t = np.pi / 4.0
f = np.pi / 4.0
r = np.linspace(0, 1.2, 40)
x = r * np.sin(t) * np.cos(f)
y = r * np.sin(t) * np.sin(f)
z = r * np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

r = 1.0
t = np.pi / 4.0
f = np.linspace(0, 2.0 * np.pi, 40)
x = r * np.sin(t) * np.cos(f)
y = r * np.sin(t) * np.sin(f)
z = r * np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

r = 1.0
f = np.pi / 4.0
t = np.linspace(0, np.pi / 2, 40)
x = r * np.sin(t) * np.cos(f)
y = r * np.sin(t) * np.sin(f)
z = r * np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 2.scatter 散點圖1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

ax.scatter(X, Y, Z, c="r")
#ax.scatter(X, Y, Z, c=Z, cmap="Reds", marker="^", label="My Points 1")
#ax.scatter(X, Y, Z, c=Z, cmap="Blues", marker="o", label="My Points 2")
#ax.scatter(x1,y1,z1,c=z1,cmap='Oranges',marker='d',label='A 資料組')
#ax.scatter(x2,y2,z2,c=z2,cmap='Blues',marker='*',label='B 資料組')
#ax.scatter(X, Y, Z + 0.7 * np.random.randn(10, 10))
#ax.scatter(X, Y, Z, color="y", s=3)
ax.scatter(X, Y, Z)
ax.scatter3D(X, Y, Z)
ax.scatter(X, Y, Z, marker='*', color='m')

c = X + Y
ax.scatter(X, Y, Z, c=c)
ax.scatter(X, Y, Z, c=c, cmap='hsv')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

count = 100
range = 100

xs = np.random.rand(count) * range
ys = np.random.rand(count) * range
zs = np.random.rand(count) * range

ax.scatter(xs, ys, zs, s=zs, c=zs)

ax.set_title("散點圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

x = np.random.randn(1000)
y = np.random.randn(1000)
z = np.random.randn(1000)
ax.scatter3D(x, y, z)
ax.set_title("繪製 3D 散佈圖 – scatter3D()")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

# 這是將 3D 的曲線與座標點畫在同一張圖的範例。

# 產生 3D 座標資料
z = np.linspace(0, 15, 100)
x = np.sin(z)
y = np.cos(z)

# 繪製 3D 曲線
ax.plot(x, y, z, color="gray", label="My Curve")

# 產生 3D 座標資料
x2 = np.sin(z) + 0.1 * np.random.randn(100)
y2 = np.cos(z) + 0.1 * np.random.randn(100)

# 繪製 3D 座標點
ax.scatter(x2, y2, z, c=z, cmap="jet", label="My Points")

ax.legend()  # 顯示圖例

ax.set_title("plot 3D 曲線")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

# 畫點 (1,1,1)-(2,2,2)-(3,3,3)-(4,4,4)
xs = np.array([1, 2, 3, 4])
ys = np.array([1, 2, 3, 4])
zs = np.array([1, 2, 3, 4])
ax.scatter(xs, ys, zs, color="y", s=100)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

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

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 2.scatter 散點圖2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection='3d')


x_heights = np.random.randint(120,190,50)
y_weights = np.random.randint(30,100,50)
z_ages = np.random.randint(low=10,high=35,size=50)

# 性別標籤 1 是男生, 0 是女生
gender = np.random.choice([0, 1],50)   

# 繪製散點圖
ax.scatter(x_heights,y_weights,z_ages,c=gender)

ax.set_xlabel('身高 (單位 : 公分)',color='m')
ax.set_ylabel('體重 (單位 : 公斤)',color='m')
ax.set_zlabel('年齡 (單位 : 歲',color='m')

ax.set_title('不同年齡體重與身高分佈圖',fontsize=16,color='b')


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
sc = ax.scatter(x, y, z, c=c, cmap='hsv')   # 散點圖物件
fig.colorbar(sc)                            # 資料條

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

N = 150
# 建立折線用的 3D 座標資料
z = np.linspace(0, 20, N)
x1 = np.cos(z)
y1 = np.sin(z)
# 繪製 3D 折線
ax.plot(x1, y1, z, color='m', label='plot')

# 建立散點用的 3D 座標資料, z 則沿用
x2 = np.cos(z) + np.random.randn(N) * 0.1
y2 = np.sin(z) + np.random.randn(N) * 0.1
# 繪製 3D 散點
ax.scatter(x2,y2,z,c=z,cmap='hsv',label='scatter')

ax.legend()

print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.5*X**2+0.5*Y**2))    # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.1*X**2+0.1*Y**2))    # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')

fig.colorbar(sc)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(X**2+Y**2))            # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')

fig.colorbar(sc)

plt.tight_layout()
plt.show()







print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 3.plot_wireframe",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

ax.plot_wireframe(X, Y, Z)
#ax.plot_wireframe(X, Y, Z, color = 'm')
#ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
#ax.plot_wireframe(X, Y, Z, cstride=10, rstride=10)

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


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖


plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 4.plot_surface",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

# 線框圖
step = 0.04
maxval = 1.0

# Create supporting points in polar coordinates
r = np.linspace(0, 1.2, 50)
p = np.linspace(0, 2 * np.pi, 50)
R, P = np.meshgrid(r, p)
# Transform them to cartesian system
X, Y = R * np.cos(P), R * np.sin(P)

Z = (R**2 - 1) ** 2
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=colormap)
ax.set_zlim3d(0, 1)

ax.set_title("3D surface plot")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

ax.plot_surface(X, Y, Z, alpha=0.3)

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

# 畫出三軸資料所構成的曲面
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_title('plot_surface 3D曲線表面')

ax.plot_surface(X, Y, Z, cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

ax.plot_surface(X, Y, Z, cmap='hsv')
ax.set_title('plot_surface 3D曲線表面')

ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("給曲面套上顏色")

ax.plot_surface(X, Y, Z, cmap="bwr")
#ax.plot_surface(X, Y, Z, cmap="seismic")
ax.set_title('plot_surface 3D曲線表面')


plt.tight_layout()
plt.show()




print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 5.contour",
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

ax.contour(X, Y, Z)
ax.contour(X, Y, Z, cmap='jet')

"""
#多了ax.clabel 16, extend3d=True
cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.clabel(cset, fontsize=9, inline=1)
"""
ax.set_title('contour')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

ax.contour3D(X, Y, Z, cmap='jet')
ax.set_title('contour3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

ax.contourf(X, Y, Z)
ax.contourf(X, Y, Z, cmap='jet')
ax.set_title('contourf')

print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

ax.contourf3D(X, Y, Z, cmap='jet')
ax.set_title('contourf3D')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')




plt.tight_layout()
plt.show()


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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 4 new",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

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

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

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

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# 這是繪製 3D 向量場（vector field）的範例。
# 產生格點資料
x, y, z = np.meshgrid(
    np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.2), np.arange(-0.8, 1, 0.8)
)

# 產生向量場資料
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z)

# 繪製向量場
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

ax.set_title("3D 向量場")


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖



plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


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

ax = fig.add_subplot(231, projection="3d")  # 第一張圖


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

# 三維球

# ax.set_aspect("equal")

# draw sphere
u, v = np.mgrid[0 : 2 * np.pi : 20j, 0 : np.pi : 10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

# draw a vector
ax.quiver(0, 0, 1, 1, 1, 0, color="k")
ax.quiver(0, 0, 0, 1, 1, 1, color="b", arrow_length_ratio=0.1)

ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
ax.set_zlabel("z", fontsize=15)

# plt.savefig('3D-sphere.png')

ax.set_title("三維球aaa")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# 3D quiver  3維向量

# ax.set_aspect("equal")

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
# plt.savefig("3-vectors.png")

ax.set_title("#3D quiver  3維向量")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

# 正交曲線座標系統
# 球座標當中的三個曲面交出三條曲線，這三個曲線形成了廣義的正交曲線座標系統(generalized orthonormal curved coordinates)

# ax.set_aspect("equal")

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

ax.set_title(
    r"3 surfaces $r=1, \theta=\pi/4, \phi=\pi/4$" " meet in 3 curves", fontsize=15
)
ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
ax.set_zlabel("z", fontsize=15)
# plt.savefig("3-surfaces-spherical-intersec-curves.png")


ax.set_title("正交曲線座標系統")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

# 三維等位面與法線

x = np.linspace(2.0, 5.0, 10)
y = np.linspace(2.0, 5.0, 10)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
Z2 = np.sqrt(X**2 + Y**2 - 2.0)
Z3 = np.sqrt(X**2 + Y**2 - 3.0)
ax.scatter([3], [4], [5], color="k", s=40)

# ax.set_aspect("equal")

ax.plot_surface(X, Y, Z, label="C=0")
ax.plot_surface(X, Y, Z2, label="C=6")
ax.plot_surface(X, Y, Z3, label="C=12")
ax.quiver(3.0, 4.0, 5.0, 6.0 / 5.0, 8.0 / 5.0, -10.0 / 5.0, color="b")
ax.set_title("$f(x,y,z)=x^2+y^2-z=C$", fontsize=15)
# ax.plot_surface(X, Y, Z)

ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
ax.set_zlabel("z", fontsize=15)
# ax.legend()

ax.set_title("三維等位面與法線dddd")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

# 1. 首先在進行 3D Plot 時除了導入 matplotlib ，還要額外添加一個模塊，即 Axes 3D 3D 坐標軸顯示：

# import matplotlib
# matplotlib.use("Agg")

# 2. 接下來給進 X 和 Y 值，並將 X 和 Y 編織成柵格。每一個（X, Y）點對應的高度值我們用下面這個函數來計算。使用ax.plot_surface繪出網格表面圖形，並將一個 colormap rainbow 填充顏色。

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # x-y 平面的网格
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap("rainbow"))

# 3.將三維圖像投影到 XY 平面上做一個等高線圖。

ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))

# 其中，rstride 和 cstride 分別代表 row 和 column 的跨度。 可比較兩個圖分別是跨度為1 和 5 的效果。

# 3D基本操作
# import matplotlib
# matplotlib.use("Agg")

# fig = plt.figure()

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)  # x-y 平面的网格
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap("rainbow"))
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))
# plt.savefig("mat-3D-mv1.png")

ax.set_title("XXXXXXX6")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import axes3d

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

ax = fig.add_subplot(234, projection='3d')


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


plt.tight_layout()
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

print('------------------------------------------------------------')	#60個

ax = fig.add_subplot(233, projection='3d')

#3D曲面

#建立一個figure
#创建3D轴对象

#用于计算X/Y对应的Z值
def f(x,y):
    return (1 - y** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#plot_surface函数可绘制对应的曲面

X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
#计算3维曲面分格线坐标
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1)
#修改曲面顏色, 使用cmap属性可指定曲面颜色
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.cm.hot)

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

plt.tight_layout()
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

ax = fig.add_subplot(235, projection='3d')


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

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import axes3d

# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={"projection": "3d"})
# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")
ax[0].set_title("繪製曲線表面圖", fontsize=16, color="b")

# 繪製曲線框面圖
# ax = fig.add_subplot(111, projection='3d')
ax[1].plot_wireframe(X, Y, Z, color="g")
ax[1].set_title("繪製曲線框線圖", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0, 1, 300)  # z 軸值
x = z * np.sin(30 * z)  # x 軸值
y = z * np.cos(30 * z)  # y 軸值
colors = x + y  # 色彩是沿 x + y 累增

# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw={"projection": "3d"})
ax[0].scatter(x, y, z, c=colors)  # 繪製左子圖
ax[1].scatter(x, y, z, c=colors, cmap="hsv")  # 繪製右子圖
ax[1].set_axis_off()  # 關閉軸

plt.show()

print("------------------------------------------------------------")  # 60個


def f1(x, y):  # 左邊曲面函數
    return np.exp(-(0.5 * X**2 + 0.5 * Y**2))


def f2(x, y):  # 右邊曲面函數
    return np.exp(-(0.1 * X**2 + 0.1 * Y**2))


N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)  # 建立 X 和 Y 資料
np.random.seed(10)
c = np.random.rand(N, N)  # 取隨機色彩值
# 建立子圖
fig, ax = plt.subplots(1, 3, figsize=(8, 4), subplot_kw={"projection": "3d"})
# 左邊子圖乎叫 f1
sc = ax[0].scatter(X, Y, f1(X, Y), c=c, marker="o", cmap="hsv")
# 中間子圖乎叫 f2
sc = ax[1].scatter(X, Y, f2(X, Y), c=c, marker="o", cmap="hsv")
ax[1].set_axis_off()
# 右邊子圖乎叫 f2, 但是用不同的仰角和方位角
sc = ax[2].scatter(X, Y, f2(X, Y), c=c, marker="o", cmap="hsv")
ax[2].set_axis_off()
ax[2].view_init(60, -30)
ax[2].set_title(f"仰角={ax[2].elev},方位角={ax[2].azim}", color="b")

plt.show()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


ax.view_init(60,45)                         # 設定 3D 視角

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_xlabel(r"$\phi_\mathrm{real}$")
ax.set_ylabel(r"$\phi_\mathrm{im}$")
ax.set_zlabel(r"$V(\phi)$")


ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')

ax.set_title('3D圖表',fontsize=16,color='b')


"""
#製作動圖
for angle in np.arange(95, 180, 12):
    ax.set_zlabel("Angle: " + str(angle))
    ax.view_init(30, angle)
    filename = "./" + str(angle) + ".png"
    plt.savefig(filename)
    print("Save " + filename + " finish")
"""

X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)

# np.add 兩個一維陣列組成一個二維陣列
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

# Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2

# R = np.sqrt(X**2 + Y**2)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# plt.savefig("matplot-3D-1.png")

print("------------------------------------------------------------")  # 60個

np.random.seed(59)
np.random.seed(59)

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

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y


X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))


x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數

ax.legend()  # 顯示圖例
