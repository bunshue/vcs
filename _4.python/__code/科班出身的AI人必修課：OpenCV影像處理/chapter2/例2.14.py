# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
a=cv2.imread("lenacolor.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("original",a)
face=np.random.randint(0,256,(180,100,3))
a[220:400,250:350]=face
cv2.imshow("result",a)
cv2.waitKey()
cv2.destroyAllWindows()

