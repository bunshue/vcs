
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#圖片處理

#-- Read image -----------------------------------------------------------------------
image = cv2.imread(filename)	#讀取本機圖片
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階

#-- Edge detection -------------------------------------------------------------------

edges = cv2.Canny(image_gray, CANNY_THRESH_1, CANNY_THRESH_2)
cv2.imshow('Canny', edges)
cv2.waitKey()
edges = cv2.dilate(edges, None)
cv2.imshow('Dilate', edges)
cv2.waitKey()
edges = cv2.erode(edges, None)
cv2.imshow('Erode', edges)
cv2.waitKey()

#cv2.imwrite('C:/Temp/person-masked.jpg', masked)           # Save

'''
# split image into channels
c_red, c_green, c_blue = cv2.split(image)

# merge with mask got on one of a previous steps
#img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

cv2.imshow('R', c_red)
cv2.waitKey()

cv2.imshow('G', c_green)
cv2.waitKey()

cv2.imshow('B', c_blue)
cv2.waitKey()

plt.imshow(img_a)
plt.show()

# save to disk
cv2.imwrite('image/girl_1.png', img_a*255)

# or the same using plt
plt.imsave('image/girl_2.png', img_a)

cv2.imshow('image', masked)                                   # Displays red, saves blue

cv2.waitKey()
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

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary', th1)#顯示圖片





'''

#影像邊緣檢測Canny()函數

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

gray_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#執行高斯模糊化
blur_gray = cv2.GaussianBlur(gray_image, (3,3), 0)
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
    blur_image = cv2.GaussianBlur(image, kernel_size, 0)
    #水平方向梯度
    x =cv2.Sobel(blur_image, cv2.CV_16S, 1, 0, kernel_size)
    abs_x = cv2.convertScaleAbs(x)
    #垂直方向梯度
    y =cv2.Sobel(blur_image, cv2.CV_16S, 0, 1, kernel_size)
    abs_y = cv2.convertScaleAbs(y)
    #合併兩個方向的梯度
    sobel_image = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return sobel_image

gray_image = cv2.imread(filename)	#讀取本機圖片

sobel_image = sobel(gray_image)
cv2.imshow('Sobel', sobel_image)#顯示圖片

'''





