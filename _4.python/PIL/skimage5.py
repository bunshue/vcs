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

'''
"""
#直方图与均衡化

在图像处理中，直方图是非常重要，也是非常有用的一个处理要素。

在skimage库中对直方图的处理，是放在exposure这个模块中。

1、计算直方图

函数：skimage.exposure.histogram(image, nbins=256)

在numpy包中，也提供了一个计算直方图的函数histogram(),两者大同小义。

返回一个tuple（hist, bins_center), 前一个数组是直方图的统计量，后一个数组是每个bin的中间值
"""

import numpy as np
from skimage import exposure,data
image =data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
print(hist1)
print(hist2)

#(array([107432, 154712], dtype=int64), array([ 0. , 127.5, 255. ]))
#(array([107432, 154712], dtype=int64), array([ 63.75, 191.25]))
#分成两个bin，每个bin的统计量是一样的，但numpy返回的是每个bin的两端的范围值，而skimage返回的是每个bin的中间值

"""
2、绘制直方图

绘图都可以调用matplotlib.pyplot库来进行，其中的hist函数可以直接绘制直方图。

调用方式：

n, bins, patches = plt.hist(arr, bins=10, normed=0, facecolor='black', edgecolor='black',alpha=1，histtype='bar')

hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选

arr: 需要计算直方图的一维数组

bins: 直方图的柱数，可选项，默认为10

normed: 是否将得到的直方图向量归一化。默认为0

facecolor: 直方图颜色

edgecolor: 直方图边框颜色

alpha: 透明度

histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’

返回值 ：

n: 直方图向量，是否归一化由参数normed设定

bins: 返回各个bin的区间范围

patches: 返回每个bin里面包含的数据，是一个list
"""

from skimage import data
import matplotlib.pyplot as plt
img = data.camera()
plt.figure("hist")
arr = img.flatten()
#n, bins, patches = plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red')
n, bins, patches = plt.hist(arr, bins=256, edgecolor='None',facecolor='red')  
plt.show()

"""
其中的flatten()函数是numpy包里面的，用于将二维数组序列化成一维数组。
是按行序列，如
mat=[[1 2 3
　　　  4 5 6]]

经过 mat.flatten()后，就变成了

mat=[1 2 3 4 5 6]

3、彩色图片三通道直方图

一般来说直方图都是征对灰度图的，如果要画rgb图像的三通道直方图，实际上就是三个直方图的叠加。

"""

from skimage import data
import matplotlib.pyplot as plt
img=data.astronaut()
ar=img[:,:,0].flatten()
#plt.hist(ar, bins=256, normed=1,facecolor='r',edgecolor='r',hold=1)
plt.hist(ar, bins=256, facecolor='r',edgecolor='r')
ag=img[:,:,1].flatten()
#plt.hist(ag, bins=256, normed=1, facecolor='g',edgecolor='g',hold=1)
plt.hist(ag, bins=256, facecolor='g',edgecolor='g')
ab=img[:,:,2].flatten()
#plt.hist(ab, bins=256, normed=1, facecolor='b',edgecolor='b')
plt.hist(ab, bins=256, facecolor='b',edgecolor='b')
plt.show()



"""
其中，加一个参数hold=1,表示可以叠加

4、直方图均衡化

如果一副图像的像素占有很多的灰度级而且分布均匀，那么这样的图像往往有高对比度和多变的灰度色调。直方图均衡化就是一种能仅靠输入图像直方图信息自动达到这种效果的变换函数。它的基本思想是对图像中像素个数多的灰度级进行展宽，而对图像中像素个数少的灰度进行压缩，从而扩展取值的动态范围，提高了对比度和灰度色调的变化，使图像更加清晰。
"""

from skimage import data,exposure
import matplotlib.pyplot as plt
img=data.moon()
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始图像
plt.subplot(222)
#plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图
plt.hist(arr, bins=256, edgecolor='None',facecolor='red') #原始图像直方图

img1=exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化图像
plt.subplot(224)
#plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='red') #均衡化直方图
plt.hist(arr1, bins=256, edgecolor='None',facecolor='red') #均衡化直方图

plt.show()

print('------------------------------------------------------------')	#60個

"""
图像简单滤波

对图像进行滤波，可以有两种效果：一种是平滑滤波，用来抑制噪声；另一种是微分算子，可以用来检测边缘和特征提取。

skimage库中通过filters模块进行滤波操作。

1、sobel算子

sobel算子可用来检测边缘

函数格式为：skimage.filters.sobel(image, mask=None)
"""

from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
edges = filters.sobel(img)
plt.imshow(edges,plt.cm.gray)
plt.show()

"""
2、roberts算子

roberts算子和sobel算子一样，用于检测边缘

调用格式也是一样的：

edges = filters.roberts(img)

3、scharr算子

功能同sobel，调用格式：

edges = filters.scharr(img)

4、prewitt算子

功能同sobel，调用格式：

edges = filters.prewitt(img)

5、canny算子

canny算子也是用于提取边缘特征，但它不是放在filters模块，而是放在feature模块

函数格式：skimage.feature.canny(image，sigma=1.0)

可以修改sigma的值来调整效果
"""

from skimage import data,filters,feature
import matplotlib.pyplot as plt
img = data.camera()
edges1 = feature.canny(img)   #sigma=1
edges2 = feature.canny(img,sigma=3)   #sigma=3

plt.figure('canny',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""

从结果可以看出，sigma越小，边缘线条越细小。

6、gabor滤波

gabor滤波可用来进行边缘检测和纹理特征提取。

函数调用格式：skimage.filters.gabor_filter(image, frequency)

通过修改frequency值来调整滤波效果，返回一对边缘结果，一个是用真实滤波核的滤波结果，一个是想象的滤波核的滤波结果。
"""

"""
#沒有 gabor_filter

from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
filt_real, filt_imag = filters.gabor_filter(img,frequency=0.6)   

plt.figure('gabor',figsize=(8,8))

plt.subplot(121)
plt.title('filt_real')
plt.imshow(filt_real,plt.cm.gray)  

plt.subplot(122)
plt.title('filt-imag')
plt.imshow(filt_imag,plt.cm.gray)

plt.show()
"""

"""

以上为frequency=0.6的结果图。

以上为frequency=0.1的结果图

7、gaussian滤波

多维的滤波器，是一种平滑滤波，可以消除高斯噪声。

调用函数为：skimage.filters.gaussian_filter(image, sigma)

通过调节sigma的值来调整滤波效果
"""

"""
#沒有 gaussian_filter
from skimage import data,filters
import matplotlib.pyplot as plt
img = data.astronaut()
edges1 = filters.gaussian_filter(img,sigma=0.4)   #sigma=0.4
edges2 = filters.gaussian_filter(img,sigma=5)   #sigma=5

plt.figure('gaussian',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
"""

"""
可见sigma越大，过滤后的图像越模糊

8.median

中值滤波，一种平滑滤波，可以消除噪声。

需要用skimage.morphology模块来设置滤波器的形状。
"""

from skimage import data,filters
import matplotlib.pyplot as plt
from skimage.morphology import disk
img = data.camera()
edges1 = filters.median(img,disk(5))
edges2= filters.median(img,disk(9))

plt.figure('median',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""
从结果可以看出，滤波器越大，图像越模糊。

9、水平、垂直边缘检测

上边所举的例子都是进行全部边缘检测，有些时候我们只需要检测水平边缘，或垂直边缘，就可用下面的方法。

水平边缘检测：sobel_h, prewitt_h, scharr_h

垂直边缘检测： sobel_v, prewitt_v, scharr_v
"""

from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
edges1 = filters.sobel_h(img)  
edges2 = filters.sobel_v(img) 

plt.figure('sobel_v_h',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""

上边左图为检测出的水平边缘，右图为检测出的垂直边缘。

10、交叉边缘检测

可使用Roberts的十字交叉核来进行过滤，以达到检测交叉边缘的目的。这些交叉边缘实际上是梯度在某个方向上的一个分量。

其中一个核：

 0   1
-1   0

对应的函数：

roberts_neg_diag(image）

"""

from skimage import data,filters
import matplotlib.pyplot as plt
img =data.camera()
dst =filters.roberts_neg_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
另外一个核：

1   0
0  -1

对应函数为：

roberts_pos_diag(image）
"""

from skimage import data,filters
import matplotlib.pyplot as plt
img =data.camera()
dst =filters.roberts_pos_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

'''

print('------------------------------------------------------------')	#60個

"""
图像自动阈值分割

图像阈值分割是一种广泛应用的分割技术，利用图像中要提取的目标区域与其背景在灰度特性上的差异，把图像看作具有不同灰度级的两类区域(目标区域和背景区域)的组合，选取一个比较合理的阈值，以确定图像中每个像素点应该属于目标区域还是背景区域，从而产生相应的二值图像。

在skimage库中，阈值分割的功能是放在filters模块中。

我们可以手动指定一个阈值，从而来实现分割。也可以让系统自动生成一个阈值，下面几种方法就是用来自动生成阈值。

1、threshold_otsu

基于Otsu的阈值分割方法，函数调用格式：

skimage.filters.threshold_otsu(image, nbins=256)

参数image是指灰度图像，返回一个阈值。
"""

from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera()
thresh = filters.threshold_otsu(image)   #返回一个阈值
dst =(image <= thresh)*1.0   #根据阈值进行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""

返回阈值为87，根据87进行分割得下图:

2、threshold_yen

使用方法同上：

thresh = filters.threshold_yen(image) 

返回阈值为198，分割如下图：

3、threshold_li

使用方法同上：

thresh = filters.threshold_li(image)

返回阈值64.5，分割如下图：

4、threshold_isodata

阈值计算方法：

threshold = (image[image <= threshold].mean() +image[image > threshold].mean()) / 2.0

使用方法同上：

thresh = filters.threshold_isodata(image)

返回阈值为87，因此分割效果和threshold_otsu一样。

5、threshold_adaptive

调用函数为：

skimage.filters.threshold_adaptive(image, block_size, method='gaussian'）

block_size: 块大小，指当前像素的相邻区域大小，一般是奇数（如3，5，7。。。）

method: 用来确定自适应阈值的方法，有'mean', 'generic', 'gaussian' 和 'median'。省略时默认为gaussian

该函数直接访问一个阈值后的图像，而不是阈值。
"""
"""
#沒有 threshold_adaptive
from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera()
dst =filters.threshold_adaptive(image, 15) #返回一个阈值图像

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()
"""

"""

大家可以修改block_size的大小和method值来查看更多的效果。如：

dst1 =filters.threshold_adaptive(image,31,'mean') 
dst2 =filters.threshold_adaptive(image,5,'median')
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


