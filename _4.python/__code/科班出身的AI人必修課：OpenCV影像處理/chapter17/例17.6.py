# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:35:29 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [0,255,0]
plt.subplot(121)
plt.imshow(ishow)
plt.axis('off')
plt.subplot(122)
plt.imshow(img)
plt.axis('off')
