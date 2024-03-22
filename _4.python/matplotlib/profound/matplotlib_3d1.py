"""
參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/



"""

# 3D plot 集合 1

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

#          編號                          圖像大小[英吋]     解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(
    num="3D繪圖 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示


# 3D surface plot
ax = fig.add_subplot(231, projection="3d")  # 第一張圖

# 111
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_wireframe(X, Y, Z)
ax.set_title("線框圖111")


# 曲面圖
ax = fig.add_subplot(232, projection="3d")  # 第二張圖

# 444
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_surface(X, Y, Z, cmap=cm.hsv)
# surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
# fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("曲面圖")


# XXXXXXX3
ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# 333
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

ax.plot_wireframe(X, Y, Z, alpha=0.1)
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("等高線333")


# XXXXXXX4
ax = fig.add_subplot(234, projection="3d")  # 第四張圖

X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)

# R = np.sqrt(X**2 + Y**2)
# R = np.sqrt(X**2 + Y**2)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
# Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)


# XXXXXXX5
ax = fig.add_subplot(235, projection="3d")  # 第五張圖


x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
# Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_title("XXXXXXX5")

# XXXXXXX6
ax = fig.add_subplot(236, projection="3d")  # 第六張圖

# ax = fig.gca(projection='3d') old
# ax = fig.add_axes(Axes3D(fig))

x = np.arange(-10, 11, 1)  # -10 .... 10
y = np.arange(-10, 11, 1)  # -10 .... 10
X, Y = np.meshgrid(x, y)

Z = np.add(np.power(X, 2), np.power(Y, 2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)


# ax.set_title('XXXXXXX6')


plt.show()


print("------------------------------------------------------------")  # 60個


#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(
    num="3D繪圖 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# XXXXXXX1
ax = fig.add_subplot(231, projection="3d")  # 第一張圖


# 曲面 contour

x = y = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

# ax = fig.gca(projection='3d') old
# ax = fig.add_axes(Axes3D(fig))
ax.plot_surface(X, Y, Z)

ax.set_title("曲面 surface")

# XXXXXXX2
ax = fig.add_subplot(232, projection="3d")  # 第二張圖

# 曲面 contour
plt.contour(X, Y, Z)
ax.set_title("曲面 contour")

# XXXXXXX3
ax = fig.add_subplot(233, projection="3d")  # 第三張圖

# 曲面 contourf
plt.contourf(X, Y, Z)
ax.set_title("曲面 contourf")

# XXXXXXX4
ax = fig.add_subplot(234, projection="3d")  # 第四張圖

t = np.linspace(-2 * np.pi, 2 * np.pi)
x, y = np.meshgrid(t, t)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot_surface(x, y, z)  # 畫出三軸資料所構成的曲面
plt.tight_layout()

ax.set_title("XXXXXXX4")


# XXXXXXX5
ax = fig.add_subplot(235, projection="3d")  # 第五張圖

# 繪製曲面 – plot_surface()
t = np.linspace(-5, 5, num=50)
x, y = np.meshgrid(t, t)
z = x * y

ax.plot_surface(x, y, z)

ax.set_title("繪製曲面")

# XXXXXXX6
ax = fig.add_subplot(236, projection="3d")  # 第六張圖

# 給曲面套上顏色
t = np.linspace(-5, 5)
x, y = np.meshgrid(t, t)
z = x * y

ax.plot_surface(x, y, z, cmap="viridis")
ax.set_title("給曲面套上顏色")

plt.show()


print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]     解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(
    num="3D繪圖 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# 線形圖
ax = fig.add_subplot(231, projection="3d")  # 第一張圖
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
z = np.add(x, y)

ax.plot(x, y, z)
ax.set_title("線形圖")


ax = fig.add_subplot(232, projection="3d")  # 第二張圖

# 圓環與直線
p = np.mgrid[0 : 2.0 * np.pi : 20j]
x = 3.0 * np.cos(p) * np.sin(np.pi / 6.0)
y = 3.0 * np.sin(p) * np.sin(np.pi / 6.0)
z = 3.0 * np.cos(np.pi / 6.0)
ax.plot(x, y, z, color="r")
ax.plot(p / 3.0, p / 3.0, p / 3.0, color="b")
# plt.savefig("matplot-3D-1.png")


ax = fig.add_subplot(233, projection="3d")  # 第三張圖


π = np.pi
θ = np.linspace(-5 * π, 5 * π, 200)

x = np.cos(θ)
y = np.sin(θ)
z = θ / (5 * π)

# ax = fig.gca(projection='3d') old
# ax = fig.add_axes(Axes3D(fig))
plt.plot(x, y, z)
ax.set_title("3D 畫圖")


ax = fig.add_subplot(234, projection="3d")  # 第四張圖


ax.set_title("XXXXXXX2")

# 等高線
ax = fig.add_subplot(235, projection="3d")  # 第五張圖


# 柱狀圖
ax = fig.add_subplot(236, projection="3d")  # 第六張圖


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]     解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(
    num="3D繪圖 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示


# 多邊形
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

ax = fig.add_subplot(233, projection="3d")  # 第三張圖


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
ax.set_xlabel(r"$\phi_\mathrm{real}$")
ax.set_ylabel(r"$\phi_\mathrm{im}$")
ax.set_zlabel(r"$V(\phi)$")
ax.set_title("3D surface plot")

ax = fig.add_subplot(234, projection="3d")  # 第四張圖

# Wireframe 圖形
# 這是 3D 的 wireframe 網格圖形範例。

# 產生測試資料
X, Y, Z = axes3d.get_test_data(0.05)

# 繪製 Wireframe 圖形
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.set_title("Wireframe 圖形")

# 3D 曲面
# 這是繪製 3D 曲面的範例。
ax = fig.add_subplot(235, projection="3d")  # 第五張圖

# 產生測試資料
X, Y, Z = axes3d.get_test_data(0.05)  # 這一個不知道是什麼函數

# 繪製 3D 曲面圖形
ax.plot_surface(X, Y, Z, cmap="seismic")

ax.set_title("3D 曲面")


# 3D 向量場
# 這是繪製 3D 向量場（vector field）的範例。
ax = fig.add_subplot(236, projection="3d")  # 第六張圖

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

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
#製作動圖
for angle in np.arange(95, 180, 12):
    ax.set_zlabel("Angle: " + str(angle))
    ax.view_init(30, angle)
    filename = "./" + str(angle) + ".png"
    plt.savefig(filename)
    print("Save " + filename + " finish")
"""
