# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:44:06 2018

@author: 天津职业技术师范大学  
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena4.bmp',0)
template = cv2.imread('lena4Temp.bmp',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, 1)
plt.imshow(img,cmap = 'gray')
plt.xticks([]), plt.yticks([])
