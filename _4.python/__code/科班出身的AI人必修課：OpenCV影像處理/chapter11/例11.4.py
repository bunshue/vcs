# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:24:28 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("lena.bmp")
up=cv2.pyrUp(o)
down=cv2.pyrDown(up)
diff=down-o   #构造diff图像，查看down与o的区别
print("o.shape=",o.shape)
print("down.shape=",down.shape)
cv2.imshow("original",o)
cv2.imshow("down",down)
cv2.imshow("difference",diff)
cv2.waitKey()
cv2.destroyAllWindows()