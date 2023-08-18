# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o=cv2.imread("image\\bilTest.bmp")
g=r=cv2.GaussianBlur(o,(55,55),0,0)
b=cv2.bilateralFilter(o,55,100,100)
cv2.imshow("original",o)
cv2.imshow("Gaussian",g)
cv2.imshow("bilateral",b)
cv2.waitKey()
cv2.destroyAllWindows()