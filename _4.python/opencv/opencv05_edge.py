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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

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

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #圖片轉為灰階

plt.subplot(232)
plt.title('灰階')
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))

#-- Edge detection -------------------------------------------------------------------

edges = cv2.Canny(image_gray, CANNY_THRESH_1, CANNY_THRESH_2)

plt.subplot(234)
plt.title('Canny')
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

edges = cv2.dilate(edges, None)

plt.subplot(235)
plt.title('Dilate')
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

edges = cv2.erode(edges, None)

plt.subplot(236)
plt.title('Erode')
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

plt.show()

#cv2存圖
#cv2.imwrite('person-masked.jpg', masked)

print('------------------------------------------------------------')	#60個

# split image into channels
c_red, c_green, c_blue = cv2.split(image)

plt.imshow(cv2.cvtColor(c_red, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(c_green, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(c_blue, cv2.COLOR_BGR2RGB))
plt.show()

# merge with mask got on one of a previous steps
# img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))
# plt.imshow(img_a)
# plt.show()

# save to disk
# cv2.imwrite('image/girl_1.png', img_a*255)

# or the same using plt
# plt.imsave('image/girl_2.png', img_a)
# plt.imshow('image', masked)                                   # Displays red, saves blue

print('------------------------------------------------------------')	#60個

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

plt.imshow(cv2.cvtColor(th1, cv2.COLOR_BGR2RGB))

plt.show()

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('th1')
plt.imshow(cv2.cvtColor(th1, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#影像邊緣檢測Canny()函數

gray_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

blur_gray = cv2.GaussianBlur(gray_image, (3,3), 0)  #執行高斯模糊化
threshold_1 = 30#強邊緣strong edge
threshold_2 = 60#弱邊緣weak edge

edges = cv2.Canny(blur_gray, threshold_1, threshold_2)

plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title('Canny')

plt.show()

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Canny')
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()



print('------------------------------------------------------------')	#60個

#影像邊緣檢測Sobel()函數

def sobel(image):
    kernel_size = (3, 3)
    blur_image = cv2.GaussianBlur(image, kernel_size, 0)    #執行高斯模糊化
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

plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))
plt.title('Sobel')

plt.show()


plt.figure('影像處理', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Sobel')
plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個


