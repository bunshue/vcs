import cv2
import numpy as np


print('------------------------------------------------------------')	#60個


img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

import cv2
img=cv2.imread("lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.3.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.4.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.5.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.6.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.7.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.8.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.9.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
print("img=\n",img)
print("t=",t)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個





#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.10.py

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:02 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("lena.bmp")
t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow("img",img)
cv2.imshow("rst",rst)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.11.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 08:07:17 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("computer.jpg",0)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
athdMEAN=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
athdGAUS=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow("img",img)
cv2.imshow("thd",thd)
cv2.imshow("athdMEAN",athdMEAN)
cv2.imshow("athdGAUS",athdGAUS)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.12.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:23:54 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img = np.zeros((5,5),dtype=np.uint8)
img[0:6,0:6]=123
img[2:6,2:6]=126
print("img=\n",img)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("thd=\n",thd)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("otsu=\n",otsu)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter6\例6.13.py

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:42:57 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
img=cv2.imread("tiffany.bmp",0)
t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("img",img)
cv2.imshow("thd",thd)
cv2.imshow("otus",otsu)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個



