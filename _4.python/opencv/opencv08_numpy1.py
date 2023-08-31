'''
opencv + numpy製作資料

'''

import cv2
import numpy as np

import sys

print('------------------------------------------------------------')	#60個

#建立一黑圖
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
random_image = np.random.randint(0,256,size=[100, 100, 3],dtype = np.uint8)

print('將一任意圖貼上來')
#     y_st  y_sp x_st  y_st
image[100 : 200, 400 : 500] = random_image


cv2.imshow("image", image)    #顯示圖片


cv2.waitKey()
cv2.destroyAllWindows()

import sys
sys.exit()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
