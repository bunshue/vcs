# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:34:27 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
o=cv2.imread("dilation.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((9,9),np.uint8)
dilation = cv2.dilate(o,kernel)
cv2.imshow("original",o)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()
