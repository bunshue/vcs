# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:39:34 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
#RGB<->GRAY
import cv2
lena=cv2.imread("lenacolor.png")
gray=cv2.cvtColor(lena,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
#==========打印shape============
print("lena.shape=",lena.shape)
print("gray.shape=",gray.shape)
print("rgb.shape=",rgb.shape)
#==========显示效果============
cv2.imshow("lena",lena)
cv2.imshow("gray",gray)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.destroyAllWindows()