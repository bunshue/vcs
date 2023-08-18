# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:18:25 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img=np.random.randint(0,256,size=[5,5],dtype=np.uint8)
min=100
max=200
mask = cv2.inRange(img, min, max)
print("img=\n",img)
print("mask=\n",mask)