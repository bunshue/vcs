"""
imshow

matplotlib直接對圖片處理 不經過opencv PIL

opencv與PIL有自己的圖片處理, 只是使用matplotlib輸出
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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

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

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image = img.imread(filename)  # 讀取原始圖像

# plt之讀取檔案 取得圖片資訊
h, w, c = image.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道數 = {c}")

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

plt.imshow(image)
plt.title("原始圖像")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

# 裁剪圖片 plt
x_l, x_r = 150, 350  # 保留的部分，由左而右
y_u, y_d = 150, 400  # 保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)
plt.title("顯示裁剪圖片")

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 打開圖像，並轉成灰度圖像
# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert("L"))  # L為8位像素黑白圖

# plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.contour(image, origin="image")
plt.axis("equal")
plt.title("圖像輪廓圖")

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

image = img.imread(filename)  # 讀取原始圖像
r = image.copy()  # 複製圖像
r[:, :, [1, 2]] = 0  # 保留紅色元素, 設定綠色和藍色元素是 0
plt.imshow(r)
plt.title("Red元素圖像")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

image = img.imread(filename)  # 讀取原始圖像
g = image.copy()  # 複製圖像
g[:, :, [0, 2]] = 0  # 保留綠色元素, 設定紅色和藍色元素是 0
plt.imshow(g)
plt.title("Green元素圖像")

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

image = img.imread(filename)  # 讀取原始圖像
b = image.copy()  # 複製圖像
b[:, :, [0, 1]] = 0  # 保留藍色元素, 設定紅色和綠色元素是 0
plt.imshow(b)
plt.title("Blue元素圖像")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/bug.bmp"

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

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

imgplot = plt.imshow(image)
plt.title("原圖(灰階)")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

lum_img = image[:, :, 0]
plt.imshow(lum_img)
plt.title("偽色彩1")

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

plt.imshow(lum_img, cmap="hot")
plt.title("偽色彩2")

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

imgplot = plt.imshow(lum_img)
imgplot.set_cmap("nipy_spectral")
plt.title("偽色彩3")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

imgplot = plt.imshow(lum_img)
plt.title("Color scale reference")

print("------------------------------------------------------------")  # 60個
plt.subplot(236)


plt.tight_layout()
plt.show()

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

plt.tight_layout()
plt.show()

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

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

print("二維 sinc 函數")

N = 100

sinc2d = np.zeros((N, N))
for x, x1 in enumerate(np.linspace(-10, 10, N)):
    for y, x2 in enumerate(np.linspace(-10, 10, N)):
        sinc2d[x, y] = np.sin(x1) * np.sin(x2) / (x1 * x2)
# print(sinc2d)

# same
x1 = np.linspace(-10, 10, N)
x2 = np.linspace(-10, 10, N)
sinc2d = np.outer(np.sin(x1), np.sin(x2)) / np.outer(x1, x2)
# print(sinc2d)

plt.imshow(sinc2d)
plt.title("二維 sinc 函數")

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
X, Y = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((X - 1) ** 2 + (Y - 1) ** 2))

plt.imshow(zz)
plt.title("default margins")

"""
plt.imshow(zz)
plt.margins(0.2)
plt.title("margins(0.2)")
"""

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

delta = 0.1
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2) - Y**2)

im = plt.imshow(
    Z, interpolation="bilinear", cmap=cm.gray, origin="lower", extent=[-3, 3, -3, 3]
)

"""
im.set_url('https://www.google.com/')
filename = 'C:/_git/vcs/_1.data/______test_files2/image.svg'
fig.savefig(filename)
print('已存圖' + filename)
"""

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

image = np.array(
    [
        [0, 1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10, 11],
        [12, 13, 14, 15, 16, 18],
        [18, 19, 20, 21, 22, 23],
        [24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35],
    ]
)
plt.imshow(image, cmap="Blues")
plt.imshow(image, cmap="Blues", origin="lower")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

print("imshow 顯示 numpy 資料")

arr = np.arange(256).reshape((16, 16))

im = plt.imshow(arr, interpolation="none")

plt.colorbar(im)


print("------------------------------------------------------------")  # 60個
plt.subplot(236)

from mpl_toolkits.axes_grid1 import make_axes_locatable

arr = np.arange(256).reshape((16, 16))
im = plt.imshow(arr, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

plt.tight_layout()
plt.show()

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

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

print("------------------------------------------------------------")  # 60個
plt.subplot(232)


print("------------------------------------------------------------")  # 60個
plt.subplot(233)


print("------------------------------------------------------------")  # 60個
plt.subplot(234)



print("------------------------------------------------------------")  # 60個
plt.subplot(235)


# make these smaller to increase the resolution
dx, dy = 0.05, 0.05

x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)

# when layering multiple images, the images need to have the same
# extent.  This does not mean they need to have the same shape, but
# they both need to render to the same coordinate system determined by
# xmin, xmax, ymin, ymax.  Note if you use different interpolations
# for the images their apparent extent could be different due to
# interpolation edge effects

extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z, cmap=plt.cm.gray, interpolation="nearest", extent=extent)
#im1 = plt.imshow(Z, cmap=plt.cm.viridis, alpha=0.9, interpolation="bilinear", extent=extent)


print("------------------------------------------------------------")  # 60個
plt.subplot(236)

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

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 6 random 影像 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

print("建立一個random圖像 0 50 100 ... 255")

W, H = 10, 10

image = (
    np.random.choice([0, 50, 100, 150, 200, 255], size=W * H)
    .reshape(H, W)
    .astype(np.uint8)
)

plt.imshow(image)
print(image)

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

print("畫出 常態分布 二維 N X N")
N = 10
image = np.random.randn(N, N)
plt.imshow(image)
print(image)

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

image = np.random.random((10, 10))
plt.imshow(image)
print(image)

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])  # 設定位置
plt.colorbar(cax=cax)

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

data = np.random.random((10, 10))
plt.imshow(data)


print("------------------------------------------------------------")  # 60個
plt.subplot(235)

data = np.random.random((10, 10))
plt.imshow(data, cmap="cool")
# plt.imshow(data, cmap="hsv")

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

N = 100
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.sin(Y)  # 建立影像

plt.imshow(Z, cmap="hot")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="imshow 集合 7 random 影像 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------------------------------------")  # 60個
plt.subplot(231)


print("------------------------------------------------------------")  # 60個
plt.subplot(232)


print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

r = src.copy()  # 複製影像色彩陣列
r[:, :, [1, 2]] = 0  # 保留紅色元素, 設定綠色和藍色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Red元素")
plt.imshow(r)

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

g = src.copy()  # 複製影像色彩陣列
g[:, :, [0, 2]] = 0  # 保留綠色元素, 設定紅色和藍色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Green元素")
plt.imshow(g)

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

b = src.copy()  # 複製影像色彩陣列
b[:, :, [0, 1]] = 0  # 保留藍色元素, 設定紅色和綠色元素是 0
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("Blue元素")
plt.imshow(b)

plt.tight_layout()
plt.show()

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

print("------------------------------------------------------------")  # 60個
plt.subplot(231)

N = 20
x = np.linspace(0, 2 * np.pi, N)
y = np.linspace(0, 2 * np.pi, N)
X, Y = np.meshgrid(x, y)

# z = np.sin(X) + np.cos(Y)   # 建立影像
z = np.sin(X) + np.sin(Y)  # 建立影像

plt.imshow(z)
# plt.imshow(z,cmap='hsv')

print("------------------------------------------------------------")  # 60個
plt.subplot(232)

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
X, Y = np.meshgrid(x, y)

# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z = np.add.outer(range(8), range(8)) % 2  # 棋盤
plt.imshow(Z, cmap="gray", extent=extent)

print("------------------------------------------------------------")  # 60個
plt.subplot(233)

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
X, Y = np.meshgrid(x, y)

# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

Z = np.sin(X) + np.cos(Y)
plt.imshow(Z, cmap="jet", alpha=0.8, interpolation="bilinear", extent=extent)

print("------------------------------------------------------------")  # 60個
plt.subplot(234)

N = 10
data = np.reshape(np.linspace(0, 1, N**2), (N, N))  # 建立 N x N 陣列

# 使用預設顏色繪製
plt.imshow(data)

plt.xticks(range(N))  # 繪製 x 軸刻度
plt.yticks(range(N))  # 繪製 y 軸刻度
plt.title("使用預設插值")

print("------------------------------------------------------------")  # 60個
plt.subplot(235)

# 相同陣列使用不同的插值法
plt.imshow(data, interpolation="bicubic")
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("使用 bicubic 插值")

print("------------------------------------------------------------")  # 60個
plt.subplot(236)

plt.imshow(data, interpolation="hamming")
plt.xticks(range(N))  # 繪製 x 軸刻度
plt.title("使用 hamming 插值")

plt.tight_layout()
plt.show()

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

fig.tight_layout()
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

sys.exit()

plt.rcParams["savefig.facecolor"] = "0.8"
plt.tight_layout()


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

