# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:07:20 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
lena=cv2.imread("lenacolor.png")
rgb = cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
cv2.imshow("lena",lena)
cv2.imshow("rgb",rgb)
cv2.waitKey()
cv2.destroyAllWindows()