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
topLeft = minLoc
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
topLeft = maxLoc
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
        p1x = x
        p1y = y
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
        p1x = x
        p1y = y
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
print('作業完成')
print('------------------------------------------------------------')	#60個


