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
'''
print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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
image = img.imread(filename)

# plt之讀取檔案 取得圖片資訊
h, w, c = image.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道數 = {c}")

# 第一張圖
plt.subplot(231)

plt.imshow(image)
plt.title("顯示圖片")

# 第二張圖
plt.subplot(232)

# 裁剪圖片 plt
x_l, x_r = 150, 350  # 保留的部分，由左而右
y_u, y_d = 150, 400  # 保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)
plt.title("顯示裁剪圖片")

# 第三張圖
plt.subplot(233)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# 打開圖像，並轉成灰度圖像
# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert("L"))  # L為8位像素黑白圖

# plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.contour(image, origin="image")
plt.axis("equal")
plt.title("圖像輪廓圖")

# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)

# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/bug.bmp"

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

# 第一張圖
plt.subplot(231)

# 原圖(灰階)
imgplot = plt.imshow(image)

# 第二張圖
plt.subplot(232)

# 1 偽色彩
lum_img = image[:, :, 0]
plt.imshow(lum_img)

# 第三張圖
plt.subplot(233)

# 2 偽色彩
plt.imshow(lum_img, cmap="hot")


# 第四張圖
plt.subplot(234)


# 3 偽色彩
imgplot = plt.imshow(lum_img)
imgplot.set_cmap("nipy_spectral")


# 第五張圖
plt.subplot(235)

# 4 Color scale reference
imgplot = plt.imshow(lum_img)
plt.colorbar()


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

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

"""


print("------------------------------------------------------------")  # 60個

#          編號                   圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="imshow 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
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

# 第二~三張圖

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
xx, yy = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((xx - 1) ** 2 + (yy - 1) ** 2))


# 第二張圖
plt.subplot(232)

plt.imshow(zz)
plt.title("default margins")


# 第三張圖
plt.subplot(233)

plt.imshow(zz)
plt.margins(0.2)
plt.title("margins(0.2)")


# 第四張圖
plt.subplot(234)

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-(X**2) - Y**2)
Z2 = np.exp(-((X - 1) ** 2) - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

im = plt.imshow(
    Z, interpolation="bilinear", cmap=cm.gray, origin="lower", extent=[-3, 3, -3, 3]
)
"""
im.set_url('https://www.google.com/')
filename = 'C:/_git/vcs/_1.data/______test_files2/image.svg'
fig.savefig(filename)
print('已存圖' + filename)
"""

# 第五張圖
plt.subplot(235)

image = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

plt.imshow(image, cmap="Blues")
plt.colorbar()

# 第六張圖
plt.subplot(236)

# Layer Images


def func3(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2 + y**2))


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

Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation="nearest", extent=extent)

Z2 = func3(X, Y)

im2 = plt.imshow(
    Z2, cmap=plt.cm.viridis, alpha=0.9, interpolation="bilinear", extent=extent
)

plt.show()


print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="imshow 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

xmin, xmax, ymin, ymax = -2, 0.8, -1.5, 1.5
max_it = 3  # maximum number of iterations
px = 300  # vertical lines
res = (ymax - ymin) / px  # grid resolution


def m(c):
    z = 0
    for n in range(1, max_it + 1):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return np.NaN


X = pylab.arange(xmin, xmax + res, res)
Y = pylab.arange(ymin, ymax + res, res)
Z = pylab.zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
    # print (iy + 1, "of", len(Y))
    for ix, x in enumerate(X):
        Z[-iy - 1, ix] = m(x + 1j * y)

# 影像存圖
# pylab.save("mandel", Z)	# save array to file

plt.imshow(
    Z,
    cmap=plt.cm.prism,
    interpolation="none",
    extent=(X.min(), X.max(), Y.min(), Y.max()),
)
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

# 第二張圖
plt.subplot(232)

xmin, xmax, ymin, ymax = -2, 0.8, -1.5, 1.5
max_it = 3  # maximum number of iterations
px = 30  # vertical lines
res = (ymax - ymin) / px  # grid resolution


def m(c):
    z = 0
    for n in range(1, max_it + 1):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return np.NaN


X = pylab.arange(xmin, xmax + res, res)
Y = pylab.arange(ymin, ymax + res, res)
Z = pylab.zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
    # print (iy + 1, "of", len(Y))
    for ix, x in enumerate(X):
        Z[-iy - 1, ix] = m(x + 1j * y)

plt.imshow(
    Z,
    cmap=plt.cm.prism,
    interpolation="none",
    extent=(X.min(), X.max(), Y.min(), Y.max()),
)
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")

# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

print("imshow 顯示 numpy 資料")
plt.rcParams["savefig.facecolor"] = "0.8"

arr = np.arange(256).reshape((16, 16))

plt.imshow(arr, interpolation="none")

plt.tight_layout()

# 第五張圖
plt.subplot(235)

print("imshow 顯示 numpy 資料")

arr = np.arange(256).reshape((16, 16))

im = plt.imshow(arr, interpolation="none")

plt.colorbar(im)

plt.tight_layout()

# 第六張圖
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

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

# 第一張圖
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

# 第二張圖
plt.subplot(232)

print("畫出 常態分布 二維 N X N")
N = 10
image = np.random.randn(N, N)
plt.imshow(image)
print(image)

# 第三張圖
plt.subplot(233)

image = np.random.random((100, 100))
plt.imshow(image)
print(image)

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])  # 設定位置
plt.colorbar(cax=cax)

# 第四張圖
plt.subplot(234)

x = np.linspace(start=-10, stop=10, num=101)

# plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap="gray")

# 第五張圖
plt.subplot(235)


def f(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-(x**2) - y**2)


n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
# plt.imshow(f(X, Y), cmap='hot', origin='low')
plt.imshow(f(X, Y), cmap="hot")
plt.colorbar(shrink=0.83)

plt.xticks(())
plt.yticks(())

# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.image as img

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

macau = img.imread(filename)     # 讀取原始圖像
plt.figure()

plt.subplot(221)        # 原始圖像
plt.axis('off')
plt.title('原始圖像')
plt.imshow(macau)

plt.subplot(222)
r = macau.copy()        # 複製圖像
r[:,:,[1,2]] = 0        # 保留紅色元素, 設定綠色和藍色元素是 0
plt.axis('off')
plt.title('Red元素圖像')
plt.imshow(r)

plt.subplot(223)
g = macau.copy()        # 複製圖像
g[:,:,[0,2]] = 0        # 保留綠色元素, 設定紅色和藍色元素是 0
plt.axis('off')
plt.title('Green元素圖像')
plt.imshow(g)

plt.subplot(224)
b = macau.copy()        # 複製圖像
b[:,:,[0,1]] = 0        # 保留藍色元素, 設定紅色和綠色元素是 0
plt.axis('off')
plt.title('Blue元素圖像')
plt.imshow(b)
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.image as img

macau = img.imread(filename)             # 讀取原始圖像
plt.figure()
for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)                       # 調整色彩明暗參數
    plt.axis('off')                         # 關閉顯示軸刻度
    plt.title(f'x = {x:2.1f}',color='b')    # 藍色浮動值標題    
    src = macau * x                         # 處理像素值
    intmacau = src.astype(int)              # 將元素值轉成整數
    plt.imshow(intmacau)                    # 顯示圖像
plt.show()
'''

print("------------------------------------------------------------")  # 60個

img = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 18],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35]])               
plt.imshow(img, cmap='Blues')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

img = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 18],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35]])               
plt.imshow(img, cmap='Blues', origin='lower')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
data = np.random.random((10, 10))
plt.imshow(data)
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
data = np.random.random((80, 80))
plt.imshow(data, cmap='cool')
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個


x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
xx, yy = np.meshgrid(x, y)

#z = np.sin(xx) + np.cos(yy)   # 建立影像
#z = np.sin(xx) + np.cos(yy)   # 建立影像
z = np.sin(xx) + np.sin(yy)   # 建立影像

plt.imshow(z)
#plt.imshow(z,cmap='hsv')
plt.show()

print("------------------------------------------------------------")  # 60個

x1 = [1,2,3]
y1 = [4,5,6,7,8]
z1 = np.add.outer(x1, y1)
print(f"z1 = \n{z1}")

x2 = range(8)
y2 = range(8)
z2 = np.add.outer(x2, y2)
print(f"z2 = \n{z2}")

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
z = np.add.outer(range(8), range(8)) % 2

im1 = plt.imshow(z, cmap='gray')

plt.show()

print("------------------------------------------------------------")  # 60個

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
xx, yy = np.meshgrid(x, y)
# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

fig = plt.figure()
z1 = np.add.outer(range(8), range(8)) % 2           # 棋盤
plt.imshow(z1, cmap='gray',extent=extent)           # 影像 1

z2 = np.sin(xx) + np.cos(yy)                        # 影像 2 公式
plt.imshow(z2, cmap='jet', alpha=0.8,
           interpolation='bilinear',extent=extent)  # 影像 2
plt.show()

print("------------------------------------------------------------")  # 60個

farmers = ["張三","李四","大成","陳王", "李曉.","林邊"]
fruits = ["釋迦","番茄","鳳梨","蓮霧","香蕉","芭樂"]
# 建立收成表
harvest = np.array([[0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
                    [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
                    [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
                    [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
                    [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
                    [0.3, 2.2, 0.0, 1.3, 0.0, 1.5]])

fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap='YlGn')
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
        text = ax.text(j, i, harvest[i,j],
                        ha="center", va="center", color="b")
ax.set_title("農夫收成(噸 / 年)",fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")
fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

farmers = ["張三","李四","大成","陳王", "李曉.","林邊"]
fruits = ["釋迦","番茄","鳳梨","蓮霧","香蕉","芭樂"]
# 建立收成表
harvest = np.array([[0.3, 2.1, 1.8, 3.5, 0.0, 2.0],
                    [2.1, 0.0, 3.0, 1.0, 2.3, 0.0],
                    [1.2, 2.6, 1.8, 4.1, 0.5, 3.6],
                    [0.5, 0.2, 0.7, 0.0, 2.3, 0.0],
                    [0.6, 1.5, 0.0, 2.1, 2.0, 4.2],
                    [0.3, 2.2, 0.0, 1.3, 0.0, 1.5]])

fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap='YlGn')
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
        if harvest[i,j] < 3.0:
            text = ax.text(j, i, harvest[i,j],
                           ha="center", va="center", color="b")
        else:
            text = ax.text(j, i, harvest[i,j],
                           ha="center", va="center", color="w")
ax.set_title("農夫收成(噸 / 年)",fontsize=18)
ax.set_xlabel("姓名")
ax.set_ylabel("水果")
fig.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

top = mpl.cm.get_cmap('OrRd_r', 128)        # OrRd_r色彩反轉
bottom = mpl.cm.get_cmap('Blues', 128)      # Blues色彩
# 組合OrRd_r和Blues色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
OrRdBlue = mpl.colors.ListedColormap(newcolors)

np.random.seed(10)
plt.subplot(211)                            # 上方子圖
data1 = np.random.random((80, 80))
plt.imshow(data1, cmap=OrRdBlue)

plt.subplot(212)                            # 下方子圖
data2 = np.random.random((80, 80))
plt.imshow(data2, cmap=OrRdBlue)
plt.subplots_adjust(left=0.2, right=0.6, bottom=0.1, top=0.9)
# 建立子圖表axes物件
ax = plt.axes([0.7, 0.1, 0.05, 0.8])        # 設定色彩條大小和位置
plt.colorbar(mpl.cm.ScalarMappable(cmap=OrRdBlue),cax=ax)
plt.show()

print("------------------------------------------------------------")  # 60個

N = 5
data = np.reshape(np.linspace(0,1,N**2), (N,N)) # 建立 N x N 陣列
plt.figure()
# 使用預設顏色繪製
plt.subplot(131)
plt.imshow(data)
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks(range(N))                            # 繪製 y 軸刻度
plt.title('使用預設插值',fontsize=12,color='b')
# 相同陣列使用不同的插值法
plt.subplot(132)
plt.imshow(data,interpolation='bicubic')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 bicubic 插值',fontsize=12,color='b')
plt.subplot(133)
plt.imshow(data,interpolation='hamming')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 hamming 插值',fontsize=12,color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

N = 5
np.random.seed(10)                  # 設定種子顏色值
src = np.random.random((N,N,3))     # 隨機產生影像圖陣列資料
plt.figure()

plt.subplot(141)
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks(range(N))    # 繪製 y 軸刻度
plt.title('RGB色彩')
plt.imshow(src)

plt.subplot(142)
r = src.copy()          # 複製影像色彩陣列
r[:,:,[1,2]] = 0        # 保留紅色元素, 設定綠色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Red元素')
plt.imshow(r)

plt.subplot(143)
g = src.copy()          # 複製影像色彩陣列
g[:,:,[0,2]] = 0        # 保留綠色元素, 設定紅色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Green元素')
plt.imshow(g)

plt.subplot(144)
b = src.copy()          # 複製影像色彩陣列
b[:,:,[0,1]] = 0        # 保留藍色元素, 設定紅色和綠色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Blue元素')
plt.imshow(b)
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
