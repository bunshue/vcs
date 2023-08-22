import cv2
import numpy as np

print('------------------------------------------------------------')	#60個


img=np.random.randint(-256,256,size=[4,5],dtype=np.int16)
rst=cv2.convertScaleAbs(img)
print("img=\n",img)
print("rst=\n",rst)




print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.2.py

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:01:23 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,-1,1,0)
cv2.imshow("original",o)
cv2.imshow("x",sobelx)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.3.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:12:22 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
cv2.imshow("original",o)
cv2.imshow("x",sobelx)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.4.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:15:34 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""


import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("original",o)
cv2.imshow("y",sobely)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.5.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:22:20 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelxy=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 
cv2.imshow("original",o)
cv2.imshow("xy",sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.6.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:26:43 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
cv2.imshow("original",o)
cv2.imshow("xy",sobelxy)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.7.py

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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.8.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:21:09 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.9.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:24:45 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)  
cv2.imshow("original",o)
cv2.imshow("y",scharry)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.10.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:26:24 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  
cv2.imshow("original",o)
cv2.imshow("xy",scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.11.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:44:12 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
scharrxy11=cv2.Scharr(o,cv2.CV_64F,1,1)
cv2.imshow("original",o)
cv2.imshow("xy11",scharrxy11)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.12.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:50:00 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Sobel(o,cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(o,cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 
cv2.imshow("original",o)
cv2.imshow("x",scharrx)
cv2.imshow("y",scharry)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.13.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:48:08 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0) 
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 
cv2.imshow("original",o)
cv2.imshow("sobelxy",sobelxy)
cv2.imshow("scharrxy",scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter9\例9.14.py

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:49:50 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
o = cv2.imread('Laplacian.bmp',cv2.IMREAD_GRAYSCALE)
Laplacian = cv2.Laplacian(o,cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   
cv2.imshow("original",o)
cv2.imshow("Laplacian",Laplacian)
cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個



