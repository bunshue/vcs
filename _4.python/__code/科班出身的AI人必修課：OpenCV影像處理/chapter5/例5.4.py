# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:19 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
img=cv2.imread("lena.bmp")
x=cv2.flip(img,0)
y=cv2.flip(img,1)
xy=cv2.flip(img,-1)
cv2.imshow("img",img)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.imshow("xy",xy)
cv2.waitKey()
cv2.destroyAllWindows()