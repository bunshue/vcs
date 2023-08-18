# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
#图层提取
import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
cv2.imshow("lena",lena)
r,c=lena.shape
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()
