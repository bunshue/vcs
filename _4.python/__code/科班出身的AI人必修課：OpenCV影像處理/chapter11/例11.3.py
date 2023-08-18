# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:06:20 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("lena.bmp")
down=cv2.pyrDown(o)
up=cv2.pyrUp(down)
diff=up-o   #构造diff图像，查看up与o的区别
print("o.shape=",o.shape)
print("up.shape=",up.shape)
cv2.imshow("original",o)
cv2.imshow("up",up)
cv2.imshow("difference",diff)
cv2.waitKey()
cv2.destroyAllWindows()
