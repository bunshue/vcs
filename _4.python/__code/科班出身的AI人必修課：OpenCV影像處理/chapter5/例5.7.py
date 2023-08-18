# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:06:11 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img=cv2.imread('lena.bmp')
rows,cols,ch=img.shape
p1=np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2=np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M=cv2.getAffineTransform(p1,p2)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("origianl",img)
cv2.imshow("result",dst)
cv2.waitKey()
cv2.destroyAllWindows()
