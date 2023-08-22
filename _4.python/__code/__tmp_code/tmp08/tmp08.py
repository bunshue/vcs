import cv2
import numpy as np

print('------------------------------------------------------------')	#60個


img=np.zeros((5,5),np.uint8)
img[1:4,1:4]=1
kernel = np.ones((3,1),np.uint8)
erosion = cv2.erode(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("erosion=\n",erosion)


print('------------------------------------------------------------')	#60個


import cv2
import numpy as np


o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(o,kernel)
cv2.imshow("orriginal",o)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個


import cv2
import numpy as np

o=cv2.imread("erode.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((9,9),np.uint8)
erosion = cv2.erode(o,kernel,iterations =5)
cv2.imshow("orriginal",o)
cv2.imshow("erosion",erosion)
cv2.waitKey()
cv2.destroyAllWindows()




print('------------------------------------------------------------')	#60個


import cv2
import numpy as np

img=np.zeros((5,5),np.uint8)
img[2:3,1:4]=1
kernel = np.ones((3,1),np.uint8)
dilation = cv2.dilate(img,kernel)
print("img=\n",img)
print("kernel=\n",kernel)
print("dilation\n",dilation)



print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.5.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:34:27 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
o=cv2.imread("dilation.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((9,9),np.uint8)
dilation = cv2.dilate(o,kernel)
cv2.imshow("original",o)
cv2.imshow("dilation",dilation)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.6.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 22:39:03 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o=cv2.imread("dilation.bmp",cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(o,kernel,iterations = 9)
cv2.imshow("original",o)
cv2.imshow("dilation", dilation)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.7.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:43:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img1=cv2.imread("opening.bmp")
img2=cv2.imread("opening2.bmp")
k=np.ones((10,10),np.uint8)
r1=cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)
r2=cv2.morphologyEx(img2,cv2.MORPH_OPEN,k)
cv2.imshow("img1",img1)
cv2.imshow("result1",r1)
cv2.imshow("img2",img2)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.8.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:07:24 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img1=cv2.imread("closing.bmp")
img2=cv2.imread("closing2.bmp")
k=np.ones((10,10),np.uint8)
r1=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,k,iterations=3)
r2=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,iterations=3)
cv2.imshow("img1",img1)
cv2.imshow("result1",r1)
cv2.imshow("img2",img2)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.9.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:19:45 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o=cv2.imread("gradient.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.10.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:26:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o1=cv2.imread("tophat.bmp",cv2.IMREAD_UNCHANGED)
o2=cv2.imread("lena.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r1=cv2.morphologyEx(o1,cv2.MORPH_TOPHAT,k)
r2=cv2.morphologyEx(o2,cv2.MORPH_TOPHAT,k)
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.11.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:50:14 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
o1=cv2.imread("blackhat.bmp",cv2.IMREAD_UNCHANGED)
o2=cv2.imread("lena.bmp",cv2.IMREAD_UNCHANGED)
k=np.ones((5,5),np.uint8)
r1=cv2.morphologyEx(o1,cv2.MORPH_BLACKHAT,k)
r2=cv2.morphologyEx(o2,cv2.MORPH_BLACKHAT,k)
cv2.imshow("original1",o1)
cv2.imshow("original2",o2)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.12.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:12:27 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (5,5))
print("kernel1=\n",kernel1)
print("kernel2=\n",kernel2)
print("kernel3=\n",kernel3)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter8\例8.13.py

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:17:41 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("kernel.bmp",cv2.IMREAD_UNCHANGED)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59,59))
dst1 = cv2.dilate(o,kernel1)
dst2 = cv2.dilate(o,kernel2)
dst3 = cv2.dilate(o,kernel3)
cv2.imshow("orriginal",o)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




