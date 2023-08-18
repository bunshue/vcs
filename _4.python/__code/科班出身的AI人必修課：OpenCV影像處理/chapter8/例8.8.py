# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:07:24 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img1=cv2.imread("closing.bmp")
img2=cv2.imread("closing2.bmp")
k=np.ones((10,10),np.uint8)
r1=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,k,iterations=3)
r2=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,iterations=3)
cv2.imshow("img1",img1)
cv2.imshow("result1",r1)
cv2.imshow("img2",img2)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()
