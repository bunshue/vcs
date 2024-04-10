"""

用直方圖分析一張圖片的顏色組成

hist = cv2.calcHist(img, channels, mask, histSize, ranges, accumulate) 函數統計直方圖
參數都要加［］括起來
img：原圖像
channels：如果輸入的圖像是灰度圖，它的值就是[0]，如果是彩色圖像，傳入的參數可以是[0]、[1]、[2],分布對應著b,g,r。
mask：掩膜圖像。要統計整幅圖像的直方圖就把這個參數設為None，如果要統計掩膜部分的圖像的直方圖，就需要這個參數。
histSize：bins的個數,就是分多少個組距。例如[256]或者[16]，都要用方括號括起來。
ranges：像素值范圍，通常為[0, 256]
accumulate：累計(累積、疊加)標識，默認值是False。
這個函數返回的對象hist是一個一維數組，數組內的元素是各個灰度級的像素個數。

https://blog.gtwang.org/programming/python-opencv-matplotlib-plot-histogram-tutorial/
https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html

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

import cv2

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("測試 01----------------------------------------------------------")  # 60個

#對於彩色的圖片，
#可以用 OpenCV 的 calcHist 函數分別計算統計值，
#並畫出 RGB 三種顏色的分佈圖：

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
filename = 'pic.bmp'

image = cv2.imread(filename)	#讀取本機圖片

# 計算直方圖每個 bin 的數值
hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])

# RGB畫在一起
# 使用 ravel 將所有的像素資料轉為一維的陣列
# 畫出直方圖
num_bins = 64  # 直方圖顯示時的束數
plt.hist(image.ravel(), 64, [0, 256], color="gray")
#plt.hist(image.ravel(), bins = num_bins, color="lime", alpha = 0.3, density=False)

# RGB分開畫
# 畫出 RGB 三種顏色的分佈圖
plt.plot(hist_r, color = 'r')
plt.plot(hist_g, color = 'g')
plt.plot(hist_b, color = 'b')

plt.xlim([0 - 10, 256 + 10])

plt.show()

print('測試 02----------------------------------------------------------')	#60個

filename = 'data/pic_brightness1.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'r', label="b1")
plt.plot(histg, 'r', label="g1")
plt.plot(histr, 'r', label="r1")

filename = 'data/pic_brightness2.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'g', label="b2")
plt.plot(histg, 'g', label="g2")
plt.plot(histr, 'g', label="r2")



filename = 'data/pic_brightness3.bmp'

image = cv2.imread(filename)
print(image.shape)

histb = cv2.calcHist([image], [0], None, [256], [0, 256])
histg = cv2.calcHist([image], [1], None, [256], [0, 256])
histr = cv2.calcHist([image], [2], None, [256], [0, 256])

plt.plot(histb, 'b', label="b3")
plt.plot(histg, 'b', label="g3")
plt.plot(histr, 'b', label="r3")

plt.legend(loc="best")
plt.xlim([0 - 10, 256 + 10])
plt.ylim([0, 4000])

plt.show()

print('測試 03----------------------------------------------------------')	#60個

print('使用mask, 因為目前mask只能用1維的 所以圖片要先轉成灰階')

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = 'data/pic_brightness1.bmp'

image = cv2.imread(filename)
print(image.shape)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(image.shape)

mask = np.zeros(image.shape, np.uint8)
print(image.shape)
print(mask.shape)
H = image.shape[0]
W = image.shape[1]
border = 20

mask[border : H - border * 2, border : W - border * 2] = 255

#全圖
hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])

#部分圖
hist2 = cv2.calcHist([image], [0], mask, [256], [0, 256])

plt.plot(hist1, 'r', label="全圖")
plt.plot(hist2, 'g', label="部分圖")

plt.legend(loc="best")

plt.show()

print('測試 04----------------------------------------------------------')	#60個

plt.figure(num = '配合圖形遮罩計算直方圖', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

image = cv2.imread(filename)	#讀取本機圖片

# 轉為灰階圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 建立圖形遮罩
mask = np.zeros(gray.shape, np.uint8)
#mask[300:780, 300:1620] = 255
W = 640
H = 480
x_st = int(W / 4)
y_st = int(H / 4)
w = int(W / 2)
h = int(H / 2)

mask[y_st : y_st + h, x_st : x_st + w] = 255    #先h 後 w
#mask[0:240, 0:320] = 255

# 計算套用遮罩後的圖形
masked_gray = cv2.bitwise_and(gray, gray, mask = mask)

# 以原圖計算直方圖
hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])

# 以套用遮罩後的圖計算直方圖
hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])

# 繪製結果
plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(222)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(223)
plt.imshow(cv2.cvtColor(masked_gray, cv2.COLOR_BGR2RGB), 'gray')

plt.subplot(224)
plt.plot(hist_full)
plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

print('測試 05----------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'


plt.figure(num = '影像分析工具 影像直方圖', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#影像分析工具
#影像直方圖

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

plt.subplot(221)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('原圖轉灰階')

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('影像直方圖')

print('測試 06------------------------------------------------------------')	#60個


#直方圖影像操作
#直方圖均值化

import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
equa = cv2.equalizeHist(image)

plt.subplot(223)
plt.hist(equa.ravel(), 256, [0,256])
plt.title('原圖轉灰階')

#均值化的影像
#均衡化後的灰度直方圖分布
plt.subplot(224)
plt.imshow(cv2.cvtColor(equa, cv2.COLOR_BGR2RGB))
plt.title('均衡化後的灰度直方圖分布')

plt.show()

print('測試 07------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
filename = 'pic.bmp'

image = cv2.imread(filename)

print('形狀1 :', image.shape)
print('大小1 :', image.size)

print('拉成一維')
image2 = image.ravel()

print('形狀2 :', image2.shape)
print('大小2 :', image2.size)

num_bins = 64  # 直方圖顯示時的束數
plt.hist(image2, bins = num_bins, color="lime", alpha = 0.3, density=False)
#density=True   #以密度表示

plt.show()

print('測試 08------------------------------------------------------------')	#60個

plt.figure(num = '影像分析工具 影像直方圖 均衡化效果比較', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#-----------讀取原始圖像---------------
image = cv2.imread('images/equ.bmp',cv2.IMREAD_GRAYSCALE)
#-----------直方圖均衡化處理---------------
equ = cv2.equalizeHist(image)
#-----------顯示均衡化前后的直方圖---------------
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

plt.subplot(222)
plt.imshow(cv2.cvtColor(equ, cv2.COLOR_BGR2RGB))
plt.title('均衡化之圖')

#-----------顯示均衡化前后的直方圖---------------

plt.subplot(223)
plt.hist(image.ravel(), 64)
plt.xlim(0, 256) # 設定 x 軸座標範圍
plt.title("原圖之直方圖")

plt.subplot(224)
plt.hist(equ.ravel(), 64)
plt.xlim(0, 256) # 設定 x 軸座標範圍
plt.title("均衡化之圖的直方圖")

plt.show()

print('測試 09------------------------------------------------------------')	#60個

plt.figure(num = 'subplot示例', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

image = cv2.imread('images/equ.bmp', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(image)

plt.subplot(121)
plt.hist(image.ravel(), 256)

plt.subplot(122)
plt.hist(equ.ravel(), 256)

plt.show()

print('測試 10------------------------------------------------------------')	#60個

plt.figure(num = '將一圖分解成 藍 綠 紅 三通道', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb256X300.bmp'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'
filename = 'data/pic_brightness1.bmp'

image = cv2.imread(filename)


cut = 50
num_bins = 50  # 直方圖顯示時的束數

b, g, r = cv2.split(image)

bb = b[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(bb, cv2.COLOR_BGR2RGB))
#plt.show()

bbb = bb.reshape(bb.shape[0]*bb.shape[1], 1)
#print(bbb.shape)
plt.hist(bbb, num_bins, color="b", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

gg = g[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(gg, cv2.COLOR_BGR2RGB))
#plt.show()

ggg = gg.reshape(gg.shape[0]*gg.shape[1], 1)
#print(ggg.shape)
plt.hist(ggg, num_bins, color="g", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

rr = r[cut:(480-cut*2), cut:(640-cut*2)]
#plt.imshow(cv2.cvtColor(rr, cv2.COLOR_BGR2RGB))
#plt.show()

rrr = rr.reshape(rr.shape[0]*rr.shape[1], 1)
#print(rrr.shape)
rrr = rrr[0:len(rrr):5]
plt.hist(rrr, num_bins, color="r", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用

plt.show()

print('測試 11----------------------------------------------------------')	#60個

img0 = cv2.imread(filename)  # 原圖, 彩色
img1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 原圖, 彩色轉灰階

plt.subplot(131)
plt.imshow(cv2.cvtColor(img0, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.hist(img1.ravel(), 256, [0, 256], log = True)

plt.show()

"""
plt.hist(img.ravel(), 256, [0, 256], log = True)
這邊使用到 matplotlib.pyplot 的 hist，它接受一組資料，計算清單中各值出現的次數，上面的範例
透過 NumPy 陣列的 ravel 方法，取得圖片攤平後的資料（只是個 NumPy 視圖）
，hist 的第二個參數指定要切出幾個直條，第三個參數指定要計算的值範圍，log 指定了是否 y 軸是否使用對數結果顯示。
"""

print('測試 12----------------------------------------------------------')	#60個


"""
OpenCV 本身也有計算直方圖資料的函式 cv2.calcHist，而且是專門針對圖片進行計算，它的參數有：

    images：一組要分析的圖片。
    channels：要分析的頻道，若是灰階圖片就指定 [0]，若是彩色圖片，可分別使用 [0]、[1]、[2] 指定 BGR 頻道。
    mask：圖片遮罩，預設為 None。
    histSize：各頻道要切分出幾個直條。
    ranges：要計算的像素值範圍，通常都是設為 [0, 256]。

計算出來的資料，可以直接透過 matplotlib.pyplot 的 plot 繪製折線圖，或者是透過 bar 繪製直條圖。

"""

filename = 'C:/_git/vcs/_4.python/_data/tiger.jpg'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

print('用 plot 或 bar 顯示 calcHist 的結果')

plt.plot(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
#plt.plot(np.arange(0, 256), hist.ravel())  # 數值直接顯示

#plt.bar(np.arange(0, 256), np.log(hist.ravel()))  # 數值取log
#plt.bar(np.arange(0, 256), hist.ravel())  # 數值直接顯示

plt.show()

print("測試 13----------------------------------------------------------")  # 60個

# 用hist()和cv2.calcHist()函數繪制直方圖

filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"

img = cv2.imread(filename)  # img.shape返回(576, 720, 3)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用hist()函數繪圖---
# 注意：用這個函數畫圖像直方圖時一定要用灰度圖像，如果非用彩圖，那得按通道畫，不然沒有什么意義
plt.figure(figsize=(16, 8))

plt.subplot(131)
plt.imshow(img[:, :, ::-1])  # 原圖
plt.title("原圖")

plt.subplot(132)
num_bins = 64  # 直方圖顯示時的束數
plt.hist(img_gray.ravel(), num_bins)  # 將灰度級劃分為 num_bins 個等級
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖轉灰階後的灰度直方圖")

# ---------使用cv2.calcHist()函數繪圖----這個函數可以傳入彩圖，因為它還有一個channel參數，就把通道分開了
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])  # 彩圖 之 第0通道, 256束
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])  # 彩圖 之 第1通道, 256束
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])  # 彩圖 之 第2通道, 256束
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])  # 灰階圖 之 第0通道, 256束

plt.subplot(133)
plt.plot(hist_b, color="b")
plt.plot(hist_g, color="g")
plt.plot(hist_r, color="r")
plt.plot(hist_gray, color="gray")
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("原圖各分量與灰階的直方圖")

plt.show()

print("測試 14----------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"

# 使用 mask 繪製直方圖

img = cv2.imread(filename)
print(img.shape)

# 做一個一樣大小的mask 黑色
mask = np.zeros(img.shape, np.uint8)
# 修改mask
offset = 50
mask[offset : 480 - offset, offset : 640 - offset] = 255  # 白色 前y 後 x
img_mask = cv2.bitwise_and(img, mask)

# 原圖之統計數據
hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])

# 原圖+mask後之統計數據
hist_img_mask = cv2.calcHist([img], [0], mask[:, :, 0], [256], [0, 256])

# 應該等同於上面數據
offset = 50
hist_mask = cv2.calcHist(
    [img_mask[offset : 480 - offset, offset : 640 - offset]], [0], None, [256], [0, 256]
)

plt.figure(figsize=(16, 8))

plt.subplot(231)
plt.imshow(img[:, :, ::-1])
plt.title("原圖")

plt.subplot(232)
plt.imshow(mask)
plt.title("mask")

plt.subplot(233)
plt.imshow(img_mask[:, :, ::-1])
plt.title("原圖mask後")

plt.subplot(234)
plt.plot(hist_img, "r")
plt.plot(hist_img_mask, "g")  # 無掩膜和有掩膜的直方圖畫到一起
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.subplot(235)
plt.plot(hist_img_mask)  # 單獨劃出有掩膜的直方圖
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.subplot(236)
plt.plot(hist_mask)  # 單獨把mask部分圖像的直方圖畫出來，和上面的一模一樣
plt.xlim(0 - 10, 256 + 10)  # 設定 x 軸座標範圍
plt.title("")

plt.show()

print("測試 15----------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_4.python/_data/ims01.bmp"

# 例13.3 實現圖像均衡化處理

img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# -----------------------圖像均衡化處理----------------
equ = cv2.equalizeHist(img_gray)

plt.figure(figsize=(16, 8))
plt.subplot(221)
plt.imshow(img[:, :, ::-1])

plt.subplot(222)
plt.imshow(img_gray, cmap="gray")

plt.subplot(223)
plt.imshow(equ, cmap="gray")

plt.subplot(224)
plt.imshow(equ, cmap="gray_r")

plt.axis("off")  # cmap和axis小知識點

plt.show()

# ----------------------直方圖對比----------------
print("aaaa")
hist_img_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])  # 生成灰度圖像的直方圖
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])  # 生成均衡化后的圖像的直方圖

plt.figure(figsize=(16, 12))
plt.subplot(221)
plt.plot(hist_img_gray)

plt.subplot(222)
plt.plot(hist_equ)

plt.subplot(223)
plt.hist(img_gray.ravel(), 256)

plt.subplot(224)
plt.hist(equ.ravel(), 256)

plt.show()

print("測試 16----------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
