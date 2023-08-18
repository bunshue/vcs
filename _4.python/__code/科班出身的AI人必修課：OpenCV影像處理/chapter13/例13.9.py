# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:16:09 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""
import cv2
import numpy as np
mask=np.zeros([600,600],np.uint8)
mask[200:400,200:400]=255
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()


