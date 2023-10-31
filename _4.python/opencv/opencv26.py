'''
import os
import time
import random
'''

# opencv 集合

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import cv2

print('------------------------------------------------------------')	#60個
'''
#opencv
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import matplotlib.pyplot as plt
import cv2

image = cv2.imread(filename)	#讀取本機圖片

#plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#先轉換成RGB再顯示

plt.show()
'''
print('------------------------------------------------------------')	#60個

#11-2-1 用 OpenCV 讀取並顯示圖片

# 執行本章各行範例前, 請先執行此儲存格, 確認 cv2 已確實匯入

def aidemy_imshow(name, img):
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    plt.title(name)
    plt.imshow(img)
    plt.show()

cv2.imshow = aidemy_imshow

img = cv2.imread(r'images/sample.jpg')

print(type(img))

print(img.shape)

cv2.imshow('Sample pic', img)

print('------------------------------------------------------------')	#60個

print('OpenCV建立檔案')
img_size = 256
img = np.array([[(255, 255, 0) for x in range(img_size)] for x in range(img_size)])
cv2.imshow('Sample pic 2', img)
#cv2.imwrite(r'sample_222.jpg', img)

print('------------------------------------------------------------')	#60個

print('OpenCV建立檔案')
img_size = 256
img = np.array( [[(x, int((x + y) / 2), y) for x in range(img_size)] for y in range(img_size)])
cv2.imshow('Sample pic 3', img)
#cv2.imwrite(r'sample_333.jpg', img)

print('------------------------------------------------------------')	#60個

print('裁剪圖片a')

img = cv2.imread(r'images/sample.jpg')

H = img.shape[0]
W = img.shape[1]
print('H * W =', img.shape)
print('H =', H)
print('W =', W)

print('裁剪圖片b')
#img_cut = img[0:(H * 2 // 3), 0:(W * 2 // 3)]
img_cut = img[0:(H * 1 // 2), 0:(W * 1 // 2)]
print(img_cut.shape)
cv2.imshow('Sample pic', img_cut)

print('------------------------------------------------------------')	#60個

print('縮放圖片')

img = cv2.imread(r'images/sample.jpg')
print(img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 3, H * 2))
cv2.imshow('Sample pic', img_resize)
print(img_resize.shape)

print('------------------------------------------------------------')	#60個

print('圖片翻轉 原圖')

img = cv2.imread(r'images/sample.jpg') 
cv2.imshow('Sample pic', img)

print('圖片翻轉 效果')
img_flip = cv2.flip(img, -999)
img_flip2 = cv2.flip(img, -88)

cv2.imshow('Sample pic', img_flip)

print('------------------------------------------------------------')	#60個

print('圖片旋轉')

img = cv2.imread(r'images/sample.jpg')

H = img.shape[0]
W = img.shape[1]
aff_matrix = cv2.getRotationMatrix2D((W / 2, H / 2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (W, H))
cv2.imshow('Sample pic', img_rotate)

print('------------------------------------------------------------')	#60個

print('圖片旋轉')
img_rotate = cv2.rotate(img, 1) 
cv2.imshow('Sample pic', img_rotate)

print('------------------------------------------------------------')	#60個

print('圖片色彩空間的轉換')
img = cv2.imread(r'images/sample.jpg')
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow('Sample pic', img_convert)

print('------------------------------------------------------------')	#60個

print('將圖片顏色反轉 (負片效果) 原圖')
img = cv2.imread(r'images/sample.jpg')
cv2.imshow('Sample pic', img)

print('將圖片顏色反轉 (負片效果) 效果')
img_invert = cv2.bitwise_not(img)       
cv2.imshow('Sample pic', img_invert)

print('------------------------------------------------------------')	#60個

#OpenCV 進階圖片處理功能

print('圖片的二值化處理')
img = cv2.imread(r'images/sample.jpg')
thr, img_binary = cv2.threshold(img, 192, 255, cv2.THRESH_TOZERO)
cv2.imshow('Sample pic', img_binary)

print('------------------------------------------------------------')	#60個

print('遮罩')

img = cv2.imread(r'images/sample.jpg')
H = img.shape[0]
W = img.shape[1]
mask = cv2.imread(r'images/mask.jpg', cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, (W, H))
img_masked = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('Sample pic', img_masked)

print('------------------------------------------------------------')	#60個

print('遮罩')
mask = cv2.bitwise_not(mask)        
img_masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('Sample pic', img_masked)

print('------------------------------------------------------------')	#60個

print('模糊效果')

img = cv2.imread(r'images/sample.jpg')

Img_blur = cv2.GaussianBlur(img, (49, 49), 3)
cv2.imshow('Sample pic', Img_blur)

print('------------------------------------------------------------')	#60個

print('去除圖片的雜訊 原圖')

img2 = cv2.imread(r'images/sample2.jpg')

cv2.imshow('Sample pic', img2)

print('去除圖片的雜訊 效果')

img2_denoised = cv2.fastNlMeansDenoisingColored(img2, h = 5)

cv2.imshow('Sample pic', img2_denoised)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



