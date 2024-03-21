"""
OpenCV 基本使用


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

#實例化8位圖
image_empty = np.zeros((480, 640), dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列
plt.title('空圖, 全黑')
plt.imshow(cv2.cvtColor(image_empty, cv2.COLOR_BGR2RGB))    #顯示圖片   #空圖, 全黑

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
        #mapx.itemset((i, j), W - 1 - j)
        mapy.itemset((i, j), i)
        #mapy.itemset((i, j), H - 1 - i)

rst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
print("image = \n", image)
print("mapx = \n",mapx)
print("mapy = \n",mapy)
print("rst = \n",rst)

plt.figure('xxxxxx3', figsize = (16, 12))
plt.title('用np建立一個隨機影像陣列')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

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
plt.title('用np建立一個隨機影像陣列')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

print('建立一個random圖像')

W = 30
H = 20

image = np.random.choice([0, 50,100,150,200,255], size = W * H).reshape(H, W).astype(np.uint8)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


