# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:50:00 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Sobel(o,cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(o,cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.imshow("y",scharry)
cv2.waitKey()
cv2.destroyAllWindows()
