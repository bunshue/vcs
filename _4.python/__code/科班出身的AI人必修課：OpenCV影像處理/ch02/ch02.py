import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

img=cv2.imread("lena.bmp",0)
print('顯示原圖')
cv2.imshow("before",img)


print('修改一部份資料')
for i in range(50, 100):
    for j in range(50, 100):
        img[i,j] = 255

print('顯示修改後的圖')
cv2.imshow("after",img)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

img=cv2.imread("lenacolor.png")

print('顯示原圖')
cv2.imshow("before",img)

print("访问img[0,0]=",img[0,0])
print("访问img[0,0,0]=",img[0,0,0])
print("访问img[0,0,1]=",img[0,0,1])
print("访问img[0,0,2]=",img[0,0,2])
print("访问img[50,0]=",img[50,0])
print("访问img[100,0]=",img[100,0])
#区域1
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img[i,j,k]=255  #白色
#区域2
for i in range(50,100):
    for j in range(0,100):
        img[i,j]=[128,128,128]  #灰色
#区域3            
for i in range(100,150):
    for j in range(0,100):
        img[i,j]=0          #黑色

print('顯示修改後的圖')
cv2.imshow("after",img)

print("修改后img[0,0]=",img[0,0])
print("修改后img[0,0,0]=",img[0,0,0])
print("修改后img[0,0,1]=",img[0,0,1])
print("修改后img[0,0,2]=",img[0,0,2])
print("修改后img[50,0]=",img[50,0])
print("修改后img[100,0]=",img[100,0])
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

img=cv2.imread("lena.bmp",0)

#测试读取、修改单个像素值
print("读取像素点img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改后像素点img.item(3,2)=",img.item(3,2))
#测试修改一个区域的像素值

print('顯示原圖')
cv2.imshow("before",img)

for i in range(10,100):
    for j in range(80,100):
        img.itemset((i,j),255)

print('顯示修改後的圖')
cv2.imshow("after",img)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


img=cv2.imread("lenacolor.png")

print('顯示原圖')
cv2.imshow("before",img)

print("访问img.item(0,0,0)=",img.item(0,0,0))
print("访问img.item(0,0,1)=",img.item(0,0,1))
print("访问img.item(0,0,2)=",img.item(0,0,2))
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k),255)     #白色

print('顯示修改後的圖')
cv2.imshow("after",img)

print("修改后img.item(0,0,0)=",img.item(0,0,0))
print("修改后img.item(0,0,1)=",img.item(0,0,1))
print("修改后img.item(0,0,2)=",img.item(0,0,2))

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("lenacolor.png",cv2.IMREAD_UNCHANGED)

face=a[220:400,250:350]

print('顯示原圖')
cv2.imshow("original",a)

print('顯示修改後的圖')
cv2.imshow("face",face)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("lenacolor.png",cv2.IMREAD_UNCHANGED)

print('顯示原圖')
cv2.imshow("original",a)

face=np.random.randint(0,256,(180,100,3))
a[220:400,250:350]=face

print('顯示修改後的圖')
cv2.imshow("result",a)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)

print('顯示原圖')
cv2.imshow("lena",lena)

cv2.imshow("dollar",dollar)

face=lena[220:400,250:350]
dollar[160:340,200:300]=face

print('顯示修改後的圖')
cv2.imshow("result",dollar)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

lena=cv2.imread("lenacolor.png")

print('顯示原圖')
cv2.imshow("lena1",lena)

b=lena[:,:,0]
g=lena[:,:,1]
r=lena[:,:,2]

print('顯示 藍 通道 圖')
cv2.imshow("b",b)

print('顯示 綠 通道 圖')
cv2.imshow("g",g)

print('顯示 紅 通道 圖')
cv2.imshow("r",r)

lena[:,:,0]=0
cv2.imshow("lenab0",lena)

lena[:,:,1]=0
cv2.imshow("lenab0g0",lena)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('將一圖分解成 藍 綠 紅 三通道')
lena=cv2.imread("lenacolor.png")

b,g,r=cv2.split(lena)

print('顯示 藍 通道 圖')
cv2.imshow("B",b)

print('顯示 綠 通道 圖')
cv2.imshow("G",g)

print('顯示 紅 通道 圖')
cv2.imshow("R",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('將一圖分解成 藍 綠 紅 三通道')
lena=cv2.imread("lenacolor.png")

b,g,r=cv2.split(lena)

bgr=cv2.merge([b,g,r])
rgb=cv2.merge([r,g,b])

cv2.imshow("lena",lena)

cv2.imshow("bgr",bgr)

cv2.imshow("rgb",rgb)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

gray=cv2.imread("lena.bmp",0)
color=cv2.imread("lenacolor.png")

print("图像gray属性：")
print("gray.shape=",gray.shape)
print("gray.size=",gray.size)
print("gray.dtype=",gray.dtype)
print("图像color属性：")
print("color.shape=",color.shape)
print("color.size=",color.size)
print("color.dtype=",color.dtype)


print('------------------------------------------------------------')	#60個

