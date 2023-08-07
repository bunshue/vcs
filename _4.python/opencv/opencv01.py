filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('取得 OpenCV 版本')

import cv2

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print('----------------------------------------------------------------------')	#70個
print('旋轉圖片')

#影像旋轉
#以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

image = cv2.imread(filename)	#讀取本機圖片

h, w, d = image.shape   #d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w//2, h//2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.7)

rotate_image = cv2.warpAffine(image, P, (w, h))

cv2.imshow('Rotate CW 30 ratio = 0.7', rotate_image)#顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('----------------------------------------------------------------------')	#70個
#影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

import numpy as np

image_original = cv2.imread(filename)	#讀取本機圖片

#縮放的倍率 fx fy
image_resized = cv2.resize(image_original, None, fx = 1.50, fy = 1.00, interpolation = cv2.INTER_LINEAR)

cv2.imshow('Original Picture', image_original) #顯示圖片
cv2.imshow('Resized Picture', image_resized) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('----------------------------------------------------------------------')	#70個

#影像對比與亮度調整
import numpy as np
import matplotlib.image as img

# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(image, alpha=1.0, beta = 0.0):
    array_alpha = np.array([alpha]) #對比度
    array_beta = np.array([beta]) #亮度
    image = cv2.add(image, array_beta)
    image = cv2.multiply(image, array_alpha)
    image = np.clip(image, 0, 255)
    return image

image = cv2.imread(filename)	#讀取本機圖片

modified_image = modify_contrast_and_brightness(image, 1.5, 10.0)
cv2.imshow('Modified Picture', modified_image) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('----------------------------------------------------------------------')	#70個


#影像分析工具
#影像直方圖

import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

plt.hist(image.ravel(), 256, [0,256])
cv2.imshow('GrayScale Picture', image) #顯示圖片
plt.show()


print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('----------------------------------------------------------------------')	#70個

#直方圖影像操作
#直方圖均值化

import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

equa = cv2.equalizeHist(image)
cv2.imshow('Histogram', equa)#顯示圖片
plt.hist(equa.ravel(), 256, [0,256])
plt.show()
#均值化的影像
#均衡化後的灰度直方圖分布

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('----------------------------------------------------------------------')	#70個


'''
cv2.imshow('視窗標題 不支持中文', image) #顯示圖片

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()




'''


