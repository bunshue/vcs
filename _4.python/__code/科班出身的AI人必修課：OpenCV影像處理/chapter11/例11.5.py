# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:49:37 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
O=cv2.imread("lena.bmp")
G0=O
G1=cv2.pyrDown(G0)
G2=cv2.pyrDown(G1)
G3=cv2.pyrDown(G2)
L0=G0-cv2.pyrUp(G1)
L1=G1-cv2.pyrUp(G2)
L2=G2-cv2.pyrUp(G3)
print("L0.shape=",L0.shape)
print("L1.shape=",L1.shape)
print("L2.shape=",L2.shape)
cv2.imshow("L0",L0)
cv2.imshow("L1",L1)
cv2.imshow("L2",L2)
cv2.waitKey()
cv2.destroyAllWindows()