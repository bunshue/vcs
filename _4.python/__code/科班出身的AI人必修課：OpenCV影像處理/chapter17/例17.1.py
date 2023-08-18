# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 13:12:34 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
o=cv2.imread("rice.png",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
e=cv2.erode(o,k)
b=cv2.subtract(o,e)
plt.subplot(131)
plt.imshow(o)
plt.axis('off')
plt.subplot(132)
plt.imshow(e)
plt.axis('off')
plt.subplot(133)
plt.imshow(b)
plt.axis('off') 
