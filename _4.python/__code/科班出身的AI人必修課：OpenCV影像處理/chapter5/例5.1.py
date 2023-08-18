# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:17:55 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.ones([2,4,3],dtype=np.uint8)
size=img.shape[:2]
rst=cv2.resize(img,size)
print("img.shape=\n",img.shape)
print("img=\n",img)
print("rst.shape=\n",rst.shape)
print("rst=\n",rst)
