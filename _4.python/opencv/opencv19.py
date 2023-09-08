import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image=cv2.imread(filename)
print('顯示原圖 彩色')
cv2.imshow("image", image)
print("image.shape=",image.shape)

print('原圖 彩色 轉 灰階1通道')
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
print("gray.shape=",gray.shape)

print('灰階 轉 BGR3通道')
rgb=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
cv2.imshow("rgb",rgb)
print("rgb.shape=",rgb.shape)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image=cv2.imread(filename)
print('顯示原圖 BGR')
cv2.imshow("B-G-R OK",image)

print('顯示原圖 BGR 轉 RGB')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("R-G-B NG",rgb)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opencv.jpg'
opencv=cv2.imread(filename)
print('顯示原圖')
cv2.imshow('opencv', opencv)

print('顯示原圖 BGR 轉 HSV')
hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

#=============指定藍色值的范圍=============
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
#確定藍色區域
mask = cv2.inRange(hsv, minBlue, maxBlue)
#通過掩碼控制的按位與，鎖定藍色區域
blue = cv2.bitwise_and(opencv,opencv, mask= mask)
cv2.imshow('blue',blue)

#=============指定綠色值的范圍=============
minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
#確定綠色區域
mask = cv2.inRange(hsv, minGreen, maxGreen)
#通過掩碼控制的按位與，鎖定綠色區域
green = cv2.bitwise_and(opencv,opencv, mask= mask)
cv2.imshow('green',green)

#=============指定紅色值的范圍=============
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
#確定紅色區域
mask = cv2.inRange(hsv, minRed, maxRed)
#通過掩碼控制的按位與，鎖定紅色區域
red= cv2.bitwise_and(opencv,opencv, mask= mask)
cv2.imshow('red',red)

cv2.waitKey()
cv2.destroyAllWindows()

sys.exit()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lesson2.jpg'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
minHue=5
maxHue=170
hueMask=cv2.inRange(h, minHue, maxHue)
minSat=25
maxSat=166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow("ROI",roi)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
v[:,:]=255
newHSV=cv2.merge([h,s,v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)
cv2.imshow("art",art)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img",img)

bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b,g,r,a=cv2.split(bgra)
a[:,:]=125
bgra125=cv2.merge([b,g,r,a])
a[:,:]=0
bgra0=cv2.merge([b,g,r,a])
cv2.imshow("bgra",bgra)
cv2.imshow("bgra125",bgra125)
cv2.imshow("bgra0",bgra0)

cv2.waitKey()
cv2.destroyAllWindows()

#偽寫入
#cv2.imwrite("bgra.png", bgra)
#cv2.imwrite("bgra125.png", bgra125)
#cv2.imwrite("bgra0.png", bgra0)

print('------------------------------------------------------------')	#60個



