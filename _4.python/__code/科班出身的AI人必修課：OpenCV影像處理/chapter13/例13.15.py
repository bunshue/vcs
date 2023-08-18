# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 10:26:57 2018


@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import matplotlib.pyplot as plt
o = cv2.imread('image\\8.bmp')
g=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
plt.figure("灰度图像显示演示")
plt.subplot(221); plt.imshow(g, cmap=plt.cm.gray)
plt.subplot(222); plt.imshow(g, cmap=plt.cm.gray_r)
plt.subplot(223); plt.imshow(g, cmap='gray')
plt.subplot(224); plt.imshow(g, cmap='gray_r')