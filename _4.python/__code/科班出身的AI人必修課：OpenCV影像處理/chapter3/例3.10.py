# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
mask=np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4]=1
img3=np.ones((4,4),dtype=np.uint8)*66
print("img1=\n",img1)
print("img2=\n",img2)
print("mask=\n",mask)
print("初始值img3=\n",img3)
img3=cv2.add(img1,img2,mask=mask)
print("求和后img3=\n",img3)