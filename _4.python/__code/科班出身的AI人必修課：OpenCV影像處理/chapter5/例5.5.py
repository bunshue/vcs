
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:17:55 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.ones([2,4,3],dtype=np.uint8)
size=img.shape[:2]
rst=cv2.resize(img,size)
print("img.shape=\n",img.shape)
print("img=\n",img)
print("rst.shape=\n",rst.shape)
print("rst=\n",rst)


# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:42:47 2018
@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("test.bmp")
rows,cols=img.shape[:2]
size=(int(cols*0.9),int(rows*0.5))
rst=cv2.resize(img,size)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)






# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:19 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
img=cv2.imread("test.bmp")
rst=cv2.resize(img,None,fx=2,fy=0.5)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)



# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:19 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
img=cv2.imread("lena.bmp")
x=cv2.flip(img,0)
y=cv2.flip(img,1)
xy=cv2.flip(img,-1)
cv2.imshow("img",img)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.imshow("xy",xy)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:20:18 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社 
"""

import cv2
import numpy as np
img=cv2.imread("lena.bmp")
height,width=img.shape[:2]
x=100
y=200
M = np.float32([[1, 0, x], [0, 1, y]])
move=cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("move",move)
cv2.waitKey()
cv2.destroyAllWindows()
