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
#對比度與亮度調整

圖像亮度與對比度的調整，是放在skimage包的exposure模塊里面

1、gamma調整

原理：I=Ig

對原圖像的像素，進行冪運算，得到新的像素值。公式中的g就是gamma值。

如果gamma>1, 新圖像比原圖像暗

如果gamma<1,新圖像比原圖像亮

函數格式為：skimage.exposure.adjust_gamma(image, gamma=1)

gamma參數默認為1，原像不發生變化 。
"""

from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
image = img_as_float(data.moon())
gam1= exposure.adjust_gamma(image, 2)   #調暗
gam2= exposure.adjust_gamma(image, 0.5)  #調亮
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(133)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.show()

"""
2、log對數調整

這個剛好和gamma相反

原理：I=log(I)
"""

from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
image = img_as_float(data.moon())
gam1= exposure.adjust_log(image)   #對數調整
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(121)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('log')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.show()

"""
3、判斷圖像對比度是否偏低
函數：is_low_contrast(img)
返回一個bool型值
"""

from skimage import data, exposure
image =data.moon()
result=exposure.is_low_contrast(image)
print(result)

#輸出為False

"""
4、調整強度

函數：skimage.exposure.rescale_intensity(image, in_range='image', out_range='dtype')

in_range 表示輸入圖片的強度范圍，默認為'image', 表示用圖像的最大/最小像素值作為范圍

out_range 表示輸出圖片的強度范圍，默認為'dype', 表示用圖像的類型的最大/最小值作為范圍

默認情況下，輸入圖片的[min,max]范圍被拉伸到[dtype.min, dtype.max]，如果dtype=uint8, 那么dtype.min=0, dtype.max=255
"""

import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
mat=exposure.rescale_intensity(image)
print(mat)

#輸出為[  0 127 255]
#即像素最小值由51變為0，最大值由153變為255，整體進行了拉伸，但是數據類型沒有變，還是uint8
#前面我們講過，可以通過img_as_float()函數將unit8類型轉換為float型，實際上還有更簡單的方法，就是乘以1.0

import numpy as np
image = np.array([51, 102, 153], dtype=np.uint8)
print(image*1.0)

#即由[51,102,153]變成了[  51.  102.  153.]
#而float類型的范圍是[0,1]，因此對float進行rescale_intensity 調整后，范圍變為[0,1],而不是[0,255]

import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=exposure.rescale_intensity(tmp)
print(mat)

#結果為[ 0.   0.5  1. ]
#如果原始像素值不想被拉伸，只是等比例縮小，就使用in_range參數，如：

import numpy as np
from skimage import exposure
image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=exposure.rescale_intensity(tmp,in_range=(0,255))
print(mat)

#輸出為：[ 0.2  0.4  0.6]，即原像素值除以255
#如果參數in_range的[main,max]范圍要比原始像素值的范圍[min,max] 大或者小，那就進行裁剪，如：

mat=exposure.rescale_intensity(tmp,in_range=(0,102))
print(mat)

#輸出[ 0.5  1.   1. ]，即原像素值除以102，超出1的變為1
#如果一個數組里面有負數，現在想調整到正數，就使用out_range參數。如：

import numpy as np
from skimage import exposure
image = np.array([-10, 0, 10], dtype=np.int8)
mat=exposure.rescale_intensity(image, out_range=(0, 127))
print(mat)

#輸出[  0  63 127]



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


