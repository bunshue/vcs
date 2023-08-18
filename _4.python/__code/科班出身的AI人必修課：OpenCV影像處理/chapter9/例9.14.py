# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:49:50 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('Laplacian.bmp',cv2.IMREAD_GRAYSCALE)
Laplacian = cv2.Laplacian(o,cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   
cv2.imshow("original",o)
cv2.imshow("Laplacian",Laplacian)
cv2.waitKey()
cv2.destroyAllWindows()

