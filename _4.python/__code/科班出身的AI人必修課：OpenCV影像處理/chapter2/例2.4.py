# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:40:14 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import numpy as np
import cv2
img=np.zeros((300,300,3),dtype=np.uint8)
img[:,0:100,0]=255
img[:,100:200,1]=255
img[:,200:300,2]=255
print("img=\n",img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
