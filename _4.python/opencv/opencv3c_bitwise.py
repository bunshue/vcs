"""

cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
cv2.bitwise_xor(a,b)
cv2.bitwise_or(a,b)
cv2.bitwise_not(a)


"""

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
a = cv2.imread(filename, 0)  #通道不同

b=np.zeros(a.shape,dtype=np.uint8) #與a一樣大的黑圖
b[100:400,200:400]=255 #某塊做mask
b[100:500,100:200]=255 #某塊做mask

print('顯示原圖與mask作用後的圖')
c=cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
print("a.shape=",a.shape)
print("b.shape=",b.shape)

plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('mask')
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('顯示原圖與mask作用後的圖')
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

plt.show()


print('------------------------------------------------------------')	#60個

plt.figure('mask', figsize = (16, 12))

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

#三維 1
a = cv2.imread(filename, 1)  #通道不同
#w, h, c = a.shape
print(a.shape)

plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

mask = np.zeros(a.shape,dtype=np.uint8) #與a一樣大的黑圖 三維mask
print(mask.shape)
#     y       x
mask[30:170,30:270]=255 #某塊做mask
mask[30:370,80:220]=255 #某塊做mask

plt.subplot(132)
plt.title('mask')
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))

print('顯示原圖與mask作用後的圖')
c=cv2.bitwise_and(a,mask)  #a mask都成立的 擷取出來 #三維XOR
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)

plt.subplot(133)
plt.title('顯示原圖與mask作用後的圖')
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個


#異或加密解密
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
#filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

#三維 1
lena = cv2.imread(filename, 1)  # 以下程式只能處理灰階 因為xor操作維度錯誤
print(lena.shape)

#一維 0
lena = cv2.imread(filename, 0)  # 以下程式只能處理灰階 因為xor操作維度錯誤
print(lena.shape)

cc = lena.shape
print(cc)

key = np.random.randint(0,256,size=[cc[0],cc[1]],dtype=np.uint8)
encryption = cv2.bitwise_xor(lena,key)
decryption = cv2.bitwise_xor(encryption,key)

plt.figure('new01', figsize = (16, 12))
plt.subplot(141)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(142)
plt.title('key')
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(143)
plt.title('encryption')
plt.imshow(cv2.cvtColor(encryption, cv2.COLOR_BGR2RGB))

plt.subplot(144)
plt.title('decryption')
plt.imshow(cv2.cvtColor(decryption, cv2.COLOR_BGR2RGB))

plt.suptitle('XOR 加密解密')
plt.show()

print('------------------------------------------------------------')	#60個


#讀取原始載體圖像
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena=cv2.imread(filename, 0)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/watermark.bmp'
#讀取水印圖像
watermark=cv2.imread(filename, 0)
print('顯示原圖')

#將水印內的255處理為1，以方便嵌入
#后續章節會介紹使用threshold處理。
w=watermark[:,:]>0
watermark[w]=1
#讀取原始載體圖像的shape值
r,c=lena.shape
#============嵌入過程============
#生成內部值都是254的數組
t254=np.ones((r,c),dtype=np.uint8)*254
#獲取lena圖像的高7位
lenaH7=cv2.bitwise_and(lena,t254)
#將watermark嵌入到lenaH7內
e=cv2.bitwise_or(lenaH7,watermark)
#============提取過程============
#生成內部值都是1的數組
t1=np.ones((r,c),dtype=np.uint8)
#從載體圖像內，提取水印圖像
wm=cv2.bitwise_and(e,t1)
print(wm)
#將水印內的1處理為255以方便顯示
#后續章節會介紹threshold實現。
w=wm[:,:]>0
wm[w]=255

plt.figure('new02', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('watermark')
#當前watermark內最大值為1
plt.imshow(cv2.cvtColor(watermark * 255, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('e')
plt.imshow(cv2.cvtColor(e, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('wm')
plt.imshow(cv2.cvtColor(wm, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

#讀取原始載體圖像
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena = cv2.imread(filename, 0)

#讀取原始載體圖像的shape值
r,c=lena.shape
mask=np.zeros((r,c),dtype=np.uint8)
mask[220:400,250:350]=1
#獲取一個key,打碼、解碼所使用的密鑰
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
#============獲取打碼臉============
#使用密鑰key加密原始圖像lena
lenaXorKey=cv2.bitwise_xor(lena,key) 
#獲取加密圖像的臉部信息encryptFace
encryptFace=cv2.bitwise_and(lenaXorKey,mask*255)
#將圖像lena內的臉部值設置為0，得到noFace1
noFace1=cv2.bitwise_and(lena,(1-mask)*255)
#得到打碼的lena圖像
maskFace=encryptFace+noFace1
#============將打碼臉解碼============
#將臉部打碼的lena與密鑰key異或，得到臉部的原始信息
extractOriginal=cv2.bitwise_xor(maskFace,key)
#將解碼的臉部信息extractOriginal提取出來得到extractFace
extractFace=cv2.bitwise_and(extractOriginal,mask*255)
#從臉部打碼的lena內提取沒有臉部信息的lena圖像，得到noFace2
noFace2=cv2.bitwise_and(maskFace,(1-mask)*255)
#得到解碼的lena圖像
extractLena=noFace2+extractFace

plt.figure('new03', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('mask')
plt.imshow(cv2.cvtColor(mask*255, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title('1-mask')
plt.imshow(cv2.cvtColor((1-mask)*255, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title('key')
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('lenaXorKey')
plt.imshow(cv2.cvtColor(lenaXorKey, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('encryptFace')
plt.imshow(cv2.cvtColor(encryptFace, cv2.COLOR_BGR2RGB))

plt.show()

plt.figure('new04', figsize = (16, 12))

plt.subplot(231)
plt.title('noFace1')
plt.imshow(cv2.cvtColor(noFace1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('maskFace')
plt.imshow(cv2.cvtColor(maskFace, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title('extractOriginal')
plt.imshow(cv2.cvtColor(extractOriginal, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title('extractFace')
plt.imshow(cv2.cvtColor(extractFace, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('noFace2')
plt.imshow(cv2.cvtColor(noFace2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('extractLena')
plt.imshow(cv2.cvtColor(extractLena, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

#圖層提取
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena = cv2.imread(filename, 0)

print('顯示原圖')

plt.figure('new05', figsize = (16, 12))
plt.subplot(331)
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))
plt.title('原圖')

r, c = lena.shape
x = np.zeros((r, c, 8), dtype = np.uint8)

for i in range(8):
    x[:,:,i]=2**i

r=np.zeros((r,c,8),dtype=np.uint8)

for i in range(8):
    print(i)
    r[:,:,i]=cv2.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(r[:,:,i], cv2.COLOR_BGR2RGB))
    plt.title(str(i))

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

plt.figure('new34 影像處理', figsize = (16, 12))
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

plt.figure('new35 影像處理', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('ROI')
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

print('將圖片顏色反轉 (負片效果) 原圖')
img = cv2.imread(r'images/sample.jpg')
cv2.imshow('Sample pic', img)

print('將圖片顏色反轉 (負片效果) 效果')
img_invert = cv2.bitwise_not(img)
cv2.imshow('Sample pic', img_invert)

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




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

