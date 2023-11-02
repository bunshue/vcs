"""
skimage : scikit-image SciKit (toolkit for SciPy)


"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

"""
霍夫线变换

在图片处理中，霍夫变换主要是用来检测图片中的几何形状，包括直线、圆、椭圆等。

在skimage中，霍夫变换是放在tranform模块内，本篇主要讲解霍夫线变换。

对于平面中的一条直线，在笛卡尔坐标系中，可用y=mx+b来表示，其中m为斜率，b为截距。但是如果直线是一条垂直线，则m为无穷大，所有通常我们在另一坐标系中表示直线，即极坐标系下的r=xcos(theta)+ysin(theta)。即可用（r,theta）来表示一条直线。其中r为该直线到原点的距离，theta为该直线的垂线与x轴的夹角。如下图所示。

对于一个给定的点（x0,y0), 我们在极坐标下绘出所有通过它的直线（r,theta)，将得到一条正弦曲线。如果将图片中的所有非0点的正弦曲线都绘制出来，则会存在一些交点。所有经过这个交点的正弦曲线，说明都拥有同样的(r,theta), 意味着这些点在一条直线上。

发上图所示，三个点(对应图中的三条正弦曲线）在一条直线上，因为这三个曲线交于一点，具有相同的（r, theta)。霍夫线变换就是利用这种方法来寻找图中的直线。

函数：skimage.transform.hough_line(img)

返回三个值：

h: 霍夫变换累积器

theta: 点与x轴的夹角集合，一般为0-179度

distance: 点到原点的距离，即上面的所说的r.

"""

import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt

# 构建测试图片
image = np.zeros((100, 100))  #背景图
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 线条\
image[idx, idx] = 255        # 线条/

# hough线变换
h, theta, d = st.hough_line(image)

#生成一个一行两列的窗口（可显示两张图片）.
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 6))
plt.tight_layout()

#显示原始图片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示hough变换所得数据
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')

plt.show()

"""

从右边那张图可以看出，有两个交点，说明原图像中有两条直线。

如果我们要把图中的两条直线绘制出来，则需要用到另外一个函数：

skimage.transform.hough_line_peaks(hspace, angles, dists）

用这个函数可以取出峰值点，即交点，也即原图中的直线。

返回的参数与输入的参数一样。我们修改一下上边的程序，在原图中将两直线绘制出来。
"""
import skimage.transform as st
import numpy as np
import matplotlib.pyplot as plt

# 构建测试图片
image = np.zeros((100, 100))  #背景图
idx = np.arange(25, 75)    #25-74序列
image[idx[::-1], idx] = 255  # 线条\
image[idx, idx] = 255        # 线条/

# hough线变换
h, theta, d = st.hough_line(image)

#生成一个一行三列的窗口（可显示三张图片）.
fig, (ax0, ax1,ax2) = plt.subplots(1, 3, figsize=(8, 6))
plt.tight_layout()

#显示原始图片
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示hough变换所得数据
ax1.imshow(np.log(1 + h))
ax1.set_title('Hough transform')
ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')
ax1.axis('image')

#显示检测出的线条
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
注意，绘制线条的时候，要从极坐标转换为笛卡尔坐标，公式为：

 

skimage还提供了另外一个检测直线的霍夫变换函数，概率霍夫线变换：

skimage.transform.probabilistic_hough_line(img, threshold=10, line_length=5,line_gap=3)

参数：

img: 待检测的图像。

threshold： 阈值，可先项，默认为10

line_length: 检测的最短线条长度，默认为50

line_gap: 线条间的最大间隙。增大这个值可以合并破碎的线条。默认为10

返回：

lines: 线条列表, 格式如((x0, y0), (x1, y0))，标明开始点和结束点。

下面，我们用canny算子提取边缘，然后检测哪些边缘是直线？
"""

import skimage.transform as st
import matplotlib.pyplot as plt
from skimage import data,feature

#使用Probabilistic Hough Transform.
image = data.camera()
edges = feature.canny(image, sigma=2, low_threshold=1, high_threshold=25)
lines = st.probabilistic_hough_line(edges, threshold=10, line_length=5,line_gap=3)

# 创建显示窗口.
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(16, 6))
plt.tight_layout()

#显示原图像
ax0.imshow(image, plt.cm.gray)
ax0.set_title('Input image')
ax0.set_axis_off()

#显示canny边缘
ax1.imshow(edges, plt.cm.gray)
ax1.set_title('Canny edges')
ax1.set_axis_off()

#用plot绘制出所有的直线
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
霍夫圆和椭圆变换

在极坐标中，圆的表示方式为：

x=x0+rcosθ

y=y0+rsinθ

圆心为(x0,y0),r为半径，θ为旋转度数，值范围为0-359

如果给定圆心点和半径，则其它点是否在圆上，我们就能检测出来了。在图像中，我们将每个非0像素点作为圆心点，以一定的半径进行检测，如果有一个点在圆上，我们就对这个圆心累加一次。如果检测到一个圆，那么这个圆心点就累加到最大，成为峰值。因此，在检测结果中，一个峰值点，就对应一个圆心点。

霍夫圆检测的函数：

skimage.transform.hough_circle(image, radius)

radius是一个数组，表示半径的集合，如[3，4，5，6]

返回一个3维的数组（radius index, M, N), 第一维表示半径的索引，后面两维表示图像的尺寸。

例1：绘制两个圆形，用霍夫圆变换将它们检测出来。
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import draw,transform,feature

img = np.zeros((250, 250,3), dtype=np.uint8)
rr, cc = draw.circle_perimeter(60, 60, 50)  #以半径50画一个圆
rr1, cc1 = draw.circle_perimeter(150, 150, 60) #以半径60画一个圆
img[cc, rr,:] =255
img[cc1, rr1,:] =255

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(img)  #显示原图
ax0.set_title('origin image')

hough_radii = np.arange(50, 80, 5)  #半径范围
hough_res =transform.hough_circle(img[:,:,0], hough_radii)  #圆变换 

centers = []  #保存所有圆心点坐标
accums = []   #累积值
radii = []    #半径

for radius, h in zip(hough_radii, hough_res):
    #每一个半径值，取出其中两个圆
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#画出最接近的圆
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

结果图如下：原图中的圆用白色绘制，检测出的圆用红色绘制。

例2，检测出下图中存在的硬币。
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color,draw,transform,feature,util

image = util.img_as_ubyte(data.coins()[0:95, 70:370]) #裁剪原图片
edges =feature.canny(image, sigma=3, low_threshold=10, high_threshold=50) #检测canny边缘

fig, (ax0,ax1) = plt.subplots(1,2, figsize=(8, 5))

ax0.imshow(edges, cmap=plt.cm.gray)  #显示canny边缘
ax0.set_title('original iamge')

hough_radii = np.arange(15, 30, 2)  #半径范围
hough_res =transform.hough_circle(edges, hough_radii)  #圆变换 

centers = []  #保存中心点坐标
accums = []   #累积值
radii = []    #半径

for radius, h in zip(hough_radii, hough_res):
    #每一个半径值，取出其中两个圆
    num_peaks = 2
    peaks =feature.peak_local_max(h, num_peaks=num_peaks) #取出峰值
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

#画出最接近的5个圆
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
椭圆变换是类似的，使用函数为：

skimage.transform.hough_ellipse(img,accuracy, threshold, min_size, max_size)

输入参数：

img: 待检测图像。

accuracy: 使用在累加器上的短轴二进制尺寸，是一个double型的值，默认为1

thresh: 累加器阈值，默认为4

min_size: 长轴最小长度，默认为4

max_size: 短轴最大长度，默认为None,表示图片最短边的一半。

返回一个 [(accumulator, y0, x0, a, b, orientation)] 数组，accumulator表示累加器，（y0,x0)表示椭圆中心点，（a,b)分别表示长短轴，orientation表示椭圆方向

例：检测出咖啡图片中的椭圆杯口
"""

""" fail
import matplotlib.pyplot as plt
from skimage import data,draw,color,transform,feature

#加载图片，转换成灰度图并检测边缘
image_rgb = data.coffee()[0:220, 160:420] #裁剪原图像，不然速度非常慢
image_gray = color.rgb2gray(image_rgb)
edges = feature.canny(image_gray, sigma=2.0, low_threshold=0.55, high_threshold=0.8)

#执行椭圆变换
result =transform.hough_ellipse(edges, accuracy=20, threshold=250,min_size=100, max_size=120)
result.sort(order='accumulator') #根据累加器排序

#估计椭圆参数
best = list(result[-1])  #排完序后取最后一个
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

#在原图上画出椭圆
cy, cx =draw.ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255) #在原图中用蓝色表示检测出的椭圆

#分别用白色表示canny边缘，用红色表示检测出的椭圆，进行对比
edges = color.gray2rgb(edges)
edges[cy, cx] = (250, 0, 0) 

fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4))

ax1.set_title('Original picture')
ax1.imshow(image_rgb)

ax2.set_title('Edge (white) and result (red)')
ax2.imshow(edges)

plt.show()


#霍夫椭圆变换速度非常慢，应避免图像太大。
"""

print('------------------------------------------------------------')	#60個


"""
边缘与轮廓

在前面的python数字图像处理（10）：图像简单滤波 中，我们已经讲解了很多算子用来检测边缘，其中用得最多的canny算子边缘检测。

本篇我们讲解一些其它方法来检测轮廓。

1、查找轮廓（find_contours)

measure模块中的find_contours()函数，可用来检测二值图像的边缘轮廓。

函数原型为：

skimage.measure.find_contours(array, level)

array: 一个二值数组图像

level: 在图像中查找轮廓的级别值

返回轮廓列表集合，可用for循环取出每一条轮廓。

"""

""" 沒有.circle
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,draw 

#生成二值测试图像
img=np.zeros([100,100])
img[20:40,60:80]=1  #矩形
rr,cc=draw.circle(60,60,10)  #小圆
rr1,cc1=draw.circle(20,30,15) #大圆
img[rr,cc]=1
img[rr1,cc1]=1

#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

#绘制轮廓
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
结果如下：不同的轮廓用不同的颜色显示

"""

""" NG
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值测试图像
img=color.rgb2gray(data.horse())

#检测所有图形的轮廓
contours = measure.find_contours(img, 0.5)

#绘制轮廓
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

2、逼近多边形曲线

逼近多边形曲线有两个函数：subdivide_polygon（)和 approximate_polygon（）

subdivide_polygon（)采用B样条（B-Splines)来细分多边形的曲线，该曲线通常在凸包线的内部。

函数格式为：

skimage.measure.subdivide_polygon(coords, degree=2, preserve_ends=False)

coords: 坐标点序列。

degree: B样条的度数，默认为2

preserve_ends: 如果曲线为非闭合曲线，是否保存开始和结束点坐标，默认为false

返回细分为的坐标点序列。

approximate_polygon（）是基于Douglas-Peucker算法的一种近似曲线模拟。它根据指定的容忍值来近似一条多边形曲线链，该曲线也在凸包线的内部。

函数格式为:

skimage.measure.approximate_polygon(coords, tolerance)

coords: 坐标点序列

tolerance: 容忍值

返回近似的多边形曲线坐标序列。

"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,data,color

#生成二值测试图像
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

#检测所有图形的轮廓
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


