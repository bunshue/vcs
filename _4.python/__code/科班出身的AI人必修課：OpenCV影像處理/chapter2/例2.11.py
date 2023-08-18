# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018
@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()
