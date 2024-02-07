# opencv 集合

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('blur 效果 1')
r = cv2.blur(image, (5, 5))

plt.figure('blur 效果', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('blur 效果 1')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('blur 效果 2')
image_blur_05 = cv2.blur(image, (5, 5))      
image_blur_30 = cv2.blur(image, (30, 30))      

plt.figure('blur 效果', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('blur 效果 2')
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('blur 效果 2')
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 1')
image_boxFilter = cv2.boxFilter(image, -1, (5, 5)) 

plt.figure('boxFilter 效果 1', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 1')
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 2')
image_boxFilter = cv2.boxFilter(image, -1, (5, 5), normalize = 0)

plt.figure('boxFilter 效果 2', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 2')
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('boxFilter 效果 3')
image_boxFilter = cv2.boxFilter(image, -1, (2, 2), normalize = 0)

plt.figure('boxFilter 效果 3', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('boxFilter 效果 3')
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('medianBlur 效果 1')
image_medianBlur = cv2.medianBlur(image, 3)

plt.figure('medianBlur 效果 1', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('medianBlur 效果 1')
plt.imshow(cv2.cvtColor(image_medianBlur, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('bilateralFilter 效果 1')
image_bilateralFilter = cv2.bilateralFilter(image, 25, 100, 100)

plt.figure('bilateralFilter 效果 1', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('bilateralFilter 效果 1')
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp'
image = cv2.imread(filename)

print('bilateralFilter 效果 2')
image_bilateralFilter = cv2.bilateralFilter(image, 55, 100, 100)

plt.figure('bilateralFilter 效果 2', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('bilateralFilter 效果 2')
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename)

print('filter2D 效果')
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure('filter2D 效果', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('filter2D 效果')
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'

image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype = int)    #水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype = int)    #垂直值一樣, 偵測垂直的邊緣

print('filter2D 效果')

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Prewitt_horizon')
#躺平的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Prewitt_vertical')
#直放的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

def saltpepper(image, n):
    m=int((image.shape[0] * image.shape[1]) * n)
    for a in range(m):
        i=int(np.random.random()*image.shape[1])
        j=int(np.random.random()*image.shape[0])
        if image.ndim==2:
            image[j,i]=255
        elif image.ndim==3:
            image[j,i,0]=255
            image[j,i,1]=255
            image[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*image.shape[1])
        j=int(np.random.random()*image.shape[0])
        if image.ndim==2:
            image[j,i]=0
        elif image.ndim==3:
            image[j,i,0]=0
            image[j,i,1]=0
            image[j,i,2]=0
    return image

#上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename)

print('saltpepper 效果')
saltImage = saltpepper(image, 0.02)

plt.figure('saltpepper 效果', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('saltpepper 效果')
plt.imshow(cv2.cvtColor(saltImage, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename)

print('二值化')
#        cv2.threshold(img, 閥值, 最大灰度值, 使用的二值化方法)
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#t, rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

plt.figure('二值化', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('二值化圖, 閥值 127, 小於變全黑, 大於變全白')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg'
img = cv2.imread(filename, 0)

t1,thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
athdMEAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
athdGAUS = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('thd')
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('athdMEAN')
plt.imshow(cv2.cvtColor(athdMEAN, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('athdGAUS')
plt.imshow(cv2.cvtColor(athdGAUS, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp'
img = cv2.imread(filename, 0)

t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('thd')
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('otsu')
plt.imshow(cv2.cvtColor(otsu, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

print('原圖 彩色')
image = cv2.imread(filename)
print("image.shape=",image.shape)

print('原圖 彩色 轉 灰階1通道')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray.shape=",gray.shape)

print('灰階 轉 BGR3通道')
rgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
print("rgb.shape=",rgb.shape)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖 彩色')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('灰階1通道')
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('BGR3通道')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image = cv2.imread(filename)

print('原圖 BGR 轉 RGB')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure('影像處理', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖 B-G-R OK')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('原圖 BGR 轉 RGB NG')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/rgb512.bmp'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/opencv.png'
image = cv2.imread(filename)

print('原圖 BGR 轉 HSV')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#=============指定藍色值的范圍=============
minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
#確定藍色區域
mask = cv2.inRange(hsv, minBlue, maxBlue)
#通過掩碼控制的按位與，鎖定藍色區域
blue = cv2.bitwise_and(image, image, mask = mask)

#=============指定綠色值的范圍=============
minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
#確定綠色區域
mask = cv2.inRange(hsv, minGreen, maxGreen)
#通過掩碼控制的按位與，鎖定綠色區域
green = cv2.bitwise_and(image, image, mask = mask)

#=============指定紅色值的范圍=============
minRed = np.array([0,50,50])
maxRed = np.array([30,255,255])
#確定紅色區域
mask = cv2.inRange(hsv, minRed, maxRed)
#通過掩碼控制的按位與，鎖定紅色區域
red= cv2.bitwise_and(image, image, mask = mask)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('HSV')
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))

#plt.subplot(233)
#plt.title('')

plt.subplot(234)
plt.title('R')
plt.imshow(cv2.cvtColor(red, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('G')
plt.imshow(cv2.cvtColor(green, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('B')
plt.imshow(cv2.cvtColor(blue, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lesson2.jpg'
img = cv2.imread(filename)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
minHue = 5
maxHue = 170
hueMask = cv2.inRange(h, minHue, maxHue)
minSat = 25
maxSat = 166
satMask = cv2.inRange(s, minSat, maxSat)
mask = hueMask & satMask
roi = cv2.bitwise_and(img, img, mask = mask)

plt.figure('影像處理', figsize = (16, 12))

plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('ROI')
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
img = cv2.imread(filename)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
v[:,:]=255
newHSV=cv2.merge([h,s,v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

plt.subplot(223)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('art')
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
img = cv2.imread(filename)

bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
b,g,r,a=cv2.split(bgra)
a[:,:]=125
bgra125=cv2.merge([b,g,r,a])
a[:,:]=0
bgra0=cv2.merge([b,g,r,a])

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('bgra')
plt.imshow(cv2.cvtColor(bgra, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('bgra125')
plt.imshow(cv2.cvtColor(bgra125, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('bgra0')
plt.imshow(cv2.cvtColor(bgra0, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

#偽寫入
#cv2.imwrite("tmp_bgra.png", bgra)
#cv2.imwrite("tmp_bgra125.png", bgra125)
#cv2.imwrite("tmp_bgra0.png", bgra0)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename, 0)

plt.figure('修改一部份資料', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print('修改一部份資料 1')
for i in range(20, 60):    # y
    for j in range(20, 100):    # x
        image[i,j] = 255

print('修改一部份資料 2')
#測試讀取、修改單個像素值
print("讀取像素點image.item(3,2)=", image.item(3,2))
image.itemset((3,2),255)
print("修改後像素點image.item(3,2)=", image.item(3,2))
#測試修改一個區域的像素值
for i in range(100,200):    #y
    for j in range(20,60): #x
        image.itemset((i,j),220)

plt.subplot(222)
plt.title('修改後的圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image = cv2.imread(filename)

plt.subplot(223)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("讀取image[0,0]=", image[0,0])
print("讀取image[0,0,0]=", image[0,0,0])
print("讀取image[0,0,1]=", image[0,0,1])
print("讀取image[0,0,2]=", image[0,0,2])
print("讀取image[50,0]=", image[50,0])
print("讀取image[100,0]=", image[100,0])
#區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            image[i, j, k] = 255  #白色
#區域2
for i in range(50, 100):
    for j in range(0, 100):
        image[i, j] = [128, 128, 128]  #灰色
#區域3
for i in range(100, 150):
    for j in range(0, 100):
        image[i, j]=0          #黑色
#區域4
print("讀取image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("讀取image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("讀取image.item(0, 0, 2) = ", image.item(0, 0, 2))
for i in range(200, 250):
    for j in range(0, 100):
        for k in range(0, 3):
            image.itemset((i, j, k), 255)     #白色

print("修改後image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("修改後image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("修改後image.item(0, 0, 2) = ", image.item(0, 0, 2))
print("修改後image[0, 0] = ",image[0, 0])
print("修改後image[0, 0, 0] = ",image[0, 0, 0])
print("修改後image[0, 0, 1] = ",image[0, 0, 1])
print("修改後image[0, 0, 2] = ",image[0, 0, 2])
print("修改後image[50, 0] = ",image[50, 0])
print("修改後image[100, 0] = ",image[100, 0])

plt.subplot(224)
plt.title('修改後的圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
a = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('擷取一塊處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print('擷取一塊出來, 並顯示之')
face = a[200:400,200:380] #h, w

plt.subplot(232)
plt.title('擷取一塊出來')
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))

print('將其中一塊亂碼化, 並顯示之')
x_st = 50
y_st = 50
w = 100
h = 180
face=np.random.randint(0,256,(h,w,3))
a[y_st:y_st+h,x_st:x_st+w]=face

plt.subplot(233)
plt.title('將其中一塊亂碼化')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

#A圖
filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp'
lena = cv2.imread(filename1,cv2.IMREAD_UNCHANGED)

#A圖抓一塊貼到B圖上
plt.subplot(234)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

#B圖
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
peony = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

plt.subplot(235)
plt.title('原圖')
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

print('A圖抓一塊貼到B圖上')
face = lena[220:400,250:350]
peony[160:340,200:300] = face

plt.subplot(236)
plt.title('顯示修改後的圖')
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個


'''
#opencv
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import matplotlib.pyplot as plt
import cv2

image = cv2.imread(filename)	#讀取本機圖片

#plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#先轉換成RGB再顯示

plt.show()
'''
print('------------------------------------------------------------')	#60個

#用 OpenCV 讀取並顯示圖片

#等同於 plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #BGR轉RGB再交由matplotlib顯示之
def aidemy_imshow(name, img):
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    plt.title(name)
    plt.imshow(img)
    plt.show()

cv2.imshow = aidemy_imshow

img = cv2.imread(r'images/sample.jpg')

print(type(img))

print(img.shape)

cv2.imshow('Sample pic', img)

print('------------------------------------------------------------')	#60個

print('OpenCV建立檔案 256X256之紅圖')
img_size = 256
img = np.array([[(0, 0, 255) for x in range(img_size)] for x in range(img_size)])
cv2.imshow('Sample pic 2', img)
#cv2.imwrite(r'sample_222.jpg', img)

print('------------------------------------------------------------')	#60個

print('OpenCV建立檔案')
img_size = 256
img = np.array( [[(x, int((x + y) / 2), y) for x in range(img_size)] for y in range(img_size)])
cv2.imshow('Sample pic 3', img)
#cv2.imwrite(r'sample_333.jpg', img)

print('------------------------------------------------------------')	#60個

print('裁剪圖片a')

img = cv2.imread(r'images/sample.jpg')

H = img.shape[0]
W = img.shape[1]
print('H * W =', img.shape)
print('H =', H)
print('W =', W)

print('裁剪圖片b')
#img_cut = img[0:(H * 2 // 3), 0:(W * 2 // 3)]
img_cut = img[0:(H * 1 // 2), 0:(W * 1 // 2)]
print(img_cut.shape)
cv2.imshow('Sample pic', img_cut)

print('------------------------------------------------------------')	#60個

print('圖片翻轉 原圖')

img = cv2.imread(r'images/sample.jpg') 
cv2.imshow('Sample pic', img)

print('圖片翻轉 效果')
img_flip = cv2.flip(img, -999)
img_flip2 = cv2.flip(img, -88)

cv2.imshow('Sample pic', img_flip)

print('------------------------------------------------------------')	#60個

print('圖片旋轉')

img = cv2.imread(r'images/sample.jpg')

H = img.shape[0]
W = img.shape[1]
aff_matrix = cv2.getRotationMatrix2D((W / 2, H / 2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (W, H))
cv2.imshow('Sample pic', img_rotate)

print('------------------------------------------------------------')	#60個

print('圖片旋轉')
img_rotate = cv2.rotate(img, 1) 
cv2.imshow('Sample pic', img_rotate)

print('------------------------------------------------------------')	#60個

print('圖片色彩空間的轉換')
img = cv2.imread(r'images/sample.jpg')
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow('Sample pic', img_convert)

print('------------------------------------------------------------')	#60個

print('將圖片顏色反轉 (負片效果) 原圖')
img = cv2.imread(r'images/sample.jpg')
cv2.imshow('Sample pic', img)

print('將圖片顏色反轉 (負片效果) 效果')
img_invert = cv2.bitwise_not(img)       
cv2.imshow('Sample pic', img_invert)

print('------------------------------------------------------------')	#60個

#OpenCV 進階圖片處理功能

print('圖片的二值化處理')
img = cv2.imread(r'images/sample.jpg')
thr, img_binary = cv2.threshold(img, 192, 255, cv2.THRESH_TOZERO)
cv2.imshow('Sample pic', img_binary)

print('------------------------------------------------------------')	#60個

print('遮罩')

img = cv2.imread(r'images/sample.jpg')
H = img.shape[0]
W = img.shape[1]
mask = cv2.imread(r'images/mask.jpg', cv2.IMREAD_GRAYSCALE)
mask = cv2.resize(mask, (W, H))
img_masked = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('Sample pic', img_masked)

print('------------------------------------------------------------')	#60個

print('遮罩')
mask = cv2.bitwise_not(mask)        
img_masked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('Sample pic', img_masked)

print('------------------------------------------------------------')	#60個

print('去除圖片的雜訊 原圖')

img2 = cv2.imread(r'images/sample2.jpg')

cv2.imshow('Sample pic', img2)

print('去除圖片的雜訊 效果')

img2_denoised = cv2.fastNlMeansDenoisingColored(img2, h = 5)

cv2.imshow('Sample pic', img2_denoised)

print('------------------------------------------------------------')	#60個

"""
各種邊緣檢測的方法

"""
print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 1')
sobelx = cv2.Sobel(image, -1, 1, 0)

plt.subplot(232)
plt.title('Sobel 效果 1')
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 2 x 方向')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  

plt.subplot(233)
plt.title('Sobel 效果 2 x 方向')
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 3 y 方向')
sobely = cv2.Sobel(image, cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)

plt.subplot(234)
plt.title('Sobel 效果 3 y 方向')
plt.imshow(cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 4 x-y 方向')
sobelxy=cv2.Sobel(image, cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 

plt.subplot(235)
plt.title('Sobel 效果 4 x-y 方向')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 5 先x 再y 方向')
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  

plt.subplot(236)
plt.title('Sobel 效果 5 先x 再y 方向')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 6')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0)
sobely = cv2.Sobel(image, cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(image, cv2.CV_64F,1,1)
sobelxy11=cv2.convertScaleAbs(sobelxy11)

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel xy')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Sobel xy11')
plt.imshow(cv2.cvtColor(sobelxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('Scharr 效果 1')
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  

print('Scharr 效果 2')
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)  

print('Scharr 效果 3')
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  

plt.figure('Scharr', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('Scharr 效果 1')
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('Scharr 效果 2')
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('Scharr 效果 3')
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('Scharr 效果')
#scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 1)   #fail
scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 0)    #ok
scharrxy11 = cv2.convertScaleAbs(scharrxy11)   # 转回uint8  

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Scharr 效果')
plt.imshow(cv2.cvtColor(scharrxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 1')
scharrx = cv2.Sobel(image, cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(image, cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel x')
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Sobel y')
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 2')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0) 
scharrx = cv2.Scharr(image, cv2.CV_64F,1,0)
scharry = cv2.Scharr(image, cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel xy')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Scharr xy')
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/laplacian.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Laplacian 效果')
Laplacian = cv2.Laplacian(image, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   

plt.figure('Laplacian', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Laplacian')
plt.imshow(cv2.cvtColor(Laplacian, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

