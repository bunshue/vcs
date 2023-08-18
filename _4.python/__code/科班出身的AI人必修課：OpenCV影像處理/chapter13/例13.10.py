# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:29:41 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread("image\\girl.bmp",cv2.IMREAD_GRAYSCALE)
mask=np.zeros(image.shape,np.uint8)
mask[200:400,200:400]=255
histImage=cv2.calcHist([image],[0],None,[256],[0,255])
histMI=cv2.calcHist([image],[0],mask,[256],[0,255])
plt.plot(histImage)
plt.plot(histMI)
