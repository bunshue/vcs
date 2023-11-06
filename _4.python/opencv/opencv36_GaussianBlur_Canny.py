"""

GaussianBlur

Canny


"""

import cv2

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
image = cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("original", image)

# 高斯模糊，Canny边缘检测需要的
image = cv2.GaussianBlur(image, (5, 5), 0)    #執行高斯模糊化
cv2.imshow('GaussianBlur', image)

# 进行边缘检测，减少图像空间中需要检测的点数量
image = cv2.Canny(image, 50, 150)
cv2.imshow('Canny', image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('模糊效果')

img = cv2.imread(filename)

Img_blur = cv2.GaussianBlur(img, (49, 49), 3)   #執行高斯模糊化
cv2.imshow('Sample pic', Img_blur)

print('------------------------------------------------------------')	#60個


#Gaussian lowpass filter

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 GaussianBlur 效果 1')
kernel_size = (5, 5)   #卷積的矩陣大小 ksize 指定區域單位 ( 必須是大於 1 的奇數 )
sigma = 0       #sigma值     sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
r = cv2.GaussianBlur(o, kernel_size, 0) #執行高斯模糊化
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(filename)

blur = cv2.GaussianBlur(img, (5, 5), 0) #執行高斯模糊化

plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(blur)
plt.title('Blurred')
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp'
o=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 GaussianBlur 效果 2')
g = r = cv2.GaussianBlur(o, (55, 55), 0) #執行高斯模糊化
cv2.imshow("Gaussian",g)

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



