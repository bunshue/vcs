# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
img=cv2.imread("image\\lena.bmp")
hist = cv2.calcHist([img],[0],None,[256],[0,255])
print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)
