"""

參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/

3D plot 集合 1 大整理

1. plot_wireframe
2. plot_surface

3. contour
contour
contour3D
contourf
contourf3D

3. scatter


ax.plot

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

fig = plt.figure(
    num="3D繪圖 集合 1 wireframe",
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
    num="3D繪圖 集合 2 surface",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖


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
    num="3D繪圖 集合 2 contour",
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


fig = plt.figure(
    num="3D繪圖 集合 3 ax.plot",
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

ax.plot(x, y, z)
ax.set_title("線形圖")

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

π = np.pi
θ = np.linspace(-5 * π, 5 * π, 200)

x = np.cos(θ)
y = np.sin(θ)
z = θ / (5 * π)

ax.plot(x, y, z)
ax.set_title("3D 畫圖")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

start = 0
end = np.pi * 20   
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x) 

ax.plot(x, y, z)

plt.title('3D Plot')

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection="3d")  # 第五張圖

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir="z", label="curve in (x, y)")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x, y, z, color='m', lw=3)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

ax.plot(x, y, z)

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

ax.plot3D(x, y, z)

plt.show()


print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 2 散點圖 scatter 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

ax.scatter(x, y, z, c="r")

ax.set_title("XXXXXXX1")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection="3d")  # 第二張圖

count = 100
range = 100

xs = np.random.rand(count) * range
ys = np.random.rand(count) * range
zs = np.random.rand(count) * range

ax.scatter(xs, ys, zs, s=zs, c=zs)

ax.set_title("散點圖")

ax.set_title("XXXXXXX2")

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# 在三維空間中繪製座標點是最常用到的基本功能。

# 產生 3D 座標資料
z1 = np.random.randn(50)
x1 = np.random.randn(50)
y1 = np.random.randn(50)
z2 = np.random.randn(50)
x2 = np.random.randn(50)
y2 = np.random.randn(50)

# 繪製 3D 座標點
ax.scatter(x1, y1, z1, c=z1, cmap="Reds", marker="^", label="My Points 1")
ax.scatter(x2, y2, z2, c=z2, cmap="Blues", marker="o", label="My Points 2")

ax.legend()  # 顯示圖例

ax.set_title("3D 座標點")

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

x = np.linspace(0, 5, 10)
y = np.linspace(0, 5, 10)
X, Y = np.meshgrid(x, y)

Z = 2 * X + Y

ax.scatter(X, Y, Z + 0.7 * np.random.randn(10, 10))
ax.plot_surface(X, Y, Z, alpha=0.3)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection="3d")  # 第六張圖

x = np.random.randn(1000)
y = np.random.randn(1000)
z = np.random.randn(1000)
ax.scatter3D(x, y, z)
ax.set_title("繪製 3D 散佈圖 – scatter3D()")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 2 散點圖 scatter 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection='3d')

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


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

# draw a point
xs = np.array([0, 0, 0, 1])
ys = np.array([0, 0, 1, 1])
zs = np.array([0, 1, 1, 1])
ax.scatter(xs, ys, zs, color="y", s=100)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')


X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.scatter(X, Y, Z, color="y", s=3)
ax.set_title('scatter')


print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數

ax.scatter(x, y, z)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數
ax.scatter3D(x, y, z)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數

ax.scatter(x, y, z, marker='*', color='m')



plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 3 散點圖 scatter 3",
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

ax.scatter(x, y, z, c = c)


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y

ax.scatter(x, y, z, c=c, cmap='hsv')


print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')

# 第 A 組資料
x1 = np.random.randn(100)
y1 = np.random.randn(100)
z1 = np.random.randn(100)
# 第 B 組資料
x2 = np.random.randn(100)
y2 = np.random.randn(100)
z2 = np.random.randn(100)

# 繪製散點圖
ax.scatter(x1,y1,z1,c=z1,cmap='Oranges',marker='d',label='A 資料組')
ax.scatter(x2,y2,z2,c=z2,cmap='Blues',marker='*',label='B 資料組')

ax.legend()                                 # 建立圖例


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
sc = ax.scatter(x, y, z, c=c, cmap='hsv')   # 散點圖物件
fig.colorbar(sc)                            # 資料條


print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')

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



plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(
    num="3D繪圖 集合 4 散點圖 scatter 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.5*X**2+0.5*Y**2))    # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(232, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.1*X**2+0.1*Y**2))    # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')

fig.colorbar(sc)

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(233, projection='3d')

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(X**2+Y**2))            # 建立 Z 資料

c = np.random.rand(N, N)

sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')

fig.colorbar(sc)

print("------------------------------------------------------------")  # 60個
                 
ax = fig.add_subplot(234, projection='3d')



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(235, projection='3d')



print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(236, projection='3d')



plt.tight_layout()
plt.show()






print("------------------------------------------------------------")  # 60個

"""
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
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

ax = fig.add_subplot(231, projection="3d")  # 第一張圖

np.random.seed(59)
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

np.random.seed(59)
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
print("作業完成")
print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes(projection="3d")

# 3D plot

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 3D plot

plt.show()


print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個


ax.view_init(60,45)                         # 設定 3D 視角


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")



ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

ax.set_xlabel(r"$\phi_\mathrm{real}$")
ax.set_ylabel(r"$\phi_\mathrm{im}$")
ax.set_zlabel(r"$V(\phi)$")


plt.rcParams["font.family"] = ["Microsoft JhengHei"]

ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')

ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')

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

ax.set_xlabel("X")
ax.set_ylabel("Y")

ax.set_xlabel("X")
ax.set_ylabel("Y")


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



