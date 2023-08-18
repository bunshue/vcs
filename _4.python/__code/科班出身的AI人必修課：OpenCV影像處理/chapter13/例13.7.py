# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:16:09 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import matplotlib.pyplot as plt
o=cv2.imread("image\\boatGray.bmp")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
plt.plot(histb,color='b')
plt.show()
