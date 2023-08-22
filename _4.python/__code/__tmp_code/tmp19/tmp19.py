import numpy as np
import cv2

print('------------------------------------------------------------')	#60個


n = 300
img = np.zeros((n+1,n+1,3), np.uint8)
img = cv2.line(img,(0,0),(n,n),(255,0,0),3)
img = cv2.line(img,(0,100),(n,100),(0,255,0),1)
img = cv2.line(img,(100,0),(100,n),(0,0,255),6)
winname = 'Demo19.1'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.2.py

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
n = 300
img = np.ones((n,n,3), np.uint8)*255
img = cv2.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
winname = 'Demo19.1'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.3.py

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
(centerX,centerY) = (round(img.shape[1] / 2),round(img.shape[0] / 2))
#将图像的中心作为圆心,实际值为=d/2
red = (0,0,255)#设置白色变量
for r in range(5,round(d/2),12):
    cv2.circle(img,(centerX,centerY),r,red,3)
    #circle(载体图像，圆心，半径，颜色)
cv2.imshow("Demo19.3",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.4.py

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
for i in range(0,100):
    centerX = np.random.randint(0,high = d)
    #生成随机圆心X,确保在画布img内
    centerY = np.random.randint(0,high = d)
    #生成随机圆心Y,确保在画布img内
    radius = np.random.randint(5,high = d/5)
    #生成随机半径，值范围：[5,d/5)，最大半径是d/5
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成随机颜色，3个[0,256)的随机数    
    cv2.circle(img,(centerX,centerY),radius,color,-1)
    #使用上述随机数，在画布img内画圆
cv2.imshow("demo19.4",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.5.py

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:30:55 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
center=(round(d/2),round(d/2))
#注意数值类型，center=(d/2,d/2)不可以
size=(100,200)
#轴的长度
for i in range(0,10):
    angle = np.random.randint(0,361)
    #偏移角度    
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    #生成随机颜色，3个[0,256)的随机数    
    thickness = np.random.randint(1,9)
    cv2.ellipse(img, center, size, angle, 0, 360, color,thickness)
cv2.imshow("demo19.5",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.6.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:49:07 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""
import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
pts=np.array([[200,50],[300,200],[200,350],[100,200]], np.int32)
#生成各个顶点,注意数据类型为int32
pts=pts.reshape((-1,1,2))
#第1个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
cv2.polylines(img,[pts],True,(0,255,0),8)
#调用函数polylines完成多边形绘图，注意第3个参数控制多边形封闭
# cv2.polylines(img,[pts],False,(0,255,0),8)  #不闭合的的多边形
cv2.imshow("demo19.6",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.7.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:49:07 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,255,0),5)
cv2.imshow("demo19.7",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.8.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:49:07 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,150),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,250),font, 3,(0,255,0),15,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv2.imshow("demo19.7",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.9.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:26:41 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
def Demo(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("单击了鼠标左键")
    elif event==cv2.EVENT_RBUTTONDOWN :
        print("单击了鼠标右键")
    elif flags==cv2.EVENT_FLAG_LBUTTON:
        print("按住左键拖动了鼠标")
    elif event==cv2.EVENT_MBUTTONDOWN :
        print("单击了中间键")
#创建名称为Demo的响应（回调）函数OnMouseAction
#将回调函数Demo与窗口“Demo19.9”建立连接
img = np.ones((300,300,3),np.uint8)*255
cv2.namedWindow('Demo19.9')
cv2.setMouseCallback('Demo19.9',Demo)     
cv2.imshow('Demo19.9',img)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.10.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:27:49 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
d = 400
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p1x=x
        p1y=y
        p2x=np.random.randint(1,d-50)
        p2y=np.random.randint(1,d-50)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,2)
img = np.ones((d,d,3),dtype="uint8")*255
cv2.namedWindow('Demo19.10')
cv2.setMouseCallback('Demo19.10',draw)
while(1):
    cv2.imshow('Demo19.10',img)
    if cv2.waitKey(20)==27:
        break
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.11.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:17:55 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
thickness=-1
mode=1
d=400
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        a=np.random.randint(1,d-50)
        r=np.random.randint(1,d/5)
        angle = np.random.randint(0,361)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        if mode==1:
            cv2.rectangle(img,(x,y),(a,a),color,thickness)
        elif mode==2:
            cv2.circle(img,(x,y),r,color,thickness)
        elif mode==3:
            cv2.line(img,(a,a),(x,y),color,3)  
        elif mode==4:
            cv2.ellipse(img, (x,y), (100,150), angle, 0, 360,color,thickness)                  
        elif mode==5:
            cv2.putText(img,'OpenCV',(0,round(d/2)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2,color,5)    
img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('r'):
        mode=1
    elif k==ord('c'):
        mode=2
    elif k==ord('l'):
        mode=3
    elif k==ord('e'):
        mode=4
    elif k==ord('t'):
        mode=5
    elif k==ord('f'):
        thickness=-1
    elif k==ord('u'):
        thickness=3
    elif k==27:
        break   
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.12.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
def changeColor(x):
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    img[:]=[b,g,r]
img=np.zeros((100,700,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',100,255,changeColor)
cv2.createTrackbar('G','image',0,255,changeColor)
cv2.createTrackbar('B','image',0,255,changeColor)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break   
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.13.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
Type=0  #阈值处理类型值
Value=0 #使用的阈值
def onType(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value,255, Type) 
    cv2.imshow(windowName,dst)
 
def onValue(a):
    Type= cv2.getTrackbarPos(tType, windowName)
    Value= cv2.getTrackbarPos(tValue, windowName)
    ret, dst = cv2.threshold(o, Value, 255, Type) 
    cv2.imshow(windowName,dst)

o = cv2.imread("lena512.bmp",0)
windowName = "Demo19.13"  #窗体名
cv2.namedWindow(windowName)
cv2.imshow(windowName,o)
#创建两个滑动条
tType = "Type"  #用来选取阈值处理类型的滚动条
tValue = "Value"    #用来选取阈值的滚动条
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tValue, windowName,0, 255, onValue) 
if cv2.waitKey(0) == 27:  
    cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.14.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
d=400
global thickness
thickness=-1
def fill(x):
    pass
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p1x=x
        p1y=y
        p2x=np.random.randint(1,d-50)
        p2y=np.random.randint(1,d-50)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        cv2.rectangle(img,(p1x,p1y),(p2x,p2y),color,thickness)

img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
cv2.createTrackbar('R','image',0,1,fill)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        thickness=-1
    else:
        thickness=2        
    if k==27:
        break   
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\科班出身的AI人必修課：OpenCV影像處理\chapter19\例19.14-2.py

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:41:47 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
def changeColor(x):
    g=cv2.getTrackbarPos('R','image')
    if g==0:
        img[:]=0
    else:
        img[:]=255
img=np.zeros((100,1000,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,1,changeColor)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==27:
        break   
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

