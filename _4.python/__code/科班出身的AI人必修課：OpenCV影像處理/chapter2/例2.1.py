# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.zeros((8,8),dtype=np.uint8)
print("img=\n",img)
cv2.imshow("one",img)
print("读取像素点img[0,3]=",img[0,3])
img[0,3]=255
print("修改后img=\n",img)
print("读取修改后像素点img[0,3]=",img[0,3])
cv2.imshow("two",img)
cv2.waitKey()
cv2.destroyAllWindows()

