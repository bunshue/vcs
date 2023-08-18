# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 13:21:51 2018

@author: 天津职业技术师范大学  
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena512g.bmp',0)
img2 = img.copy()
template = cv2.imread('temp.bmp',0)
tw, th = template.shape[::-1]
img = img2.copy()
rv = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)
plt.subplot(121),plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.show()
