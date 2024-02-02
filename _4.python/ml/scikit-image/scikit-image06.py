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
#直方圖與均衡化

在圖像處理中，直方圖是非常重要，也是非常有用的一個處理要素。

在skimage庫中對直方圖的處理，是放在exposure這個模塊中。

1、計算直方圖

函數：skimage.exposure.histogram(image, nbins=256)

在numpy包中，也提供了一個計算直方圖的函數histogram(),兩者大同小義。

返回一個tuple（hist, bins_center), 前一個數組是直方圖的統計量，后一個數組是每個bin的中間值
"""

import numpy as np
from skimage import exposure,data
image =data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包計算直方圖
hist2=exposure.histogram(image, nbins=2)  #用skimage計算直方圖
print(hist1)
print(hist2)

#(array([107432, 154712], dtype=int64), array([ 0. , 127.5, 255. ]))
#(array([107432, 154712], dtype=int64), array([ 63.75, 191.25]))
#分成兩個bin，每個bin的統計量是一樣的，但numpy返回的是每個bin的兩端的范圍值，而skimage返回的是每個bin的中間值

"""
2、繪制直方圖

繪圖都可以調用matplotlib.pyplot庫來進行，其中的hist函數可以直接繪制直方圖。

調用方式：

n, bins, patches = plt.hist(arr, bins=10, density=False, facecolor='black', edgecolor='black',alpha=1，histtype='bar')

hist的參數非常多，但常用的就這六個，只有第一個是必須的，后面四個可選

arr: 需要計算直方圖的一維數組

bins: 直方圖的柱數，可選項，默認為10

density: 是否將得到的直方圖向量歸一化。默認為False

facecolor: 直方圖顏色

edgecolor: 直方圖邊框顏色

alpha: 透明度

histtype: 直方圖類型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’

返回值 ：

n: 直方圖向量，是否歸一化由參數density設定

bins: 返回各個bin的區間范圍

patches: 返回每個bin里面包含的數據，是一個list
"""

from skimage import data
import matplotlib.pyplot as plt
img = data.camera()
plt.figure("hist")
arr = img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density = True, edgecolor='None',facecolor='red')
plt.show()

"""
其中的flatten()函數是numpy包里面的，用于將二維數組序列化成一維數組。
是按行序列，如
mat=[[1 2 3
　　　  4 5 6]]

經過 mat.flatten()后，就變成了

mat=[1 2 3 4 5 6]

3、彩色圖片三通道直方圖

一般來說直方圖都是征對灰度圖的，如果要畫rgb圖像的三通道直方圖，實際上就是三個直方圖的疊加。

"""

from skimage import data
import matplotlib.pyplot as plt
img=data.astronaut()
ar=img[:,:,0].flatten()
plt.hist(ar, bins=256, density = True, facecolor='r',edgecolor='r',stacked=1)
ag=img[:,:,1].flatten()
plt.hist(ag, bins=256, density = True, facecolor='g',edgecolor='g',stacked=1)
ab=img[:,:,2].flatten()
plt.hist(ab, bins=256, density = True, facecolor='b',edgecolor='b')
plt.show()

"""
其中，加一個參數hold=1,表示可以疊加

4、直方圖均衡化

如果一副圖像的像素占有很多的灰度級而且分布均勻，那么這樣的圖像往往有高對比度和多變的灰度色調。直方圖均衡化就是一種能僅靠輸入圖像直方圖信息自動達到這種效果的變換函數。它的基本思想是對圖像中像素個數多的灰度級進行展寬，而對圖像中像素個數少的灰度進行壓縮，從而擴展取值的動態范圍，提高了對比度和灰度色調的變化，使圖像更加清晰。
"""

from skimage import data,exposure
import matplotlib.pyplot as plt
img=data.moon()
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始圖像
plt.subplot(222)
plt.hist(arr, bins=256, density = True, edgecolor='None',facecolor='red') #原始圖像直方圖

img1=exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化圖像
plt.subplot(224)
plt.hist(arr1, bins=256, density = True,edgecolor='None',facecolor='red') #均衡化直方圖

plt.show()

print('------------------------------------------------------------')	#60個

"""
圖像簡單濾波

對圖像進行濾波，可以有兩種效果：一種是平滑濾波，用來抑制噪聲；另一種是微分算子，可以用來檢測邊緣和特征提取。

skimage庫中通過filters模塊進行濾波操作。

1、sobel算子

sobel算子可用來檢測邊緣

函數格式為：skimage.filters.sobel(image, mask=None)
"""

from skimage import data,filters
import matplotlib.pyplot as plt
img = data.camera()
edges = filters.sobel(img)
plt.imshow(edges,plt.cm.gray)
plt.show()

"""
2、roberts算子

roberts算子和sobel算子一樣，用于檢測邊緣

調用格式也是一樣的：

edges = filters.roberts(img)

3、scharr算子

功能同sobel，調用格式：

edges = filters.scharr(img)

4、prewitt算子

功能同sobel，調用格式：

edges = filters.prewitt(img)

5、canny算子

canny算子也是用于提取邊緣特征，但它不是放在filters模塊，而是放在feature模塊

函數格式：skimage.feature.canny(image，sigma=1.0)

可以修改sigma的值來調整效果
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

從結果可以看出，sigma越小，邊緣線條越細小。

6、gabor濾波

gabor濾波可用來進行邊緣檢測和紋理特征提取。

函數調用格式：skimage.filters.gabor_filter(image, frequency)

通過修改frequency值來調整濾波效果，返回一對邊緣結果，一個是用真實濾波核的濾波結果，一個是想象的濾波核的濾波結果。
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

以上為frequency=0.6的結果圖。

以上為frequency=0.1的結果圖

7、gaussian濾波

多維的濾波器，是一種平滑濾波，可以消除高斯噪聲。

調用函數為：skimage.filters.gaussian_filter(image, sigma)

通過調節sigma的值來調整濾波效果
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
可見sigma越大，過濾后的圖像越模糊

8.median

中值濾波，一種平滑濾波，可以消除噪聲。

需要用skimage.morphology模塊來設置濾波器的形狀。
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
從結果可以看出，濾波器越大，圖像越模糊。

9、水平、垂直邊緣檢測

上邊所舉的例子都是進行全部邊緣檢測，有些時候我們只需要檢測水平邊緣，或垂直邊緣，就可用下面的方法。

水平邊緣檢測：sobel_h, prewitt_h, scharr_h

垂直邊緣檢測： sobel_v, prewitt_v, scharr_v
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

上邊左圖為檢測出的水平邊緣，右圖為檢測出的垂直邊緣。

10、交叉邊緣檢測

可使用Roberts的十字交叉核來進行過濾，以達到檢測交叉邊緣的目的。這些交叉邊緣實際上是梯度在某個方向上的一個分量。

其中一個核：

 0   1
-1   0

對應的函數：

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
另外一個核：

1   0
0  -1

對應函數為：

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

print('------------------------------------------------------------')	#60個

"""
圖像自動閾值分割

圖像閾值分割是一種廣泛應用的分割技術，利用圖像中要提取的目標區域與其背景在灰度特性上的差異，把圖像看作具有不同灰度級的兩類區域(目標區域和背景區域)的組合，選取一個比較合理的閾值，以確定圖像中每個像素點應該屬于目標區域還是背景區域，從而產生相應的二值圖像。

在skimage庫中，閾值分割的功能是放在filters模塊中。

我們可以手動指定一個閾值，從而來實現分割。也可以讓系統自動生成一個閾值，下面幾種方法就是用來自動生成閾值。

1、threshold_otsu

基于Otsu的閾值分割方法，函數調用格式：

skimage.filters.threshold_otsu(image, nbins=256)

參數image是指灰度圖像，返回一個閾值。
"""

from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera()
thresh = filters.threshold_otsu(image)   #返回一個閾值
dst =(image <= thresh)*1.0   #根據閾值進行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""

返回閾值為87，根據87進行分割得下圖:

2、threshold_yen

使用方法同上：

thresh = filters.threshold_yen(image) 

返回閾值為198，分割如下圖：

3、threshold_li

使用方法同上：

thresh = filters.threshold_li(image)

返回閾值64.5，分割如下圖：

4、threshold_isodata

閾值計算方法：

threshold = (image[image <= threshold].mean() +image[image > threshold].mean()) / 2.0

使用方法同上：

thresh = filters.threshold_isodata(image)

返回閾值為87，因此分割效果和threshold_otsu一樣。

5、threshold_adaptive

調用函數為：

skimage.filters.threshold_adaptive(image, block_size, method='gaussian'）

block_size: 塊大小，指當前像素的相鄰區域大小，一般是奇數（如3，5，7。。。）

method: 用來確定自適應閾值的方法，有'mean', 'generic', 'gaussian' 和 'median'。省略時默認為gaussian

該函數直接訪問一個閾值后的圖像，而不是閾值。
"""
"""
#沒有 threshold_adaptive
from skimage import data,filters
import matplotlib.pyplot as plt
image = data.camera()
dst =filters.threshold_adaptive(image, 15) #返回一個閾值圖像

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

大家可以修改block_size的大小和method值來查看更多的效果。如：

dst1 =filters.threshold_adaptive(image,31,'mean') 
dst2 =filters.threshold_adaptive(image,5,'median')
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

