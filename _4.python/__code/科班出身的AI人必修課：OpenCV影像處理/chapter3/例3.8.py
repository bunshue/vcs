# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=cv2.imread("lena.bmp",0)
b=np.zeros(a.shape,dtype=np.uint8)
b[100:400,200:400]=255
b[100:500,100:200]=255
c=cv2.bitwise_and(a,b)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()
