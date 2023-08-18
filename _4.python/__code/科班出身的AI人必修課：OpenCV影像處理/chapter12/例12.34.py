# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:59:57 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
#-----------------读取原始图像----------------------
o = cv2.imread('cc.bmp')  
cv2.imshow("original",o)
#-----------------获取轮廓------------------------
gray = cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
image,contours, hierarchy = cv2.findContours(binary,
                                             cv2.RETR_LIST,
                                             cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[0]
#-----------------绘制空心轮廓------------------------
mask1 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask1,[cnt],0,255,2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=",pixelpoints1.shape)
print("pixelpoints1=\n",pixelpoints1)
cv2.imshow("mask1",mask1)
#-----------------绘制实心轮廓---------------------
mask2 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask2,[cnt],0,255,-1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=",pixelpoints2.shape)
print("pixelpoints2=\n",pixelpoints2)
cv2.imshow("mask2",mask2)
#-----------------释放窗口------------------------
cv2.waitKey()
cv2.destroyAllWindows()


