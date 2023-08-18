# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:20:18 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
import numpy as np
img=cv2.imread("lena.bmp")
height,width=img.shape[:2]
x=100
y=200
M = np.float32([[1, 0, x], [0, 1, y]])
move=cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("move",move)
cv2.waitKey()
cv2.destroyAllWindows()
