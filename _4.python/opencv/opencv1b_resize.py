"""

resize


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

print('縮放圖片')

img = cv2.imread(r'images/sample.jpg')
print(img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 3, H * 2))
print(img_resize.shape)

#cv2.imshow('Sample pic', img_resize)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

image_original = cv2.imread(filename)	#讀取本機圖片

#縮放的倍率 fx fy
image_resized = cv2.resize(image_original, None, fx = 1.50, fy = 1.00, interpolation = cv2.INTER_LINEAR)

image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
plt.imshow(image_original)
plt.show()

image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(image_resized)
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

img = cv2.imread(filename, 1)

print('改變圖片大小')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

print('旋轉')
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#cv2.imwrite("tmp_pic01.jpg", img)     # 將檔案寫入 tmp_pic01.jpg

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個







