# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:17:41 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("kernel.bmp",cv2.IMREAD_UNCHANGED)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59,59))
dst1 = cv2.dilate(o,kernel1)
dst2 = cv2.dilate(o,kernel2)
dst3 = cv2.dilate(o,kernel3)
cv2.imshow("orriginal",o)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
cv2.waitKey()
cv2.destroyAllWindows()
