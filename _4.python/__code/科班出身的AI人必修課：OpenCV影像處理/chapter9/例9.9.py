# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:24:45 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)  
cv2.imshow("original",o)
cv2.imshow("y",scharry)
cv2.waitKey()
cv2.destroyAllWindows()
