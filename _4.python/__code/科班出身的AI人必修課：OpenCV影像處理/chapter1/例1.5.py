# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:19:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
lena=cv2.imread("lenacolor.png")
cv2.imshow("demo", lena )
cv2.waitKey()
cv2.destroyWindow("demo")
