import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

#RGB<->GRAY
lena=cv2.imread("lenacolor.png")
print('顯示原圖')
cv2.imshow("lena",lena)

gray=cv2.cvtColor(lena,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
#==========打印shape============
print("lena.shape=",lena.shape)
print("gray.shape=",gray.shape)
print("rgb.shape=",rgb.shape)
#==========显示效果============
cv2.imshow("gray",gray)
cv2.imshow("rgb",rgb)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

lena=cv2.imread("lenacolor.png")
print('顯示原圖')
cv2.imshow("lena",lena)

print('顯示BGR2RGB')
rgb = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
cv2.imshow("rgb",rgb)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

opencv=cv2.imread("opencv.jpg")
print('顯示原圖')
cv2.imshow('opencv',opencv)

hsv = cv2.cvtColor(opencv, cv2.COLOR_BGR2HSV)

#=============指定蓝色值的范围=============
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
#确定蓝色区域
mask = cv2.inRange(hsv, minBlue, maxBlue)
#通过掩码控制的按位与，锁定蓝色区域
blue = cv2.bitwise_and(opencv,opencv, mask= mask)
cv2.imshow('blue',blue)
#=============指定绿色值的范围=============
minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
#确定绿色区域
mask = cv2.inRange(hsv, minGreen, maxGreen)
#通过掩码控制的按位与，锁定绿色区域
green = cv2.bitwise_and(opencv,opencv, mask= mask)
cv2.imshow('green',green)
#=============指定红色值的范围=============
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
#确定红色区域
mask = cv2.inRange(hsv, minRed, maxRed)
#通过掩码控制的按位与，锁定红色区域
red= cv2.bitwise_and(opencv,opencv, mask= mask)

cv2.imshow('red',red)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

img=cv2.imread("lesson2.jpg")
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

img=cv2.imread("barbara.bmp")
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

img=cv2.imread("lenacolor.png")
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

cv2.imwrite("bgra.png", bgra)
cv2.imwrite("bgra125.png", bgra125)
cv2.imwrite("bgra0.png", bgra0)

print('------------------------------------------------------------')	#60個







