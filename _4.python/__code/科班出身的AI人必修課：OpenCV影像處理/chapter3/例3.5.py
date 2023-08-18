# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:28:42 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
a=cv2.imread("boat.bmp")
b=cv2.imread("lena.bmp")
result=cv2.addWeighted(a,0.6,b,0.4,0)
cv2.imshow("boat",a)
cv2.imshow("lena",b)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()
