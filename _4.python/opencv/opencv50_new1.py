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

filename1 = 'C:/_git/vcs/_4.python/_data/picture_mix1.bmp'
filename2 = 'C:/_git/vcs/_4.python/_data/picture_mix2.bmp'

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)

print('兩圖直接相加')
result1 = image1 + image2

print('兩圖用cv相加')
result2 = cv2.add(image1, image2)

print('兩圖做alpha疊加')
result3 = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="相加",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title('原圖1')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title('原圖2')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title('兩圖直接相加')
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title('兩圖用cv相加')
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title('兩圖做alpha疊加')
plt.imshow(cv2.cvtColor(result3, cv2.COLOR_BGR2RGB))

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

plt.show()

print('------------------------------------------------------------')	#60個

#異或加密解密
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
#filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

lena = cv2.imread(filename, 0)  # 以下程式只能處理灰階 因為xor操作維度錯誤

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

plt.figure('new06', figsize = (16, 8))
plt.subplot(121)
plt.imshow(orgb)

plt.subplot(122)
plt.imshow(ogc)

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

plt.figure('new07', figsize = (16, 8))
plt.subplot(121)
plt.imshow(m2rgb)

plt.subplot(122)
plt.imshow(ogc)

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

plt.figure('new08', figsize = (16, 8))
plt.subplot(121)
plt.imshow(orgb)

plt.subplot(122)
plt.imshow(ogc)

plt.show()

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

plt.figure('new09 影像處理 move', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('move')
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))

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

plt.figure('new10', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

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

plt.figure('new11', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('result')
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

#Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename)

print('filter2D 效果')
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure('new26 filter2D 效果', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('filter2D 效果')
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))

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

plt.figure('new27', figsize = (16, 12))
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

plt.figure('new28 saltpepper 效果', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('saltpepper 效果')
plt.imshow(cv2.cvtColor(saltImage, cv2.COLOR_BGR2RGB))

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

plt.figure('new29 二值化', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('二值化圖, 閥值 127, 小於變全黑, 大於變全白')
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg'
img = cv2.imread(filename, 0)

t1,thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
athdMEAN = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
athdGAUS = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

plt.figure('new30', figsize = (16, 12))
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

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp'
img = cv2.imread(filename, 0)

t1,thd=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
t2,otsu=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.figure('new31', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('thd')
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('otsu')
plt.imshow(cv2.cvtColor(otsu, cv2.COLOR_BGR2RGB))

plt.show()

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

plt.figure('new32 影像處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖 彩色')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('灰階1通道')
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('BGR3通道')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
image = cv2.imread(filename)

print('原圖 BGR 轉 RGB')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure('new33 影像處理', figsize = (16, 12))

plt.subplot(121)
plt.title('原圖 B-G-R OK')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('原圖 BGR 轉 RGB NG')
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

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

plt.figure('new36 影像處理', figsize = (16, 12))
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

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename, 0)

plt.figure('new37 修改一部份資料', figsize = (16, 12))
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

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'
a = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure('new38 擷取一塊處理', figsize = (16, 12))
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
filename2 = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
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

plt.show()

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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("absolute")

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #確定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result
    
original_image_test1 = cv2.imread('data/lena.png',0)
def my_laplace_result_add_abs(image, model):
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            if model[i][j] < 0:
                model[i][j] = 0
            if model[i][j] > 255:
                model[i][j] = 255
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

# 調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type='big')
# 繪制結果
fig = plt.figure('new39')
fig.add_subplot(121)
plt.title('原始圖像')
plt.imshow(original_image_test1)
fig.add_subplot(122)
plt.title('銳化濾波')
plt.imshow(my_laplace_result_add_abs(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("createCLAHE_image")

img = cv2.imread('data/building.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('img',img)
cv2.imshow('cl1',cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("equalizeHist_image")

img = cv2.imread('data/wu_2.png',0)
equ = cv2.equalizeHist(img) #只能傳入灰度圖
res = np.hstack((img,equ))  #圖像列拼接（用于顯示）

cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("gradient")

# 輸入圖像，輸出提取的邊緣信息
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape,dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    # 確定拉普拉斯模板的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += image[i+ii-1][j+jj-1] * my_model_x[ii][jj]
                        result_y[i][j] += image[i+ii-1][j+jj-1] * my_model_y[ii][jj]
            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            if result[i][j] > 255:
                result[i][j] = 255
    return result


# 將邊緣信息按一定比例加到原始圖像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result



original_image_lena= cv2.imread('data/lena.png', 0)

# 獲得圖像邊界信息
edge_image_lena = my_sobel_sharpen(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_result_add(original_image_lena, edge_image_lena, -0.5)

# 顯示結果
plt.subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('邊緣檢測')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('梯度處理')
plt.imshow(sharpen_image_lena)

plt.show()


print("------------------------------------------------------------")  # 60個

print("imaeg_laplace")

original_image_test1 = cv2.imread('data/lena.png',0)
#用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

def my_laplace_sharpen(image, my_type = 'small'):
    result = np.zeros(image.shape,dtype=np.int64)
    #確定拉普拉斯模板的形式
    if my_type == 'small':
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-1)<0 or (i+ii-1)>=image.shape[0]:
                        pass
                    elif (j+jj-1)<0 or (j+jj-1)>=image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i+ii-1][j+jj-1] * my_model[ii][jj]
    return result

#將計算結果限制為正值
def my_show_edge(model):
    #這里一定要用copy函數，不然會改變原來數組的值
    mid_model = model.copy()
    for i in range(mid_model.shape[0]):
        for j in range(mid_model.shape[1]):
            if mid_model[i][j] < 0:
                mid_model[i][j] = 0
            if mid_model[i][j] > 255:
                mid_model[i][j] = 255
    return mid_model

#調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type='big')
#繪制結果
fig = plt.figure('new40')
fig.add_subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_test1)
fig.add_subplot(132)
plt.title('邊緣檢測')
plt.imshow(my_show_edge(result))
fig.add_subplot(133)
plt.title('銳化處理')
plt.imshow(my_laplace_result_add(original_image_test1,result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")

from matplotlib import pyplot as plt

# 用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image-model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result

original_image_test1 = cv2.imread('data/lena.png',0)
# 函數中的參數ddepth為輸出圖像的深度，也就是每個像素點是多少位的。
# CV_16S表示16位有符號數
computer_result = cv2.Laplacian(original_image_test1,ksize=3,ddepth=cv2.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_fft")

Fs=1200;  #采樣頻率
Ts=1/Fs;  #采樣區間
x=np.arange(0,1,Ts)  #時間向量，1200個
y=5*np.sin(2*np.pi*600*x)
N=1200
frq=np.arange(N)            #頻率數1200個數
half_x=frq[range(int(N/2))]  #取一半區間
fft_y=np.fft.fft(y)
abs_y=np.abs(fft_y)                #取復數的絕對值，即復數的模(雙邊頻譜)
angle_y=180*np.angle(fft_y)/np.pi   #取復數的弧度,并換算成角度
gui_y=abs_y/N                       #歸一化處理（雙邊頻譜）                              
gui_half_y = gui_y[range(int(N/2))] #由于對稱性，只取一半區間（單邊頻譜）
#畫出原始波形的前50個點
plt.subplot(231)
plt.plot(frq[0:50],y[0:50])   
plt.title('原始波形')
#畫出雙邊未求絕對值的振幅譜
plt.subplot(232)
plt.plot(frq,fft_y,'black')
plt.title('雙邊振幅譜(未求振幅絕對值)') 
#畫出雙邊求絕對值的振幅譜
plt.subplot(233)
plt.plot(frq,abs_y,'r')
plt.title('雙邊振幅譜(未歸一化)') 
#畫出雙邊相位譜
plt.subplot(234)
plt.plot(frq[0:50],angle_y[0:50],'violet')
plt.title('雙邊相位譜(未歸一化)')
#畫出雙邊振幅譜(歸一化)
plt.subplot(235)
plt.plot(frq,gui_y,'g')
plt.title('雙邊振幅譜(歸一化)')

#畫出單邊振幅譜(歸一化)
plt.subplot(236)
plt.plot(half_x,gui_half_y,'blue')
plt.title('單邊振幅譜(歸一化)')
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

img = plt.imread('data/castle3.jpg')

#根據公式轉成灰度圖
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]

#顯示原圖
plt.subplot(231)
plt.imshow(img,'gray')
plt.title('原始圖像')
#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(img)
plt.subplot(232)
plt.imshow(np.abs(fft2),'gray')
plt.title('二維傅里葉變換')
#將圖像變換的原點移動到頻域矩形的中心，并顯示效果
shift2center = np.fft.fftshift(fft2)
plt.subplot(233)
plt.imshow(np.abs(shift2center),'gray')
plt.title('頻域矩形的中心')
#對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(235)
plt.imshow(log_fft2,'gray')
plt.title('傅立葉變換對數變換')
#對中心化后的結果進行對數變換，并顯示結果
log_shift2center = np.log(1 + np.abs(shift2center))
plt.subplot(236)
plt.imshow(log_shift2center,'gray')
plt.title('中心化的對數變化')

plt.show()

print("------------------------------------------------------------")  # 60個

print("magnitude_spectrum")

img = cv2.imread('data/lena.png',0)  
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('原始圖像')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('級頻譜')
plt.xticks([]), plt.yticks([])

plt.show()

print("------------------------------------------------------------")  # 60個

print("optimize")

def ComputeMinLevel(hist, pnum):
    index = np.add.accumulate(hist)
    return np.argwhere(index>pnum * 8.3 * 0.01)[0][0]

def ComputeMaxLevel(hist, pnum):
    hist_0 = hist[::-1]
    Iter_sum = np.add.accumulate(hist_0)
    index = np.argwhere(Iter_sum > (pnum * 2.2 * 0.01))[0][0]
    return 255-index

def LinearMap(minlevel, maxlevel):
    if (minlevel >= maxlevel):
        return []
    else:
        index = np.array(list(range(256)))
        screenNum = np.where(index<minlevel,0,index)
        screenNum = np.where(screenNum> maxlevel,255,screenNum)
        for i in range(len(screenNum)):
            if screenNum[i]> 0 and screenNum[i] < 255:
                screenNum[i] = (i - minlevel) / (maxlevel - minlevel) * 255
        return screenNum

def CreateNewImg(img):
    h, w, d = img.shape
    newimg = np.zeros([h, w, d])
    for i in range(d):
        imghist = np.bincount(img[:, :, i].reshape(1, -1)[0])
        minlevel = ComputeMinLevel(imghist,  h * w)
        maxlevel = ComputeMaxLevel(imghist, h * w)
        screenNum = LinearMap(minlevel, maxlevel)
        if (screenNum.size == 0):
            continue
        for j in range(h):
            newimg[j, :, i] = screenNum[img[j, :, i]]
    return newimg

img = cv2.imread('data/building.png')
newimg = CreateNewImg(img)
cv2.imshow('原始圖像', img)
cv2.imshow('去霧后圖像', newimg / 255)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

filename = 'p1.bmp'
image1 = cv2.imread(filename)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.show()


filename = 'p2.bmp'
image2 = cv2.imread(filename)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.show()


#image3 = math.fabs(image1-image2)
image3 = image1-image2

plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



"""
特殊

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
"""



"""
print("gaussion")

print('跑很久 skip')

#高斯濾波函數
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*math.pi*sigma**2)

#產生高斯濾波矩陣
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根據尺寸和sigma值計算高斯矩陣
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    #將高斯矩陣歸一化
    blur_retric = blur_retric / blur_retric[0][0]
    #將高斯矩陣轉換為整數
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩陣
    return blur_retric

#計算灰度圖像的高斯濾波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data += image[i+ii-sizepart][j+jj-sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0
    #返回變換后的圖像矩陣
    return image

#計算彩色圖像的高斯濾波
def my_gaussion_blur_RGB(image, size, sigma):
    (b ,r, g) = cv2.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

image_test1 = cv2.imread('data/lena.png')
#進行高斯濾波器比較
my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
computer_image_blur_gaussion = cv2.GaussianBlur(image_test1, (5, 5), 0.75)  #執行高斯模糊化

fig = plt.figure(figsize = (20, 15))

fig.add_subplot(131)
plt.title('原始圖像')
plt.imshow(image_test1)

fig.add_subplot(132)
plt.title('自定義高斯濾波器')
plt.imshow(my_image_blur_gaussion)

fig.add_subplot(133)
plt.title('庫高斯濾波器')
plt.imshow(computer_image_blur_gaussion)

plt.show()
"""

print('------------------------------------------------------------')	#60個

"""
print("image_dft2")

print('跑不出來 skip')

PI = 3.141591265

img = plt.imread('data/castle3.jpg')
#根據公式轉成灰度圖
img = 0.2126 * img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]

#顯示原圖
plt.subplot(131),plt.imshow(img,'gray'),plt.title('original')

#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(img)
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(132),plt.imshow(log_fft2,'gray'),plt.title('log_fft2')

h , w = img.shape
#生成一個同樣大小的復數矩陣
F = np.zeros([h,w],'complex128')
for u in range(h):
    for v in range(w):
        res = 0
        for x in range(h):
            for y in range(w):
                res += img[x,y] * np.exp(-1.j * 2 * PI * (u * x / h + v * y / w))
        F[u,v] = res

log_F = np.log(1 + np.abs(F))
plt.subplot(133)
plt.imshow(log_F,'gray')
plt.title('log_F')
"""


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#偽寫入
#cv2.imwrite("tmp_bgra.png", bgra)
#cv2.imwrite("tmp_bgra125.png", bgra125)
#cv2.imwrite("tmp_bgra0.png", bgra0)

print('------------------------------------------------------------')	#60個




#直接改寫image的內容
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = cv2.imread(filename)

for i in range(20, 80):
    image[i, 180]=[0,0,255] #紅色一點

#     H          x
image[10:100, 200:290]=[0,0,255] #紅色 一塊 90X90

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

sys.exit()

print('------------------------------------------------------------')	#60個




