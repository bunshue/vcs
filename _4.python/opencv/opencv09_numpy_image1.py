'''
opencv + numpy + 圖片之影像處理


'''

import cv2
import numpy as np

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個
print('測試 1')

print('將一圖分解成 藍 綠 紅 三通道')

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/white_300X300.bmp'
image=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("image", image)

'''same
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
'''
b,g,r=cv2.split(image)

print('顯示 ch0 藍 通道 圖')
cv2.imshow('B', b)

print('顯示 ch1 綠 通道 圖')
cv2.imshow('G', g)

print('顯示 ch2 紅 通道 圖')
cv2.imshow('R', r)

cv2.waitKey()
cv2.destroyAllWindows()

print('設定第0通道為0')
image[:,:,0]=0
cv2.imshow("image ch0 = 0", image)

print('設定第1通道為0')
image[:,:,1]=0
cv2.imshow("image ch0 = ch1 = 0",image)

print('設定第2通道為0')
image[:,:,2]=0
cv2.imshow("image ch0 = ch1 = ch2 = 0",image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('將一圖分解成 藍 綠 紅 三通道')
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

image=cv2.imread(filename)

b,g,r=cv2.split(image)

bgr=cv2.merge([b,g,r])
rgb=cv2.merge([r,g,b])

cv2.imshow("image", image)   #原圖
cv2.imshow("B-G-R OK", bgr) #照BGR排列 OK
cv2.imshow("R-G-B NG", rgb) #照RGB排列 錯相

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個
print('測試 2')

img = cv2.imread('images/girl.bmp')
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure("顯示結果")

plt.subplot(121)
plt.imshow(img)
plt.axis('off')

plt.subplot(122)
plt.imshow(imgRGB)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 3 subplot')

o = cv2.imread('images/8.bmp')
g=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

plt.figure("灰度圖像顯示演示")

plt.subplot(221)
plt.imshow(g, cmap=plt.cm.gray)

plt.subplot(222)
plt.imshow(g, cmap=plt.cm.gray_r)

plt.subplot(223)
plt.imshow(g, cmap='gray')

plt.subplot(224)
plt.imshow(g, cmap='gray_r')

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 4 subplot')

o = cv2.imread('images/girl.bmp')
g=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)

plt.figure("灰度圖像顯示演示")
plt.subplot(221)
plt.imshow(o)
plt.axis('off')

plt.subplot(222)
plt.imshow(o,cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(223)
plt.imshow(g)
plt.axis('off')

plt.subplot(224)
plt.imshow(g,cmap=plt.cm.gray)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 5')

o=cv2.imread("images/boat.bmp")
plt.hist(o.ravel(),16)

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 6')
o=cv2.imread("images/boat.jpg")
cv2.imshow("original",o)    #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()

plt.hist(o.ravel(),256)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 7')

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img=cv2.imread(filename)
hist = cv2.calcHist([img],[0],None,[256],[0,255])
print(type(hist))
print(hist.shape)
print(hist.size)
print(hist)
plt.plot(hist)

plt.show()

print('------------------------------------------------------------')	#60個

print('測試 8')

#-----------讀取原始圖像---------------
img = cv2.imread('images/equ.bmp',cv2.IMREAD_GRAYSCALE)
#-----------直方圖均衡化處理---------------
equ = cv2.equalizeHist(img)
#-----------顯示均衡化前后的直方圖---------------
cv2.imshow("original",img)  #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("result",equ)    #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
#-----------顯示均衡化前后的直方圖---------------
plt.figure("原始圖像直方圖")  #構建窗口
plt.hist(img.ravel(),256)
plt.figure("均衡化結果直方圖")  #構建新窗口
plt.hist(equ.ravel(),256)

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個
print('測試 9')

image=cv2.imread("images/girl.bmp",cv2.IMREAD_GRAYSCALE)
mask=np.zeros(image.shape,np.uint8)
mask[200:400,200:400]=255
histImage=cv2.calcHist([image],[0],None,[256],[0,255])
histMI=cv2.calcHist([image],[0],mask,[256],[0,255])
plt.plot(histImage)
plt.plot(histMI)

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 10')

o=cv2.imread("images/boatGray.bmp")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
plt.plot(histb,color='b')

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 11')

o=cv2.imread("images/girl.bmp")
histb = cv2.calcHist([o],[0],None,[256],[0,255])
histg = cv2.calcHist([o],[1],None,[256],[0,255])
histr = cv2.calcHist([o],[2],None,[256],[0,255])
plt.plot(histb,color='b')
plt.plot(histg,color='g')
plt.plot(histr,color='r')

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 12')

img = cv2.imread('images/equ.bmp',cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)

plt.figure("subplot示例")
plt.subplot(121)
plt.hist(img.ravel(),256)

plt.subplot(122)
plt.hist(equ.ravel(),256)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

