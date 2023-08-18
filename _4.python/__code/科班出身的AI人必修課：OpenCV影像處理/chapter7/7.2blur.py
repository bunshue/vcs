# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r5=cv2.blur(o,(5,5))      
r30=cv2.blur(o,(30,30))      
cv2.imshow("original",o)
cv2.imshow("result5",r5)
cv2.imshow("result30",r30)
cv2.waitKey()
cv2.destroyAllWindows()