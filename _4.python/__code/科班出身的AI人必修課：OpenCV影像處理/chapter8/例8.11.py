# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:50:14 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o1=cv2.imread("blackhat.bmp",cv2.IMREAD_UNCHANGED)
o2=cv2.imread("lena.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r1=cv2.morphologyEx(o1,cv2.MORPH_BLACKHAT,k)
r2=cv2.morphologyEx(o2,cv2.MORPH_BLACKHAT,k)
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()