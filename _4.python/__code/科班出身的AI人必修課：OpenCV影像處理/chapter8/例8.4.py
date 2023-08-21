# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:48:09 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img=np.zeros((5,5),np.uint8)
img[1:4,1:4]=1
kernel = np.ones((3,1),np.uint8)
erosion = cv2.erode(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("erosion=\n",erosion)


# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:48:09 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(o,kernel)
cv2.imshow("orriginal",o)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:29:20 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((9,9),np.uint8)
erosion = cv2.erode(o,kernel,iterations =5)
cv2.imshow("orriginal",o)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()





# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:48:09 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img=np.zeros((5,5),np.uint8)
img[2:3,1:4]=1
kernel = np.ones((3,1),np.uint8)
dilation = cv2.dilate(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("dilation\n",dilation)
