filename = 'C:/______test_files/_emgu/lena.jpg'
#filename = 'C:/______test_files/ims01.bmp'

window_name = 'Show Picture'

import cv2

'''
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
img = cv2.imread(filename, 1)   #0: 黑白圖片 1: 原色圖片
cv2.imshow(window_name, img)

cv2.imwrite('aaaaaaa.pgm', img) #無效????


print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
'''

'''
print('使用matplotlib顯示圖片')
import matplotlib.pyplot as plt
img = cv2.imread(filename, 1)   #0: 黑白圖片 1: 原色圖片
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])  #隱藏x座標
plt.yticks([])  #隱藏y座標
plt.show()

'''

import matplotlib.pyplot as plt
print('畫圖')

import numpy as np
img = np.zeros((600, 600, 3))

#畫直線
cv2.line(img, (0, 0), (600, 600), 2)
#畫矩形
cv2.rectangle(img, (50, 50), (250, 250), (255, 255, 0), 2)

#畫圓
cx = 150
cy = 150
r = 100
cv2.circle(img, (cx, cy), r, (255, 255, 0), 2)

#畫橢圓
cx = 300
cy = 300
a = 200  #長軸
b = 100  #短軸
cv2.ellipse(img, (cx, cy), (a, b), 0, 0, 360, (255, 255, 0), 2)

#畫多邊形
px1 = 50
py1 = 400
px2 = 150
py2 = 450
px3 = 170
py3 = 420
px4 = 250
py4 = 510
px5 = 250
py5 = 550

pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5]])
cv2.polylines(img, [pts], True, (255, 255, 0), 2)   #True表示封口

#顯示文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Show English', (300, 500), font, 2, (255, 255, 0), 2)


cv2.imshow('draw picture', img)

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件












































'''
print('取得 OpenCV 版本')
import cv2
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)
'''

'''
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename)	#讀取本機圖片

shape = img.shape
h = shape[0]    #高
w = shape[1]    #寬
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階

print("寬 = ",w,", 高 = ",h,", D = ",d)

cv2.imshow('Original Picture', img) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#裁剪圖片

import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要

x_l, x_r = 150, 350 #保留的部分，由左而右
y_u, y_d = 150, 400 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要



#影像旋轉
#以影像中心為準，順時針旋轉30度 縮小為 0.5 倍

img = cv2.imread(filename)	#讀取本機圖片
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w//2, h//2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.7)

rotate_img = cv2.warpAffine(img, P, (w, h))

cv2.imshow('Rotate CW 30 ratio = 0.7', rotate_img)#顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4
import cv2	#導入 OpenCV 模組
import numpy as np

img_original = cv2.imread(filename)	#讀取本機圖片

#縮放的倍率 fx fy
img_resized = cv2.resize(img_original, None, fx=1.50, fy=1.00, interpolation = cv2.INTER_LINEAR)

cv2.imshow('Original Picture', img_original) #顯示圖片
cv2.imshow('Resized Picture', img_resized) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#影像對比與亮度調整
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.image as img

# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(img, alpha=1.0, beta = 0.0):
    array_alpha = np.array([alpha]) #對比度
    array_beta = np.array([beta]) #亮度
    img = cv2.add(img, array_beta)
    img = cv2.multiply(img, array_alpha)
    img = np.clip(img, 0, 255)
    return img

img = cv2.imread(filename)	#讀取本機圖片
modified_image = modify_contrast_and_brightness(img, 1.5, 10.0)
cv2.imshow('Modified Picture', modified_image) #顯示圖片


#影像分析工具
#影像直方圖

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
plt.hist(img.ravel(), 256, [0,256])
cv2.imshow('GrayScale Picture', img) #顯示圖片
plt.show()


#直方圖影像操作
#直方圖均值化

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
equa = cv2.equalizeHist(img)
cv2.imshow('Histogram', equa)#顯示圖片
plt.hist(equa.ravel(), 256, [0,256])
plt.show()
#均值化的影像
#均衡化後的灰度直方圖分布

'''

'''
#直方圖二值化
# 不同模式的Threshold方法
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary', th1)#顯示圖片
'''

'''

#影像邊緣檢測Canny()函數

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

gray_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#執行高斯模糊化
blur_gray = cv2.GaussianBlur(gray_img, (3,3), 0)
threshold_1 = 30#強邊緣strong edge
threshold_2 = 60#弱邊緣weak edge
edges = cv2.Canny(blur_gray, threshold_1, threshold_2)
cv2.imshow('Canny', edges)#顯示圖片




#影像邊緣檢測Sobel()函數

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

def sobel(image):
    kernel_size = (3, 3)
    blur_img = cv2.GaussianBlur(image, kernel_size, 0)
    #水平方向梯度
    x =cv2.Sobel(blur_img, cv2.CV_16S, 1, 0, kernel_size)
    abs_x = cv2.convertScaleAbs(x)
    #垂直方向梯度
    y =cv2.Sobel(blur_img, cv2.CV_16S, 0, 1, kernel_size)
    abs_y = cv2.convertScaleAbs(y)
    #合併兩個方向的梯度
    sobel_image = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return sobel_image

gray_img = cv2.imread(filename)
sobel_image = sobel(gray_img)
cv2.imshow('Sobel', sobel_image)#顯示圖片

'''





'''
cv2.imshow('視窗標題 不支持中文', img) #顯示圖片

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()




'''


