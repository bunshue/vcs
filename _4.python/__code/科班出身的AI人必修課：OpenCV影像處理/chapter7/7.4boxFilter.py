# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.boxFilter(o,-1,(5,5),normalize=0) 
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()