# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:22:20 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelxy=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 
cv2.imshow("original",o)
cv2.imshow("xy",sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()
