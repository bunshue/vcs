# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=cv2.imread("lena.bmp",1)
w,h,c=a.shape
mask=np.zeros((w,h),dtype=np.uint8)
mask[100:400,200:400]=255
mask[100:500,100:200]=255
c=cv2.bitwise_and(a,a,mask)
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)
cv2.imshow("a",a)
cv2.imshow("mask",mask)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()