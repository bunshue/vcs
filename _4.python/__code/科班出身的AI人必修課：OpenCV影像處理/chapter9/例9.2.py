# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:01:23 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,-1,1,0)
cv2.imshow("original",o)
cv2.imshow("x",sobelx)
cv2.waitKey()
cv2.destroyAllWindows()
