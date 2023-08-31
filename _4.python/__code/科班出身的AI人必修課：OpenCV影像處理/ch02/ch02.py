import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("before",img)

print('修改一部份資料 1')
for i in range(20, 60):    # y
    for j in range(20, 100):    # x
        img[i,j] = 255

print('修改一部份資料 2')
#測試讀取、修改單個像素值
print("讀取像素點img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改後像素點img.item(3,2)=",img.item(3,2))
#測試修改一個區域的像素值
for i in range(100,200):    #y
    for j in range(20,60): #x
        img.itemset((i,j),220)

print('顯示修改後的圖')
cv2.imshow("after",img)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
gray=cv2.imread(filename, 0)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
color=cv2.imread(filename)

print("圖像gray屬性：")
print("gray.shape=",gray.shape)
print("gray.size=",gray.size)
print("gray.dtype=",gray.dtype)
print("圖像color屬性：")
print("color.shape=",color.shape)
print("color.size=",color.size)
print("color.dtype=",color.dtype)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
img=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("before",img)

print("讀取img[0,0]=",img[0,0])
print("讀取img[0,0,0]=",img[0,0,0])
print("讀取img[0,0,1]=",img[0,0,1])
print("讀取img[0,0,2]=",img[0,0,2])
print("讀取img[50,0]=",img[50,0])
print("讀取img[100,0]=",img[100,0])
#區域1
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img[i,j,k]=255  #白色
#區域2
for i in range(50,100):
    for j in range(0,100):
        img[i,j]=[128,128,128]  #灰色
#區域3
for i in range(100,150):
    for j in range(0,100):
        img[i,j]=0          #黑色
#區域4
print("讀取img.item(0,0,0)=",img.item(0,0,0))
print("讀取img.item(0,0,1)=",img.item(0,0,1))
print("讀取img.item(0,0,2)=",img.item(0,0,2))
for i in range(200,250):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k),255)     #白色

print("修改後img.item(0,0,0)=",img.item(0,0,0))
print("修改後img.item(0,0,1)=",img.item(0,0,1))
print("修改後img.item(0,0,2)=",img.item(0,0,2))

print('顯示修改後的圖')
cv2.imshow("after",img)

print("修改後img[0,0]=",img[0,0])
print("修改後img[0,0,0]=",img[0,0,0])
print("修改後img[0,0,1]=",img[0,0,1])
print("修改後img[0,0,2]=",img[0,0,2])
print("修改後img[50,0]=",img[50,0])
print("修改後img[100,0]=",img[100,0])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
a=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",a)

print('擷取一塊出來, 並顯示之')
face=a[200:400,200:380] #h, w
cv2.imshow("face",face)

print('將其中一塊亂碼化, 並顯示之')
x_st = 50
y_st = 50
w = 100
h = 180
face=np.random.randint(0,256,(h,w,3))
a[y_st:y_st+h,x_st:x_st+w]=face
cv2.imshow("result",a)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena=cv2.imread(filename,cv2.IMREAD_UNCHANGED)
print('顯示原圖')
#cv2.imshow("lena",lena)

dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
print('顯示原圖')
#cv2.imshow("dollar",dollar)

print('A圖抓一塊貼到B圖上')
face=lena[220:400,250:350]
dollar[160:340,200:300]=face
print('顯示修改後的圖')
cv2.imshow("result",dollar)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
lena=cv2.imread(filename)
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


print('設定第0通道為0')
lena[:,:,0]=0
cv2.imshow("lenab0",lena)

print('設定第1通道為0')
lena[:,:,1]=0
cv2.imshow("lenab0g0",lena)
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('將一圖分解成 藍 綠 紅 三通道')
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
lena=cv2.imread(filename)

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
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
lena=cv2.imread(filename)

b,g,r=cv2.split(lena)

bgr=cv2.merge([b,g,r])
rgb=cv2.merge([r,g,b])

cv2.imshow("lena",lena)

cv2.imshow("bgr",bgr)

cv2.imshow("rgb",rgb)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個
