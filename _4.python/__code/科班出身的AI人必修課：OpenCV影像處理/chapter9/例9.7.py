# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:17:12 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy11=cv2.convertScaleAbs(sobelxy11) 
cv2.imshow("original",o)
cv2.imshow("xy",sobelxy)
cv2.imshow("xy11",sobelxy11)
cv2.waitKey()
cv2.destroyAllWindows()
