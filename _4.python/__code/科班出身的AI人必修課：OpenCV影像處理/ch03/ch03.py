import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

a=cv2.imread("lena.bmp",0)
print('顯示原圖')
cv2.imshow("original",a)

b=a

print('兩圖直接相加')
result1=a+b
cv2.imshow("result1",result1)

print('兩圖用cv相')
result2=cv2.add(a,b)
cv2.imshow("result2",result2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("boat.bmp")
print('顯示原圖')
cv2.imshow("boat",a)

b=cv2.imread("lena.bmp")
print('顯示原圖')
cv2.imshow("lena",b)

print('兩圖做alpha疊加')
result=cv2.addWeighted(a,0.6,b,0.4,0)
cv2.imshow("result",result)

cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

lena=cv2.imread("lena512.bmp",cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("lena",lena)

dollar=cv2.imread("dollar.bmp",cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("dollar",dollar)

print('兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之')
face1=lena[220:400,250:350]
face2=dollar[160:340,200:300]
add=cv2.addWeighted(face1,0.6,face2,0.4,0)
dollar[160:340,200:300]=add
cv2.imshow("result",dollar)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("lena.bmp",0)  #通道不同
print('顯示原圖')
cv2.imshow("a",a)

b=np.zeros(a.shape,dtype=np.uint8) #與a一樣大的黑圖
b[100:400,200:400]=255 #某塊做mask
b[100:500,100:200]=255 #某塊做mask
print('顯示mask')
cv2.imshow("b",b)

print('顯示原圖與mask作用後的圖')
c=cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
print("a.shape=",a.shape)
print("b.shape=",b.shape)
cv2.imshow("c",c)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("lena.bmp",1)  #通道不同
print('顯示原圖')
cv2.imshow("a",a)

b=np.zeros(a.shape,dtype=np.uint8) #與a一樣大的黑圖
b[100:400,200:400]=255 #某塊做mask
b[100:500,100:200]=255 #某塊做mask
print('顯示mask')
cv2.imshow("b",b)

print('顯示原圖與mask作用後的圖')
c=cv2.bitwise_and(a,b)  #ab都成立的 擷取出來
print("a.shape=",a.shape)
print("b.shape=",b.shape)
cv2.imshow("c",c)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

a=cv2.imread("lena.bmp",1)
print('顯示原圖')
cv2.imshow("a",a)

w,h,c=a.shape

mask=np.zeros((w,h),dtype=np.uint8)
mask[100:400,200:400]=255
mask[100:500,100:200]=255
c=cv2.bitwise_and(a,a,mask)
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)
cv2.imshow("mask",mask)
cv2.imshow("c",c)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#圖層提取
lena=cv2.imread("lena.bmp",0)
print('顯示原圖')
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

print('------------------------------------------------------------')	#60個

#異或加密解密
lena=cv2.imread("lena.bmp",0)
print('顯示原圖')
cv2.imshow("lena",lena)

r,c=lena.shape
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption=cv2.bitwise_xor(lena,key)
decryption=cv2.bitwise_xor(encryption,key)
cv2.imshow("key",key)
cv2.imshow("encryption",encryption)
cv2.imshow("decryption",decryption)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#讀取原始載體圖像
lena=cv2.imread("lena.bmp",0)
print('顯示原圖')
cv2.imshow("lena",lena)

#讀取水印圖像
watermark=cv2.imread("watermark.bmp",0)
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
#============顯示============
cv2.imshow("watermark",watermark*255)   #當前watermark內最大值為1
cv2.imshow("e",e)
cv2.imshow("wm",wm)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#讀取原始載體圖像
lena=cv2.imread("lena.bmp",0)
print('顯示原圖')
cv2.imshow("lena",lena)

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
#============顯示圖像============
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

print('------------------------------------------------------------')	#60個

#圖層提取
lena=cv2.imread("lena.bmp",0)
print('顯示原圖')
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

print('------------------------------------------------------------')	#60個
