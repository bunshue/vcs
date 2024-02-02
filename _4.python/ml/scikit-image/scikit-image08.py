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
基本形態學濾波

對圖像進行形態學變換。變換對象一般為灰度圖或二值圖，功能函數放在morphology子模塊內。

1、膨脹（dilation)

原理：一般對二值圖像進行操作。找到像素值為1的點，將它的鄰近像素點都設置成這個值。1值表示白，0值表示黑，因此膨脹操作可以擴大白色值范圍，壓縮黑色值范圍。一般用來擴充邊緣或填充小的孔洞。

功能函數：skimage.morphology.dilation(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。
"""

from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.dilation(img,sm.square(5))  #用邊長為5的正方形濾波器進行膨脹濾波
dst2=sm.dilation(img,sm.square(15))  #用邊長為15的正方形濾波器進行膨脹濾波

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

分別用邊長為5或15的正方形濾波器對棋盤圖片進行膨脹操作，結果如下：

可見濾波器的大小，對操作結果的影響非常大。一般設置為奇數。

除了正方形的濾波器外，濾波器的形狀還有一些，現列舉如下：

morphology.square: 正方形

morphology.disk:  平面圓形

morphology.ball: 球形

morphology.cube: 立方體形

morphology.diamond: 鉆石形

morphology.rectangle: 矩形

morphology.star: 星形

morphology.octagon: 八角形

morphology.octahedron： 八面體

注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_dilation(image, selem=None）

用此函數比處理灰度圖像要快。

2、腐蝕（erosion)

函數：skimage.morphology.erosion(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

和膨脹相反的操作，將0值擴充到鄰近像素。擴大黑色部分，減小白色部分。可用來提取骨干信息，去掉毛刺，去掉孤立的像素。
"""

from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=data.checkerboard()
dst1=sm.erosion(img,sm.square(5))  #用邊長為5的正方形濾波器進行膨脹濾波
dst2=sm.erosion(img,sm.square(25))  #用邊長為25的正方形濾波器進行膨脹濾波

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
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_erosion(image, selem=None）

用此函數比處理灰度圖像要快。

3、開運算（opening)

函數：skimage.morphology.openning(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

先腐蝕再膨脹，可以消除小物體或小斑塊。
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.opening(img,sm.disk(9))  #用邊長為9的圓形濾波器進行膨脹濾波

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
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_opening(image, selem=None）

用此函數比處理灰度圖像要快。

4、閉運算（closing)

函數：skimage.morphology.closing(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

先膨脹再腐蝕，可用來填充孔洞。
"""

from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
img=color.rgb2gray(io.imread('data/mor.bmp'))
dst=sm.closing(img,sm.disk(9))  #用邊長為5的圓形濾波器進行膨脹濾波

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
注意，如果處理圖像為二值圖像（只有0和1兩個值），則可以調用：

skimage.morphology.binary_closing(image, selem=None）

用此函數比處理灰度圖像要快。

5、白帽（white-tophat)

函數：skimage.morphology.white_tophat(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

將原圖像減去它的開運算值，返回比結構化元素小的白點
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

函數：skimage.morphology.black_tophat(image, selem=None）

selem表示結構元素，用于設定局部區域的形狀和大小。

將原圖像減去它的閉運算值，返回比結構化元素小的黑點，且將這些黑點反色。
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
高級濾波
本文提供更多更強大的濾波方法，這些方法放在filters.rank子模塊內。
這些方法需要用戶自己設定濾波器的形狀和大小，因此需要導入morphology模塊來設定。
1、autolevel
這個詞在photoshop里面翻譯成自動色階，用局部直方圖來對圖片進行濾波分級。
該濾波器局部地拉伸灰度像素值的直方圖，以覆蓋整個像素值范圍。
格式：skimage.filters.rank.autolevel(image, selem）
selem表示結構化元素，用于設定濾波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.autolevel(img, disk(5))  #半徑為5的圓形濾波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(auto,plt.cm.gray)

plt.show()

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
from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.bottomhat(img, disk(5))  #半徑為5的圓形濾波器

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

對比度增強。求出局部區域的最大值和最小值，然后看當前點像素值最接近最大值還是最小值，然后替換為最大值或最小值。

函數： enhance_contrast(image, selem）

selem表示結構化元素，用于設定濾波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
auto =sfr.enhance_contrast(img, disk(5))  #半徑為5的圓形濾波器

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

求局部熵，熵是使用基為2的對數運算出來的。該函數將局部區域的灰度值分布進行二進制編碼，返回編碼的最小值。

函數格式：entropy(image, selem）

selem表示結構化元素，用于設定濾波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.entropy(img, disk(5))  #半徑為5的圓形濾波器

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

均衡化濾波。利用局部直方圖對圖像進行均衡化濾波。

函數格式：equalize(image, selem）

selem表示結構化元素，用于設定濾波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.equalize(img, disk(5))  #半徑為5的圓形濾波器

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

返回圖像的局部梯度值（如：最大值-最小值），用此梯度值代替區域內所有像素值。

函數格式：gradient(image, selem）

selem表示結構化元素，用于設定濾波器。
"""

from skimage import data,color
import matplotlib.pyplot as plt
from skimage.morphology import disk
import skimage.filters.rank as sfr
#img =color.rgb2gray(data.lena())
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
img=io.imread(filename, True)   #True:轉為灰階
dst =sfr.gradient(img, disk(5))  #半徑為5的圓形濾波器

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
7、其它濾波器

濾波方式很多，下面不再一一詳細講解，僅給出核心代碼，所有的函數調用方式都是一樣的。

最大值濾波器（maximum):返回圖像局部區域的最大值，用此最大值代替該區域內所有像素值。

dst =sfr.maximum(img, disk(5)) 

最小值濾波器（minimum)：返回圖像局部區域內的最小值，用此最小值取代該區域內所有像素值。

dst =sfr.minimum(img, disk(5))

均值濾波器（mean) : 返回圖像局部區域內的均值，用此均值取代該區域內所有像素值。

dst =sfr.mean(img, disk(5)) 

中值濾波器（median): 返回圖像局部區域內的中值，用此中值取代該區域內所有像素值。

dst =sfr.median(img, disk(5))

莫代爾濾波器（modal) : 返回圖像局部區域內的modal值，用此值取代該區域內所有像素值。

dst =sfr.modal(img, disk(5))

otsu閾值濾波（otsu): 返回圖像局部區域內的otsu閾值，用此值取代該區域內所有像素值。

dst =sfr.otsu(img, disk(5))

閾值濾波（threshhold): 將圖像局部區域中的每個像素值與均值比較，大于則賦值為1，小于賦值為0，得到一個二值圖像。

dst =sfr.threshold(img, disk(5)) 

減均值濾波（subtract_mean):  將局部區域中的每一個像素，減去該區域中的均值。

dst =sfr.subtract_mean(img, disk(5))

求和濾波（sum) :求局部區域的像素總和，用此值取代該區域內所有像素值。

dst =sfr.sum(img, disk(5))
"""



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

