# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:21:09 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.waitKey()
cv2.destroyAllWindows()
