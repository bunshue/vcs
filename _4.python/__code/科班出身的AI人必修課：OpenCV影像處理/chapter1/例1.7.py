# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 09:35:39 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
lena=cv2.imread("lena.bmp")
r=cv2.imwrite("result.bmp",lena)

