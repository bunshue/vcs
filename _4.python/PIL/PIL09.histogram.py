"""
PIL histogram

用直方圖分析一張圖片的顏色組成

"""

print('------------------------------------------------------------')	#60個

from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageFilter

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

print('------------------------------------------------------------')	#60個

#把一張圖的RGB通道分開顯示出來

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
#filename = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.bmp' #400X400
#filename = '../opencv/data/pic_calcHist.jpg'
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"  # 560X400
#filename = "C:/_git/vcs/_4.python/_data/eq3.bmp"  # 480X360
#filename = "C:/_git/vcs/_4.python/_data/eq4.bmp"  # 480X360

plt.figure(
    num="配合圖形遮罩計算直方圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(211)

# 檔案 => PIL影像
image1 = Image.open(filename)
plt.imshow(image1)

# PIL影像 => 灰階
# 灰階才能做histogram處理
image2 = image1.convert('L')	#轉換成灰階圖像

plt.subplot(212)

image2_hist = image2.histogram()
print('len = ', len(image2_hist))
index = np.arange(0, len(image2_hist))
plt.plot(index, image2_hist, color = 'yellow', label = '原圖灰階', linewidth = 2)

print('RGB影像不可以做histogram, 分離成獨立通道後才可以做histogram')
r, g, b = image1.split()   #r, g, b為三個通道的list
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(r_hist))
index = np.arange(0, len(r_hist))

plt.subplot(212)

plt.plot(index, r_hist, color = 'red', label = 'R 通道')
plt.plot(index, g_hist, color = 'green', label = 'G 通道')
plt.plot(index, b_hist, color = 'blue', label = 'B 通道')

plt.xlim(0-10, 256+10)
plt.ylim(0, 4500+2000+2000)
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

print('用plot畫出三色分布')

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"  # 560X400

plt.figure(
    num="配合圖形遮罩計算直方圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(211)

# 檔案 => PIL影像
image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image1)

r, g, b = image1.split()   #r, g, b為三個通道的list
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

ind0 = np.arange(0, len(r_hist))

plt.subplot(212)

plt.plot(ind0, r_hist, color = 'red', label = 'R 通道')
plt.plot(ind0, g_hist, color = 'green', label = 'G 通道')
plt.plot(ind0, b_hist, color = 'blue', label = 'B 通道')

plt.xlim(0-10, 256+10)
plt.ylim(0, 4500+2000+2000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from PIL import ImageChops

def compare_images(filename1, filename2, threshold=0.8):
    #比較兩張圖像的相似度，返回相似度值（0~1之間的浮點數）
    # 檔案 => PIL影像 => RGBA
    image1 = Image.open(filename1).convert('RGBA')
    # 檔案 => PIL影像 => RGBA
    image2 = Image.open(filename2).convert('RGBA')
    diff = ImageChops.difference(image1, image2)
    histogram = diff.histogram()
    pixels = sum(histogram)
    similarity = 1 - (pixels / float(image1.size[0] * image1.size[1] * 3))
    print(similarity)
    return similarity >= threshold

# 測試比較相似度
filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'
is_similar = compare_images(filename1, filename2)
print('相似度:', is_similar)

print('------------------------------------------------------------')	#60個
'''
"""
圖像直方圖

我們先來看兩個函數reshape和flatten:

假設我們先生成一個一維數組：

vec=np.arange(15)
print vec

顯示為：

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

如果我們要把這個一維數組，變成一個3*5二維矩陣，我們可以使用reshape來實現

mat= vec.reshape(3,5)
print mat

顯示為

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

現在如果我們返過來，知道一個二維矩陣，要變成一個一維數組，就不能用reshape了，只能用flatten. 我們來看兩者的區別

a1=mat.reshape(1,-1)  #-1表示為任意，讓系統自動計算
print a1
a2=mat.flatten()
print a2

顯示為：

a1:  [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
a2:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

可以看出，用reshape進行變換，實際上變換后還是二維數組，兩個方括號，因此只能用flatten.

我們要對圖像求直方圖，就需要先把圖像矩陣進行flatten操作，使之變為一維數組，然后再進行統計。

一、畫灰度圖直方圖

繪圖都可以調用matplotlib.pyplot庫來進行，其中的hist函數可以直接繪制直方圖。

調用方式：

n, bins, patches = plt.hist(arr, bins=50, density = True, facecolor='green', alpha=0.75)

hist的參數非常多，但常用的就這五個，只有第一個是必須的，后面四個可選

arr: 需要計算直方圖的一維數組

bins: 直方圖的柱數，可選項，默認為10

density: 是否將得到的直方圖向量歸一化。默認為False

facecolor: 直方圖顏色

alpha: 透明度

返回值 ：
n: 直方圖向量，是否歸一化由參數設定
bins: 返回各個bin的區間范圍
patches: 返回每個bin里面包含的數據，是一個list
"""

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert('L'))

# 利用hist來繪制直方圖
# 第一個參數為一個一維數組
# 因為hist只接受一維數組作為輸入，所以要用flatten()方法將任意數組按照行優先準則轉化成一個一維數組
# 第二個參數指定bin的個數
n, bins, patches = plt.hist(image.flatten(), bins=256, density = True, facecolor='green', alpha=0.5)

plt.title('影像直方圖 密度')

#設定軸範圍
plt.xlim([0-10, 255+10])
plt.ylim([0, 0.01])

plt.show()

print("------------------------------")  # 30個

plt.hist(image.flatten(), 256, cumulative=True)
plt.title('影像直方圖 累計')
plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

# 檔案 => PIL影像 => 灰階 => np陣列
image = np.array(Image.open(filename).convert('L'))

plt.subplot(1, 2, 1)
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.title(u'原始圖像')
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.title(u'原始直方圖')
plt.hist(image.flatten(), bins=128, density=True)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
二、彩色圖片直方圖
實際上是和灰度直方圖一樣的，只是分別畫出三通道的直方圖，然后疊加在一起。
"""

# 檔案 => PIL影像
image=Image.open(filename)
r, g, b=image.split()

array_r = np.array(r).flatten()
plt.hist(array_r, bins=256, alpha=0.3, density = True, facecolor='r', edgecolor='r', stacked=1)

array_g = np.array(g).flatten()
plt.hist(array_g, bins=256, alpha=0.3, density = True, facecolor='g', edgecolor='g', stacked=1)

array_b = np.array(b).flatten()
plt.hist(array_b, bins=256, alpha=0.3, density = True, facecolor='b', edgecolor='b')

plt.title('影像直方圖 密度 三色分離')
plt.show()
'''
print("------------------------------------------------------------")  # 60個

import pylab

def imresize(im, sz):
    """ 使用PIL对象重新定义图像数组的大小 """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """ 对一幅灰度图像进行直方图均衡化 """
    # 计算图像的直方图
    imhist, bins = pylab.histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()   # 累积分布函数
    cdf = 255 * cdf / cdf[-1]   # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = pylab.interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

def compute_average(imlist):
    """ 计算图像列表的平均图像 """
    # 打开第一幅图像，将其存储在浮点型数组中
    average = array(Image.open(imlist[0]), 'f')
    for imnae in imlist[1:]:
        try:
            average += array(Image.open(imname))
        except:
            print(imname + '...skipped')
        averageim /= len(imlist)

    # 返回uint8类型的平均图像
    return array(averageim, 'uint8')

# 直方图均衡化
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

im = np.array(Image.open(filename).convert('L'))
im2, cdf = histeq(im)

plt.gray()
plt.subplot(221)
plt.title(r'before')
plt.imshow(im)

plt.subplot(222)
plt.title(r'after')
plt.imshow(im2)

plt.subplot(223)
plt.hist(im.flatten(), 128)

plt.subplot(224)
plt.hist(im2.flatten(), 128)

plt.show()

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




