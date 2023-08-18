# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
n = 300
img = np.zeros((n+1,n+1,3), np.uint8)
img = cv2.line(img,(0,0),(n,n),(255,0,0),3)
img = cv2.line(img,(0,100),(n,100),(0,255,0),1)
img = cv2.line(img,(100,0),(100,n),(0,0,255),6)
winname = 'Demo19.1'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()