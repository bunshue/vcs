# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)
