"""
等高線圖 Contour Chart 集合
輪廓圖

等高線圖(Contour Chart)
contour()  等高線圖
contourf() 等高線面積圖

pyplot.contour() 參數
參數 	說明
x 	必填，等高線圖的中心點 x 座標，使用串列格式。
y 	必填，等高線圖的中心點 y 座標，使用串列格式。
z 	必填，等高線圖的高度，使用串列格式。
levels 	等高線的數量。
colors 	等高線顏色，使用串列格式，若不足 levels 的數量，則會自動重複，不能和 map 同時使用。
cmap 	等高線顏色，使用 colormaps，不能和 colors 同時使用。
vmin, vmax 	等高線顏色的最小值與最大值。
linewidths 	等高線的粗細。
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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="Contour 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)

xx = yy = np.arange(-1.02, 1.02, 0.02)
X, Y = np.meshgrid(xx, yy)

Z = X * X + Y * Y

plt.contourf(X, Y, Z, alpha=0.3, cmap="Paired")  # contourf 等高線面積圖

plt.title("contourf")

print("------------------------------")  # 30個
plt.subplot(232)

# 下方的程式碼，執行後會先使用 x 和 y 畫出一個二維的直角座標系統，
# 接著 z 使用二維陣列，標記每個位置的高度，最後就會根據數據資料畫出等高線圖。

x = np.linspace(-3, 3, 7)  # 產生從 -3～3 共 7個 的數值的 x
y = np.linspace(-3, 3, 7)
# z 5 X 5
z = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 9, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

print(x.shape)
print(y.shape)

plt.contour(x, y, z, levels=10)  # 10階
# plt.contour(x, y, z)    #預設維6階


print("------------------------------")  # 30個
plt.subplot(233)


print("------------------------------")  # 30個
# 圖4~圖6 用

# 繪製更精緻的等高線圖
# 參考 matplotlib 官方網站的運算式，搭配 numpy 的 linspace 方法，就能做出更細緻的等高線圖。

N = 200
x = np.linspace(-3, 3, N)  # 產生從 -3～3 共 N個 的數值的 x
y = np.linspace(-3, 3, N)  # 產生從 -3～3 共 N個 的數值的 y

# 根據 x 和 y 計算出 z
z = [
    [
        # (1 - x[i] / 2 + x[i] * 3 + y[j] * 5) * math.exp(-x[i] ** 2 - y[j] ** 2)
        (np.sinc(np.sqrt((x[i] - 1) ** 2 + (y[j] - 1) ** 2)))
        for i in range(N)
    ]
    for j in range(N)
]

# 指定每階的數值
lv = np.linspace(np.min(z), np.max(z), 20)  # 根據 z 的最大值和最小值，定義 level 區間

print("max =", np.max(z))
print("min =", np.min(z))
print("level =", lv)  # 20階

print("------------------------------")  # 30個

plt.subplot(234)

plt.contour(x, y, z)  # 預設階數
plt.title("預設階數")

print("------------------------------")  # 30個
plt.subplot(235)

plt.contour(x, y, z, levels=lv)  # 20階
plt.title("指定每階的數值, 20階")

print("------------------------------")  # 30個
plt.subplot(236)

# 使用 contourf() 繪製等高線面積圖
# 如果將 contour() 換成 contourf()，繪製的圖形就會變成「等高線面積圖」，
# 下方的程式碼執行後，會畫出等高線面積圖和等高線結合的圖表。
lv = np.linspace(np.min(z), np.max(z), 10)
plt.contourf(x, y, z, levels=lv, cmap="Reds")  # 等高線面積圖
plt.contour(x, y, z, levels=lv, colors=["#000", "#000"])  # 等高線圖
plt.title("contourf")

show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="Contour 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)


print("------------------------------")  # 30個
plt.subplot(232)


print("------------------------------")  # 30個
plt.subplot(233)


print("------------------------------")  # 30個
plt.subplot(234)


print("------------------------------")  # 30個
plt.subplot(235)


print("------------------------------")  # 30個
plt.subplot(236)


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="Contour 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)


print("------------------------------")  # 30個
plt.subplot(232)


print("------------------------------")  # 30個
plt.subplot(233)


print("------------------------------")  # 30個
plt.subplot(234)


print("------------------------------")  # 30個
plt.subplot(235)


print("------------------------------")  # 30個
plt.subplot(236)


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = np.arange(1, 10)
y = x.reshape(-1, 1)
h = x * y

cs = plt.contourf(
    h, levels=[10, 30, 50], colors=["#808080", "#A0A0A0", "#C0C0C0"], extend="both"
)
cs.cmap.set_over("red")
cs.cmap.set_under("blue")
cs.changed()

show()

print("------------------------------------------------------------")  # 60個

Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)

show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # tilt the coordinates.
Y = Y + 0.3 * X

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)

show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
xx, yy = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((xx - 3) ** 2 + (yy - 3) ** 2))
plt.contourf(xx, yy, zz, alpha=0.3)
xmin, xmax, ymin, ymax = 0, 6, 0, 6
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
plt.title("二維 sinc 函數")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

N = 5
x = np.arange(-N, (N + 1), 1)
xx, yy = np.meshgrid(x, x)
zz = xx * xx + yy * yy
# print(x)
# print(xx)
# print(yy)
# print(zz)

plt.contourf(xx, yy, zz, alpha=0.3)

plt.title("函數 z = x^2 + y^2")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
X, Y = np.meshgrid(x, y)

Z = np.random.randint(0, 3, (4, 4))
plt.contour(X, Y, Z)

show()

plt.contourf(X, Y, Z)

show()

print("------------------------------------------------------------")  # 60個

for i in range(4):
    plt.subplot(2, 2, i + 1)
    Z = np.random.randint(0, 3, (4, 4))
    plt.contour(X, Y, Z, cmap="Paired")
    plt.scatter(X.ravel(), Y.ravel(), c=Z.ravel(), s=20, cmap="Paired")

show()

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

X, Y = np.meshgrid(x, y)

Z = np.random.randint(1, 3, (4, 4))

Z = np.random.randint(1, 3, X.shape)  # same

plt.contour(X, Y, Z)

show()

print("------------------------------------------------------------")  # 60個

x = X.ravel()

x.reshape(4, 4)
y = Y.ravel()

z = Z.ravel()
plt.contour(X, Y, Z)
plt.scatter(x, y, c=z)

show()

print("------------------------------------------------------------")  # 60個

plt.contourf(X, Y, Z)

show()

print("------------------------------------------------------------")  # 60個

x = range(5)
y = range(5)
X, Y = np.meshgrid(x, y)
Z = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 2, 2, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
fig = plt.figure(figsize=(10, 4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title("使用contour函數", fontsize=16, color="b")

fig.add_subplot(122)
plt.contourf(X, Y, Z)
plt.title("使用contourf函數", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個

x = range(5)
y = range(5)
X, Y = np.meshgrid(x, y)
Z = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 2, 2, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
fig = plt.figure(figsize=(10, 4.5))
fig.add_subplot(121)
plt.contourf(X, Y, Z, cmap="PuRd")
plt.title("contourf函數, cmap=PuRd", fontsize=16, color="b")

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap="YlOrBr")
plt.title("contourf函數, cmap=YlOrBr", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return np.sin(x) ** 5 + np.cos(5 + y) * np.cos(x)


x = np.linspace(0, 5, 30)
y = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure(figsize=(10, 4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title("contour函數", fontsize=16, color="b")

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap="Oranges")
plt.title("contourf函數, cmap=Oranges", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return (x**2) / 10 + (y**2) / 4


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure(figsize=(10, 4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title("contour() 橢圓輪廓平面", fontsize=16, color="b")

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap="GnBu")
plt.title("contourf() 填充橢圓輪廓圓平面", fontsize=16, color="b")
plt.colorbar()  # 色彩條

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return -(x**2 + y**2)


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z)  # 填充輪廓圖
plt.colorbar()  # 色彩條
oval = plt.contour(X, Y, Z)  # 輪廓圖
plt.clabel(oval, colors="b")  # 增加高度標記
plt.title("有高度標記的輪廓圖", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return (1.2 - x**2 + y**5) * np.exp(-(x**2) - y**2)


x = np.linspace(-2.5, 2.5, 100)
y = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z, cmap="Greens")  # 填充輪廓圖
plt.colorbar()  # 色彩條
oval = plt.contour(X, Y, Z, colors="b")  # 輪廓圖
plt.clabel(oval, colors="b")  # 增加高度標記
plt.title("指數函數的輪廓圖", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return (1.2 - x**2 + y**5) * np.exp(-(x**2) - y**2)


x = np.linspace(-2.5, 2.5, 100)
y = np.linspace(-2.5, 2.5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z, 12, cmap="Greens")  # 填充輪廓圖
plt.colorbar()  # 色彩條
oval = plt.contour(X, Y, Z, 12, colors="b")  # 輪廓圖
plt.clabel(oval, colors="b")  # 增加高度標記
plt.title("指數函數的輪廓圖,levels=12", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return (1.2 - x**2 + y**5) * np.exp(-(x**2) - y**2)


x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 建立 2 個子圖
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
# 繪製左圖 level 是預設
con = ax[0].contourf(X, Y, Z, cmap="Greens")  # 填充輪廓圖
plt.colorbar(con, ax=ax[0])
oval = ax[0].contour(X, Y, Z, colors="b")  # 輪廓圖
ax[0].clabel(oval, colors="b")  # 增加高度標記
ax[0].set_title("指數函數等高圖level是預設", fontsize=16, color="b")
# 繪製右圖 level=12
ax[1].contourf(X, Y, Z, 12, cmap="Greens")  # 填充輪廓圖
oval = ax[1].contour(X, Y, Z, 12, colors="b")  # 輪廓圖
ax[1].clabel(oval, colors="b")  # 增加高度標記
ax[1].set_title("指數函數等高圖level=12", fontsize=16, color="b")

show()

print("------------------------------------------------------------")  # 60個


def f(x, y):
    return np.sqrt(x**2 + y**2)


N = 256
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, N)
X, Y = np.meshgrid(x, y)

# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors="black", linewidth=0.5)

# adding label
plt.clabel(C, inline=True, fontsize=10)

show()

print("------------------------------------------------------------")  # 60個

# 用contour(左)和contourf(右)描繪相等線圖
y, x = np.ogrid[-2:2:200j, -3:3:300j]
z = x * np.exp(-(x**2) - y**2)

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.subplot(121)
cs = plt.contour(z, 10, extent=extent)
plt.clabel(cs)
plt.subplot(122)
plt.contourf(x.reshape(-1), y.reshape(-1), z, 20)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 若果需要對雜湊點資料繪制相等線圖，
# 可以先使用scipy.interpolate模組中提供的插值函數將雜湊點資料插值為網格資料。

# 使用相等線繪制隱函數曲線（左），取得相等線資料並繪圖（右）
y, x = np.ogrid[-1.5:1.5:200j, -1.5:1.5:200j]
f = (x**2 + y**2) ** 4 - (x**2 - y**2) ** 2

plt.subplot(121)
extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
cs = plt.contour(
    f,
    extent=extent,
    levels=[0, 0.1],
    colors=["b", "r"],
    linestyles=["solid", "dashed"],
    linewidths=[2, 2],
)

plt.subplot(122)
""" NG
for c in cs.collections:
    data = c.get_paths()[0].vertices
    plt.plot(data[:,0], data[:,1], 
        color=c.get_color()[0],  linewidth=c.get_linewidth()[0])
"""
show()

print(cs)
# cs.collections

# NG print(cs.collections[0].get_color()[0])
print(cs.collections[0].get_linewidth()[0])

cc = len(cs.collections[0].get_paths())
print(cc)

path = cs.collections[0].get_paths()[0]
# cc = os.path.vertices
# print(cc)

print("------------------------------------------------------------")  # 60個

# 三角網格

with open("data/diffusion.txt", encoding="UTF-8-sig") as f:
    data = {"points": [], "triangles": [], "values": []}
    values = None
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            values = data[line[1:]]
            continue
        values.append([float(s) for s in line.split()])

data = {key: np.array(data[key]) for key in data}

# 使用tripcolor()和tricontour()繪制三角網格和相等線
X, Y = data["points"].T
triangles = data["triangles"].astype(int)
values = data["values"].squeeze()

fig, ax = plt.subplots(figsize=(12, 4.5))
ax.set_aspect("equal")

mapper = ax.tripcolor(X, Y, triangles, values, cmap="gray")
plt.colorbar(mapper, label="溫度")

plt.triplot(X, Y, triangles, lw=0.5, alpha=0.3, color="k")

Xc = X[triangles].mean(axis=1)
Yc = Y[triangles].mean(axis=1)
plt.tricontour(Xc, Yc, values, 10)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, colors="black")
show()

plt.contour(X, Y, Z, 20, cmap="RdGy")
show()

plt.contourf(X, Y, Z, 20, cmap="RdGy")
plt.colorbar()
show()

plt.imshow(Z, extent=[0, 5, 0, 5], origin="lower", cmap="RdGy")
plt.colorbar()
# plt.axis(aspect='image')
show()

contours = plt.contour(X, Y, Z, 3, colors="black")
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin="lower", cmap="RdGy", alpha=0.5)
plt.colorbar()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 畫  (x^2 + y^2 -1)^3 - x^2*y^3 = 0
# %fig=matplotlib繪制心形隱函數曲線
x, y = np.mgrid[-2:2:500j, -2:2:500j]
z = (x**2 + y**2 - 1) ** 3 - x**2 * y**3
plt.contourf(x, y, z, levels=[-1, 0], colors=["red"])
plt.gca().set_aspect("equal")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個


# z 5 X 5
z = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 9, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


print("畫熱圖")
ndarray2d = np.array(z)
print(type(ndarray2d))
print(ndarray2d.shape)
print(ndarray2d)
print("維度", ndarray2d.ndim)
print("形狀", ndarray2d.shape)
print("數量", ndarray2d.size)

ndarray2d = np.array(z)

sns.heatmap(ndarray2d, cmap="Reds")
# sns.heatmap(ndarray2d, cmap="coolwarm")
# sns.heatmap(ndarray2d, annot = True)

show()
