# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
def changeColor(x):
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        img[:]=0
    else:
        img[:]=255
img=np.zeros((100,1000,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,1,changeColor)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break   
cv2.destroyAllWindows()