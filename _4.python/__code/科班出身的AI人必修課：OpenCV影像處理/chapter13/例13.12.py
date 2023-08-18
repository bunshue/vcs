# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:41:08 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image\\equ.bmp',cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
plt.figure("subplot示例")
plt.subplot(121),plt.hist(img.ravel(),256)
plt.subplot(122),plt.hist(equ.ravel(),256)