# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:19 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
img=cv2.imread("test.bmp")
rst=cv2.resize(img,None,fx=2,fy=0.5)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)
