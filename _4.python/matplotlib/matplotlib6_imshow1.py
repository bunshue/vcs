"""
imshow

matplotlib直接對圖片處理 不經過opencv PIL

opencv與PIL有自己的圖片處理, 只是使用matplotlib輸出

要用 matplotlib 顯示圖片，要先透過 matplotlib.image 模組中的
imread() 方法讀取圖片，讀取後使用 imshow() 在圖表中繪製圖片，最後透過 plt.show() 顯示圖表。
"""

import matplotlib.cm as cm
import matplotlib.image as img
import pylab
from PIL import Image, ImageEnhance

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
    num="imshow 集合 1 顯示圖片 簡單圖片處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
image = img.imread(filename)  # 讀取原始圖像

# plt之讀取檔案 取得圖片資訊
h, w, c = image.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道數 = {c}")

print("------------------------------")  # 30個
plt.subplot(231)

plt.imshow(image)
plt.title("原始圖像")

print("------------------------------")  # 30個
plt.subplot(232)

# 裁剪圖片 plt
x_l, x_r = 150, 350  # 保留的部分，由左而右
y_u, y_d = 150, 400  # 保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)
plt.title("顯示裁剪圖片")

print("------------------------------")  # 30個
plt.subplot(233)

filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
# 打開圖像，並轉成灰度圖像
# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert("L"))  # L為8位像素黑白圖

# plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.contour(image, origin="image")
plt.axis("equal")
plt.title("圖像輪廓圖")

print("------------------------------")  # 30個
plt.subplot(234)

image = img.imread(filename)  # 讀取原始圖像
r = image.copy()  # 複製圖像
r[:, :, [1, 2]] = 0  # 保留紅色元素, 設定綠色和藍色元素是 0
plt.imshow(r)
plt.title("Red元素圖像")

print("------------------------------")  # 30個
plt.subplot(235)

image = img.imread(filename)  # 讀取原始圖像
g = image.copy()  # 複製圖像
g[:, :, [0, 2]] = 0  # 保留綠色元素, 設定紅色和藍色元素是 0
plt.imshow(g)
plt.title("Green元素圖像")

print("------------------------------")  # 30個
plt.subplot(236)

image = img.imread(filename)  # 讀取原始圖像
b = image.copy()  # 複製圖像
b[:, :, [0, 1]] = 0  # 保留藍色元素, 設定紅色和綠色元素是 0
plt.imshow(b)
plt.title("Blue元素圖像")

print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/bug.bmp"

plt.figure(
    num="imshow 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => PIL影像 => np陣列
image = np.asarray(Image.open(filename))
# print(repr(image))

print("------------------------------")  # 30個
plt.subplot(231)

imgplot = plt.imshow(image)
plt.title("原圖(灰階)")

print("------------------------------")  # 30個
plt.subplot(232)

lum_img = image[:, :, 0]
plt.imshow(lum_img)
plt.title("偽色彩1")

print("------------------------------")  # 30個
plt.subplot(233)

plt.imshow(lum_img, cmap="hot")
plt.title("偽色彩2")

print("------------------------------")  # 30個
plt.subplot(234)

imgplot = plt.imshow(lum_img)
imgplot.set_cmap("nipy_spectral")
plt.title("偽色彩3")

print("------------------------------")  # 30個
plt.subplot(235)

imgplot = plt.imshow(lum_img)
plt.title("Color scale reference")

print("------------------------------")  # 30個
plt.subplot(236)


print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib.image as img

plt.figure(
    num="imshow 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

image = img.imread(filename)  # 讀取原始圖像

for i in range(1, 5):
    plt.subplot(2, 2, i)
    x = 1 - 0.2 * (i - 1)  # 調整色彩明暗參數
    print(f"i = {i}  x = {x:2.1f}")
    plt.axis("off")  # 關閉顯示軸刻度
    plt.title(f"x = {x:2.1f}", color="b")  # 藍色浮動值標題
    src = image * x  # 處理像素值
    int_image = src.astype(int)  # 將元素值轉成整數
    plt.imshow(int_image)  # 顯示圖像

print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)

N = 100
sinc2d = np.zeros((N, N))
for x, x1 in enumerate(np.linspace(-2 * np.pi, 2 * np.pi, N)):
    for y, x2 in enumerate(np.linspace(-2 * np.pi, 2 * np.pi, N)):
        # sinc2d[x, y] = np.sin(x1) * np.sin(x2) / (x1 * x2)  # 二維 sinc 函數
        sinc2d[x, y] = np.sqrt(x1**2 + x2**2)
# print(sinc2d)

""" same
x1 = np.linspace(-10, 10, N)
x2 = np.linspace(-10, 10, N)
sinc2d = np.outer(np.sin(x1), np.sin(x2)) / np.outer(x1, x2)  # 二維 sinc 函數
# print(sinc2d)
"""
plt.imshow(sinc2d)

print("------------------------------")  # 30個
plt.subplot(232)

N = 100
x = np.linspace(-2 * np.pi, 2 * np.pi, N)
y = np.linspace(-2 * np.pi, 2 * np.pi, N)
X, Y = np.meshgrid(x, y)
zz = np.sinc(np.sqrt(X**2 + Y**2))
zz = np.sqrt(X**2 + Y**2)

plt.imshow(zz)
plt.title("default margins")

"""
plt.imshow(zz)
plt.margins(0.2)
plt.title("margins(0.2)")
"""

print("------------------------------")  # 30個
plt.subplot(233)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
X, Y = np.meshgrid(x, y)

# Z = np.exp(-(X**2) - Y**2)
Z = np.sqrt((X**2) + Y**2)

im = plt.imshow(
    Z, interpolation="bilinear", cmap=cm.gray, origin="lower", extent=[-3, 3, -3, 3]
)

"""
im.set_url('https://www.google.com/')
filename = 'D:/_git/vcs/_1.data/______test_files2/image.svg'
fig.savefig(filename)
print('已存圖' + filename)
"""

print("------------------------------")  # 30個
plt.subplot(234)

np_array_2d = np.array(
    [
        [0, 1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10, 11],
        [12, 13, 14, 15, 16, 18],
        [18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35],
    ]
)

# same
np_array_2d = np.arange(36).reshape((6, 6))

plt.imshow(np_array_2d, cmap="Blues")
plt.imshow(np_array_2d, cmap="Blues", origin="lower")

print("------------------------------")  # 30個
plt.subplot(235)

print("imshow 顯示 numpy 資料")

np_array_2d = np.arange(256).reshape((16, 16))

im = plt.imshow(np_array_2d, interpolation="none")

plt.colorbar(im)

print("------------------------------")  # 30個
plt.subplot(236)

from mpl_toolkits.axes_grid1 import make_axes_locatable

np_array_2d = np.arange(256).reshape((16, 16))
im = plt.imshow(np_array_2d, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 5",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)

N = 100
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.sin(Y)  # 建立影像

plt.imshow(Z, cmap="hot")

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


print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 6 random 影像",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

print("------------------------------")  # 30個
plt.subplot(231)

print("6數任選 MXN random圖像")

W, H = 8, 8

image = (
    np.random.choice([0, 50, 100, 150, 200, 255], size=W * H)
    .reshape(H, W)
    .astype(np.uint8)
)
print(str(W) + "X" + str(H) + " 6數任選")

N = 10
image = np.random.randn(N, N)
print("常態分布 二維 N X N")

plt.imshow(image)

print(image)

print("------------------------------")  # 30個
plt.subplot(232)

image = np.random.random((10, 10))
plt.imshow(image)
# plt.imshow(image, cmap="cool")
# plt.imshow(image, cmap="hsv")
# print(image)

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])  # 設定位置
plt.colorbar(cax=cax)

print("------------------------------")  # 30個
plt.subplot(233)

# 四圖
N = 4
src = np.random.random((N, N, 3))  # 隨機產生影像圖陣列資料

print(src)
print(src[:, :, 0])
print(src[:, :, 1])
print(src[:, :, 2])

plt.xticks(range(N))  # 繪製 x 軸刻度
plt.yticks(range(N))  # 繪製 y 軸刻度
plt.title("RGB色彩")
plt.imshow(src)

print("------------------------------")  # 30個
plt.subplot(234)

r = src.copy()  # 複製影像色彩陣列
r[:, :, [1, 2]] = 0  # 保留紅色元素, 設定綠色和藍色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Red元素")
plt.imshow(r)

print("------------------------------")  # 30個
plt.subplot(235)

g = src.copy()  # 複製影像色彩陣列
g[:, :, [0, 2]] = 0  # 保留綠色元素, 設定紅色和藍色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Green元素")
plt.imshow(g)

print("------------------------------")  # 30個
plt.subplot(236)

b = src.copy()  # 複製影像色彩陣列
b[:, :, [0, 1]] = 0  # 保留藍色元素, 設定紅色和綠色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Blue元素")
plt.imshow(b)

print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 7",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)

x = np.arange(-3.0, 3.0, 0.05)
y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z, cmap=plt.cm.gray, interpolation="nearest", extent=extent)
# im1 = plt.imshow(Z, cmap=plt.cm.viridis, alpha=0.9, interpolation="bilinear", extent=extent)

print("------------------------------")  # 30個
plt.subplot(232)

""" outer 用法
x1 = [1,2,3]
y1 = [4,5,6,7,8]
z1 = np.add.outer(x1, y1)
print(f"z1 = \n{z1}")

x2 = range(8)
y2 = range(8)
z2 = np.add.outer(x2, y2)
print(f"z2 = \n{z2}")
"""

z = np.add.outer(range(8), range(8)) % 2
im1 = plt.imshow(z, cmap="gray")


print("------------------------------")  # 30個
plt.subplot(233)


print("------------------------------")  # 30個
plt.subplot(234)


print("------------------------------")  # 30個
plt.subplot(235)


print("------------------------------")  # 30個
plt.subplot(236)


print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 8",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)

N = 20
x = np.linspace(0, 2 * np.pi, N)
y = np.linspace(0, 2 * np.pi, N)
X, Y = np.meshgrid(x, y)

# z = np.sin(X) + np.cos(Y)   # 建立影像
z = np.sin(X) + np.sin(Y)  # 建立影像

plt.imshow(z)
# plt.imshow(z,cmap='hsv')

print("------------------------------")  # 30個
plt.subplot(232)

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
X, Y = np.meshgrid(x, y)

# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z = np.add.outer(range(8), range(8)) % 2  # 棋盤
plt.imshow(Z, cmap="gray", extent=extent)

print("------------------------------")  # 30個
plt.subplot(233)

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
X, Y = np.meshgrid(x, y)

# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

# Z = np.sin(X) + np.cos(Y)
Z = np.sqrt(X**2 + Y**2)
plt.imshow(Z, cmap="jet", alpha=0.8, interpolation="bilinear", extent=extent)

print("------------------------------")  # 30個
plt.subplot(234)

N = 10
data = np.reshape(np.linspace(0, 1, N**2), (N, N))  # 建立 N x N 陣列

# 使用預設顏色繪製
plt.imshow(data)

plt.xticks(range(N))  # 繪製 x 軸刻度
plt.yticks(range(N))  # 繪製 y 軸刻度
plt.title("使用預設插值")

print("------------------------------")  # 30個
plt.subplot(235)

# 相同陣列使用不同的插值法
plt.imshow(data, interpolation="bicubic")
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("使用 bicubic 插值")

print("------------------------------")  # 30個
plt.subplot(236)

plt.imshow(data, interpolation="hamming")
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("使用 hamming 插值")

print("------------------------------")  # 30個
plt.suptitle("")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


image = np.array(
    [
        [0, 0, 7, 15, 13, 1, 0, 0],
        [0, 8, 13, 6, 15, 4, 0, 0],
        [0, 2, 1, 13, 13, 0, 0, 0],
        [0, 0, 2, 15, 11, 1, 0, 0],
        [0, 0, 0, 1, 12, 12, 1, 0],
        [0, 0, 0, 0, 1, 10, 8, 0],
        [0, 0, 8, 4, 5, 14, 9, 0],
        [0, 0, 7, 13, 13, 9, 0, 0],
    ]
)

plt.figure(figsize=(12, 8))

# cmap
plt.subplot(5, 8, 1)
plt.imshow(image)
plt.subplot(5, 8, 2)
plt.imshow(image, cmap="hot")
plt.subplot(5, 8, 3)
plt.imshow(image, cmap="cool")
plt.subplot(5, 8, 4)
plt.imshow(image, cmap="hsv")
plt.subplot(5, 8, 5)
plt.imshow(image, cmap="YlGn")
plt.subplot(5, 8, 6)
plt.imshow(image, cmap="Blues")
plt.subplot(5, 8, 7)
plt.imshow(image, cmap="binary")  # 顯示黑白圖片
plt.subplot(5, 8, 8)
plt.imshow(image, cmap="gray")
plt.subplot(5, 8, 9)
plt.imshow(image, cmap="copper")
plt.subplot(5, 8, 10)
plt.imshow(image, cmap="jet")
plt.subplot(5, 8, 11)
plt.imshow(image, cmap="viridis")

# interpolation
plt.subplot(5, 8, 17)
plt.imshow(image, interpolation="none")
plt.subplot(5, 8, 18)
plt.imshow(image, interpolation="bicubic")
plt.subplot(5, 8, 19)
plt.imshow(image, interpolation="bilinear")
plt.subplot(5, 8, 20)
plt.imshow(image, interpolation="hamming")

# cmap + interpolation

plt.subplot(5, 8, 25)
plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
plt.subplot(5, 8, 26)
plt.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
plt.subplot(5, 8, 27)
plt.imshow(image, cmap=plt.cm.gray, interpolation="none")

plt.subplot(5, 8, 33)
plt.imshow(image)
plt.subplot(5, 8, 34)
plt.imshow(image, origin="lower")
plt.subplot(5, 8, 35)
plt.imshow(image * 1.0)
plt.subplot(5, 8, 36)
plt.imshow(image / 255.0)
plt.subplot(5, 8, 37)
plt.imshow(np.clip(image / 200.0, 0, 1))

"""
plt.imshow(image, interpolation="bilinear", cmap=cm.gray, origin="lower", extent=[-3, 3, -3, 3])
plt.imshow(image, cmap=plt.cm.gray, interpolation="nearest", extent=extent)
plt.imshow(image, cmap=plt.cm.viridis, alpha=0.9, interpolation="bilinear", extent=extent)
plt.imshow(image, extent=extent, origin="lower")
plt.imshow(image, extent=extent, cmap=cm.gray, origin="lower")
plt.imshow(image, clim=(0, 175))
plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap="gray")
plt.imshow(image, extent=extent)
plt.imshow(image, alpha=0.8, interpolation="bilinear", extent=extent)
"""

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

farmers = ["張三", "李四", "大成", "陳王", "李曉.", "林邊"]
fruits = ["釋迦", "番茄", "鳳梨", "蓮霧", "香蕉", "芭樂"]

# 建立收成表
harvest = np.array(
    [
        [0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
        [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
        [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
        [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
        [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
        [0.3, 2.2, 0.0, 1.3, 0.0, 1.5],
    ]
)

fig, ax = plt.subplots()

im = ax.imshow(harvest, cmap="YlGn")

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
        if harvest[i, j] < 3.0:
            text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="b")
        else:
            text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="r")

ax.set_title("農夫收成(噸 / 年)", fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")

print("------------------------------------------------------------")  # 60個
plt.suptitle("")
fig.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

W, H, D = 5, 5, 3

print("建立 0 ~ 255 的隨機陣列")
image1 = np.random.randint(0, 256, size=[W, H, D], dtype=np.uint8)
print(image1.shape)

image1[:, :, 0] = 0
# R通道
image1[:, :, 1] = 0
# G通道
image1[:, :, 2] = 0
# B通道
print(image1)

plt.imshow(image1)
show()

print("建立 0.0 ~ 1.0 的隨機陣列")
image2 = np.random.random((W, H, D))
print(image2.shape)
# print(image2)

plt.imshow(image2)
show()

print("建立 0 ~ 255 的 16 X 16 陣列")
image3 = np.arange(0, 256).reshape(16, 16)
print(image3.shape)
# print(image3)

plt.imshow(image3)
show()

print("------------------------------------------------------------")  # 60個

print("建立一黑圖")

W = 640
H = 480
print("numpy製作一個 %d X %d 的圖 黑色, 2維 3 通道" % (W, H))
image = np.zeros((H, W, 3), dtype=np.uint8)  # 預設為0, 黑色, 2維, 3通道
# image = np.zeros((H, W), dtype = np.uint8)    #預設為0, 黑色, 2維, 1通道

print("中間一塊用填成灰色")
for i in range(100, 200):
    for j in range(100, 200):
        image[i, j] = 200

print("中間一塊用填成白色")
#     y_st y_sp  x_st y_st
image[300:400, 50:200] = 255

# image[:, :, 0] = 255 #將第0通道設為全亮 藍
# image[:, :, 1] = 255 #將第1通道設為全亮 綠
# image[:, :, 2] = 255 #將第0通道設為全亮 紅

image[:, 0:50, 0] = 255  # 第0通道, 藍色通道
image[:, 50:100, 1] = 255  # 第1通道, 綠色通道
image[:, 100:150, 2] = 255  # 第2通道, 紅色通道

y = 75
#                  y   x
print("讀取像素點 (y, 25) =", image[y, 25])
print("讀取像素點 (y, 75) =", image[y, 75])
print("讀取像素點 (y, 125) =", image[y, 125])
print("讀取像素點 (y, 125) 裡面的紅 =", image[y, 125, 2])

# 逕行修改
image[:, 75] = 255
image[:, 125, 2] = 0


print("建立一個每點顏色任意顏色之圖")
random_image = np.random.randint(0, 256, size=[100, 100, 3], dtype=np.uint8)

print("將一任意圖貼上來")
#     y_st  y_sp x_st  y_st
image[100:200, 400:500] = random_image

plt.imshow(image)

show()

print("------------------------------------------------------------")  # 60個

img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
print("img1 = \n", img1)
plt.imshow(img1)
show()

img2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
print("img2 = \n", img2)
plt.imshow(img2)
show()

img3 = img1 + img2
print("img3 = \n", img3)
plt.imshow(img3)
show()

print("------------------------------------------------------------")  # 60個

img = np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)
print("img = \n", img)

print("讀取像素點img.item(3, 2) = ", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img.item(3, 2) = ", img.item(3, 2))

print("------------------------------------------------------------")  # 60個

img = np.random.randint(10, 99, size=[2, 4, 3], dtype=np.uint8)
print("img = \n", img)

print("讀取像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("讀取像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("讀取像素點img[1, 0, 2] = ", img.item(1, 0, 2))
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("修改后像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("修改后像素點img[1, 0, 2] = ", img.item(1, 0, 2))

print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/lena_color.jpg"

img = plt.imread(filename)
print(img.shape, img.dtype)

# 用imread()和imshow()顯示圖形
img = plt.imread(filename)
fig, axes = plt.subplots(2, 4, figsize=(11, 4))
fig.subplots_adjust(0, 0, 1, 1, 0.05, 0.05)

axes = axes.ravel()

axes[0].imshow(img)
axes[1].imshow(img, origin="lower")
axes[2].imshow(img * 1.0)
axes[3].imshow(img / 255.0)
axes[4].imshow(np.clip(img / 200.0, 0, 1))

axe_img = axes[5].imshow(img[:, :, 0])
plt.colorbar(axe_img, ax=axes[5])

axe_img = axes[6].imshow(img[:, :, 0], cmap="copper")
plt.colorbar(axe_img, ax=axes[6])

for ax in axes:
    ax.set_axis_off()

show()

print("------------------------------------------------------------")  # 60個

import matplotlib.cm as cm

""" NG

cc = cm._cmapnames[:5]
print(cc)
#['Spectral', 'copper', 'RdYlGn', 'Set2', 'summer']
"""

# 使用imshow()可視化二元函數
y, x = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp(-(x**2) - y**2)

extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.subplot(121)
plt.imshow(z, extent=extent, origin="lower")
plt.colorbar()
plt.subplot(122)
plt.imshow(z, extent=extent, cmap=cm.gray, origin="lower")
plt.colorbar()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 調整子圖布局

filename = "D:/_git/vcs/_4.python/_data/elephant.jpg"
image = img.imread(filename)  # 讀取原始圖像

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(image)

plt.subplot(232)
plt.imshow(image)

plt.subplot(233)
plt.imshow(image)

plt.subplot(234)
plt.imshow(image)

plt.subplot(235)
plt.imshow(image)

plt.subplot(236)
plt.imshow(image)

# 調整子圖布局     左起  下起  寬佔比 高佔比 水平距 垂直距
plt.subplots_adjust(
    left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.01, hspace=0.05
)
# plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
# wspace=None, hspace=None)

plt.suptitle("")
# plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


plt.rcParams["savefig.facecolor"] = "0.8"

"""

#5
#plt.hist(image.ravel(), bins=range(256), fc='k', ec='k')


#6
plt.imshow(lum_img, clim=(0, 175))

#7
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0, 175)


# Array Interpolation schemes
#8
# 檔案 => PIL影像
image = Image.open(filename)
image.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(image)

#9
imgplot = plt.imshow(image, interpolation="bilinear")

#10
imgplot = plt.imshow(image, interpolation="bicubic")


plt.imshow(
    Z,
    cmap=plt.cm.prism,
    interpolation="none",
    extent=(X.min(), X.max(), Y.min(), Y.max()),
)

x = np.linspace(start=-10, stop=10, num=101)

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap="gray")

#plt.colorbar(shrink=0.83)



"""

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import matplotlib.image as img

fig = img.imread("out20_12.jpg")
plt.imshow(fig)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------")  # 30個
