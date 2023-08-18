# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:49:07 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,150),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,250),font, 3,(0,255,0),15,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv2.imshow("demo19.7",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
