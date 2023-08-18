# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:42:21 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
cv2.imshow("lena",lena)
cv2.imshow("dollar",dollar)
face=lena[220:400,250:350]
dollar[160:340,200:300]=face
cv2.imshow("result",dollar)
cv2.waitKey()
cv2.destroyAllWindows()
