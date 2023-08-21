# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)
print("img2=\n",img2)
print("img1+img2=\n",img1+img2)

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import numpy as np
import cv2
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)
print("img2=\n",img2)
img3=cv2.add(img1,img2)
print("cv2.add(img1,img2)=\n",img3)


# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:00:44 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
a=cv2.imread("lena.bmp",0)
b=a
result1=a+b
result2=cv2.add(a,b)
cv2.imshow("original",a)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:28:42 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
img1=np.ones((3,4),dtype=np.uint8)*100
img2=np.ones((3,4),dtype=np.uint8)*10
gamma=3
img3=cv2.addWeighted(img1,0.6,img2,5,gamma)
print(img3)



# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:28:42 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
a=cv2.imread("boat.bmp")
b=cv2.imread("lena.bmp")
result=cv2.addWeighted(a,0.6,b,0.4,0)
cv2.imshow("boat",a)
cv2.imshow("lena",b)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()




# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:00:43 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
cv2.imshow("lena",lena)
cv2.imshow("dollar",dollar)
face1=lena[220:400,250:350]
face2=dollar[160:340,200:300]
add=cv2.addWeighted(face1,0.6,face2,0.4,0)
dollar[160:340,200:300]=add
cv2.imshow("result",dollar)
cv2.waitKey()
cv2.destroyAllWindows()



# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=np.random.randint(0,255,(5,5),dtype=np.uint8)
b=np.zeros((5,5),dtype=np.uint8)
b[0:3,0:3]=255
b[4,4]=255
c=cv2.bitwise_and(a,b)
print("a=\n",a)
print("b=\n",b)
print("c=\n",c)

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=cv2.imread("lena.bmp",0)
b=np.zeros(a.shape,dtype=np.uint8)
b[100:400,200:400]=255
b[100:500,100:200]=255
c=cv2.bitwise_and(a,b)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018
@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=cv2.imread("lena.bmp",1)
b=np.zeros(a.shape,dtype=np.uint8)
b[100:400,200:400]=255
b[100:500,100:200]=255
c=cv2.bitwise_and(a,b)
print("a.shape=",a.shape)
print("b.shape=",b.shape)
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
mask=np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4]=1
img3=np.ones((4,4),dtype=np.uint8)*66
print("img1=\n",img1)
print("img2=\n",img2)
print("mask=\n",mask)
print("初始值img3=\n",img3)
img3=cv2.add(img1,img2,mask=mask)
print("求和后img3=\n",img3)











# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:50:56 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy  as np
a=cv2.imread("lena.bmp",1)
w,h,c=a.shape
mask=np.zeros((w,h),dtype=np.uint8)
mask[100:400,200:400]=255
mask[100:500,100:200]=255
c=cv2.bitwise_and(a,a,mask)
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)
cv2.imshow("a",a)
cv2.imshow("mask",mask)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
img1=np.ones((4,4),dtype=np.uint8)*3
img2=np.ones((4,4),dtype=np.uint8)*5
print("img1=\n",img1)
print("img2=\n",img2)
img3=cv2.add(img1,img2)
print("cv2.add(img1,img2)=\n",img3)
img4=cv2.add(img1,6)
print("cv2.add(img1,6)\n",img4)
img5=cv2.add(6,img2)
print("cv2.add(6,img2)=\n",img5)





# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
#图层提取
import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
cv2.imshow("lena",lena)
r,c=lena.shape
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:00:35 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
#异或加密解密
import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
r,c=lena.shape
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption=cv2.bitwise_xor(lena,key)
decryption=cv2.bitwise_xor(encryption,key)
cv2.imshow("lena",lena)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:43:10 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

import cv2
import numpy as np
#读取原始载体图像
lena=cv2.imread("lena.bmp",0)
#读取水印图像
watermark=cv2.imread("watermark.bmp",0)
#将水印内的255处理为1，以方便嵌入
#后续章节会介绍使用threshold处理。
w=watermark[:,:]>0
watermark[w]=1
#读取原始载体图像的shape值
r,c=lena.shape
#============嵌入过程============
#生成内部值都是254的数组
t254=np.ones((r,c),dtype=np.uint8)*254
#获取lena图像的高7位
lenaH7=cv2.bitwise_and(lena,t254)
#将watermark嵌入到lenaH7内
e=cv2.bitwise_or(lenaH7,watermark)
#============提取过程============
#生成内部值都是1的数组
t1=np.ones((r,c),dtype=np.uint8)
#从载体图像内，提取水印图像
wm=cv2.bitwise_and(e,t1)
print(wm)
#将水印内的1处理为255以方便显示
#后续章节会介绍threshold实现。
w=wm[:,:]>0
wm[w]=255
#============显示============
cv2.imshow("lena",lena)
cv2.imshow("watermark",watermark*255)   #当前watermark内最大值为1
cv2.imshow("e",e)
cv2.imshow("wm",wm)
cv2.waitKey()
cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:29:34 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""
import cv2
import numpy as np
#读取原始载体图像
lena=cv2.imread("lena.bmp",0)
#读取原始载体图像的shape值
r,c=lena.shape
mask=np.zeros((r,c),dtype=np.uint8)
mask[220:400,250:350]=1
#获取一个key,打码、解码所使用的密钥
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
#============获取打码脸============
#使用密钥key加密原始图像lena
lenaXorKey=cv2.bitwise_xor(lena,key) 
#获取加密图像的脸部信息encryptFace
encryptFace=cv2.bitwise_and(lenaXorKey,mask*255)
#将图像lena内的脸部值设置为0，得到noFace1
noFace1=cv2.bitwise_and(lena,(1-mask)*255)
#得到打码的lena图像
maskFace=encryptFace+noFace1
#============将打码脸解码============
#将脸部打码的lena与密钥key异或，得到脸部的原始信息
extractOriginal=cv2.bitwise_xor(maskFace,key)
#将解码的脸部信息extractOriginal提取出来得到extractFace
extractFace=cv2.bitwise_and(extractOriginal,mask*255)
#从脸部打码的lena内提取没有脸部信息的lena图像，得到noFace2
noFace2=cv2.bitwise_and(maskFace,(1-mask)*255)
#得到解码的lena图像
extractLena=noFace2+extractFace
#============显示图像============
cv2.imshow("lena",lena)
cv2.imshow("mask",mask*255)
cv2.imshow("1-mask",(1-mask)*255)
cv2.imshow("key",key)
cv2.imshow("lenaXorKey",lenaXorKey)
cv2.imshow("encryptFace",encryptFace)
cv2.imshow("noFace1",noFace1)
cv2.imshow("maskFace",maskFace)
cv2.imshow("extractOriginal",extractOriginal)
cv2.imshow("extractFace",extractFace)
cv2.imshow("noFace2",noFace2)
cv2.imshow("extractLena",extractLena)
cv2.waitKey()
cv2.destroyAllWindows()






# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:46:04 2018

@author: 李立宗  lilizong@gmail.com
"""
#图层提取
import cv2
import numpy as np
lena=cv2.imread("lena.bmp",0)
cv2.imshow("lena",lena)
r,c=lena.shape
x=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv2.imshow(str(i),r[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()


