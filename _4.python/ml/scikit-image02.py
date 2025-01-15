"""
skimage : scikit-image SciKit (toolkit for SciPy)


"""

import skimage

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

"""
基本形態學濾波

對圖像進行形態學變換。變換對象一般為灰度圖或二值圖，功能函數放在morphology子模塊內。

1、膨脹（dilation)

原理：一般對二值圖像進行操作。找到像素值為1的點，將它的鄰近像素點都設置成這個值。1值表示白，0值表示黑，因此膨脹操作可以擴大白色值范圍，壓縮黑色值范圍。一般用來擴充邊緣或填充小的孔洞。

功能函數：skimage.morphology.dilation(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。
"""

img = skimage.data.checkerboard()

# 用邊長為5的正方形濾波器進行膨脹濾波
dst1 = skimage.morphology.dilation(img, skimage.morphology.square(5))

# 用邊長為15的正方形濾波器進行膨脹濾波
dst2 = skimage.morphology.dilation(img, skimage.morphology.square(15))

plt.figure("膨脹", figsize=(8, 8))
plt.subplot(131)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(132)
plt.title("白色膨脹1")
plt.imshow(dst1, plt.cm.gray)

plt.subplot(133)
plt.title("白色膨脹2")
plt.imshow(dst2, plt.cm.gray)

show()

"""

分別用邊長為5或15的正方形濾波器對棋盤圖片進行膨脹操作，結果如下：
可見濾波器的大小，對操作結果的影響非常大。一般設置為奇數。

除了正方形的濾波器外，濾波器的形狀還有一些，現列舉如下：

skimage.morphology.morphology.square: 正方形
skimage.morphology.disk:  平面圓形
skimage.morphology.ball: 球形
skimage.morphology.cube: 立方體形
skimage.morphology.diamond: 鉆石形
skimage.morphology.rectangle: 矩形
skimage.morphology.star: 星形
skimage.morphology.octagon: 八角形
skimage.morphology.octahedron： 八面體

注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_dilation(image, selem=None）

用此函數比處理灰度圖像要快。
"""
print("------------------------------------------------------------")  # 60個

"""
2、腐蝕（erosion)

函數：skimage.morphology.erosion(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

和膨脹相反的操作，將0值擴充到鄰近像素。擴大黑色部分，減小白色部分。可用來提取骨干信息，去掉毛刺，去掉孤立的像素。
"""

img = skimage.data.checkerboard()

# 用邊長為5的正方形濾波器進行膨脹濾波
dst1 = skimage.morphology.erosion(img, skimage.morphology.square(5))

# 用邊長為25的正方形濾波器進行膨脹濾波
dst2 = skimage.morphology.erosion(img, skimage.morphology.square(25))

plt.figure("腐蝕", figsize=(8, 8))
plt.subplot(131)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(132)
plt.title("白色腐蝕1")
plt.imshow(dst1, plt.cm.gray)

plt.subplot(133)
plt.title("白色腐蝕2")
plt.imshow(dst2, plt.cm.gray)

show()

"""
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：
skimage.morphology.binary_erosion(image, selem=None）
用此函數比處理灰度圖像要快。

"""
print("------------------------------------------------------------")  # 60個

"""
3、開運算（opening)

函數：skimage.morphology.openning(image, selem=None）
selem表示結構元素，用于設定局部區域的形狀和大小。
先腐蝕再膨脹，可以消除小物體或小斑塊。
"""

img = skimage.color.rgb2gray(skimage.io.imread("data/mor.bmp"))

# 用邊長為9的圓形濾波器進行膨脹濾波
dst = skimage.morphology.opening(img, skimage.morphology.disk(9))

plt.figure("morphology 開運算", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)
plt.axis("off")

plt.subplot(122)
plt.title("開運算")
plt.imshow(dst, plt.cm.gray)
plt.axis("off")

show()

"""
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_opening(image, selem=None）

用此函數比處理灰度圖像要快。
"""
print("------------------------------------------------------------")  # 60個

"""
4、閉運算（closing)

函數：skimage.morphology.closing(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

先膨脹再腐蝕，可用來填充孔洞。
"""

img = skimage.color.rgb2gray(skimage.io.imread("data/mor.bmp"))

# 用邊長為5的圓形濾波器進行膨脹濾波
dst = skimage.morphology.closing(img, skimage.morphology.disk(9))

plt.figure("morphology 閉運算", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)
plt.axis("off")

plt.subplot(122)
plt.title("閉運算")
plt.imshow(dst, plt.cm.gray)
plt.axis("off")

show()

"""
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_closing(image, selem=None）

用此函數比處理灰度圖像要快。

"""
print("------------------------------------------------------------")  # 60個

"""
5、白帽（white-tophat)

函數：skimage.morphology.white_tophat(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

將原圖像減去它的開運算值，返回比結構化元素小的白點
"""

img = skimage.color.rgb2gray(skimage.io.imread("data/mor.bmp"))
dst = skimage.morphology.white_tophat(img, skimage.morphology.square(21))

plt.figure("morphology 白帽", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)
plt.axis("off")

plt.subplot(122)
plt.title("白帽")
plt.imshow(dst, plt.cm.gray)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

"""
6、黑帽（black-tophat)

函數：skimage.morphology.black_tophat(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

將原圖像減去它的閉運算值，返回比結構化元素小的黑點，且將這些黑點反色。
"""

img = skimage.color.rgb2gray(skimage.io.imread("data/mor.bmp"))
dst = skimage.morphology.black_tophat(img, skimage.morphology.square(21))

plt.figure("morphology 黑帽", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)
plt.axis("off")

plt.subplot(122)
plt.title("黑帽")
plt.imshow(dst, plt.cm.gray)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

"""
高級濾波
本文提供更多更強大的濾波方法，這些方法放在filters.rank子模塊內。
這些方法需要用戶自己設定濾波器的形狀和大小，因此需要導入morphology模塊來設定。
"""
print("------------------------------------------------------------")  # 60個

"""
1、autolevel
這個詞在photoshop里面翻譯成自動色階，用局部直方圖來對圖片進行濾波分級。
該濾波器局部地拉伸灰度像素值的直方圖，以覆蓋整個像素值范圍。
格式：skimage.filters.rank.autolevel(image, selem）
selem表示結構化元素，用于設定濾波器。
"""

import skimage.filters.rank as sfr

# img =skimage.color.rgb2gray(skimage.data.lena())
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = skimage.io.imread(filename, True)  # True:轉為灰階

# 半徑為5的圓形濾波器
auto = sfr.autolevel(img, skimage.morphology.disk(5))

plt.figure("filters", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title("濾波")
plt.imshow(auto, plt.cm.gray)

show()

print("------------------------------------------------------------")  # 60個

"""
2、bottomhat 與 tophat

bottomhat: 此濾波器先計算圖像的形態學閉運算，然后用原圖像減去運算的結果值，有點像黑帽操作。
bottomhat: 此濾波器先計算圖像的形態學開運算，然后用原圖像減去運算的結果值，有點像白帽操作。

格式：

skimage.filters.rank.bottomhat(image, selem）
skimage.filters.rank.tophat(image, selem）

selem表示結構化元素，用于設定濾波器。

下面是bottomhat濾波的例子：
"""

"""沒有 bottomhat

import skimage.filters.rank as sfr

#img =skimage.color.rgb2gray(skimage.data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=skimage.io.imread(filename, True)   #True:轉為灰階

#半徑為5的圓形濾波器
auto =sfr.bottomhat(img, skimage.morphology.disk(5))

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('原圖')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('濾波')
plt.imshow(auto,plt.cm.gray)

show()
"""

"""
3、enhance_contrast
對比度增強。求出局部區域的最大值和最小值，然后看當前點像素值最接近最大值還是最小值，然后替換為最大值或最小值。
函數： enhance_contrast(image, selem）
selem表示結構化元素，用于設定濾波器。
"""

import skimage.filters.rank as sfr

# img = skimage.color.rgb2gray(skimage.data.lena())
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = skimage.io.imread(filename, True)  # True:轉為灰階

# 半徑為5的圓形濾波器
auto = sfr.enhance_contrast(img, skimage.morphology.disk(5))

plt.figure("filters", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title("濾波")
plt.imshow(auto, plt.cm.gray)

show()

"""
4、entropy

求局部熵，熵是使用基為2的對數運算出來的。該函數將局部區域的灰度值分布進行二進制編碼，返回編碼的最小值。

函數格式：entropy(image, selem）

selem表示結構化元素，用于設定濾波器。
"""

import skimage.filters.rank as sfr

# img = skimage.color.rgb2gray(skimage.data.lena())
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = skimage.io.imread(filename, True)  # True:轉為灰階

# 半徑為5的圓形濾波器
dst = sfr.entropy(img, skimage.morphology.disk(5))

plt.figure("filters", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title("濾波")
plt.imshow(dst, plt.cm.gray)

show()

"""
5、equalize
均衡化濾波。利用局部直方圖對圖像進行均衡化濾波。
函數格式：equalize(image, selem）
selem表示結構化元素，用于設定濾波器。
"""

import skimage.filters.rank as sfr

# img = skimage.color.rgb2gray(skimage.data.lena())
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = skimage.io.imread(filename, True)  # True:轉為灰階

# 半徑為5的圓形濾波器
dst = sfr.equalize(img, skimage.morphology.disk(5))

plt.figure("filters", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title("濾波")
plt.imshow(dst, plt.cm.gray)

show()

"""
6、gradient
返回圖像的局部梯度值（如：最大值-最小值），用此梯度值代替區域內所有像素值。
函數格式：gradient(image, selem）
selem表示結構化元素，用于設定濾波器。
"""

import skimage.filters.rank as sfr

# img = skimage.color.rgb2gray(skimage.data.lena())
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
img = skimage.io.imread(filename, True)  # True:轉為灰階

# 半徑為5的圓形濾波器
dst = sfr.gradient(img, skimage.morphology.disk(5))

plt.figure("filters", figsize=(8, 8))
plt.subplot(121)
plt.title("原圖")
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title("濾波")
plt.imshow(dst, plt.cm.gray)

show()

"""
7、其它濾波器

濾波方式很多，下面不再一一詳細講解，僅給出核心代碼，所有的函數調用方式都是一樣的。

最大值濾波器（maximum):返回圖像局部區域的最大值，用此最大值代替該區域內所有像素值。
dst =sfr.maximum(img, skimage.morphology.disk(5)) 

最小值濾波器（minimum)：返回圖像局部區域內的最小值，用此最小值取代該區域內所有像素值。
dst =sfr.minimum(img, skimage.morphology.disk(5))

均值濾波器（mean) : 返回圖像局部區域內的均值，用此均值取代該區域內所有像素值。
dst =sfr.mean(img, skimage.morphology.disk(5)) 

中值濾波器（median): 返回圖像局部區域內的中值，用此中值取代該區域內所有像素值。
dst =sfr.median(img, skimage.morphology.disk(5))

莫代爾濾波器（modal) : 返回圖像局部區域內的modal值，用此值取代該區域內所有像素值。
dst =sfr.modal(img, skimage.morphology.disk(5))

otsu閾值濾波（otsu): 返回圖像局部區域內的otsu閾值，用此值取代該區域內所有像素值。
dst =sfr.otsu(img, skimage.morphology.disk(5))

閾值濾波（threshhold): 將圖像局部區域中的每個像素值與均值比較，大于則賦值為1，小于賦值為0，得到一個二值圖像。
dst =sfr.threshold(img, skimage.morphology.disk(5)) 

減均值濾波（subtract_mean):  將局部區域中的每一個像素，減去該區域中的均值。
dst =sfr.subtract_mean(img, skimage.morphology.disk(5))

求和濾波（sum) :求局部區域的像素總和，用此值取代該區域內所有像素值。
dst =sfr.sum(img, skimage.morphology.disk(5))
"""

print("------------------------------------------------------------")  # 60個

"""
霍夫線變換

在圖片處理中，霍夫變換主要是用來檢測圖片中的幾何形狀，包括直線、圓、橢圓等。
在skimage中，霍夫變換是放在tranform模塊內，本篇主要講解霍夫線變換。
對于平面中的一條直線，在笛卡爾坐標系中，可用y=mx+b來表示，其中m為斜率，b為截距。
但是如果直線是一條垂直線，則m為無窮大，所有通常我們在另一坐標系中表示直線，
即極坐標系下的r=xcos(theta)+ysin(theta)。即可用（r,theta）來表示一條直線。
其中r為該直線到原點的距離，theta為該直線的垂線與x軸的夾角。如下圖所示。
對于一個給定的點（x0,y0), 我們在極坐標下繪出所有通過它的直線（r,theta)，
將得到一條正弦曲線。如果將圖片中的所有非0點的正弦曲線都繪制出來，則會存在一些交點。
所有經過這個交點的正弦曲線，說明都擁有同樣的(r,theta), 意味著這些點在一條直線上。
發上圖所示，三個點(對應圖中的三條正弦曲線）在一條直線上，因為這三個曲線交于一點，
具有相同的（r, theta)。霍夫線變換就是利用這種方法來尋找圖中的直線。
函數：skimage.transform.hough_line(img)

返回三個值：
h: 霍夫變換累積器
theta: 點與x軸的夾角集合，一般為0-179度
distance: 點到原點的距離，即上面的所說的r.
"""

# 構建測試圖片
image = np.zeros((100, 100))  # 背景圖
idx = np.arange(25, 75)  # 25-74序列
image[idx[::-1], idx] = 255  # 線條\
image[idx, idx] = 255  # 線條/

# hough線變換
h, theta, d = skimage.transform.hough_line(image)

# 生成一個一行兩列的窗口（可顯示兩張圖片）.
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
plt.tight_layout()

# 顯示原始圖片
ax0.imshow(image, plt.cm.gray)
ax0.set_title("Input image")
ax0.set_axis_off()

# 顯示hough變換所得數據
ax1.imshow(np.log(1 + h))
ax1.set_title("Hough transform")
ax1.set_xlabel("Angles (degrees)")
ax1.set_ylabel("Distance (pixels)")
ax1.axis("image")

show()

"""
從右邊那張圖可以看出，有兩個交點，說明原圖像中有兩條直線。
如果我們要把圖中的兩條直線繪制出來，則需要用到另外一個函數：
skimage.transform.hough_line_peaks(hspace, angles, dists）
用這個函數可以取出峰值點，即交點，也即原圖中的直線。
返回的參數與輸入的參數一樣。我們修改一下上邊的程序，在原圖中將兩直線繪制出來。
"""

# 構建測試圖片
image = np.zeros((100, 100))  # 背景圖
idx = np.arange(25, 75)  # 25-74序列
image[idx[::-1], idx] = 255  # 線條\
image[idx, idx] = 255  # 線條/

# hough線變換
h, theta, d = skimage.transform.hough_line(image)

# 生成一個一行三列的窗口（可顯示三張圖片）.
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(8, 6))
plt.tight_layout()

# 顯示原始圖片
ax0.imshow(image, plt.cm.gray)
ax0.set_title("Input image")
ax0.set_axis_off()

# 顯示hough變換所得數據
ax1.imshow(np.log(1 + h))
ax1.set_title("Hough transform")
ax1.set_xlabel("Angles (degrees)")
ax1.set_ylabel("Distance (pixels)")
ax1.axis("image")

# 顯示檢測出的線條
ax2.imshow(image, plt.cm.gray)
row1, col1 = image.shape
for _, angle, dist in zip(*skimage.transform.hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
    ax2.plot((0, col1), (y0, y1), "-r")
ax2.axis((0, col1, row1, 0))
ax2.set_title("Detected lines")
ax2.set_axis_off()

show()

"""
注意，繪制線條的時候，要從極坐標轉換為笛卡爾坐標，公式為：
 ???
skimage還提供了另外一個檢測直線的霍夫變換函數，概率霍夫線變換：
skimage.transform.probabilistic_hough_line(img, threshold=10, line_length=5,line_gap=3)

參數：
img: 待檢測的圖像。
threshold： 閾值，可先項，默認為10
line_length: 檢測的最短線條長度，默認為50
line_gap: 線條間的最大間隙。增大這個值可以合并破碎的線條。默認為10

返回：
lines: 線條列表, 格式如((x0, y0), (x1, y0))，標明開始點和結束點。
下面，我們用canny算子提取邊緣，然后檢測哪些邊緣是直線？
"""

# 使用Probabilistic Hough Transform.
image = skimage.data.camera()
edges = skimage.feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
lines = skimage.transform.probabilistic_hough_line(
    edges, threshold=10, line_length=5, line_gap=3
)

# 創建顯示窗口.
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6))
plt.tight_layout()

# 顯示原圖像
ax0.imshow(image, plt.cm.gray)
ax0.set_title("Input image")
ax0.set_axis_off()

# 顯示canny邊緣
ax1.imshow(edges, plt.cm.gray)
ax1.set_title("Canny edges")
ax1.set_axis_off()

# 用plot繪制出所有的直線
ax2.imshow(edges * 0)
for line in lines:
    p0, p1 = line
    ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))
row2, col2 = image.shape
ax2.axis((0, col2, row2, 0))
ax2.set_title("Probabilistic Hough")
ax2.set_axis_off()

show()

print("------------------------------------------------------------")  # 60個


"""
霍夫圓和橢圓變換
在極坐標中，圓的表示方式為：
x=x0+rcosθ
y=y0+rsinθ
圓心為(x0,y0),r為半徑，θ為旋轉度數，值范圍為0-359
如果給定圓心點和半徑，則其它點是否在圓上，我們就能檢測出來了。
在圖像中，我們將每個非0像素點作為圓心點，以一定的半徑進行檢測，
如果有一個點在圓上，我們就對這個圓心累加一次。
如果檢測到一個圓，那么這個圓心點就累加到最大，成為峰值。
因此，在檢測結果中，一個峰值點，就對應一個圓心點。
霍夫圓檢測的函數：
skimage.transform.hough_circle(image, radius)
radius是一個數組，表示半徑的集合，如[3，4，5，6]
返回一個3維的數組（radius index, M, N), 第一維表示半徑的索引，后面兩維表示圖像的尺寸。
例1：繪制兩個圓形，用霍夫圓變換將它們檢測出來。
"""

img = np.zeros((250, 250, 3), dtype=np.uint8)
rr, cc = skimage.draw.circle_perimeter(60, 60, 50)  # 以半徑50畫一個圓
rr1, cc1 = skimage.draw.circle_perimeter(150, 150, 60)  # 以半徑60畫一個圓
img[cc, rr, :] = 255
img[cc1, rr1, :] = 255

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 5))

ax0.imshow(img)  # 顯示原圖
ax0.set_title("原圖")

hough_radii = np.arange(50, 80, 5)  # 半徑范圍
hough_res = skimage.transform.hough_circle(img[:, :, 0], hough_radii)  # 圓變換

centers = []  # 保存所有圓心點坐標
accums = []  # 累積值
radii = []  # 半徑

for radius, h in zip(hough_radii, hough_res):
    # 每一個半徑值，取出其中兩個圓
    num_peaks = 2
    peaks = skimage.feature.peak_local_max(h, num_peaks=num_peaks)  # 取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

# 畫出最接近的圓
image = np.copy(img)
for idx in np.argsort(accums)[::-1][:2]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy = skimage.draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] = (255, 0, 0)

ax1.imshow(image)
ax1.set_title("detected image")

show()

"""
結果圖如下：原圖中的圓用白色繪制，檢測出的圓用紅色繪制。
例2，檢測出下圖中存在的硬幣。
"""

image = skimage.util.img_as_ubyte(skimage.data.coins()[0:95, 70:370])  # 裁剪原圖片
edges = skimage.feature.canny(
    image, sigma=3, low_threshold=10, high_threshold=50
)  # 檢測canny邊緣

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 5))

ax0.imshow(edges, cmap=plt.cm.gray)  # 顯示canny邊緣
ax0.set_title("original image")

hough_radii = np.arange(15, 30, 2)  # 半徑范圍
hough_res = skimage.transform.hough_circle(edges, hough_radii)  # 圓變換

centers = []  # 保存中心點坐標
accums = []  # 累積值
radii = []  # 半徑

for radius, h in zip(hough_radii, hough_res):
    # 每一個半徑值，取出其中兩個圓
    num_peaks = 2
    peaks = skimage.feature.peak_local_max(h, num_peaks=num_peaks)  # 取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

# 畫出最接近的5個圓
image = skimage.color.gray2rgb(image)
for idx in np.argsort(accums)[::-1][:5]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy = skimage.draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] = (255, 0, 0)

ax1.imshow(image)
ax1.set_title("detected image")

show()

"""
橢圓變換是類似的，使用函數為：
skimage.transform.hough_ellipse(img,accuracy, threshold, min_size, max_size)
輸入參數：
img: 待檢測圖像。
accuracy: 使用在累加器上的短軸二進制尺寸，是一個double型的值，默認為1
thresh: 累加器閾值，默認為4
min_size: 長軸最小長度，默認為4
max_size: 短軸最大長度，默認為None,表示圖片最短邊的一半。
返回一個 [(accumulator, y0, x0, a, b, orientation)] 數組，
accumulator表示累加器，（y0,x0)表示橢圓中心點，（a,b)分別表示長短軸，orientation表示橢圓方向
例：檢測出咖啡圖片中的橢圓杯口
"""

""" fail

#加載圖片，轉換成灰度圖并檢測邊緣
image_rgb = skimage.data.coffee()[0:220, 160:420] #裁剪原圖像，不然速度非常慢
image_gray = skimage.color.rgb2gray(image_rgb)
edges = skimage.feature.canny(image_gray, sigma=2.0, low_threshold=0.55, high_threshold=0.8)

#執行橢圓變換
result = skimage.transform.hough_ellipse(edges, accuracy=20, threshold=250,min_size=100, max_size=120)
result.sort(order='accumulator') #根據累加器排序

#估計橢圓參數
best = list(result[-1])  #排完序后取最后一個
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

#在原圖上畫出橢圓
cy, cx = skimage.draw.ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255) #在原圖中用藍色表示檢測出的橢圓

#分別用白色表示canny邊緣，用紅色表示檢測出的橢圓，進行對比
edges = skimage.color.gray2rgb(edges)
edges[cy, cx] = (250, 0, 0) 

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))

ax1.set_title('Original picture')
ax1.imshow(image_rgb)

ax2.set_title('Edge (white) and result (red)')
ax2.imshow(edges)

show()

#霍夫橢圓變換速度非常慢，應避免圖像太大。
"""

print("------------------------------------------------------------")  # 60個


"""
邊緣與輪廓

在前面的python數字圖像處理（10）：圖像簡單濾波 中，我們已經講解了很多算子用來檢測邊緣，
其中用得最多的canny算子邊緣檢測。

本篇我們講解一些其它方法來檢測輪廓。

1、查找輪廓（find_contours)

measure模塊中的find_contours()函數，可用來檢測二值圖像的邊緣輪廓。

函數原型為：

skimage.measure.find_contours(array, level)

array: 一個二值數組圖像

level: 在圖像中查找輪廓的級別值

返回輪廓列表集合，可用for循環取出每一條輪廓。

"""

""" 沒有.circle

#生成二值測試圖像
img=np.zeros([100,100])
img[20:40,60:80]=1  #矩形
rr,cc= skimage.draw.circle(60,60,10)  #小圓
rr1,cc1= skimage.draw.circle(20,30,15) #大圓
img[rr,cc]=1
img[rr1,cc1]=1

#檢測所有圖形的輪廓
contours = skimage.measure.find_contours(img, 0.5)

#繪制輪廓
fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
ax0.imshow(img,plt.cm.gray)
ax1.imshow(img,plt.cm.gray)
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])

show()
"""

"""
結果如下：不同的輪廓用不同的顏色顯示

"""

""" NG

#生成二值測試圖像
img = skimage.color.rgb2gray(skimage.data.horse())

#檢測所有圖形的輪廓
contours = skimage.measure.find_contours(img, 0.5)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1 = axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

rows,cols = img.shape
ax1.axis([0,rows,cols,0])
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_title('contours')
show()
"""

"""

2、逼近多邊形曲線
逼近多邊形曲線有兩個函數：subdivide_polygon（)和 approximate_polygon（）
subdivide_polygon（)采用B樣條（B-Splines)來細分多邊形的曲線，該曲線通常在凸包線的內部。
函數格式為：
skimage.measure.subdivide_polygon(coords, degree=2, preserve_ends=False)
coords: 坐標點序列。
degree: B樣條的度數，默認為2
preserve_ends: 如果曲線為非閉合曲線，是否保存開始和結束點坐標，默認為false
返回細分為的坐標點序列。
approximate_polygon（）是基于Douglas-Peucker算法的一種近似曲線模擬。它根據指定的容忍值來近似一條多邊形曲線鏈，該曲線也在凸包線的內部。
函數格式為:
skimage.measure.approximate_polygon(coords, tolerance)
coords: 坐標點序列
tolerance: 容忍值
返回近似的多邊形曲線坐標序列。
"""

# 生成二值測試圖像
hand = np.array(
    [
        [1.64516129, 1.16145833],
        [1.64516129, 1.59375],
        [1.35080645, 1.921875],
        [1.375, 2.18229167],
        [1.68548387, 1.9375],
        [1.60887097, 2.55208333],
        [1.68548387, 2.69791667],
        [1.76209677, 2.56770833],
        [1.83064516, 1.97395833],
        [1.89516129, 2.75],
        [1.9516129, 2.84895833],
        [2.01209677, 2.76041667],
        [1.99193548, 1.99479167],
        [2.11290323, 2.63020833],
        [2.2016129, 2.734375],
        [2.25403226, 2.60416667],
        [2.14919355, 1.953125],
        [2.30645161, 2.36979167],
        [2.39112903, 2.36979167],
        [2.41532258, 2.1875],
        [2.1733871, 1.703125],
        [2.07782258, 1.16666667],
    ]
)

# 檢測所有圖形的輪廓
new_hand = hand.copy()
for _ in range(5):
    new_hand = skimage.measure.subdivide_polygon(new_hand, degree=2)

# approximate subdivided polygon with Douglas-Peucker algorithm
appr_hand = skimage.measure.approximate_polygon(new_hand, tolerance=0.02)

print("Number of coordinates:", len(hand), len(new_hand), len(appr_hand))

fig, axes = plt.subplots(2, 2, figsize=(9, 8))
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.plot(hand[:, 0], hand[:, 1], "r")
ax0.set_title("original hand")
ax1.plot(new_hand[:, 0], new_hand[:, 1], "g")
ax1.set_title("subdivide_polygon")
ax2.plot(appr_hand[:, 0], appr_hand[:, 1], "b")
ax2.set_title("approximate_polygon")

ax3.plot(hand[:, 0], hand[:, 1], "r")
ax3.plot(new_hand[:, 0], new_hand[:, 1], "g")
ax3.plot(appr_hand[:, 0], appr_hand[:, 1], "b")
ax3.set_title("all")

show()

print("------------------------------------------------------------")  # 60個

"""
高級形態學處理
形態學處理，除了最基本的膨脹、腐蝕、開/閉運算、黑/白帽處理外，還有一些更高級的運用，如凸包，連通區域標記，刪除小塊區域等。
1、凸包
凸包是指一個凸多邊形，這個凸多邊形將圖片中所有的白色像素點都包含在內。
函數為：
skimage.morphology.convex_hull_image(image)
輸入為二值圖像，輸出一個邏輯二值圖像。在凸包內的點為True, 否則為False
"""
""" pic NG
#生成二值測試圖像
img = skimage.color.rgb2gray(skimage.data.horse())
img = (img<0.5)*1

chull = skimage.morphology.convex_hull_image(img)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

show()
"""

"""
convex_hull_image()是將圖片中的所有目標看作一個整體，因此計算出來只有一個最小凸多邊形。如果圖中有多個目標物體，每一個物體需要計算一個最小凸多邊形，則需要使用convex_hull_object（）函數。

函數格式：skimage.morphology.convex_hull_object(image, neighbors=8)

輸入參數image是一個二值圖像，neighbors表示是采用4連通還是8連通，默認為8連通。

"""

""" NG

#生成二值測試圖像
img = skimage.color.rgb2gray(skimage.data.coins())
#檢測canny邊緣,得到二值圖片
edgs = skimage.feature.canny(img, sigma=3, low_threshold=10, high_threshold=50) 

chull = skimage.morphology.convex_hull_object(edgs)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(edgs,plt.cm.gray)
ax0.set_title('many objects')
ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

show()
"""

print("------------------------------------------------------------")  # 60個

"""
2、連通區域標記
在二值圖像中，如果兩個像素點相鄰且值相同（同為0或同為1），那么就認為這兩個像素點在一個相互連通的區域內。而同一個連通區域的所有像素點，都用同一個數值來進行標記，這個過程就叫連通區域標記。在判斷兩個像素是否相鄰時，我們通常采用4連通或8連通判斷。在圖像中，最小的單位是像素，每個像素周圍有8個鄰接像素，常見的鄰接關系有2種：4鄰接與8鄰接。4鄰接一共4個點，即上下左右，如下左圖所示。8鄰接的點一共有8個，包括了對角線位置的點，如下右圖所示。
在skimage包中，我們采用measure子模塊下的label（）函數來實現連通區域標記。
函數格式：
skimage.measure.label（image,connectivity=None)
參數中的image表示需要處理的二值圖像，connectivity表示連接的模式，1代表4鄰接，2代表8鄰接。
輸出一個標記數組（labels), 從0開始標記。
"""

import scipy.ndimage as ndi


# 編寫一個函數來生成原始二值圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  # 生成網絡
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l / (4.0 * n))  # 高斯濾波
    return mask > mask.mean()


data = microstructure(l=128) * 1  # 生成測試圖片

labels = skimage.measure.label(data, connectivity=2)  # 8連通區域標記
dst = skimage.color.label2rgb(labels)  # 根據不同的標記顯示不同的顏色
print("regions number:", labels.max() + 1)  # 顯示連通區域塊數(從0開始標記)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation="nearest")
ax1.axis("off")
ax2.imshow(dst, interpolation="nearest")
ax2.axis("off")

fig.tight_layout()
show()

"""
在代碼中，有些地方乘以1，則可以將bool數組快速地轉換為int數組。

結果如圖：有10個連通的區域，標記為0-9

如果想分別對每一個連通區域進行操作，比如計算面積、外接矩形、凸包面積等，
則需要調用measure子模塊的regionprops（）函數。該函數格式為：

skimage.measure.regionprops(label_image)

返回所有連通區塊的屬性列表，常用的屬性列表如下表：
屬性名稱 	類型 	描述
area 	int 	區域內像素點總數
bbox 	tuple 	邊界外接框(min_row, min_col, max_row, max_col)
centroid 	array　　 	質心坐標
convex_area 	int 	凸包內像素點總數
convex_image 	ndarray 	和邊界外接框同大小的凸包　　
coords 	ndarray 	區域內像素點坐標
Eccentricity  	float 	離心率
equivalent_diameter  	float 	和區域面積相同的圓的直徑
euler_number 	int　　 	區域歐拉數
extent  	float 	區域面積和邊界外接框面積的比率
filled_area 	int 	區域和外接框之間填充的像素點總數
perimeter  	float 	區域周長
label 	int 	區域標記
"""

print("------------------------------------------------------------")  # 60個

"""
3、刪除小塊區域

有些時候，我們只需要一些大塊區域，那些零散的、小塊的區域，我們就需要刪除掉，
則可以使用morphology子模塊的remove_small_objects（)函數。

函數格式：skimage.morphology.remove_small_objects(ar, min_size=64, connectivity=1, in_place=False)

參數：

ar: 待操作的bool型數組。

min_size: 最小連通區域尺寸，小于該尺寸的都將被刪除。默認為64.

connectivity: 鄰接模式，1表示4鄰接，2表示8鄰接

in_place: bool型值，如果為True,表示直接在輸入圖像中刪除小塊區域，否則進行復制后再刪除。默認為False.

返回刪除了小塊區域的二值圖像。
"""

import scipy.ndimage as ndi


# 編寫一個函數來生成原始二值圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  # 生成網絡
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l / (4.0 * n))  # 高斯濾波
    return mask > mask.mean()


data = microstructure(l=128)  # 生成測試圖片

dst = skimage.morphology.remove_small_objects(data, min_size=300, connectivity=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation="nearest")
ax2.imshow(dst, plt.cm.gray, interpolation="nearest")

fig.tight_layout()
show()

# 在此例中，我們將面積小于300的小塊區域刪除（由1變為0），結果如下圖：

print("------------------------------------------------------------")  # 60個

# 4、綜合示例：閾值分割+閉運算+連通區域標記+刪除小區塊+分色顯示

import matplotlib.patches as mpatches

# 加載并裁剪硬幣圖片
image = skimage.data.coins()[50:-50, 50:-50]

thresh = filters.threshold_otsu(image)  # 閾值分割
bw = skimage.morphology.closing(image > thresh, skimage.morphology.square(3))  # 閉運算

cleared = bw.copy()  # 復制
skimage.segmentation.clear_border(cleared)  # 清除與邊界相連的目標物

label_image = skimage.measure.label(cleared)  # 連通區域標記
borders = np.logical_xor(bw, cleared)  # 異或
label_image[borders] = -1
image_label_overlay = skimage.color.label2rgb(label_image, image=image)  # 不同標記用不同顏色顯示

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
ax0.imshow(cleared, plt.cm.gray)
ax1.imshow(image_label_overlay)

for region in skimage.measure.regionprops(label_image):  # 循環得到每一個連通區域屬性集
    # 忽略小區域
    if region.area < 100:
        continue

    # 繪制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle(
        (minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor="red", linewidth=2
    )
    ax1.add_patch(rect)

fig.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

"""
骨架提取與分水嶺算法

骨架提取與分水嶺算法也屬于形態學處理范疇，都放在morphology子模塊內。

1、骨架提取

骨架提取，也叫二值圖像細化。這種算法能將一個連通區域細化成一個像素的寬度，用于特征提取和目標拓撲表示。

morphology子模塊提供了兩個函數用于骨架提取，分別是Skeletonize（）函數和medial_axis（）函數。我們先來看Skeletonize（）函數。

格式為：skimage.morphology.skeletonize(image)

輸入和輸出都是一幅二值圖像。
"""

# 創建一個二值圖像用于測試
image = np.zeros((400, 400))

# 生成目標對象1(白色U型)
image[10:-10, 10:100] = 1
image[-100:-10, 10:-10] = 1
image[10:-10, -100:-10] = 1

# 生成目標對象2（X型）
rs, cs = skimage.draw.line(250, 150, 10, 280)
for i in range(10):
    image[rs + i, cs] = 1
rs, cs = skimage.draw.line(10, 150, 250, 280)
for i in range(20):
    image[rs + i, cs] = 1

# 生成目標對象3（O型）
ir, ic = np.indices(image.shape)
circle1 = (ic - 135) ** 2 + (ir - 150) ** 2 < 30**2
circle2 = (ic - 135) ** 2 + (ir - 150) ** 2 < 20**2
image[circle1] = 1
image[circle2] = 0

# 實施骨架算法
skeleton = skimage.morphology.skeletonize(image)

# 顯示結果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis("off")
ax1.set_title("原圖")

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis("off")
ax2.set_title("骨架skeleton")

fig.tight_layout()
show()

"""
生成一幅測試圖像，上面有三個目標對象，分別進行骨架提取，結果如下：

例2：利用系統自帶的馬圖片進行骨架提取
"""

""" pic NG

image = skimage.color.rgb2gray(skimage.data.horse())
image = 1 - image #反相
#實施骨架算法
skeleton = skimage.morphology.skeletonize(image)

#顯示結果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('原圖')

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('骨架skeleton')

fig.tight_layout()
show()
"""

"""
medial_axis就是中軸的意思，利用中軸變換方法計算前景（1值）目標對象的寬度，格式為：

skimage.morphology.medial_axis(image, mask=None, return_distance=False)

mask: 掩模。默認為None, 如果給定一個掩模，則在掩模內的像素值才執行骨架算法。

return_distance: bool型值，默認為False. 如果為True, 則除了返回骨架，還將距離變換值也同時返回。這里的距離指的是中軸線上的所有點與背景點的距離。
"""

import scipy.ndimage as ndi


# 編寫一個函數，生成測試圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l / (4.0 * n))
    return mask > mask.mean()


data = microstructure(l=64)  # 生成測試圖像

# 計算中軸和距離變換值
skel, distance = skimage.morphology.medial_axis(data, return_distance=True)

# 中軸上的點到背景像素點的距離
dist_on_skel = distance * skel

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, cmap=plt.cm.gray, interpolation="nearest")
# 用光譜色顯示中軸
# ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
ax2.imshow(dist_on_skel, interpolation="nearest")
ax2.contour(data, [0.5], colors="w")  # 顯示輪廓線

fig.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

"""
2、分水嶺算法
分水嶺在地理學上就是指一個山脊，水通常會沿著山脊的兩邊流向不同的“匯水盆”。分水嶺算法是一種用于圖像分割的經典算法，是基于拓撲理論的數學形態學的分割方法。如果圖像中的目標物體是連在一起的，則分割起來會更困難，分水嶺算法經常用于處理這類問題，通常會取得比較好的效果。
分水嶺算法可以和距離變換結合，尋找“匯水盆地”和“分水嶺界限”，從而對圖像進行分割。二值圖像的距離變換就是每一個像素點到最近非零值像素點的距離，我們可以使用scipy包來計算距離變換。
在下面的例子中，需要將兩個重疊的圓分開。我們先計算圓上的這些白色像素點到黑色背景像素點的距離變換，選出距離變換中的最大值作為初始標記點（如果是反色的話，則是取最小值），從這些標記點開始的兩個匯水盆越集越大，最后相交于分山嶺。從分山嶺處斷開，我們就得到了兩個分離的圓。
例1：基于距離變換的分山嶺圖像分割
"""

from scipy import ndimage as ndi

# 創建兩個帶有重疊圓的圖像
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1**2
mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

# 現在我們用分水嶺算法分離兩個圓
distance = ndi.distance_transform_edt(image)  # 距離變換
# local_maxi = skimage.feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
#                            labels=image)   #尋找峰值
local_maxi = skimage.feature.peak_local_max(
    distance, footprint=np.ones((3, 3)), labels=image
)  # 尋找峰值

markers = ndi.label(local_maxi)[0]  # 初始標記點

"""沒有watershed
labels = skimage.morphology.watershed(-distance, markers, mask=image) #基于距離變換的分水嶺算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
ax1.set_title("Distance")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
show()
"""

"""

分水嶺算法也可以和梯度相結合，來實現圖像分割。一般梯度圖像在邊緣處有較高的像素值，
而在其它地方則有較低的像素值，理想情況 下，分山嶺恰好在邊緣。因此，我們可以根據梯度來尋找分山嶺。

例2：基于梯度的分水嶺圖像分割
"""

""" pic NG
from scipy import ndimage as ndi

image =skimage.color.rgb2gray(skimage.data.camera())
denoised = filter.rank.median(image, skimage.morphology.disk(2)) #過濾噪聲

#將梯度值低于10的作為開始標記點
markers = filters.rank.gradient(denoised, skimage.morphology.disk(5)) <10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denoised, skimage.morphology.disk(2)) #計算梯度
labels = skimage.morphology.watershed(gradient, markers, mask=image) #基于梯度的分水嶺算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax1.set_title("Gradient")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
show()
"""
print("------------------------------------------------------------")  # 60個

"""
圖像中的像素訪問

前面的一些例子中，我們都是利用Image.open()來打開一幅圖像，
然後直接對這個PIL對象進行操作。
如果只是簡單的操作還可以，但是如果操作稍微復雜一些，就比較吃力了。
因此，通常我們加載完圖片後，都是把圖片轉換成矩陣來進行更加復雜的操作。

python中利用numpy庫和scipy庫來進行各種數據操作和科學計算。
我們可以通過pip來直接安裝這兩個庫

pip install numpy
pip install scipy

"""

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageFilter

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("------------------------------------------------------------")  # 60個

from scipy.ndimage import gaussian_filter

print("------------------------------------------------------------")  # 60個

print("de-noise")

import scipy.misc
import scipy.signal
import scipy.ndimage


# 中值濾波函數
def medium_filter(im, x, y, step):
    sum_s = []
    for k in range(-int(step / 2), int(step / 2) + 1):
        for m in range(-int(step / 2), int(step / 2) + 1):
            sum_s.append(im[x + k][y + m])
    sum_s.sort()
    return sum_s[(int(step * step / 2) + 1)]


# 均值濾波函數
def mean_filter(im, x, y, step):
    sum_s = 0
    for k in range(-int(step / 2), int(step / 2) + 1):
        for m in range(-int(step / 2), int(step / 2) + 1):
            sum_s += im[x + k][y + m] / (step * step)
    return sum_s


def convert_2d(r):
    n = 3
    # 3*3濾波器，每個系數都是1/9
    window = np.ones((n, n)) / n**2
    # 使用濾波器卷積圖像
    # mode = same 表示輸出尺寸等于輸入尺寸
    # boundary 表示采用對稱邊界條件處理圖像邊緣
    s = scipy.signal.convolve2d(r, window, mode="same", boundary="symm")
    return s.astype(np.uint8)


# 添加噪聲
def add_salt_noise(image):
    rows, cols, dims = image.shape
    R = np.mat(image[:, :, 0])
    G = np.mat(image[:, :, 1])
    B = np.mat(image[:, :, 2])
    Grey_sp = R * 0.299 + G * 0.587 + B * 0.114
    Grey_gs = R * 0.299 + G * 0.587 + B * 0.114
    snr = 0.9
    mu = 0
    sigma = 0.12
    noise_num = int((1 - snr) * rows * cols)

    for i in range(noise_num):
        rand_x = random.randint(0, rows - 1)
        rand_y = random.randint(0, cols - 1)
        if random.randint(0, 1) == 0:
            Grey_sp[rand_x, rand_y] = 0
        else:
            Grey_sp[rand_x, rand_y] = 255
    Grey_gs = Grey_gs + np.random.normal(0, 48, Grey_gs.shape)
    Grey_gs = Grey_gs - np.full(Grey_gs.shape, np.min(Grey_gs))
    Grey_gs = Grey_gs * 255 / np.max(Grey_gs)
    Grey_gs = Grey_gs.astype(np.uint8)

    # 中值濾波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))
    Grey_gs_mf = scipy.ndimage.median_filter(Grey_gs, (8, 8))

    # 均值濾波
    n = 3
    window = np.ones((n, n)) / n**2
    Grey_sp_me = convert_2d(Grey_sp)
    Grey_gs_me = convert_2d(Grey_gs)

    plt.subplot(231)
    plt.title("椒鹽噪聲")
    plt.imshow(Grey_sp, cmap="gray")

    plt.subplot(232)
    plt.title("高斯噪聲")
    plt.imshow(Grey_gs, cmap="gray")

    plt.subplot(233)
    plt.title("椒鹽噪聲的中值濾波")
    plt.imshow(Grey_sp_mf, cmap="gray")

    plt.subplot(234)
    plt.title("高斯噪聲的中值濾波")
    plt.imshow(Grey_gs_mf, cmap="gray")

    plt.subplot(235)
    plt.title("椒鹽噪聲的均值濾波")
    plt.imshow(Grey_sp_me, cmap="gray")

    plt.subplot(236)
    plt.title("高斯噪聲的均值濾波")
    plt.imshow(Grey_gs_me, cmap="gray")

    show()


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

plt.figure(
    num="影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => PIL影像 => numpy陣列
image = np.array(Image.open(filename))
add_salt_noise(image)

print("------------------------------------------------------------")  # 60個

print("PIL_derivative")

import scipy.ndimage

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open(filename).convert("L"))

plt.figure(
    num="PIL_derivative",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(141)
plt.title("(a)原圖")
plt.imshow(image)
# sobel算子
imagex = np.zeros(image.shape)
scipy.ndimage.sobel(image, 1, imagex)

plt.subplot(142)
plt.title("(b)x方向差分")
plt.imshow(imagex)
imagey = np.zeros(image.shape)
scipy.ndimage.sobel(image, 0, imagey)

plt.subplot(143)
plt.title("(c)y方向差分")
plt.imshow(imagey)
mag = 255 - np.sqrt(imagex**2 + imagey**2)

plt.subplot(144)
plt.title("(d)梯度幅值")
plt.imshow(mag)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_fuzzy")

import scipy.ndimage
from matplotlib.font_manager import FontProperties

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open(filename).convert("L"))

plt.figure(
    num="PIL_fuzzy",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(141)
plt.title("原圖")
plt.imshow(image)

for bi, blur in enumerate([2, 4, 8]):
    image2 = np.zeros(image.shape)
    image2 = scipy.ndimage.gaussian_filter(image, blur)
    image2 = np.uint8(image2)
    imageNum = str(blur)
    plt.subplot(1, 4, 2 + bi)
    plt.title("標準差為" + imageNum)
    plt.imshow(image2)

# 如果是彩色圖像，則分別對三個通道進行模糊
# for bi, blur in enumerate([2,4,8]):
#  image2 = np.zeros(image.shape)
#  for i in range(3):
#    image2[:, :, i] = filters.gaussian_filter(image[:, :, i], blur)
#  image2 = np.uint8(image2)
#  plt.subplot(1, 4,  2 + bi)
#  plt.imshow(image2)

show()

print("------------------------------------------------------------")  # 60個

print("PIL_gaussian")

import scipy.ndimage


def imx(image, sigma):
    imagex = np.zeros(image.shape)
    scipy.ndimage.gaussian_filter(image, sigma, (0, 1), imagex)
    return imagex


def imy(image, sigma):
    imagey = np.zeros(image.shape)
    scipy.ndimage.gaussian_filter(image, sigma, (1, 0), imagey)
    return imagey


def mag(image, sigma):
    # 還有gaussian_gradient_magnitude()
    imagemag = 255 - np.sqrt(imagex**2 + imagey**2)
    return imagemag


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open(filename).convert("L"))

plt.figure(
    num="PIL_gaussian",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示
sigma = [2, 5, 10]
for i in sigma:
    plt.subplot(3, 4, 4 * (sigma.index(i)) + 1)
    plt.imshow(image)
    imagex = imx(image, i)
    plt.subplot(3, 4, 4 * (sigma.index(i)) + 2)
    plt.imshow(imagex)
    imagey = imy(image, i)
    plt.subplot(3, 4, 4 * (sigma.index(i)) + 3)
    plt.imshow(imagey)
    imagemag = mag(image, i)
    plt.subplot(3, 4, 4 * (sigma.index(i)) + 4)
    plt.imshow(imagemag)

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

from PIL import Image

# measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
import scipy.ndimage

# 加載圖像和閾值，以確保它是二進制的

plt.figure(
    num="PIL_opening",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open("data/castle.jpg").convert("L"))

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image)
plt.title("原圖")
image = image < 128
labels, nbr_objects = scipy.ndimage.label(image)  # 圖像的灰度值表示對象的標簽
print("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title("標記後的圖")
# 形態學——使物體分離更好
image_open = scipy.ndimage.binary_opening(
    image, np.ones((9, 5)), iterations=4
)  # 開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title("開運算後的圖像")
labels_open, nbr_objects_open = scipy.ndimage.label(image_open)
print("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title("開運算後進行標記後的圖像")

show()

print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

# measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
import scipy.ndimage

# 加載圖像和閾值，以確保它是二進制的
# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open("data/castle.jpg").convert("L"))

plt.figure(
    num="PIL_PCA",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(221)
plt.imshow(image)
plt.title("原圖")
image = image < 128
labels, nbr_objects = scipy.ndimage.label(image)  # 圖像的灰度值表示對象的標簽
print("Number of objects:", nbr_objects)

plt.subplot(222)
plt.imshow(labels)
plt.title("標記後的圖")
# 形態學——使物體分離更好
image_open = scipy.ndimage.binary_opening(
    image, np.ones((9, 5)), iterations=4
)  # 開操作，第二個參數為結構元素，iterations覺定執行該操作的次數

plt.subplot(223)
plt.imshow(image_open)
plt.title("開運算後的圖像")
labels_open, nbr_objects_open = scipy.ndimage.label(image_open)
print("Number of objects:", nbr_objects_open)

plt.subplot(224)
plt.imshow(labels_open)
plt.title("開運算後進行標記後的圖像")

show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

import scipy.ndimage

# from PCV.tools import rof

# 檔案 => PIL影像 => 灰階 => numpy陣列
image = np.array(Image.open("data/girl.jpg").convert("L"))

# U,T = rof.denoise(image,image)
G = scipy.ndimage.gaussian_filter(image, 10)

plt.figure(
    num="PIL_realROF",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(1, 3, 1)
plt.imshow(image)
# plt.axis('equal')
plt.title("原噪聲圖像")

plt.subplot(1, 3, 2)
plt.imshow(G)
# plt.axis('equal')
plt.title("高斯模糊後的圖像")

plt.subplot(1, 3, 3)
# plt.imshow(U)
# plt.axis('equal')
plt.title("ROF降噪後的圖像")

show()

print("------------------------------------------------------------")  # 60個

print("PIL_ROF")

import scipy.ndimage

# from PCV.tools import rof

# 創建合成圖像與噪聲
image = np.zeros((500, 500))
image[100:400, 100:400] = 128
image[200:300, 200:300] = 255
image = image + 30 * np.random.standard_normal((500, 500))
# roll()函數：循環滾動數組中的元素，計算領域元素的差異。linalg.norm()函數可以衡量兩個數組見得差異
# U,T = rof.denoise(image,image)
G = scipy.ndimage.gaussian_filter(image, 10)

plt.figure(
    num="PIL_ROF",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.gray()  # 不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(1, 3, 1)
plt.imshow(image)
# plt.axis('equal')
plt.title("原噪聲圖像")

plt.subplot(1, 3, 2)
plt.imshow(G)
# plt.axis('equal')
plt.title("高斯模糊後的圖像")

plt.subplot(1, 3, 3)
# plt.imshow(U)
# plt.axis('equal')
plt.title("ROF降噪後的圖像")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

im = np.array(Image.open(filename).convert("L"))
plt.gray()
plt.subplot(2, 2, 1)
plt.axis("off")
plt.title("Original Image")
plt.imshow(im)

for bi, blur in enumerate([2, 5, 10]):
    print("bi = ", bi)
    im2 = np.zeros(im.shape)
    im2 = scipy.ndimage.gaussian_filter(im, blur)
    im2 = np.uint8(im2)
    imNum = str(blur)
    plt.subplot(2, 2, 2 + bi)
    plt.axis("off")
    plt.title("GaussVar = " + imNum)
    plt.imshow(im2)

show()

print("------------------------------------------------------------")  # 60個

image = skimage.color.rgb2gray(skimage.data.chelsea())
hogVec, hogVis = skimage.feature.hog(image, visualize=True)

fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap="gray")
ax[0].set_title("input image")
ax[1].imshow(hogVis)
ax[1].set_title("extarcting features from image")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy import ndimage as ndi
from skimage import morphology
from skimage import color
from skimage import filters

plt.imshow(skimage.data.camera(), cmap=plt.cm.gray)
show()

# image = color.rgb2gray(skimage.data.camera())
image = skimage.data.camera()

denoised = filters.rank.median(image, morphology.disk(2))  # 过滤噪声
# 将梯度值低于10的作为开始标记点
markers = filters.rank.gradient(denoised, morphology.disk(5)) < 10
markers = ndi.label(markers)[0]
gradient = filters.rank.gradient(denoised, morphology.disk(2))  # 计算梯度
# labels = morphology.watershed(gradient, markers, mask=image)  # 基于梯度的分水岭算法
labels = skimage.segmentation.watershed(gradient, markers, mask=image)  # 基于梯度的分水岭算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap=plt.cm.gray, interpolation="nearest")
ax0.set_title("原始图像")
ax1.imshow(gradient, cmap=plt.cm.Spectral, interpolation="nearest")
ax1.set_title("梯度")
ax2.imshow(markers, cmap=plt.cm.Spectral, interpolation="nearest")
ax2.set_title("标记")
ax3.imshow(labels, cmap=plt.cm.Spectral, interpolation="nearest")
ax3.set_title("分割")
for ax in axes:
    ax.axis("off")
fig.tight_layout()

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
