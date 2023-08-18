# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.bilateralFilter(o,25,100,100)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()