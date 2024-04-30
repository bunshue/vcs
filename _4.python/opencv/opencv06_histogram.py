"""

用直方圖分析一張圖片的顏色組成

hist = cv2.calcHist(image, channels, mask, histSize, ranges, accumulate) 函數統計直方圖
參數都要加［］括起來
image：原圖像
channels：如果輸入的圖像是灰度圖，它的值就是[0]，如果是彩色圖像，傳入的參數可以是[0]、[1]、[2],分布對應著b,g,r。
mask：掩膜圖像。要統計整幅圖像的直方圖就把這個參數設為None，如果要統計掩膜部分的圖像的直方圖，就需要這個參數。
histSize：bins的個數,就是分多少個組距。例如[256]或者[16]，都要用方括號括起來。
ranges：像素值范圍，通常為[0, 256]
accumulate：累計(累積、疊加)標識，默認值是False。
這個函數返回的對象hist是一個一維數組，數組內的元素是各個灰度級的像素個數。

https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html


plt.hist(image,ravel(), hitsizes, ranges, color=)

img.ravel() 将原图像的array数组转成一维的数组
hitsizes 为直方图的灰度级数
ranges 为灰度范围[0,255]
color 是参数，需要使用color=''来指定颜色

num_bins = 256  # 直方圖顯示時的束數
plt.hist(image.ravel(), num_bins, [0, 256], log = True)
這邊使用到 matplotlib.pyplot 的 hist，它接受一組資料，計算清單中各值出現的次數，上面的範例
透過 NumPy 陣列的 ravel 方法，取得圖片攤平後的資料（只是個 NumPy 視圖）
，hist 的第二個參數指定要切出幾個直條，第三個參數指定要計算的值範圍，log 指定了是否 y 軸是否使用對數結果顯示。
"""

import cv2

#測試圖片
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"
filename = "data/pic_brightness1.bmp"
filename = "data/pic_brightness2.bmp"
filename = "data/pic_brightness3.bmp"
filename = "data/pic_calcHist.jpg"
filename = "C:/_git/vcs/_4.python/opencv\data/pic_gray_400X400_100-200.png"

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

print("測試 01 ravel() 的用法----------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread(filename)
print("形狀1 :", image.shape)
print("大小1 :", image.size)

cc = image.ravel()  #拉成一維
print("形狀 :", cc.shape)
print("大小 :", cc.size)

num_bins = 256  # 直方圖顯示時的束數
plt.hist(cc, num_bins, [0, 256], color="r")

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("形狀2 :", image.shape)
print("大小2 :", image.size)

cc = image.ravel()  # 拉成一維
print("形狀 :", cc.shape)
print("大小 :", cc.size)

num_bins = 256  # 直方圖顯示時的束數
plt.hist(cc, num_bins, [0, 256], color="g")
# plt.hist(cc, bins=num_bins, color="g", alpha=0.5, density=False)
# density=True   #以密度表示
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print("測試 02----------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image0 = cv2.imread(filename)  # 原圖, 彩色

# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("灰階")

plt.subplot(223)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image0.ravel(), num_bins, [0, 256], log=False, color="r")#拉成一維
plt.title("原圖的直方圖")

plt.subplot(224)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image1.ravel(), num_bins, [0, 256], log=False, color="r")#拉成一維
plt.title("灰階後的直方圖")

plt.show()

print("測試 03 calcHist----------------------------------------------------------")  # 60個

print('分析一張彩圖的RGB分佈')

# 對於彩色的圖片，
# 可以用 OpenCV 的 calcHist 函數分別計算統計值，
# 並畫出 RGB 三種顏色的分佈圖：

# 檔案 => cv2影像
image0 = cv2.imread(filename)
print("形狀 :", image0.shape)
print("大小 :", image0.size)

# 計算直方圖每個 bin 的數值, 將彩圖的RGB通道分離出來
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# RGB畫在一起
# 使用 ravel 將所有的像素資料轉為一維的陣列
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image0.ravel(), num_bins, [0, 256], color="gray", alpha = 0.3, density=False)
#plt.hist(image0.ravel(), bins = num_bins, color="gray", alpha = 0.3, density=False)

# RGB分開畫
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color="r", label="R", lw =3)
plt.plot(hist_g, color="g", label="G", lw =2)
plt.plot(hist_b, color="b", label="B", lw =1)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

plt.show()

print("測試 04 calcHist----------------------------------------------------------")  # 60個

print("使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階")

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("形狀 :", image.shape)
print("大小 :", image.size)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image.shape, np.uint8)
print("形狀 :", image.shape)
print("大小 :", image.size)
print(mask.shape)
H = image.shape[0]
W = image.shape[1]
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 先h 後 w

"""顯示原圖與mask
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "gray")
plt.subplot(122)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")
plt.show()
"""

# 全圖
hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])

# 部分圖
hist2 = cv2.calcHist([image], [0], mask, [256], [0, 256])

plt.plot(hist1, "r", label="全圖", lw =3)
plt.plot(hist2, "g", label="部分圖", lw =2)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

plt.show()

print("測試 05 calcHist----------------------------------------------------------")  # 60個

plt.figure(
    num="配合圖形遮罩計算直方圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階")

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print("形狀 :", image.shape)
print("大小 :", image.size)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image.shape, np.uint8)
print("形狀 :", image.shape)
print("大小 :", image.size)

print(mask.shape)
H = image.shape[0]
W = image.shape[1]
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 先h 後 w

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(image, image, mask=mask)

# 以原圖計算直方圖
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

# 繪製結果
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(223)
plt.imshow(cv2.cvtColor(masked_gray, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(224)
plt.plot(hist_full, "r", label="全圖", lw =3)
plt.plot(hist_mask, "g", label="部分圖", lw =2)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

plt.show()

print("測試 06 將一圖分解成 藍 綠 紅 三通道------------------------------------------------------------")  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => cv2影像
image = cv2.imread(filename)

cut = 50
num_bins = 256  # 直方圖顯示時的束數

b, g, r = cv2.split(image)

bb = b[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
# plt.show()

bbb = bb.reshape(bb.shape[0] * bb.shape[1], 1)
# print(bbb.shape)
plt.hist(bbb, num_bins, color="b", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
# plt.show()

ggg = gg.reshape(gg.shape[0] * gg.shape[1], 1)
# print(ggg.shape)
plt.hist(ggg, num_bins, color="g", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

rr = r[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
# plt.show()

rrr = rr.reshape(rr.shape[0] * rr.shape[1], 1)
# print(rrr.shape)
rrr = rrr[0 : len(rrr) : 5]
plt.hist(rrr, num_bins, color="r", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

plt.show()

print("測試 07 calcHist----------------------------------------------------------")  # 60個

"""
OpenCV 本身也有計算直方圖資料的函式 cv2.calcHist，而且是專門針對圖片進行計算，它的參數有：

    images：一組要分析的圖片。
    channels：要分析的頻道，若是灰階圖片就指定 [0]，若是彩色圖片，可分別使用 [0]、[1]、[2] 指定 BGR 頻道。
    mask：圖片遮罩，預設為 None。
    histSize：各頻道要切分出幾個直條。
    ranges：要計算的像素值範圍，通常都是設為 [0, 256]。

計算出來的資料，可以直接透過 matplotlib.pyplot 的 plot 繪製折線圖，或者是透過 bar 繪製直條圖。
"""

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

print("用 plot 或 bar 顯示 calcHist 的結果")

plt.plot(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
# plt.plot(np.arange(0, 256), hist.ravel())  # 數值直接顯示

# plt.bar(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
# plt.bar(np.arange(0, 256), hist.ravel())  # 數值直接顯示

plt.show()

print("測試 08 calcHist----------------------------------------------------------")  # 60個

# 用hist()和cv2.calcHist()函數繪制直方圖

# 檔案 => cv2影像
image = cv2.imread(filename)  # image.shape返回(576, 720, 3)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用hist()函數繪圖---
# 注意：用這個函數畫圖像直方圖時一定要用灰度圖像，如果非用彩圖，那得按通道畫，不然沒有什么意義
plt.figure(figsize=(16, 8))

plt.subplot(131)
plt.imshow(image[:, :, ::-1])  # 原圖
plt.title("原圖")

plt.subplot(132)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image_gray.ravel(), num_bins, color="r")  # 將灰度級劃分為 num_bins 個等級
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖轉灰階後的灰度直方圖")

# ---------使用cv2.calcHist()函數繪圖----這個函數可以傳入彩圖，因為它還有一個channel參數，就把通道分開了
hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])  # 彩圖 之 第0通道, 256束
hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])  # 彩圖 之 第1通道, 256束
hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])  # 彩圖 之 第2通道, 256束
hist_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])  # 灰階圖 之 第0通道, 256束

plt.subplot(133)
plt.plot(hist_b, color="b")
plt.plot(hist_g, color="g")
plt.plot(hist_r, color="r")
plt.plot(hist_gray, color="gray")
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖各分量與灰階的直方圖")

plt.show()

print("測試 09 calcHist----------------------------------------------------------")  # 60個

# 使用 mask 繪製直方圖

# 檔案 => cv2影像
image = cv2.imread(filename)
print("形狀 :", image.shape)
print("大小 :", image.size)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image.shape, np.uint8)
# 修改mask
offset = 50
mask[offset : 480 - offset, offset : 640 - offset] = 255  # 白色 前y 後 x

image_mask = cv2.bitwise_and(image, mask)

# 原圖之統計數據
hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])

# 原圖+mask後之統計數據
hist_image_mask = cv2.calcHist([image], [0], mask[:, :, 0], [256], [0, 256])

# 應該等同於上面數據
offset = 50
hist_mask = cv2.calcHist(
    [image_mask[offset : 480 - offset, offset : 640 - offset]],
    [0],
    None,
    [256],
    [0, 256],
)

plt.figure(figsize=(16, 8))

plt.subplot(231)
plt.imshow(image[:, :, ::-1])
plt.title("原圖")

plt.subplot(232)
plt.imshow(mask)
plt.title("mask")

plt.subplot(233)
plt.imshow(image_mask[:, :, ::-1])
plt.title("原圖mask後")

plt.subplot(234)
plt.plot(hist_image, "r")
plt.plot(hist_image_mask, "g")  # 無掩膜和有掩膜的直方圖畫到一起
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.subplot(235)
plt.plot(hist_image_mask)  # 單獨劃出有掩膜的直方圖
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.subplot(236)
plt.plot(hist_mask)  # 單獨把mask部分圖像的直方圖畫出來，和上面的一模一樣
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.show()

print("------------------------------------------------------------")  # 60個
print("測試 10 equalizeHist----------------------------------------------------------")  # 60個

plt.figure(
    num="直方圖均衡化處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 影像分析工具
# 影像直方圖

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.subplot(221)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image.ravel(), num_bins, [0, 256], color="r")
plt.title("原圖轉灰階")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("影像直方圖")

# 直方圖均衡化處理

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
equa = cv2.equalizeHist(image)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(223)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(equa.ravel(), num_bins, [0, 256], color="g")
plt.title("原圖轉灰階")

# 均值化的影像
# 均衡化後的灰度直方圖分布
plt.subplot(224)
plt.imshow(cv2.cvtColor(equa, cv2.COLOR_BGR2RGB))
plt.title("均衡化後的灰度直方圖分布")

plt.show()

print("測試 11 equalizeHist------------------------------------------------------------")  # 60個

plt.figure(
    num="直方圖均衡化處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(image)  # 直方圖均衡化處理, 只能處理灰階圖

# -----------顯示均衡化前後的直方圖---------------
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("均衡化之圖")

# -----------顯示均衡化前後的直方圖---------------

plt.subplot(223)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image.ravel(), num_bins, color="r") #拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖的直方圖")

plt.subplot(224)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(equ.ravel(), num_bins, color="g") #拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("均衡化之圖的直方圖")

plt.show()

print("測試 12 equalizeHist------------------------------------------------------------")  # 60個

plt.figure(
    num="直方圖均衡化處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(image)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(121)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image.ravel(), num_bins, color="r") #拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(122)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(equ.ravel(), num_bins, color="g") #拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print("測試 13 equalizeHist----------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(image_gray)  # 直方圖均衡化處理, 只能處理灰階圖

plt.figure(figsize=(16, 8))
plt.subplot(221)
plt.imshow(image[:, :, ::-1])

plt.subplot(222)
plt.imshow(image_gray, cmap="gray")

plt.subplot(223)
plt.imshow(equ, cmap="gray")

plt.subplot(224)
plt.imshow(equ, cmap="gray_r")

plt.show()

# ----------------------直方圖對比----------------

hist_image_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])  # 生成灰度圖像的直方圖
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])  # 生成均衡化後的圖像的直方圖

plt.figure(figsize=(16, 12))
plt.subplot(221)
plt.plot(hist_image_gray)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(222)
plt.plot(hist_equ)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(223)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image_gray.ravel(), num_bins, color="r")#拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(224)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(equ.ravel(), num_bins, color="r")#拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print("測試 14 equalizeHist----------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉成灰階
equ = cv2.equalizeHist(image)  # 直方圖均衡化處理, 只能處理灰階圖

# 繪製結果
fig = plt.figure(
    num="直方圖均衡化處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

plt.show()

print("測試 15 calcHist equalizeHist----------------------------------------------------------")  # 60個

"""
opencv之影像直方圖均衡化 直方圖均衡化處理 cv2.equalizeHist

函数原型：cv2.calcHist(image,channels,mask,histSize,ranges)
image为待计算直方图的图像，需用[]包裹
channels指定待计算直方图的图像的哪一通道用来计算直方图，RGB图像可以指定[0,1,2]，灰度图像只有[0],需用[]包裹,
mask为掩码，可以指定图像的范围，如果是全图，默认为none
hitsize为直方图的灰度级数，例如[0,255]一共256级，故参数为256，需用[]包裹
range为像素值范围，为[0,255]
返回值为hist，直方图
"""

# 檔案 => cv2影像 => 灰階
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.figure(
    num="histogram",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# 法一: 用plt.plot畫圖
plt.plot(hist, "r")
plt.title("用plot")

# 法二: 用 plot 或 bar 顯示 calcHist 的結果

plt.subplot(232)
# plt.plot(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
plt.plot(np.arange(0, 256), hist.ravel())  # 數值直接顯示
plt.title("用plot")

plt.subplot(233)
# plt.bar(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
plt.bar(np.arange(0, 256), hist.ravel())  # 數值直接顯示
plt.title("用bar")

# 法三: 用plt.hist()畫圖
plt.subplot(234)
num_bins = 256  # 直方圖顯示時的束數
plt.hist(image.ravel(), num_bins, [0, 256], color="b")
plt.title("用hist")

"""
三、直方圖均衡化
影像的直方圖是對影像對比度效果上的一種處理，旨在使得影像整體效果均勻，黑與白之間的各個畫素級之間的點更均勻一點。 
通過這種方法，亮度可以更好地在直方圖上分佈。這樣就可以用於增強區域性的對比度而不影響整體的對比度，直方圖均衡化通過有效地擴充套件常用的亮度來實現這種功能。
這種方法對於背景和前景都太亮或者太暗的影像非常有用，這種方法尤其是可以帶來X光影像中更好的骨骼結構顯示以及曝光過度或者曝光不足照片中更好的細節。
利用
cv2.equalizeHist(img)，將要均衡化的原影像【要求是灰度影像】作為引數傳入，則返回值即為均衡化後的影像。
"""

plt.subplot(235)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image2 = cv2.equalizeHist(image)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(236)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
