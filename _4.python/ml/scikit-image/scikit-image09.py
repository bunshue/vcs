"""
skimage : scikit-image SciKit (toolkit for SciPy)


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


"""
霍夫線變換

在圖片處理中，霍夫變換主要是用來檢測圖片中的幾何形狀，包括直線、圓、橢圓等。

在skimage中，霍夫變換是放在tranform模塊內，本篇主要講解霍夫線變換。

對于平面中的一條直線，在笛卡爾坐標系中，可用y=mx+b來表示，其中m為斜率，b為截距。但是如果直線是一條垂直線，則m為無窮大，所有通常我們在另一坐標系中表示直線，即極坐標系下的r=xcos(theta)+ysin(theta)。即可用（r,theta）來表示一條直線。其中r為該直線到原點的距離，theta為該直線的垂線與x軸的夾角。如下圖所示。

對于一個給定的點（x0,y0), 我們在極坐標下繪出所有通過它的直線（r,theta)，將得到一條正弦曲線。如果將圖片中的所有非0點的正弦曲線都繪制出來，則會存在一些交點。所有經過這個交點的正弦曲線，說明都擁有同樣的(r,theta), 意味著這些點在一條直線上。

發上圖所示，三個點(對應圖中的三條正弦曲線）在一條直線上，因為這三個曲線交于一點，具有相同的（r, theta)。霍夫線變換就是利用這種方法來尋找圖中的直線。

函數：skimage.transform.hough_line(img)

返回三個值：

h: 霍夫變換累積器

theta: 點與x軸的夾角集合，一般為0-179度

distance: 點到原點的距離，即上面的所說的r.

"""

import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt

# 構建測試圖片
image = np.zeros((100, 100))  #背景圖
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 線條\
image[idx, idx] = 255        # 線條/

# hough線變換
h, theta, d = st.hough_line(image)

#生成一個一行兩列的窗口（可顯示兩張圖片）.
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
plt.tight_layout()

#顯示原始圖片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#顯示hough變換所得數據
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')

plt.show()

"""

從右邊那張圖可以看出，有兩個交點，說明原圖像中有兩條直線。

如果我們要把圖中的兩條直線繪制出來，則需要用到另外一個函數：

skimage.transform.hough_line_peaks(hspace, angles, dists）

用這個函數可以取出峰值點，即交點，也即原圖中的直線。

返回的參數與輸入的參數一樣。我們修改一下上邊的程序，在原圖中將兩直線繪制出來。
"""
import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt

# 構建測試圖片
image = np.zeros((100, 100))  #背景圖
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 線條\
image[idx, idx] = 255        # 線條/

# hough線變換
h, theta, d = st.hough_line(image)

#生成一個一行三列的窗口（可顯示三張圖片）.
fig, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(8, 6))
plt.tight_layout()

#顯示原始圖片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#顯示hough變換所得數據
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')

#顯示檢測出的線條
ax2.imshow(image, plt.cm.gray)
row1, col1 = image.shape
for _, angle, dist in zip(*st.hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - col1 * np.cos(angle)) / np.sin(angle)
    ax2.plot((0, col1), (y0, y1), '-r')
ax2.axis((0, col1, row1, 0))
ax2.set_title('Detected lines')
ax2.set_axis_off()

plt.show()

"""
注意，繪制線條的時候，要從極坐標轉換為笛卡爾坐標，公式為：

 

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

import skimage.transform as st
import matplotlib.pyplot as plt
from skimage import data,feature

#使用Probabilistic Hough Transform.
image = data.camera()
edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5,line_gap=3)

# 創建顯示窗口.
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6))
plt.tight_layout()

#顯示原圖像
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#顯示canny邊緣
ax1.imshow(edges, plt.cm.gray)
ax1.set_title('Canny edges')
ax1.set_axis_off()

#用plot繪制出所有的直線
ax2.imshow(edges * 0)
for line in lines:
    p0, p1 = line
    ax2.plot((p0[0], p1[0]), (p0[1], p1[1]))
row2, col2 = image.shape
ax2.axis((0, col2, row2, 0))
ax2.set_title('Probabilistic Hough')
ax2.set_axis_off()

plt.show()


print('------------------------------------------------------------')	#60個


"""
霍夫圓和橢圓變換

在極坐標中，圓的表示方式為：

x=x0+rcosθ

y=y0+rsinθ

圓心為(x0,y0),r為半徑，θ為旋轉度數，值范圍為0-359

如果給定圓心點和半徑，則其它點是否在圓上，我們就能檢測出來了。在圖像中，我們將每個非0像素點作為圓心點，以一定的半徑進行檢測，如果有一個點在圓上，我們就對這個圓心累加一次。如果檢測到一個圓，那么這個圓心點就累加到最大，成為峰值。因此，在檢測結果中，一個峰值點，就對應一個圓心點。

霍夫圓檢測的函數：

skimage.transform.hough_circle(image, radius)

radius是一個數組，表示半徑的集合，如[3，4，5，6]

返回一個3維的數組（radius index, M, N), 第一維表示半徑的索引，后面兩維表示圖像的尺寸。

例1：繪制兩個圓形，用霍夫圓變換將它們檢測出來。
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import draw,transform,feature

img = np.zeros((250, 250,3), dtype=np.uint8)
rr, cc = draw.circle_perimeter(60, 60, 50)  #以半徑50畫一個圓
rr1, cc1 = draw.circle_perimeter(150, 150, 60) #以半徑60畫一個圓
img[cc, rr,:] =255
img[cc1, rr1,:] =255

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(img)  #顯示原圖
ax0.set_title('origin image')

hough_radii = np.arange(50, 80, 5)  #半徑范圍
hough_res =transform.hough_circle(img[:,:,0], hough_radii)  #圓變換 

centers = []  #保存所有圓心點坐標
accums = []   #累積值
radii = []    #半徑

for radius, h in zip(hough_radii, hough_res):
    #每一個半徑值，取出其中兩個圓
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#畫出最接近的圓
image =np.copy(img)
for idx in np.argsort(accums)[::-1][:2]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy =draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] =(255,0,0)

ax1.imshow(image)
ax1.set_title('detected image')

plt.show()

"""

結果圖如下：原圖中的圓用白色繪制，檢測出的圓用紅色繪制。

例2，檢測出下圖中存在的硬幣。
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color,draw,transform,feature,util

image = util.img_as_ubyte(data.coins()[0:95, 70:370]) #裁剪原圖片
edges =feature.canny(image, sigma=3, low_threshold=10, high_threshold=50) #檢測canny邊緣

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(edges, cmap=plt.cm.gray)  #顯示canny邊緣
ax0.set_title('original image')

hough_radii = np.arange(15, 30, 2)  #半徑范圍
hough_res =transform.hough_circle(edges, hough_radii)  #圓變換 

centers = []  #保存中心點坐標
accums = []   #累積值
radii = []    #半徑

for radius, h in zip(hough_radii, hough_res):
    #每一個半徑值，取出其中兩個圓
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#畫出最接近的5個圓
image = color.gray2rgb(image)
for idx in np.argsort(accums)[::-1][:5]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy =draw.circle_perimeter(center_y, center_x, radius)
    image[cy, cx] = (255,0,0)

ax1.imshow(image)
ax1.set_title('detected image')

plt.show()

"""
橢圓變換是類似的，使用函數為：

skimage.transform.hough_ellipse(img,accuracy, threshold, min_size, max_size)

輸入參數：

img: 待檢測圖像。

accuracy: 使用在累加器上的短軸二進制尺寸，是一個double型的值，默認為1

thresh: 累加器閾值，默認為4

min_size: 長軸最小長度，默認為4

max_size: 短軸最大長度，默認為None,表示圖片最短邊的一半。

返回一個 [(accumulator, y0, x0, a, b, orientation)] 數組，accumulator表示累加器，（y0,x0)表示橢圓中心點，（a,b)分別表示長短軸，orientation表示橢圓方向

例：檢測出咖啡圖片中的橢圓杯口
"""

""" fail
import matplotlib.pyplot as plt
from skimage import data,draw,color,transform,feature

#加載圖片，轉換成灰度圖并檢測邊緣
image_rgb = data.coffee()[0:220, 160:420] #裁剪原圖像，不然速度非常慢
image_gray = color.rgb2gray(image_rgb)
edges = feature.canny(image_gray, sigma=2.0, low_threshold=0.55, high_threshold=0.8)

#執行橢圓變換
result =transform.hough_ellipse(edges, accuracy=20, threshold=250,min_size=100, max_size=120)
result.sort(order='accumulator') #根據累加器排序

#估計橢圓參數
best = list(result[-1])  #排完序后取最后一個
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

#在原圖上畫出橢圓
cy, cx =draw.ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255) #在原圖中用藍色表示檢測出的橢圓

#分別用白色表示canny邊緣，用紅色表示檢測出的橢圓，進行對比
edges = color.gray2rgb(edges)
edges[cy, cx] = (250, 0, 0) 

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))

ax1.set_title('Original picture')
ax1.imshow(image_rgb)

ax2.set_title('Edge (white) and result (red)')
ax2.imshow(edges)

plt.show()


#霍夫橢圓變換速度非常慢，應避免圖像太大。
"""

print('------------------------------------------------------------')	#60個


"""
邊緣與輪廓

在前面的python數字圖像處理（10）：圖像簡單濾波 中，我們已經講解了很多算子用來檢測邊緣，其中用得最多的canny算子邊緣檢測。

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
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,draw 

#生成二值測試圖像
img=np.zeros([100,100])
img[20:40,60:80]=1  #矩形
rr,cc=draw.circle(60,60,10)  #小圓
rr1,cc1=draw.circle(20,30,15) #大圓
img[rr,cc]=1
img[rr1,cc1]=1

#檢測所有圖形的輪廓
contours = measure.find_contours(img, 0.5)

#繪制輪廓
fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
ax0.imshow(img,plt.cm.gray)
ax1.imshow(img,plt.cm.gray)
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])

plt.show()
"""

"""
結果如下：不同的輪廓用不同的顏色顯示

"""

""" NG
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值測試圖像
img=color.rgb2gray(data.horse())

#檢測所有圖形的輪廓
contours = measure.find_contours(img, 0.5)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

rows,cols=img.shape
ax1.axis([0,rows,cols,0])
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_title('contours')
plt.show()
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

import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值測試圖像
hand = np.array([[1.64516129, 1.16145833],
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
                 [2.07782258, 1.16666667]])

#檢測所有圖形的輪廓
new_hand = hand.copy()
for _ in range(5):
    new_hand =measure.subdivide_polygon(new_hand, degree=2)

# approximate subdivided polygon with Douglas-Peucker algorithm
appr_hand =measure.approximate_polygon(new_hand, tolerance=0.02)

print("Number of coordinates:", len(hand), len(new_hand), len(appr_hand))

fig, axes= plt.subplots(2,2, figsize=(9, 8))
ax0,ax1,ax2,ax3=axes.ravel()

ax0.plot(hand[:, 0], hand[:, 1],'r')
ax0.set_title('original hand')
ax1.plot(new_hand[:, 0], new_hand[:, 1],'g')
ax1.set_title('subdivide_polygon')
ax2.plot(appr_hand[:, 0], appr_hand[:, 1],'b')
ax2.set_title('approximate_polygon')

ax3.plot(hand[:, 0], hand[:, 1],'r')
ax3.plot(new_hand[:, 0], new_hand[:, 1],'g')
ax3.plot(appr_hand[:, 0], appr_hand[:, 1],'b')
ax3.set_title('all')

plt.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



