"""
C : cut
C : copy
R : resize
R : rotate

"""

import cv2

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# 裁剪圖片

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
image = cv2.imread(filename)  # 讀取本機圖片

# 裁切區域的 x 與 y 座標（左上角）
x_st = 100
y_st = 100

# 裁切區域的長度與寬度
w = 250
h = 250

# 裁切圖片
crop_image = image[y_st : y_st + h, x_st : x_st + w]

cv2.imshow("cropped", crop_image)  # 顯示圖片

image_empty = np.zeros(image.shape, dtype=np.uint8)  # 依照原圖大小建立一個圖像的二維陣列

# cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

# 將擷取的圖貼到新建的黑圖
image_empty[y_st : y_st + h, x_st : x_st + w] = crop_image
cv2.imshow("cropped+new", image_empty)  # 顯示圖片

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖片裁剪縮放")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg"

image = cv2.imread(filename)  # 讀取本機圖片

x = 100
y = 100
w = 100
h = 100

print("------------------------------------------------------------")  # 60個


print("旋轉圖片")

# 影像旋轉
# 以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

image = cv2.imread(filename)  # 讀取本機圖片
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w // 2, h // 2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.7)

rotate_image = cv2.warpAffine(image, P, (w, h))

rotate_image = cv2.cvtColor(rotate_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotate_image)
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
print("讀取圖檔 :", filename)
img = cv2.imread(filename)

x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)

plt.figure("鏡射", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("x鏡射")
plt.imshow(cv2.cvtColor(x, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("y鏡射")
plt.imshow(cv2.cvtColor(y, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("xy鏡射")
plt.imshow(cv2.cvtColor(xy, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個


"""

resize


"""

print("------------------------------------------------------------")  # 60個

print("縮放圖片")

img = cv2.imread(r"images/sample.jpg")
print(img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 3, H * 2))
print(img_resize.shape)

# cv2.imshow('Sample pic', img_resize)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

image_original = cv2.imread(filename)  # 讀取本機圖片

# 縮放的倍率 fx fy
image_resized = cv2.resize(
    image_original, None, fx=1.50, fy=1.00, interpolation=cv2.INTER_LINEAR
)

image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
plt.imshow(image_original)
plt.show()

image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(image_resized)
plt.show()

print("------------------------------------------------------------")  # 60個

print("用np建立一個影像陣列")

W = 640
H = 480
D = 3

# 建立陣列
image = np.ones([H, W, D], dtype=np.uint8) * 128  # 填滿 128

# 改變陣列內容
image[:, :, 0] = 0
# 第0通道 B
image[:, :, 1] = 255
# 第1通道 G
image[:, :, 2] = 255
# 第2通道 R

# 做resize
size = H, W
print(size)
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
# print("image = \n", image)

print("rst.shape = ", rst.shape)
# print("rst = \n", rst)

plt.figure("用np建立一個影像陣列", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖 640X480")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("resize 480X640")
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print("讀取圖檔 :", filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print("W = ", W)
print("H = ", H)
print("D = ", D)

size = (int(W * 0.9), int(H * 1.1))  # 變瘦變高
rst = cv2.resize(image, size)

print("image.shape = ", image.shape)
print("rst.shape = ", rst.shape)

plt.figure("resize", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("resize 變瘦1成變高1成")
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print("讀取圖檔 :", filename)
image = cv2.imread(filename)

rst = cv2.resize(image, None, fx=2, fy=0.5)
print("image.shape =", image.shape)
print("rst.shape =", rst.shape)

plt.subplot(223)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("resize x變2倍, y變一半")
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image0 = cv2.imread(filename, 1)
print('原圖大小 :', image0.shape)
w = image0.shape[1]
h = image0.shape[0]

print('cv2.resize 之方法 1')

print("改變圖片大小 指定大小 改成 640 X 480")

image1 = cv2.resize(image0,(640, 480))   # 改變圖片尺寸

cv2.imshow("Image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("改變圖片大小 依比例 寬變兩倍 高變一半")
image2 = cv2.resize(image0, (0, 0), fx=2.0, fy=0.5)

cv2.imshow("Image", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

"""

rotate


"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename, 1)

print("旋轉")
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
print("讀取圖檔 :", filename)
image = cv2.imread(filename)

H, W, D = image.shape
print(image.shape)
print("W = ", W)
print("H = ", H)
print("D = ", D)

M = cv2.getRotationMatrix2D((W / 2, H / 2), 45, 0.6)
rotate = cv2.warpAffine(image, M, (W, H))

plt.figure("rotate", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("rotate")
plt.imshow(cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

print("圖片旋轉")

img = cv2.imread(r"images/sample.jpg")

H = img.shape[0]
W = img.shape[1]
aff_matrix = cv2.getRotationMatrix2D((W / 2, H / 2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (W, H))
cv2.imshow("Sample pic", img_rotate)

print("------------------------------------------------------------")  # 60個

print("圖片旋轉")
img_rotate = cv2.rotate(img, 1)
cv2.imshow("Sample pic", img_rotate)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

