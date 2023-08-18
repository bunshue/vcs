# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:12:27 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (5,5))
print("kernel1=\n",kernel1)
print("kernel2=\n",kernel2)
print("kernel3=\n",kernel3)