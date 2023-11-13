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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

print('原圖 彩色')
image = cv2.imread(filename)
print("image.shape=",image.shape)

print('原圖 彩色 轉 灰階1通道')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray.shape=",gray.shape)

print('灰階 轉 BGR3通道')
rgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
print("rgb.shape=",rgb.shape)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖 彩色')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('灰階1通道')
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('BGR3通道')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image = cv2.imread(filename)

print('原圖 BGR 轉 RGB')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure('影像處理', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖 B-G-R OK')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('原圖 BGR 轉 RGB NG')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opencv.jpg'
image = cv2.imread(filename)

print('原圖 BGR 轉 HSV')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#=============指定藍色值的范圍=============
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
#確定藍色區域
mask = cv2.inRange(hsv, minBlue, maxBlue)
#通過掩碼控制的按位與，鎖定藍色區域
blue = cv2.bitwise_and(image, image, mask = mask)

#=============指定綠色值的范圍=============
minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
#確定綠色區域
mask = cv2.inRange(hsv, minGreen, maxGreen)
#通過掩碼控制的按位與，鎖定綠色區域
green = cv2.bitwise_and(image, image, mask = mask)

#=============指定紅色值的范圍=============
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
#確定紅色區域
mask = cv2.inRange(hsv, minRed, maxRed)
#通過掩碼控制的按位與，鎖定紅色區域
red= cv2.bitwise_and(image, image, mask = mask)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('HSV')
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))

#plt.subplot(233)
#plt.title('')

plt.subplot(234)
plt.title('R')
plt.imshow(cv2.cvtColor(red, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('G')
plt.imshow(cv2.cvtColor(green, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('B')
plt.imshow(cv2.cvtColor(blue, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lesson2.jpg'
img = cv2.imread(filename)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask = mask)

plt.figure('影像處理', figsize = (16, 12))

plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('ROI')
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
img = cv2.imread(filename)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
v[:,:]=255
newHSV=cv2.merge([h,s,v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

plt.subplot(223)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('art')
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
img = cv2.imread(filename)

bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b,g,r,a=cv2.split(bgra)
a[:,:]=125
bgra125=cv2.merge([b,g,r,a])
a[:,:]=0
bgra0=cv2.merge([b,g,r,a])

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('bgra')
plt.imshow(cv2.cvtColor(bgra, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('bgra125')
plt.imshow(cv2.cvtColor(bgra125, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('bgra0')
plt.imshow(cv2.cvtColor(bgra0, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

#偽寫入
#cv2.imwrite("bgra.png", bgra)
#cv2.imwrite("bgra125.png", bgra125)
#cv2.imwrite("bgra0.png", bgra0)

print('------------------------------------------------------------')	#60個

