# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:42:21 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
lena=cv2.imread("lenacolor.png")
b,g,r=cv2.split(lena)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
cv2.waitKey()
cv2.destroyAllWindows()
