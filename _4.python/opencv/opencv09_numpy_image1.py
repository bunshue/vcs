'''
opencv + numpy + 圖片之影像處理


'''

import cv2
import numpy as np

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('測試 2')

img = cv2.imread('images/girl.bmp')
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure("显示结果")
plt.subplot(121)
plt.imshow(img),plt.axis('off')
plt.subplot(122)
plt.imshow(imgRGB),plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個
print('測試 3 subplot')

o = cv2.imread('images/8.bmp')
g=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
plt.figure("灰度图像显示演示")
plt.subplot(221); plt.imshow(g, cmap=plt.cm.gray)
plt.subplot(222); plt.imshow(g, cmap=plt.cm.gray_r)
plt.subplot(223); plt.imshow(g, cmap='gray')
plt.subplot(224); plt.imshow(g, cmap='gray_r')

plt.show()




print('------------------------------------------------------------')	#60個

print('測試 4 subplot')

o = cv2.imread('images/girl.bmp')
g=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
plt.figure("灰度图像显示演示")
plt.subplot(221)
plt.imshow(o),plt.axis('off')
plt.subplot(222)
plt.imshow(o,cmap=plt.cm.gray),plt.axis('off')
plt.subplot(223)
plt.imshow(g),plt.axis('off')
plt.subplot(224)
plt.imshow(g,cmap=plt.cm.gray),plt.axis('off')

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

#-----------读取原始图像---------------
img = cv2.imread('images/equ.bmp',cv2.IMREAD_GRAYSCALE)
#-----------直方图均衡化处理---------------
equ = cv2.equalizeHist(img)
#-----------显示均衡化前后的直方图---------------
cv2.imshow("original",img)  #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("result",equ)    #有cv2.imshow的, 要對應destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
#-----------显示均衡化前后的直方图---------------
plt.figure("原始图像直方图")  #构建窗口
plt.hist(img.ravel(),256)
plt.figure("均衡化结果直方图")  #构建新窗口
plt.hist(equ.ravel(),256)

plt.show()

#----------等待释放窗口---------------------
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
plt.subplot(121),plt.hist(img.ravel(),256)
plt.subplot(122),plt.hist(equ.ravel(),256)

plt.show()




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


