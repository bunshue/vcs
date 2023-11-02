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
高级形态学处理

形态学处理，除了最基本的膨胀、腐蚀、开/闭运算、黑/白帽处理外，还有一些更高级的运用，如凸包，连通区域标记，删除小块区域等。

1、凸包

凸包是指一个凸多边形，这个凸多边形将图片中所有的白色像素点都包含在内。

函数为：

skimage.morphology.convex_hull_image(image)

输入为二值图像，输出一个逻辑二值图像。在凸包内的点为True, 否则为False

"""
""" pic NG
import matplotlib.pyplot as plt
from skimage import data,color,morphology

#生成二值测试图像
img=color.rgb2gray(data.horse())
img=(img<0.5)*1

chull = morphology.convex_hull_image(img)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

plt.show()
"""

"""
convex_hull_image()是将图片中的所有目标看作一个整体，因此计算出来只有一个最小凸多边形。如果图中有多个目标物体，每一个物体需要计算一个最小凸多边形，则需要使用convex_hull_object（）函数。

函数格式：skimage.morphology.convex_hull_object(image, neighbors=8)

输入参数image是一个二值图像，neighbors表示是采用4连通还是8连通，默认为8连通。

"""

""" NG
import matplotlib.pyplot as plt
from skimage import data,color,morphology,feature

#生成二值测试图像
img=color.rgb2gray(data.coins())
#检测canny边缘,得到二值图片
edgs=feature.canny(img, sigma=3, low_threshold=10, high_threshold=50) 

chull = morphology.convex_hull_object(edgs)

#绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(edgs,plt.cm.gray)
ax0.set_title('many objects')
ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

plt.show()
"""


"""
2、连通区域标记

在二值图像中，如果两个像素点相邻且值相同（同为0或同为1），那么就认为这两个像素点在一个相互连通的区域内。而同一个连通区域的所有像素点，都用同一个数值来进行标记，这个过程就叫连通区域标记。在判断两个像素是否相邻时，我们通常采用4连通或8连通判断。在图像中，最小的单位是像素，每个像素周围有8个邻接像素，常见的邻接关系有2种：4邻接与8邻接。4邻接一共4个点，即上下左右，如下左图所示。8邻接的点一共有8个，包括了对角线位置的点，如下右图所示。

在skimage包中，我们采用measure子模块下的label（）函数来实现连通区域标记。

函数格式：

skimage.measure.label（image,connectivity=None)

参数中的image表示需要处理的二值图像，connectivity表示连接的模式，1代表4邻接，2代表8邻接。

输出一个标记数组（labels), 从0开始标记。

"""

import numpy as np
import scipy.ndimage as ndi
from skimage import measure,color
import matplotlib.pyplot as plt

#编写一个函数来生成原始二值图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  #随机数种子
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯滤波
    return mask > mask.mean()

data = microstructure(l=128)*1 #生成测试图片

labels=measure.label(data,connectivity=2)  #8连通区域标记
dst=color.label2rgb(labels)  #根据不同的标记显示不同的颜色
print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()

"""
在代码中，有些地方乘以1，则可以将bool数组快速地转换为int数组。

结果如图：有10个连通的区域，标记为0-9

如果想分别对每一个连通区域进行操作，比如计算面积、外接矩形、凸包面积等，则需要调用measure子模块的regionprops（）函数。该函数格式为：

skimage.measure.regionprops(label_image)

返回所有连通区块的属性列表，常用的属性列表如下表：
属性名称 	类型 	描述
area 	int 	区域内像素点总数
bbox 	tuple 	边界外接框(min_row, min_col, max_row, max_col)
centroid 	array　　 	质心坐标
convex_area 	int 	凸包内像素点总数
convex_image 	ndarray 	和边界外接框同大小的凸包　　
coords 	ndarray 	区域内像素点坐标
Eccentricity  	float 	离心率
equivalent_diameter  	float 	和区域面积相同的圆的直径
euler_number 	int　　 	区域欧拉数
extent  	float 	区域面积和边界外接框面积的比率
filled_area 	int 	区域和外接框之间填充的像素点总数
perimeter  	float 	区域周长
label 	int 	区域标记

3、删除小块区域

有些时候，我们只需要一些大块区域，那些零散的、小块的区域，我们就需要删除掉，则可以使用morphology子模块的remove_small_objects（)函数。

函数格式：skimage.morphology.remove_small_objects(ar, min_size=64, connectivity=1, in_place=False)

参数：

ar: 待操作的bool型数组。

min_size: 最小连通区域尺寸，小于该尺寸的都将被删除。默认为64.

connectivity: 邻接模式，1表示4邻接，2表示8邻接

in_place: bool型值，如果为True,表示直接在输入图像中删除小块区域，否则进行复制后再删除。默认为False.

返回删除了小块区域的二值图像。
"""

import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#编写一个函数来生成原始二值图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  #随机数种子
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯滤波
    return mask > mask.mean()

data = microstructure(l=128) #生成测试图片

dst=morphology.remove_small_objects(data,min_size=300,connectivity=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax2.imshow(dst,plt.cm.gray,interpolation='nearest')

fig.tight_layout()
plt.show()

"""
在此例中，我们将面积小于300的小块区域删除（由1变为0），结果如下图：

 4、综合示例：阈值分割+闭运算+连通区域标记+删除小区块+分色显示
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data,filters,segmentation,measure,morphology,color

#加载并裁剪硬币图片
image = data.coins()[50:-50, 50:-50]

thresh =filters.threshold_otsu(image) #阈值分割
bw =morphology.closing(image > thresh, morphology.square(3)) #闭运算

cleared = bw.copy()  #复制
segmentation.clear_border(cleared)  #清除与边界相连的目标物

label_image =measure.label(cleared)  #连通区域标记
borders = np.logical_xor(bw, cleared) #异或
label_image[borders] = -1
image_label_overlay =color.label2rgb(label_image, image=image) #不同标记用不同颜色显示

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(cleared,plt.cm.gray)
ax1.imshow(image_label_overlay)

for region in measure.regionprops(label_image): #循环得到每一个连通区域属性集
    
    #忽略小区域
    if region.area < 100:
        continue

    #绘制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax1.add_patch(rect)
fig.tight_layout()
plt.show()

'''

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""
骨架提取与分水岭算法

骨架提取与分水岭算法也属于形态学处理范畴，都放在morphology子模块内。

1、骨架提取

骨架提取，也叫二值图像细化。这种算法能将一个连通区域细化成一个像素的宽度，用于特征提取和目标拓扑表示。

morphology子模块提供了两个函数用于骨架提取，分别是Skeletonize（）函数和medial_axis（）函数。我们先来看Skeletonize（）函数。

格式为：skimage.morphology.skeletonize(image)

输入和输出都是一幅二值图像。
"""

from skimage import morphology,draw
import numpy as np
import matplotlib.pyplot as plt

#创建一个二值图像用于测试
image = np.zeros((400, 400))

#生成目标对象1(白色U型)
image[10:-10, 10:100] = 1
image[-100:-10, 10:-10] = 1
image[10:-10, -100:-10] = 1

#生成目标对象2（X型）
rs, cs = draw.line(250, 150, 10, 280)
for i in range(10):
    image[rs + i, cs] = 1
rs, cs = draw.line(10, 150, 250, 280)
for i in range(20):
    image[rs + i, cs] = 1

#生成目标对象3（O型）
ir, ic = np.indices(image.shape)
circle1 = (ic - 135)**2 + (ir - 150)**2 < 30**2
circle2 = (ic - 135)**2 + (ir - 150)**2 < 20**2
image[circle1] = 1
image[circle2] = 0

#实施骨架算法
skeleton =morphology.skeletonize(image)

#显示结果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()

"""
生成一幅测试图像，上面有三个目标对象，分别进行骨架提取，结果如下：

例2：利用系统自带的马图片进行骨架提取
"""

""" pic NG
from skimage import morphology,data,color
import matplotlib.pyplot as plt

image=color.rgb2gray(data.horse())
image=1-image #反相
#实施骨架算法
skeleton =morphology.skeletonize(image)

#显示结果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
"""

"""
medial_axis就是中轴的意思，利用中轴变换方法计算前景（1值）目标对象的宽度，格式为：

skimage.morphology.medial_axis(image, mask=None, return_distance=False)

mask: 掩模。默认为None, 如果给定一个掩模，则在掩模内的像素值才执行骨架算法。

return_distance: bool型值，默认为False. 如果为True, 则除了返回骨架，还将距离变换值也同时返回。这里的距离指的是中轴线上的所有点与背景点的距离。
"""

import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#编写一个函数，生成测试图像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n))
    return mask > mask.mean()

data = microstructure(l=64) #生成测试图像

#计算中轴和距离变换值
skel, distance =morphology.medial_axis(data, return_distance=True)

#中轴上的点到背景像素点的距离
dist_on_skel = distance * skel

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
#用光谱色显示中轴
#ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
ax2.imshow(dist_on_skel, interpolation='nearest')
ax2.contour(data, [0.5], colors='w')  #显示轮廓线

fig.tight_layout()
plt.show()

"""
2、分水岭算法

分水岭在地理学上就是指一个山脊，水通常会沿着山脊的两边流向不同的“汇水盆”。分水岭算法是一种用于图像分割的经典算法，是基于拓扑理论的数学形态学的分割方法。如果图像中的目标物体是连在一起的，则分割起来会更困难，分水岭算法经常用于处理这类问题，通常会取得比较好的效果。

分水岭算法可以和距离变换结合，寻找“汇水盆地”和“分水岭界限”，从而对图像进行分割。二值图像的距离变换就是每一个像素点到最近非零值像素点的距离，我们可以使用scipy包来计算距离变换。

在下面的例子中，需要将两个重叠的圆分开。我们先计算圆上的这些白色像素点到黑色背景像素点的距离变换，选出距离变换中的最大值作为初始标记点（如果是反色的话，则是取最小值），从这些标记点开始的两个汇水盆越集越大，最后相交于分山岭。从分山岭处断开，我们就得到了两个分离的圆。

例1：基于距离变换的分山岭图像分割
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature

#创建两个带有重叠圆的图像
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1)**2 + (y - y1)**2 < r1**2
mask_circle2 = (x - x2)**2 + (y - y2)**2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

#现在我们用分水岭算法分离两个圆
distance = ndi.distance_transform_edt(image) #距离变换
#local_maxi =feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
#                            labels=image)   #寻找峰值
local_maxi =feature.peak_local_max(distance, footprint=np.ones((3, 3)),
                            labels=image)   #寻找峰值

markers = ndi.label(local_maxi)[0] #初始标记点
"""沒有watershed
labels =morphology.watershed(-distance, markers, mask=image) #基于距离变换的分水岭算法

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
plt.show()
"""

"""

分水岭算法也可以和梯度相结合，来实现图像分割。一般梯度图像在边缘处有较高的像素值，而在其它地方则有较低的像素值，理想情况 下，分山岭恰好在边缘。因此，我们可以根据梯度来寻找分山岭。

例2：基于梯度的分水岭图像分割
"""

""" pic NG
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,color,data,filters

image =color.rgb2gray(data.camera())
denoised = filter.rank.median(image, morphology.disk(2)) #过滤噪声

#将梯度值低于10的作为开始标记点
markers = filters.rank.gradient(denoised, morphology.disk(5)) <10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denoised, morphology.disk(2)) #计算梯度
labels =morphology.watershed(gradient, markers, mask=image) #基于梯度的分水岭算法

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
plt.show()

"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

