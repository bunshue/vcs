# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:44:12 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrxy11=cv2.Scharr(o,cv2.CV_64F,1,1)
cv2.imshow("original",o)
cv2.imshow("xy11",scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()
