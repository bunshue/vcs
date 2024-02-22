"""
opencv 集合

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/boat.bmp'
image1 = cv2.imread(filename)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image2 = cv2.imread(filename)

print('兩圖直接相加')
result1 = image1 + image2

print('兩圖用cv相加')
result2 = cv2.add(image1, image2)

plt.figure('相加', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('兩圖直接相加')
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title('兩圖用cv相加')
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

print('兩圖做alpha疊加')
result = cv2.addWeighted(image1, 0.6, image2, 0.4, 0)

plt.subplot(234)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('兩圖做alpha疊加')
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

#plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp'
lena = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dollar.bmp'
dollar = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('疊加', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

print('兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之')
face1=lena[220:400,250:350]
face2=dollar[160:340,200:300]
add=cv2.addWeighted(face1,0.6,face2,0.4,0)
dollar[160:340,200:300]=add

plt.subplot(233)
plt.title('兩圖擷取某塊做alpha疊加, 再貼回原圖')
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

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

plt.subplot(234)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('mask')
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('顯示原圖與mask作用後的圖')
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

#plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
a = cv2.imread(filename, 1)  #通道不同

plt.figure('mask', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

b = np.zeros(a.shape,dtype=np.uint8) #與a一樣大的黑圖
b[100:400,200:400]=255 #某塊做mask
b[100:500,100:200]=255 #某塊做mask

plt.subplot(232)
plt.title('mask')
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))

print('顯示原圖與mask作用後的圖')
c=cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
print("a.shape=",a.shape)
print("b.shape=",b.shape)

plt.subplot(233)
plt.title('顯示原圖與mask作用後的圖')
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
a = cv2.imread(filename, 1)

plt.subplot(234)
plt.title('原圖')
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

w, h, c = a.shape

mask=np.zeros((w,h),dtype=np.uint8)
mask[100:400,200:400]=255
mask[100:500,100:200]=255
c=cv2.bitwise_and(a,a,mask)
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)

plt.subplot(235)
plt.title('mask')
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('顯示原圖與mask作用後的圖')
plt.imshow(cv2.cvtColor(c, cv2.COLOR_BGR2RGB))

#plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#異或加密解密
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena = cv2.imread(filename, 0)

r, c = lena.shape
key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption = cv2.bitwise_xor(lena,key)
decryption = cv2.bitwise_xor(encryption,key)

plt.figure('g', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('key')
plt.imshow(cv2.cvtColor(key, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('encryption')
plt.imshow(cv2.cvtColor(encryption, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('decryption')
plt.imshow(cv2.cvtColor(decryption, cv2.COLOR_BGR2RGB))

plt.tight_layout()
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

plt.figure('h', figsize = (16, 12))
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

plt.tight_layout()
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

plt.figure('', figsize = (16, 12))
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

plt.tight_layout()
plt.show()

plt.figure('', figsize = (16, 12))

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

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

"""
#圖層提取
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
lena = cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("lena",lena)

r, c = lena.shape
x = np.zeros((r, c, 8), dtype = np.uint8)
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
"""
print('------------------------------------------------------------')	#60個

"""
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

img = cv2.imread(filename) #cv2讀取圖片, 自動轉成array

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #轉換為HSV
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #轉換為RGB

plt.imshow(rgb)
plt.show()

coordinate = rgb[131, 81] #輸入要取得顏色的指定座標
print(coordinate)

#print(array([255, 219,  79], dtype=uint8))




print('------------------------------------------------------------')	#60個


import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = cv2.imread(filename)

image[0,0]=[0,0,255]
image[70:120, 200:250]=[0,255,0]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()
"""

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

o = cv2.imread("images/rice.png", cv2.IMREAD_UNCHANGED)
k = np.ones((5, 5), np.uint8)
e = cv2.erode(o, k)
b = cv2.subtract(o, e)

plt.figure('', figsize = (16, 8))
plt.subplot(131)
plt.imshow(o)

plt.subplot(132)
plt.imshow(e)

plt.subplot(133)
plt.imshow(b)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, fore = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

plt.figure('', figsize = (16, 8))
plt.subplot(131)
plt.imshow(ishow)

plt.subplot(132)
plt.imshow(dist_transform)

plt.subplot(133)
plt.imshow(fore)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
bg = cv2.dilate(opening,kernel,iterations=3)
dist = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, fore = cv2.threshold(dist,0.7*dist.max(),255,0)
fore = np.uint8(fore)
un = cv2.subtract(bg,fore)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.imshow(ishow)

plt.subplot(222)
plt.imshow(bg)

plt.subplot(223)
plt.imshow(fore)

plt.subplot(224)
plt.imshow(un)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, fore = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
fore = np.uint8(fore)
ret, markers = cv2.connectedComponents(fore)
print(ret)

plt.figure('', figsize = (16, 8))
plt.subplot(131)
plt.imshow(ishow)

plt.subplot(132)
plt.imshow(fore)

plt.subplot(133)
plt.imshow(markers)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, fore = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
fore = np.uint8(fore)
ret, markers1 = cv2.connectedComponents(fore)
foreAdv=fore.copy()
unknown = cv2.subtract(sure_bg,foreAdv)
ret, markers2 = cv2.connectedComponents(foreAdv)
markers2 = markers2+1
markers2[unknown==255] = 0

plt.figure('', figsize = (16, 8))
plt.subplot(121)
plt.imshow(markers1)

plt.subplot(122)
plt.imshow(markers2)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/water_coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
ishow=img.copy()
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [0,255,0]

plt.figure('', figsize = (16, 8))
plt.subplot(121)
plt.imshow(ishow)

plt.subplot(122)
plt.imshow(img)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
o = cv2.imread(filename)
orgb=cv2.cvtColor(o,cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,50,400,400)
cv2.grabCut(o,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
ogc = o*mask2[:,:,np.newaxis]
ogc = cv2.cvtColor(ogc,cv2.COLOR_BGR2RGB)

plt.figure('', figsize = (16, 8))
plt.subplot(121)
plt.imshow(orgb)

plt.subplot(122)
plt.imshow(ogc)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
o= cv2.imread(filename)
orgb=cv2.cvtColor(o,cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2],np.uint8)
bgd = np.zeros((1,65),np.float64)
fgd = np.zeros((1,65),np.float64)
rect = (50,50,400,500)
cv2.grabCut(o,mask,rect,bgd,fgd,5,cv2.GC_INIT_WITH_RECT)
mask2 = cv2.imread('images/mask.png',0)
mask2Show = cv2.imread('images/mask.png',-1)
m2rgb=cv2.cvtColor(mask2Show,cv2.COLOR_BGR2RGB)
mask[mask2 == 0] = 0
mask[mask2 == 255] = 1
mask, bgd, fgd = cv2.grabCut(o,mask,None,bgd,fgd,5,cv2.GC_INIT_WITH_MASK)
mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
ogc = o*mask[:,:,np.newaxis]
ogc = cv2.cvtColor(ogc,cv2.COLOR_BGR2RGB)

plt.figure('', figsize = (16, 8))
plt.subplot(121)
plt.imshow(m2rgb)

plt.subplot(122)
plt.imshow(ogc)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
o= cv2.imread(filename)
orgb=cv2.cvtColor(o,cv2.COLOR_BGR2RGB)
bgd = np.zeros((1,65),np.float64)
fgd = np.zeros((1,65),np.float64)
mask2 = np.zeros(o.shape[:2],np.uint8)
mask2[30:512,50:400]=3
mask2[50:300,150:200]=1
cv2.grabCut(o,mask2,None,bgd,fgd,5,cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask2==2)|(mask2==0),0,1).astype('uint8')
ogc = o*mask2[:,:,np.newaxis]
ogc = cv2.cvtColor(ogc,cv2.COLOR_BGR2RGB)

plt.figure('', figsize = (16, 8))
plt.subplot(121)
plt.imshow(orgb)

plt.subplot(122)
plt.imshow(ogc)

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

img = cv2.imread(filename, 0)
img2 = img.copy()
template = cv2.imread('images/temp.bmp',0)
th, tw = template.shape[::]
img = img2.copy()
rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

#矩形之左上點
topLeft = minLoc
#矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)

plt.subplot(121)
plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result')

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)
img2 = img.copy()
template = cv2.imread('images/temp.bmp',0)
tw, th = template.shape[::-1]
img = img2.copy()
rv = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

#矩形之左上點
topLeft = maxLoc
#矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)

plt.subplot(121)
plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result')

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/lena4.bmp',0)
template = cv2.imread('images/lena4Temp.bmp',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, 1)
plt.imshow(img,cmap = 'gray')

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

d = 400
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #矩形之左上點
        p1x = x
        p1y = y
        #矩形之右下點
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x, p1y),(p2x, p2y), color, 2)
image = np.ones((d, d, 3), dtype = "uint8") * 255
cv2.namedWindow('Demo19.10')
cv2.setMouseCallback('Demo19.10', draw)
while(1):
    cv2.imshow('Demo19.10', image)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#fail
d = 400
global thickness
thickness = -1
def fill(x):
    pass
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #矩形之左上點
        p1x = x
        p1y = y
        #矩形之右下點
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x,p1y),(p2x,p2y),color,thickness)

image = np.ones((d, d, 3), np.uint8) * 255
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)
cv2.createTrackbar('R', 'image', 0, 1, fill)
while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xFF
    g = cv2.getTrackbarPos('R', 'image')
    if g == 0:
        thickness = -1
    else:
        thickness = 2        
    if k == 27:
        break   

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


"""
cv2.erode()
cv2.dilate()
cv2.morphologyEx()

erode 侵蝕
dilate 擴大 膨脹
morphology 形態學 構詞學

"""

print('------------------------------------------------------------')	#60個

def draw_line(img):
    for i in range(8):
        cv2.line(img, (0, 100*i), (700, 100*i), (0, 0, 255), 2) #水平線
        cv2.line(img, (100*i, 0), (100*i, 700), (0, 0, 255), 2) #垂直線
    
print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp'
filename = 'C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png'

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image3 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image4 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('erode 侵蝕 效果', figsize = (16, 12))

plt.subplot(221)
plt.title('原圖')
draw_line(image1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

print('erode 侵蝕 效果 1')
kernel = np.ones((25, 25), np.uint8)
erosion = cv2.erode(image2, kernel)

plt.subplot(222)
plt.title('erode 侵蝕 效果 1')
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

print('erode 侵蝕 效果 2')
kernel = np.ones((25, 25), np.uint8)
erosion = cv2.erode(image3, kernel)

plt.subplot(223)
plt.title('erode 侵蝕 效果 2')
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

print('erode 侵蝕 效果 3 加 iterations')
kernel = np.ones((9, 9), np.uint8)
erosion = cv2.erode(image4, kernel,iterations = 5)

plt.subplot(224)
plt.title('erode 侵蝕 效果 3')
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域被侵蝕、縮小了")
plt.tight_layout()
plt.show()


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp'
filename = 'C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png'

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image3 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image4 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('', figsize = (16, 12))

print('dilate 擴大 膨脹 效果')

plt.subplot(221)
plt.title('原圖')
draw_line(image1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('dilate 擴大 膨脹 效果 1')
kernel = np.ones((20, 20), np.uint8)
dilation = cv2.dilate(image2, kernel)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('dilate 擴大 膨脹 效果 2')
kernel = np.ones((40, 40), np.uint8)
dilation = cv2.dilate(image3, kernel)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('dilate 擴大 膨脹 效果 3 加 iterations')
kernel = np.ones((10, 10), np.uint8)
dilation = cv2.dilate(image4, kernel, iterations = 9)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域擴大、膨脹")
plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening.bmp'
img1 = cv2.imread(filename)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening2.bmp'
img2 = cv2.imread(filename)

print('morphologyEx 效果 1')
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 1')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 1')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing.bmp'
img1 = cv2.imread(filename)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing2.bmp'
img2 = cv2.imread(filename)

print('morphologyEx 效果 2')
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k, iterations = 3)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k, iterations = 3)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 2')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 2')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/gradient.bmp'
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 3')
k=np.ones((5, 5), np.uint8)
r=cv2.morphologyEx(image, cv2.MORPH_GRADIENT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('morphologyEx 效果 3')
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tophat.bmp'
image1 = cv2.imread(filename,cv2.IMREAD_UNCHANGED)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image2=cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 4')
k = np.ones((5,5),np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_TOPHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_TOPHAT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 4')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 4')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/blackhat.bmp'
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('morphologyEx 效果 5')
k = np.ones((5,5), np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_BLACKHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_BLACKHAT, k)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('morphologyEx 效果 5')
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('morphologyEx 效果 5')
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("kernel1 =\n", kernel1)
print("kernel2 =\n", kernel2)
print("kernel3 =\n", kernel3)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/kernel.bmp'
o = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print('dilate 擴大 膨脹 效果')
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59, 59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59, 59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59, 59))
dst1 = cv2.dilate(o, kernel1)
dst2 = cv2.dilate(o, kernel2)
dst3 = cv2.dilate(o, kernel3)

plt.figure('', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('dilate 擴大 膨脹 效果')
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('dilate 擴大 膨脹 效果')
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('dilate 擴大 膨脹 效果')
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('用np建立一個影像陣列')

W = 640
H = 480
D = 3

#建立陣列
image = np.ones([H, W, D], dtype = np.uint8) * 128  # 填滿 128

#改變陣列內容
image[:, :, 0] = 0;     #第0通道 B
image[:, :, 1] = 255;   #第1通道 G
image[:, :, 2] = 255;   #第2通道 R

#做resize
size = H, W
print(size)
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
#print("image = \n", image)

print("rst.shape = ", rst.shape)
#print("rst = \n", rst)

plt.figure('用np建立一個影像陣列', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖 640X480')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('resize 480X640')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

size = (int(W * 0.9), int(H * 1.1))#變瘦變高
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
print("rst.shape = ", rst.shape)

plt.figure('resize', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('resize 變瘦1成變高1成')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

rst = cv2.resize(image, None, fx = 2, fy = 0.5)
print("image.shape =", image.shape)
print("rst.shape =", rst.shape)

plt.subplot(223)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('resize x變2倍, y變一半')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

x = 100
y = 100
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.figure('影像處理 move', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('move')
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

M = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 0.6)
rotate = cv2.warpAffine(image, M, (W, H))

plt.figure('rotate', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('rotate')
plt.imshow(cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.figure('xxxxxx1', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/demo.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure('xxxxxx2', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape,np.float32)
mapy = np.zeros(image.shape,np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n",mapx)
print("mapy = \n",mapy)
print("rst = \n",rst)

plt.figure('xxxxxx3', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx4', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx5', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx6', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx7', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxx8', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 5], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxx9', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxa', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
image = np.random.randint(0, 256, size = [4, 6], dtype = np.uint8)

H, W = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)

mapx = np.zeros(image.shape, np.float32)
mapy = np.zeros(image.shape, np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), i)
            mapy.itemset((i, j), j)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n", mapx)
print("mapy = \n", mapy)
print("rst = \n", rst)

plt.figure('xxxxxxb', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
            mapx.itemset((i, j), W - 1 - j)
            mapy.itemset((i, j), H - 1 - i)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxc', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('上下顛倒')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print('W = ', W)
print('H = ', H)
print('D = ', D)

mapx = np.zeros(image.shape[:2], np.float32)
mapy = np.zeros(image.shape[:2], np.float32)
for i in range(H):
    for j in range(W):
        if 0.25 * W < i < 0.75 * W and 0.25 * H < j < 0.75 * H:
                mapx.itemset((i, j), 2 * (j - W * 0.25 ) + 0.5)
                mapy.itemset((i, j), 2 * (i - H * 0.25 ) + 0.5)
        else:     
                mapx.itemset((i, j), 0)
                mapy.itemset((i, j), 0)
rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

plt.figure('xxxxxxd', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('縮小圖')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個



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


"""
#opencv
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import matplotlib.pyplot as plt
import cv2

image = cv2.imread(filename)	#讀取本機圖片

#plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#先轉換成RGB再顯示

plt.show()
"""
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



"""
#輸出邊緣和結構信息

image = cv2.imread('data/contours.bmp')

plt.figure('輸出邊緣和結構信息', figsize = (10, 6))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
o = cv2.drawContours(image, contours, -1, (0, 0, 255), 5)

plt.subplot(122)
plt.title('輸出邊緣和結構信息')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/contours.bmp')

plt.figure('影像處理1', figsize = (10, 6))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours) #獲取輪廓個數
print('總共找到', n, '個輪廓')

contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(
            contoursImg[i],contours,i,(255,255,255),5) 
    index = "22"+str(i+2)
    plt.subplot(int(index))
    plt.title('輪廓 '+ str(i+1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/loc3.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image.shape, np.uint8)

mask = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)

loc = cv2.bitwise_and(image, mask)    

plt.figure('影像處理2', figsize = (10, 6))

plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('mask')
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('location')
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/moments.bmp')

plt.figure('影像處理3', figsize = (10, 6))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  

n = len(contours) #獲取輪廓個數
print('總共找到', n, '個輪廓')

contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],contours,i,255,3) 
    index = "22"+str(i+2)
    plt.subplot(int(index))
    plt.title('輪廓 '+ str(i+1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    
print("觀察各個輪廓的矩（moments）:")
for i in range(n):
    print("輪廓"+str(i)+"的矩:\n", cv2.moments(contours[i]))
print("觀察各個輪廓的面積:")
for i in range(n):
    print("輪廓"+str(i)+"的面積:%d" %cv2.moments(contours[i])['m00'])

plt.show()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/contours.bmp')

plt.figure('影像處理4', figsize = (10, 6))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  

n = len(contours) #獲取輪廓個數
print('總共找到', n, '個輪廓')

contoursImg = []
for i in range(n):
    print("contours["+str(i)+"]面積=", cv2.contourArea(contours[i]))
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i],
                                      contours,
                                      i,
                                      (255,255,255),
                                      3)
    #cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
    index = "22"+str(i+2)
    plt.subplot(int(index))
    plt.title('輪廓 '+ str(i+1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()
"""
print('------------------------------------------------------------')	#60個

#篩選出大于特定大小的輪廓

image = cv2.imread('data/contours.bmp')

plt.figure('影像處理5', figsize = (10, 6))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  

n = len(contours) #獲取輪廓個數
print('總共找到', n, '個輪廓')

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i],
                                      contours,
                                      i,
                                      (255, 255, 255),
                                      3)
    if cv2.contourArea(contours[i]) > 15000:
        #cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
        index = "22"+str(i+2)
        plt.subplot(int(index))
        plt.title('輪廓 '+ str(i+1))
        plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

#篩選出大于特定大小的輪廓

#--------------讀取及顯示原始圖像--------------------
image = cv2.imread('data/contours0.bmp')
print('顯示原圖')
cv2.imshow("original", image)

#--------------獲取輪廓--------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#--------------計算各個輪廓的長度和、平均長度--------------------
n = len(contours) #獲取輪廓個數
print('總共找到', n, '個輪廓')

cntLen=[]           #存儲各個輪廓的長度
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i],True))
    print("第"+str(i)+"個輪廓的長度:%d"%cntLen[i])
cntLenSum=np.sum(cntLen)  #各個輪廓長度和
cntLenAvr=cntLenSum/n    #各個輪廓長度平均值
print("各個輪廓的總長度為：%d"%cntLenSum)
print("各個輪廓的平均長度為：%d"%cntLenAvr)

#--------------顯示超過平均值的輪廓--------------------
contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i],
                                      contours,
                                      i,
                                      (255, 255, 255),
                                      3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        cv2.imshow("contours[" + str(i) + "]", contoursImg[i])

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cs1.bmp')
print('顯示原圖')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
HuM1=cv2.HuMoments(cv2.moments(gray)).flatten()

print("cv2.moments(gray)=\n", cv2.moments(gray))
print("\nHuM1=\n",HuM1)
print("\ncv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']=%f+%f=%f\n" 
      %(cv2.moments(gray)['nu20'], cv2.moments(gray)['nu02'],
        cv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']))
print("HuM1[0]=",HuM1[0])
print("\nHu[0]-(nu02+nu20)=",
      HuM1[0]-(cv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']))

print('------------------------------------------------------------')	#60個

#----------------計算圖像1的Hu矩-------------------
image1 = cv2.imread('data/cs1.bmp')
print('顯示原圖')

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()
#----------------計算圖像2的Hu矩-------------------
image2 = cv2.imread('data/cs3.bmp')
print('顯示原圖')

gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()
#----------------計算圖像3的Hu矩-------------------
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image3 = cv2.imread(filename)
print('顯示原圖')

gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

#---------打印圖像1、圖像2、圖像3的特征值------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
print("cv2.moments(gray1)=\n", cv2.moments(gray1))
print("cv2.moments(gray2)=\n", cv2.moments(gray2))
print("cv2.moments(gray3)=\n", cv2.moments(gray3))
print("\nHuM1=\n",HuM1)
print("\nHuM2=\n",HuM2)
print("\nHuM3=\n",HuM3)

#---------計算圖像1與圖像2、圖像3的Hu矩之差----------------
print("\nHuM1-HuM2=",HuM1-HuM2)
print("\nHuM1-HuM3=",HuM1-HuM3)

plt.figure('影像處理6', figsize = (16, 12))

plt.subplot(131)
plt.title('original1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('original2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('original3')
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#--------------讀取3幅原始圖像--------------------
image1 = cv2.imread('data/cs1.bmp')
image2 = cv2.imread('data/cs2.bmp')
image3 = cv2.imread('data/cc.bmp')

#----------打印3幅原始圖像的shape屬性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
#--------------色彩空間轉換-------------------- 
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY) 
#-------------進行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0.0)
#--------------打印差值--------------------
print("相同圖像的matchShape=",ret0)
print("相似圖像的matchShape=",ret1)
print("不相似圖像的matchShape=",ret2)

#--------------顯示3幅原始圖像--------------------

plt.figure('影像處理7', figsize = (16, 12))

plt.subplot(131)
plt.title('original1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('original2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('original3')
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#---------------讀取并顯示原始圖像------------------ 
image = cv2.imread('data/cc.bmp')
print('顯示原圖')

#---------------提取圖像輪廓------------------ 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#---------------返回頂點及邊長------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
print("頂點及長寬的點形式:")
print("x=",x)
print("y=",y)
print("w=",w)
print("h=",h)
#---------------僅有一個返回值的情況------------------
rect = cv2.boundingRect(contours[0])
print("\n頂點及長寬的元組（tuple）形式：")
print("rect=",rect)

print('------------------------------------------------------------')	#60個

#---------------讀取并顯示原始圖像------------------
image = cv2.imread('data/cc.bmp')

print('顯示原圖')
cv2.imshow("original", image)

plt.figure('影像處理8', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#---------------構造矩形邊界------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
cv2.drawContours(image, [brcnt], -1, (0, 0,255), 2)

#---------------顯示矩形邊界------------------
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#---------------讀取并顯示原始圖像------------------ 
image = cv2.imread('data/cc.bmp')

print('顯示原圖')
cv2.imshow("original", image)

plt.figure('影像處理9', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#---------------提取圖像輪廓------------------ 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#---------------構造矩形邊界------------------
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(image, (x,y), (x+w,y+h), (0, 0, 255), 2)

#---------------顯示矩形邊界------------------
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cc.bmp')
print('顯示原圖')

cv2.imshow("original", image)

plt.figure('影像處理10', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n",rect)
points = cv2.boxPoints(rect)
print("\n轉換后的points：\n",points)
points = np.int0(points)  #取整
image=cv2.drawContours(image, [points], 0, (0, 0,255),2)

cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original", image)

plt.figure('影像處理11', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(x,y),radius = cv2.minEnclosingCircle(contours[0])
center = (int(x),int(y))
radius = int(radius)
cv2.circle(image,center,radius, (0, 0, 255),2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cc.bmp')
print('顯示原圖')

plt.figure('影像處理12', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original", image)
ellipse = cv2.fitEllipse(contours[0])
print("ellipse=",ellipse)
cv2.ellipse(image, ellipse,(0,255,0),3)
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cc.bmp')
print('顯示原圖')

cv2.imshow("original", image)

plt.figure('影像處理13', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rows,cols = image.shape[:2]
[vx,vy,x,y] = cv2.fitLine(contours[0], cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(image, (cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original", image)

plt.figure('影像處理14', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area,trgl = cv2.minEnclosingTriangle(contours[0])
print("area=",area)
print("trgl:",trgl)
for i in range(0, 3):
    print('x')
    #cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), (255,255,255), 2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------讀取并顯示原始圖像-------------------------------
image = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original", image)

#----------------獲取輪廓-------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#----------------epsilon=0.1*周長-------------------------------
adp = image.copy()
epsilon = 0.1*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.1",adp)

#----------------epsilon=0.09*周長-------------------------------
adp = image.copy()
epsilon = 0.09*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.09",adp)

#----------------epsilon=0.055*周長-------------------------------
adp = image.copy()
epsilon = 0.055*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.055",adp)

#----------------epsilon=0.05*周長-------------------------------
adp = image.copy()
epsilon = 0.05*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.05", adp)

#----------------epsilon=0.02*周長-------------------------------
adp = image.copy()
epsilon = 0.02*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
adp=cv2.drawContours(adp,[approx],0,(0,0,255),2)
cv2.imshow("result0.02",adp)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

image = cv2.imread('data/contours.bmp')
print('顯示原圖')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])   #返回坐標值
print("returnPoints為默認值True時返回值hull的值：\n",hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False) #返回索引值
print("returnPoints為False時返回值hull的值：\n",hull2)

print('------------------------------------------------------------')	#60個

# --------------讀取并繪製原始圖像------------------
o = cv2.imread('data/hand.bmp')
print('顯示原圖')
cv2.imshow("original",o)
# --------------提取輪廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  

# --------------尋找凸包，得到凸包的角點------------------
hull = cv2.convexHull(contours[0])
# --------------繪製凸包------------------
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
# --------------顯示凸包------------------
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------原圖--------------------------
img = cv2.imread('data/hand.bmp')
print('顯示原圖')
cv2.imshow('original',img)
#----------------構造輪廓--------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255,0)
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)  
#----------------凸包--------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
print("defects=\n",defects)
#----------------構造凸缺陷--------------------------
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,0,255],2)
    cv2.circle(img,far,5,[255,0,0],-1)
#----------------顯示結果--------------------------
cv2.imshow('result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/hand.bmp')
print('顯示原圖')
cv2.imshow("original",o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
#--------------凸包----------------------
image1=o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, (0, 255, 0), 2)
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：",
      cv2.isContourConvex(hull))
cv2.imshow("result1",image1)
#------------逼近多邊形--------------------
image2=o.copy()
epsilon = 0.01*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)
image2=cv2.drawContours(image2,[approx],0,(0,0,255),2)
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：",
      cv2.isContourConvex(approx))
cv2.imshow("result2",image2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#----------------原始圖像-------------------------
o = cv2.imread('data/cs.bmp')
print('顯示原圖')
cv2.imshow("original",o)
#----------------獲取凸包------------------------  
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
hull = cv2.convexHull(contours[0])

""" fail
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)

#----------------內部點A的距離-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部點B的距離-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#------------正好處于邊緣上的點C的距離-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的
#----------------顯示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print('------------------------------------------------------------')	#60個

#----------------原始圖像-------------------------
o = cv2.imread('data/cs.bmp')
print('顯示原圖')
cv2.imshow("original",o)
#----------------獲取凸包------------------------ 
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
hull = cv2.convexHull(contours[0])
""" fail
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
#----------------內部點A與多邊形的關系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部點B與多邊形的關系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#----------------邊緣線上點C與多邊形的關系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的
#----------------顯示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print('------------------------------------------------------------')	#60個

#-----------原始圖像o1邊緣--------------------
o1 = cv2.imread('data/cs.bmp')
print('顯示原圖')
cv2.imshow("original1",o1)

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY) 
ret, binary1 = cv2.threshold(gray1,127,255, cv2.THRESH_BINARY) 
contours1, hierarchy = cv2.findContours(binary1,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE) 
cnt1 = contours1[0]
#-----------原始圖像o2邊緣--------------------
o2 = cv2.imread('data/cs3.bmp')
print('顯示原圖')
cv2.imshow("original2",o2)

gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY) 
ret, binary2 = cv2.threshold(gray2,127,255, cv2.THRESH_BINARY) 
contours2, hierarchy = cv2.findContours(binary2,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)  
cnt2 = contours2[0]
#-----------原始圖像o3邊緣--------------------
o3 = cv2.imread('data/hand.bmp')
print('顯示原圖')
cv2.imshow("original3",o3)

gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY) 
ret, binary3 = cv2.threshold(gray3,127,255, cv2.THRESH_BINARY) 
contours3, hierarchy = cv2.findContours(binary3,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]
#-----------構造距離提取算子--------------------
sd = cv2.createShapeContextDistanceExtractor()
#-----------計算距離--------------------
d1 = sd.computeDistance(cnt1,cnt1)
print("自身距離d1=", d1)
d2 = sd.computeDistance(cnt1,cnt2)
print("旋轉縮放后距離d2=", d2)
d3 = sd.computeDistance(cnt1,cnt3)
print("不相似對象距離d3=", d3)
#-----------顯示距離--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#-----------讀取原始圖像--------------------
o1 = cv2.imread('data/cs.bmp')
print('顯示原圖')

o2 = cv2.imread('data/cs3.bmp')
print('顯示原圖')

o3 = cv2.imread('data/hand.bmp')
print('顯示原圖')

cv2.imshow("original1",o1)
cv2.imshow("original2",o2) 
cv2.imshow("original3",o3) 
#-----------色彩轉換--------------------
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY) 
#-----------閾值處理--------------------
ret, binary1 = cv2.threshold(gray1,127,255, cv2.THRESH_BINARY) 
ret, binary2 = cv2.threshold(gray2,127,255, cv2.THRESH_BINARY) 
ret, binary3 = cv2.threshold(gray3,127,255, cv2.THRESH_BINARY) 
#-----------提取輪廓--------------------
contours1, hierarchy = cv2.findContours(binary1,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)  
contours2, hierarchy = cv2.findContours(binary2,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)  
contours3, hierarchy = cv2.findContours(binary3,
                                        cv2.RETR_LIST,
                                        cv2.CHAIN_APPROX_SIMPLE)  
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
#-----------構造距離提取算子--------------------
hd = cv2.createHausdorffDistanceExtractor()
#-----------計算距離--------------------
d1 = hd.computeDistance(cnt1,cnt1)
print("自身Hausdorff距離d1=", d1)
d2 = hd.computeDistance(cnt1,cnt2)
print("旋轉縮放后Hausdorff距離d2=", d2)
d3 = hd.computeDistance(cnt1,cnt3)
print("不相似對象Hausdorff距離d3=", d3)
#-----------顯示距離--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(o,(x,y),(x+w,y+h),(255,255,255),3)

aspectRatio = float(w)/h
print(aspectRatio)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
x,y,w,h = cv2.boundingRect(contours[0])
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cv2.rectangle(o,(x,y),(x+w,y+h),(255,0,0),3)

rectArea=w*h
cntArea=cv2.contourArea(contours[0])
extend=float(cntArea)/rectArea
print(extend)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/hand.bmp')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cntArea=cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
solidity=float(cntArea)/hullArea
print(solidity)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(o,contours[0],-1,(0,0,255),3) 
cntArea=cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4*cntArea/np.pi)
print(equiDiameter)
cv2.circle(o,(100,100),int(equiDiameter/2),(0,0,255),3) #展示等直徑大小的圓
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
ellipse = cv2.fitEllipse(contours[0])
retval=cv2.fitEllipse(contours[0])
print("單個返回值形式：")
print("retval=\n",retval)
(x,y),(MA,ma),angle = cv2.fitEllipse(contours[0])
print("三個返回值形式：")
print("(x,y)=(",x,y,")")
print("(MA,ma)=(",MA,ma,")")
print("angle=",angle)
cv2.ellipse(o,ellipse,(0,0,255),2)
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#------------生成一個都是0值的a-------------------
a=np.zeros((5,5),dtype=np.uint8)
#-------隨機將其中10個位置上的數值設置為1------------
#---times控制次數
#---i,j是隨機生成的行、列位置
#---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i=np.random.randint(0,5)
    j=np.random.randint(0,5)
    a[i,j]=1
#-------打印a，觀察a內值的情況-----------
print("a=\n",a)
#------查找a內非零值的位置信息------------
loc=np.transpose(np.nonzero(a))
#-----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n",loc)

print('------------------------------------------------------------')	#60個

#-----------------讀取原始圖像----------------------
o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)
#-----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[0]
#-----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask1,[cnt],0,255,2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=",pixelpoints1.shape)
print("pixelpoints1=\n",pixelpoints1)
cv2.imshow("mask1",mask1)
#-----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask2,[cnt],0,255,-1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=",pixelpoints2.shape)
print("pixelpoints2=\n",pixelpoints2)
cv2.imshow("mask2",mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#------------生成一個都是0值的a-------------------
a=np.zeros((5,5),dtype=np.uint8)
#-------隨機將其中10個位置上的數值設置為1------------
#---times控制次數
#---i,j是隨機生成的行、列位置
#---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i=np.random.randint(0,5)
    j=np.random.randint(0,5)
    a[i,j]=1
#-------打印a，觀察a內值的情況-----------
print("a=\n",a)
#------查找a內非零值的位置信息------------
loc = cv2.findNonZero(a)
#-----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n",loc)

print('------------------------------------------------------------')	#60個

#-----------------讀取原始圖像----------------------
o = cv2.imread('data/cc.bmp')
print('顯示原圖')
cv2.imshow("original",o)
#-----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[0]
#-----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask1,[cnt],0,255,2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=",pixelpoints1.shape)
print("pixelpoints1=\n",pixelpoints1)
cv2.imshow("mask1",mask1)
#-----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape,np.uint8)
cv2.drawContours(mask2,[cnt],0,255,-1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=",pixelpoints2.shape)
print("pixelpoints2=\n",pixelpoints2)
cv2.imshow("mask2",mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/ct.png')
print('顯示原圖')
cv2.imshow("original",o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2]   #coutours[0]、coutours[1]是左側字母R
#--------使用掩膜獲取感興趣區域的最值-----------------
#需要注意minMaxLoc處理的對象為灰度圖像，本例中處理對象為灰度圖像gray
#如果希望獲取彩色圖像的，需要提取各個通道，將每個通道獨立計算最值
mask = np.zeros(gray.shape,np.uint8)
mask=cv2.drawContours(mask,[cnt],-1,255,-1)   
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray,mask = mask)
print("minVal=",minVal)
print("maxVal=",maxVal)
print("minLoc=",minLoc)
print("maxLoc=",maxLoc)
#--------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape,np.uint8)
masko=cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko) 
cv2.imshow("mask",loc)
#顯示灰度結果
#loc=cv2.bitwise_and(gray,mask) 
#cv2.imshow("mask",loc)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#--------讀取并顯示原始圖像-----------------
o = cv2.imread('data/ct.png')
print('顯示原圖')
cv2.imshow("original",o)
#--------獲取輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
cnt=contours[2] 
#--------使用掩膜獲取感興趣區域的均值----------------- 
mask = np.zeros(gray.shape,np.uint8)#構造mean所使用的掩膜，必須是單通道的
cv2.drawContours(mask,[cnt],0,(255,255,255),-1)
meanVal = cv2.mean(o,mask = mask)  #mask是區域，所以必須是單通道的
print("meanVal=\n",meanVal)
#--------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape,np.uint8)
cv2.drawContours(masko,[cnt],-1,(255,255,255),-1)
loc=cv2.bitwise_and(o,masko)
cv2.imshow("mask",loc)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('data/cs.bmp')
print('顯示原圖')

#--------獲取并繪製輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255, cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_SIMPLE)  
mask = np.zeros(gray.shape,np.uint8)
cnt=contours[0] 
cv2.drawContours(mask,[cnt],0,255,-1)
#--------計算極值----------------- 
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
#--------計算極值----------------- 
print("leftmost=",leftmost)
print("rightmost=",rightmost)
print("topmost=",topmost)
print("bottommost=",bottommost)
#--------繪製說明文字----------------- 
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o,'A',leftmost, font, 1,(0,0,255),2)
cv2.putText(o,'B',rightmost, font, 1,(0,0,255),2)
cv2.putText(o,'C',topmost, font, 1,(0,0,255),2)
cv2.putText(o,'D',bottommost, font, 1,(0,0,255),2)
#--------繪製圖像----------------- 
cv2.imshow("result",o)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print('使用 cv2 顯示圖片')

image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('取兩圖的影像差異 diff')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/compare/compare1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/compare/compare2.jpg'

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

print('image1.shape內容 :', img1.shape)
print('image2.shape內容 :', img2.shape)


# 比較並顯示差異影像
diff = cv2.absdiff(img1, img2)

cv2.imshow('Difference', diff)

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('疊合')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/ims02.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/ims03.bmp'

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)


blended = cv2.addWeighted(img1, 1, img2, 1, 0)

cv2.imshow('Surveyed', blended)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


