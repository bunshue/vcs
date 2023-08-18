# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("lena.bmp",0)
cv2.imshow("before",img)
for i in range(10,100):
    for j in range(80,100):
        img[i,j]=255
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
