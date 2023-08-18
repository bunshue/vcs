# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:23:54 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img = np.zeros((5,5),dtype=np.uint8)
img[0:6,0:6]=123
img[2:6,2:6]=126
print("img=\n",img)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("thd=\n",thd)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("otsu=\n",otsu)
