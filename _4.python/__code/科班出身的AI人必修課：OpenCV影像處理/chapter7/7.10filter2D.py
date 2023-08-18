# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
o=cv2.imread("image\\lena.bmp")
kernel = np.ones((9,9),np.float32)/81
r = cv2.filter2D(o,-1,kernel)
cv2.imshow("original",o)
cv2.imshow("Gaussian",r)
cv2.waitKey()
cv2.destroyAllWindows()
