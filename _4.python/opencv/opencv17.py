import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)

plt.figure('修改一部份資料', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

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

plt.subplot(122)
plt.title('修改後的圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
gray = cv2.imread(filename, 0)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
color = cv2.imread(filename)

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
img = cv2.imread(filename)

plt.figure('修改一部份資料', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

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
print("修改後img[0,0]=",img[0,0])
print("修改後img[0,0,0]=",img[0,0,0])
print("修改後img[0,0,1]=",img[0,0,1])
print("修改後img[0,0,2]=",img[0,0,2])
print("修改後img[50,0]=",img[50,0])
print("修改後img[100,0]=",img[100,0])

plt.subplot(122)
plt.title('修改後的圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
a = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('擷取一塊處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print('擷取一塊出來, 並顯示之')
face = a[200:400,200:380] #h, w

plt.subplot(132)
plt.title('擷取一塊出來')
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))

print('將其中一塊亂碼化, 並顯示之')
x_st = 50
y_st = 50
w = 100
h = 180
face=np.random.randint(0,256,(h,w,3))
a[y_st:y_st+h,x_st:x_st+w]=face

plt.subplot(133)
plt.title('將其中一塊亂碼化')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

#A圖
filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp'
lena = cv2.imread(filename1,cv2.IMREAD_UNCHANGED)

plt.figure('A圖抓一塊貼到B圖上', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

#B圖
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
peony = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

plt.subplot(132)
plt.title('原圖')
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

print('A圖抓一塊貼到B圖上')
face = lena[220:400,250:350]
peony[160:340,200:300] = face

plt.subplot(133)
plt.title('顯示修改後的圖')
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

