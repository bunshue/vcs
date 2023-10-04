'''
#numpy製作資料 修改資料 用matplotlib顯示

'''

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

W, H, D = 5, 5, 3

print('建立 0 ~ 255 的隨機陣列')
image1 = np.random.randint(0, 256, size = [W, H, D], dtype = np.uint8)
print(image1.shape)
#print(image1)

plt.imshow(image1)
plt.show()

print('建立 0.0 ~ 1.0 的隨機陣列')
image2 = np.random.random((W, H, D))
print(image2.shape)
#print(image2)

plt.imshow(image2)
plt.show()

print('建立 0 ~ 255 的 16 X 16 陣列')
image3 = np.arange(0, 256).reshape(16, 16)
print(image3.shape)
#print(image3)

plt.imshow(image3)
plt.show()

print('------------------------------------------------------------')	#60個

print('建立一黑圖')

W = 640
H = 480
print('numpy製作一個 %d X %d 的圖 黑色, 2維 3 通道' % (W, H))
image = np.zeros((H, W, 3), dtype = np.uint8)    #預設為0, 黑色, 2維, 3通道
#image = np.zeros((H, W), dtype = np.uint8)    #預設為0, 黑色, 2維, 1通道

print('中間一塊用填成灰色')
for i in range(100, 200):
    for j in range(100, 200):
        image[i,j] = 200

print('中間一塊用填成白色')
#     y_st y_sp  x_st y_st
image[300 : 400, 50 : 200] = 255

#image[:, :, 0] = 255 #將第0通道設為全亮 藍
#image[:, :, 1] = 255 #將第1通道設為全亮 綠
#image[:, :, 2] = 255 #將第0通道設為全亮 紅

image[:,0:50,0]=255      #第0通道, 藍色通道
image[:,50:100,1]=255    #第1通道, 綠色通道
image[:,100:150,2]=255    #第2通道, 紅色通道

y = 75
#                  y   x
print('讀取像素點 (y, 25) =', image[y, 25])
print('讀取像素點 (y, 75) =', image[y, 75])
print('讀取像素點 (y, 125) =', image[y, 125])
print('讀取像素點 (y, 125) 裡面的紅 =', image[y, 125, 2])

#逕行修改
image[:, 75] = 255
image[:, 125, 2] = 0


print('建立一個每點顏色任意顏色之圖')
random_image = np.random.randint(0, 256, size = [100, 100, 3], dtype = np.uint8)

print('將一任意圖貼上來')
#     y_st  y_sp x_st  y_st
image[100 : 200, 400 : 500] = random_image

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

img1 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
print("img1 = \n", img1)
plt.imshow(img1)
plt.show()

img2 = np.random.randint(0, 256, size = [3, 3], dtype = np.uint8)
print("img2 = \n", img2)
plt.imshow(img2)
plt.show()

img3 = img1 + img2
print("img3 = \n", img3)
plt.imshow(img3)
plt.show()

print('------------------------------------------------------------')	#60個

img = np.random.randint(10, 99, size = [5, 5], dtype = np.uint8)
print("img = \n", img)

print("讀取像素點img.item(3, 2) = ", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img.item(3, 2) = ", img.item(3, 2))

print('------------------------------------------------------------')	#60個

img = np.random.randint(10, 99, size = [2, 4, 3], dtype = np.uint8)
print("img = \n", img)

print("讀取像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("讀取像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("讀取像素點img[1, 0, 2] = ", img.item(1, 0, 2))
img.itemset((1, 2, 0), 255)
img.itemset((0, 2, 1), 255)
img.itemset((1, 0, 2), 255)
print("修改后img = \n", img)
print("修改后像素點img[1, 2, 0] = ", img.item(1, 2, 0))
print("修改后像素點img[0, 2, 1] = ", img.item(0, 2, 1))
print("修改后像素點img[1, 0, 2] = ", img.item(1, 0, 2))

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


