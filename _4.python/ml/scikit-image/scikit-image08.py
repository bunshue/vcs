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

from skimage import io

'''
"""
基本形态学滤波

对图像进行形态学变换。变换对象一般为灰度图或二值图，功能函数放在morphology子模块内。

1、膨胀（dilation)

原理：一般对二值图像进行操作。找到像素值为1的点，将它的邻近像素点都设置成这个值。1值表示白，0值表示黑，因此膨胀操作可以扩大白色值范围，压缩黑色值范围。一般用来扩充边缘或填充小的孔洞。

功能函数：skimage.morphology.dilation(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。
"""

from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.dilation(img,sm.square(5))  #用边长为5的正方形滤波器进行膨胀滤波
dst2=sm.dilation(img,sm.square(15))  #用边长为15的正方形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(131)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(132)
plt.title('morphological image')
plt.imshow(dst1,plt.cm.gray)

plt.subplot(133)
plt.title('morphological image')
plt.imshow(dst2,plt.cm.gray)

plt.show()


"""

分别用边长为5或15的正方形滤波器对棋盘图片进行膨胀操作，结果如下：

可见滤波器的大小，对操作结果的影响非常大。一般设置为奇数。

除了正方形的滤波器外，滤波器的形状还有一些，现列举如下：

morphology.square: 正方形

morphology.disk:  平面圆形

morphology.ball: 球形

morphology.cube: 立方体形

morphology.diamond: 钻石形

morphology.rectangle: 矩形

morphology.star: 星形

morphology.octagon: 八角形

morphology.octahedron： 八面体

注意，如果处理图像为二值图像（只有0和1两个值），则可以调用：

skimage.morphology.binary_dilation(image, selem=None）

用此函数比处理灰度图像要快。

2、腐蚀（erosion)

函数：skimage.morphology.erosion(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。

和膨胀相反的操作，将0值扩充到邻近像素。扩大黑色部分，减小白色部分。可用来提取骨干信息，去掉毛刺，去掉孤立的像素。
"""

from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.erosion(img,sm.square(5))  #用边长为5的正方形滤波器进行膨胀滤波
dst2=sm.erosion(img,sm.square(25))  #用边长为25的正方形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(131)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(132)
plt.title('morphological image')
plt.imshow(dst1,plt.cm.gray)

plt.subplot(133)
plt.title('morphological image')
plt.imshow(dst2,plt.cm.gray)

plt.show()

"""
注意，如果处理图像为二值图像（只有0和1两个值），则可以调用：

skimage.morphology.binary_erosion(image, selem=None）

用此函数比处理灰度图像要快。

3、开运算（opening)

函数：skimage.morphology.openning(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。

先腐蚀再膨胀，可以消除小物体或小斑块。
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.opening(img,sm.disk(9))  #用边长为9的圆形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')

plt.show()

"""
注意，如果处理图像为二值图像（只有0和1两个值），则可以调用：

skimage.morphology.binary_opening(image, selem=None）

用此函数比处理灰度图像要快。

4、闭运算（closing)

函数：skimage.morphology.closing(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。

先膨胀再腐蚀，可用来填充孔洞。
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.closing(img,sm.disk(9))  #用边长为5的圆形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')

plt.show()

"""
注意，如果处理图像为二值图像（只有0和1两个值），则可以调用：

skimage.morphology.binary_closing(image, selem=None）

用此函数比处理灰度图像要快。

5、白帽（white-tophat)

函数：skimage.morphology.white_tophat(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。

将原图像减去它的开运算值，返回比结构化元素小的白点
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.white_tophat(img,sm.square(21))  

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')

plt.show()

"""

6、黑帽（black-tophat)

函数：skimage.morphology.black_tophat(image, selem=None）

selem表示结构元素，用于设定局部区域的形状和大小。

将原图像减去它的闭运算值，返回比结构化元素小的黑点，且将这些黑点反色。
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.black_tophat(img,sm.square(21))  

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('morphological image')
plt.imshow(dst,plt.cm.gray)
plt.axis('off')

plt.show()

'''
print('------------------------------------------------------------')	#60個


"""
高级滤波
本文提供更多更强大的滤波方法，这些方法放在filters.rank子模块内。
这些方法需要用户自己设定滤波器的形状和大小，因此需要导入morphology模块来设定。
1、autolevel
这个词在photoshop里面翻译成自动色阶，用局部直方图来对图片进行滤波分级。
该滤波器局部地拉伸灰度像素值的直方图，以覆盖整个像素值范围。
格式：skimage.filters.rank.autolevel(image, selem）
selem表示结构化元素，用于设定滤波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.autolevel(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)

plt.show()

"""
2、bottomhat 与 tophat

bottomhat: 此滤波器先计算图像的形态学闭运算，然后用原图像减去运算的结果值，有点像黑帽操作。

bottomhat: 此滤波器先计算图像的形态学开运算，然后用原图像减去运算的结果值，有点像白帽操作。

格式：

skimage.filters.rank.bottomhat(image, selem）

skimage.filters.rank.tophat(image, selem）

selem表示结构化元素，用于设定滤波器。

下面是bottomhat滤波的例子：
"""

"""沒有 bottomhat
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.bottomhat(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)

plt.show()
"""

"""
3、enhance_contrast

对比度增强。求出局部区域的最大值和最小值，然后看当前点像素值最接近最大值还是最小值，然后替换为最大值或最小值。

函数： enhance_contrast(image, selem）

selem表示结构化元素，用于设定滤波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.enhance_contrast(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)

plt.show()

"""
4、entropy

求局部熵，熵是使用基为2的对数运算出来的。该函数将局部区域的灰度值分布进行二进制编码，返回编码的最小值。

函数格式：entropy(image, selem）

selem表示结构化元素，用于设定滤波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.entropy(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
5、equalize

均衡化滤波。利用局部直方图对图像进行均衡化滤波。

函数格式：equalize(image, selem）

selem表示结构化元素，用于设定滤波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.equalize(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
6、gradient

返回图像的局部梯度值（如：最大值-最小值），用此梯度值代替区域内所有像素值。

函数格式：gradient(image, selem）

selem表示结构化元素，用于设定滤波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.gradient(img, disk(5))  #半径为5的圆形滤波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
7、其它滤波器

滤波方式很多，下面不再一一详细讲解，仅给出核心代码，所有的函数调用方式都是一样的。

最大值滤波器（maximum):返回图像局部区域的最大值，用此最大值代替该区域内所有像素值。

dst =sfr.maximum(img, disk(5)) 

最小值滤波器（minimum)：返回图像局部区域内的最小值，用此最小值取代该区域内所有像素值。

dst =sfr.minimum(img, disk(5))

均值滤波器（mean) : 返回图像局部区域内的均值，用此均值取代该区域内所有像素值。

dst =sfr.mean(img, disk(5)) 

中值滤波器（median): 返回图像局部区域内的中值，用此中值取代该区域内所有像素值。

dst =sfr.median(img, disk(5))

莫代尔滤波器（modal) : 返回图像局部区域内的modal值，用此值取代该区域内所有像素值。

dst =sfr.modal(img, disk(5))

otsu阈值滤波（otsu): 返回图像局部区域内的otsu阈值，用此值取代该区域内所有像素值。

dst =sfr.otsu(img, disk(5))

阈值滤波（threshhold): 将图像局部区域中的每个像素值与均值比较，大于则赋值为1，小于赋值为0，得到一个二值图像。

dst =sfr.threshold(img, disk(5)) 

减均值滤波（subtract_mean):  将局部区域中的每一个像素，减去该区域中的均值。

dst =sfr.subtract_mean(img, disk(5))

求和滤波（sum) :求局部区域的像素总和，用此值取代该区域内所有像素值。

dst =sfr.sum(img, disk(5))
"""



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


