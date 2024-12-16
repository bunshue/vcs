"""
影像分析工具 - 影像直方圖
cv2.calcHist()
cv2.equalizeHist()

用直方圖分析一張圖片的顏色組成

hist = cv2.calcHist(image, channels, mask, histSize, ranges, accumulate) 函數統計直方圖
參數都要加［］括起來
image：原圖像
channels：如果輸入的圖像是灰度圖，它的值就是[0]，如果是彩色圖像，傳入的參數可以是[0]、[1]、[2],分布對應著b,g,r。
mask：掩膜圖像。要統計整幅圖像的直方圖就把這個參數設為None，如果要統計掩膜部分的圖像的直方圖，就需要這個參數。
histSize：bins的個數,就是分多少個組距。例如[256]或者[16]，都要用方括號括起來。
ranges：像素值範圍，通常為[0, 256]
accumulate：累計(累積、疊加)標識，默認值是False。
這個函數返回的對象hist是一個一維數組，數組內的元素是各個灰度級的像素個數。

https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

plt.hist(image,ravel(), hitsizes, ranges, color)

img.ravel() 將原圖像的array數組轉成一維的數組
hitsizes 為直方圖的灰度級數
ranges 為灰度範圍[0,255]
color 是參數，需要使用color=''來指定顏色

plt.hist(image.ravel(), num_bins, [0, 256], log = True)
這邊使用到 matplotlib.pyplot 的 hist，它接受一組資料，計算清單中各值出現的次數，上面的範例
透過 NumPy 陣列的 ravel 方法，取得圖片攤平後的資料（只是個 NumPy 視圖）
，hist 的第二個參數指定要切出幾個直條，第三個參數指定要計算的值範圍，log 指定了是否 y 軸是否使用對數結果顯示。

OpenCV 本身也有計算直方圖資料的函式 cv2.calcHist，而且是專門針對圖片進行計算，它的參數有：

    images：一組要分析的圖片。
    channels：要分析的頻道，若是灰階圖片就指定 [0]，若是彩色圖片，可分別使用 [0]、[1]、[2] 指定 BGR 頻道。
    mask：圖片遮罩，預設為 None。
    histSize：各頻道要切分出幾個直條。
    ranges：要計算的像素值範圍，通常都是設為 [0, 256]。

計算出來的資料，可以直接透過 matplotlib.pyplot 的 plot 繪製折線圖，或者是透過 bar 繪製直條圖。

image0 原圖 彩圖
image1 灰階
image2 遮罩過後
"""
import cv2

# 測試圖片
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"
filename = "data/pic_brightness1.bmp"
filename = "data/pic_brightness2.bmp"
filename = "data/pic_brightness3.bmp"
filename = "data/pic_calcHist.jpg"
filename = "C:/_git/vcs/_4.python/opencv\data/pic_gray_400X400_100-200.png"

num_bins = 256  # 直方圖顯示時的束數

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
'''
filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"  # 560X400

print("一張彩圖")
print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.show()

print(
    "測試 01 ravel() 的用法----------------------------------------------------------"
)  # 60個

print("一張彩圖的RGB與灰度的統計資料1")

print("直接把影像的 灰階值 或 RGB值 用直方圖統計出來")

plt.figure(
    num="原圖的直方圖 RGB值 3通道分開畫",
    figsize=(16, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("灰階")

plt.subplot(223)
b, g, r = cv2.split(image0)
bb = b.ravel()  # 拉成一維
gg = g.ravel()  # 拉成一維
rr = r.ravel()  # 拉成一維
plt.hist(bb, num_bins, [0, 256], color="b", label="B", alpha=0.5)
plt.hist(gg, num_bins, [0, 256], color="g", label="G", alpha=0.5)
plt.hist(rr, num_bins, [0, 256], color="r", label="R", alpha=1.0)

cc = image1.ravel()  # 拉成一維
plt.hist(cc, num_bins, [0, 256], color="gray", label="灰階", alpha=0.5)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.title("原圖的直方圖 RGB值 3通道分開畫")

# plt.title("灰階後的直方圖 灰階值 變成1通道")

print("使用 calcHist")

# image1 灰階影像
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
print(hist.shape)
print(hist.size)

plt.subplot(224)
plt.plot(hist, color="b", label="plot", lw=2)
plt.plot(np.arange(0, 256), hist.ravel(), color="gold", label="plot", lw=2)  # 同上
plt.bar(np.arange(0, 256), hist.ravel(), color="gray", label="bar", lw=2)  # 要這麼寫
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.title("用 plot 和 bar 顯示 calcHist 的結果")

plt.show()

print("測試 03 calcHist----------------------------------------------------------")  # 60個

print("一張彩圖的RGB與灰度的統計資料2")

# 對於彩色的圖片，
# 可以用 OpenCV 的 calcHist 函數分別計算統計值，
# 並畫出 RGB 三種顏色的分佈圖

print("彩圖 image0")
# 檔案 => cv2影像(彩圖)
image0 = cv2.imread(filename)

# ---------使用cv2.calcHist()函數繪圖----
# 這個函數可以傳入彩圖，因為它還有一個channel參數，就把通道分開了
# 計算直方圖每個 bin 的數值, 將彩圖的RGB通道分離出來

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# RGB畫在一起
# 使用 ravel 將所有的像素資料轉為一維的陣列
plt.hist(image0.ravel(), num_bins, [0, 256], color="gray", alpha=0.3, density=False)
# plt.hist(image0.ravel(), bins = num_bins, color="gray", alpha = 0.3, density=False)

# RGB分開畫
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.ylim(0, 8000)  # 設定 y 軸座標範圍
plt.legend(loc="best")

plt.show()

print("測試 04 calcHist----------------------------------------------------------")  # 60個

print("一張彩圖的RGB與灰度的統計資料3 使用mask")
print("使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階")

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image1.shape, np.uint8)

H = image1.shape[0]
W = image1.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

"""顯示原圖與mask
plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB), "gray")
plt.subplot(122)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")
plt.show()
"""

# 灰階 全圖
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])

# 灰階 部分圖
hist2 = cv2.calcHist([image1], [0], mask, [256], [0, 256])

plt.plot(hist1, "r", label="全圖", lw=3)
plt.plot(hist2, "g", label="部分圖", lw=2)

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

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image1.shape, np.uint8)

H = image1.shape[0]
W = image1.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(image1, image1, mask=mask)

# 以原圖計算直方圖
# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_full = cv2.calcHist([image1], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([image1], [0], mask, [256], [0, 256])

# 繪製結果
plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(223)
plt.imshow(cv2.cvtColor(masked_gray, cv2.COLOR_BGR2RGB), "gray")

plt.subplot(224)
plt.plot(hist_full, "r", label="全圖", lw=3)
plt.plot(hist_mask, "g", label="部分圖", lw=2)

plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.legend(loc="best")

plt.show()

print(
    "測試 06 將一圖分解成 藍 綠 紅 三通道------------------------------------------------------------"
)  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

cut = 50

b, g, r = cv2.split(image0)

rr = r[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
# plt.show()

rrr = rr.reshape(rr.shape[0] * rr.shape[1], 1)
# print(rrr.shape)
rrr = rrr[0 : len(rrr) : 5]
plt.hist(rrr, num_bins, color="r", label="R", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
# plt.show()

ggg = gg.reshape(gg.shape[0] * gg.shape[1], 1)
# print(ggg.shape)
plt.hist(ggg, num_bins, color="g", label="G", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

bb = b[cut : (480 - cut * 2), cut : (640 - cut * 2)]
# plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
# plt.show()

bbb = bb.reshape(bb.shape[0] * bb.shape[1], 1)
# print(bbb.shape)
plt.hist(bbb, num_bins, color="b", label="B", alpha=0.5)  # alpha調整透明度 給多個直方圖畫在一起用

plt.legend(loc="best")

plt.show()

print("測試 07 calcHist----------------------------------------------------------")  # 60個

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

print("灰階 image1")
# 轉灰階
image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(16, 8))

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_gray = cv2.calcHist([image1], [0], None, [256], [0, 256])

plt.plot(hist_gray, color="gray", label="灰", lw=3)
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)

plt.plot(hist_gray, color="gray")
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖各分量與灰階的直方圖")
plt.legend(loc="best")

plt.show()

print("測試 08 calcHist----------------------------------------------------------")  # 60個

# 使用 mask 繪製直方圖

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

# 建立圖形遮罩, 一樣大小, 黑色
mask = np.zeros(image0.shape, np.uint8)

H = image0.shape[0]
W = image0.shape[1]

# 修改mask
BORDER = 50
mask[BORDER : H - BORDER, BORDER : W - BORDER] = 255  # 白色 先h 後 w

image_mask = cv2.bitwise_and(image0, mask)

# 生成圖像之直方圖, 256束, 彩圖之第0通道
hist_b = cv2.calcHist([image0], [0], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第1通道
hist_g = cv2.calcHist([image0], [1], None, [256], [0, 256])
# 生成圖像之直方圖, 256束, 彩圖之第2通道
hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])

# 原圖+mask後之統計數據
hist_image_mask0 = cv2.calcHist([image0], [0], mask[:, :, 0], [256], [0, 256])
# 原圖+mask後之統計數據
hist_image_mask1 = cv2.calcHist([image0], [1], mask[:, :, 0], [256], [0, 256])
# 原圖+mask後之統計數據
hist_image_mask2 = cv2.calcHist([image0], [2], mask[:, :, 0], [256], [0, 256])

plt.figure(figsize=(16, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_mask, cv2.COLOR_BGR2RGB))  # 原圖
plt.title("原圖mask後")

plt.subplot(223)
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color="r", label="R", lw=3)
plt.plot(hist_g, color="g", label="G", lw=2)
plt.plot(hist_b, color="b", label="B", lw=1)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(224)
# 畫出 B 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask0, "b")  # 無掩膜和有掩膜的直方圖畫到一起
# 畫出 G 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask1, "g")  # 無掩膜和有掩膜的直方圖畫到一起
# 畫出 R 通道 遮罩後的 分佈圖
plt.plot(hist_image_mask2, "r")  # 無掩膜和有掩膜的直方圖畫到一起
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print("測試 09 calcHist----------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

# 將image0 依據RGB三通道分離到一個三維矩陣
bgr_planes = cv2.split(image0)

hist_r = cv2.calcHist([image0], [2], None, [256], [0, 256])
histRange = (0, 256)  # the upper boundary is exclusive
accumulate = False

histSize = 256
# 生成圖像之直方圖, 256束, B bgr_planes 之 第0通道
b_hist = cv2.calcHist(
    bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate
)

# 生成圖像之直方圖, 256束, G bgr_planes 之 第1通道
g_hist = cv2.calcHist(
    bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate
)

# 生成圖像之直方圖, 256束, R bgr_planes 之 第2通道
r_hist = cv2.calcHist(
    bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate
)

## [Draw the histograms for B, G and R]
hist_w = 512
hist_h = 400
bin_w = int(round(hist_w / histSize))

histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
## [Draw the histograms for B, G and R]

## [Normalize the result to ( 0, histImage.rows )]
cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
## [Normalize the result to ( 0, histImage.rows )]

## [Draw for each channel]
for i in range(1, histSize):
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(b_hist[i - 1])),
        (bin_w * (i), hist_h - int(b_hist[i])),
        (255, 0, 0),
        thickness=2,
    )
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(g_hist[i - 1])),
        (bin_w * (i), hist_h - int(g_hist[i])),
        (0, 255, 0),
        thickness=2,
    )
    cv2.line(
        histImage,
        (bin_w * (i - 1), hist_h - int(r_hist[i - 1])),
        (bin_w * (i), hist_h - int(r_hist[i])),
        (0, 0, 255),
        thickness=2,
    )
## [Draw for each channel]

plt.subplot(121)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(histImage, cv2.COLOR_BGR2RGB))
plt.title("均衡化之圖")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print(
    "測試 10 equalizeHist----------------------------------------------------------"
)  # 60個

plt.figure(
    num="直方圖均衡化處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.subplot(221)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖轉灰階")

plt.subplot(222)
plt.hist(image1.ravel(), num_bins, [0, 256], color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖的影像直方圖")

# 直方圖均衡化處理

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(223)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("均衡化之圖")

# 均值化的影像
# 均衡化後的灰度直方圖分布
plt.subplot(224)
plt.title("均衡化後的直方圖分布")
plt.hist(equ.ravel(), num_bins, [0, 256], color="g")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print(
    "測試 13 equalizeHist----------------------------------------------------------"
)  # 60個

print("彩圖 image0")
# 檔案 => cv2影像
image0 = cv2.imread(filename)

# 轉灰階
image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)

equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.figure(figsize=(16, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))  # 原圖

plt.subplot(222)
plt.imshow(image1, cmap="gray")

plt.subplot(223)
plt.imshow(equ, cmap="gray")

plt.subplot(224)
plt.imshow(equ, cmap="gray_r")

plt.show()

# ----------------------直方圖對比----------------

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist_image1 = cv2.calcHist([image1], [0], None, [256], [0, 256])

hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])  # 生成均衡化後的圖像的直方圖

plt.figure(figsize=(16, 12))
plt.subplot(221)
plt.plot(hist_image1)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(222)
plt.plot(hist_equ)
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(223)
plt.hist(image1.ravel(), num_bins, color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.subplot(224)
plt.hist(equ.ravel(), num_bins, color="r")  # 拉成一維
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍

plt.show()

print(
    "測試 14 equalizeHist----------------------------------------------------------"
)  # 60個

# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

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
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

plt.show()

print(
    "測試 15 calcHist equalizeHist----------------------------------------------------------"
)  # 60個

"""
opencv之影像直方圖均衡化 直方圖均衡化處理 cv2.equalizeHist

函數原型：cv2.calcHist(image,channels,mask,histSize,ranges)
image為待計算直方圖的圖像，需用[]包裹
channels指定待計算直方圖的圖像的哪一通道用來計算直方圖，RGB圖像可以指定[0,1,2]，灰度圖像只有[0],需用[]包裹,
mask為掩碼，可以指定圖像的範圍，如果是全圖，默認為none
hitsize為直方圖的灰度級數，例如[0,255]一共256級，故參數為256，需用[]包裹
range為像素值範圍，為[0,255]
返回值為hist，直方圖
"""

print("灰階 image1")
# 檔案 => cv2影像 => 灰階
image1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

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

# 生成圖像之直方圖, 256束, 灰階圖只有第0通道
hist = cv2.calcHist([image1], [0], None, [256], [0, 256])


# 法一: 用plt.plot畫圖
plt.plot(hist, "r")
plt.title("用plot")

# 法二: 用 plot 或 bar 顯示 calcHist 的結果

plt.subplot(232)
plt.plot(np.arange(0, 256), hist.ravel())  # 拉成一維 並畫出
plt.title("用plot")

plt.subplot(233)
plt.bar(np.arange(0, 256), hist.ravel())  # 拉成一維 並畫出
plt.title("用bar")

# 法三: 用plt.hist()畫圖
plt.subplot(234)
plt.hist(image1.ravel(), num_bins, [0, 256], color="b")  # 拉成一維
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
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image2 = cv2.equalizeHist(image1)  # 直方圖均衡化處理, 只能處理灰階圖

plt.subplot(236)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("直方圖均衡化處理")

plt.show()

print("------------------------------------------------------------")  # 60個
'''
ESC = 27

print("------------------------------------------------------------")  # 60個

print("把 直方圖均衡化處理 套用在webcam上 黑白")
print("把 直方圖均衡化處理 套用在webcam上 彩色")

video_filename = "D:/內視鏡影片/NBI錄影_V20241009_081309.mp4"
#cap = cv2.VideoCapture(video_filename)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    cut = 80

    #畫一些標記
    dd = 5
    topLeft = (cut-dd, cut-dd)
    bottomRight = (640-cut+dd, 480-cut+dd)

    cv2.rectangle(frame, topLeft, bottomRight, 255, 2)

    # 原圖
    cv2.imshow("Original", frame)

    # 裁切圖片 ST
    # 裁切區域的 x 與 y 座標（左上角）
    x_st, y_st = cut, cut
    # 裁切區域的長度與寬度
    w, h = 640 - x_st * 2, 480 - y_st * 2
    frame2 = frame[y_st : y_st + h, x_st : x_st + w]
    frame3 = frame2
    # 裁切圖片 SP

    gray1 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Gray", gray1)

    gray2 = cv2.equalizeHist(gray1)
    cv2.imshow("Histogram1", gray2)
    # 裁切圖片 SP

    b, g, r = cv2.split(frame3)

    bb = cv2.equalizeHist(b)
    gg = cv2.equalizeHist(g)
    rr = cv2.equalizeHist(r)

    frame3 = cv2.merge([bb, gg, rr])

    cv2.imshow("Histogram2", frame3)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# plt.hist 參數
# plt.hist(cc, bins=num_bins, color="g", alpha=0.5, density=False)
# density=True   #以密度表示
