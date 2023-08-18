# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
n = 300
img = np.ones((n,n,3), np.uint8)*255
img = cv2.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
winname = 'Demo19.1'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()