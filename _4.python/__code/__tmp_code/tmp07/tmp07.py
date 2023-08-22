import cv2


print('------------------------------------------------------------')	#60個


o=cv2.imread("image\\lenaNoise.png")
r=cv2.blur(o,(5,5))
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.2blur.py

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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.3boxFilter.py

# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.boxFilter(o,-1,(5,5)) 
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.4boxFilter.py

# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.boxFilter(o,-1,(5,5),normalize=0) 
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.5boxFilter.py

# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:10:47 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.boxFilter(o,-1,(2,2),normalize=0) 
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.6GaussianBlur.py

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 20:31:55 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.GaussianBlur(o,(5,5),0,0)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.7medianBlur.py

# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.medianBlur(o,3)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.8bilaternalFilter.py

# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o=cv2.imread("image\\lenaNoise.png")
r=cv2.bilateralFilter(o,25,100,100)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.9bilaternalFilterDiff.py

# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:18:05 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o=cv2.imread("image\\bilTest.bmp")
g=r=cv2.GaussianBlur(o,(55,55),0,0)
b=cv2.bilateralFilter(o,55,100,100)
cv2.imshow("original",o)
cv2.imshow("Gaussian",g)
cv2.imshow("bilateral",b)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\7.10filter2D.py

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:03:50 2018
@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
o=cv2.imread("image\\lena.bmp")
kernel = np.ones((9,9),np.float32)/81
r = cv2.filter2D(o,-1,kernel)
cv2.imshow("original",o)
cv2.imshow("Gaussian",r)
cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter7\addNoise.py

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:16:09 2018

@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""
import cv2
import numpy as np
def saltpepper(img,n):
    m=int((img.shape[0]*img.shape[1])*n)
    for a in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=255
        elif img.ndim==3:
            img[j,i,0]=255
            img[j,i,1]=255
            img[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=0
        elif img.ndim==3:
            img[j,i,0]=0
            img[j,i,1]=0
            img[j,i,2]=0
    return img


#上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
img=cv2.imread('image\\lena.bmp')
saltImage=saltpepper(img,0.02)
cv2.imshow('saltImage',saltImage)

cv2.imwrite('image\\test.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




