# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:00:43 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
cv2.imshow("lena",lena)
cv2.imshow("dollar",dollar)
face1=lena[220:400,250:350]
face2=dollar[160:340,200:300]
add=cv2.addWeighted(face1,0.6,face2,0.4,0)
dollar[160:340,200:300]=add
cv2.imshow("result",dollar)
cv2.waitKey()
cv2.destroyAllWindows()
