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
import time
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
# 檔案 => cv2影像
image = cv2.imread(filename)  # 讀取本機圖片

# 裁切區域的 x 與 y 座標（左上角）
x_st, y_st = 100, 100

# 裁切區域的長度與寬度
w, h = 250, 250

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

# 檔案 => cv2影像
image = cv2.imread(filename)  # 讀取本機圖片

x = 100
y = 100
w = 100
h = 100

print("------------------------------------------------------------")  # 60個


print("旋轉圖片")

# 影像旋轉
# 以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

# 檔案 => cv2影像
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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
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

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
print("原圖大小 :", img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 2, H // 2))  # .resize 改變圖片大小W,H
print("縮放後大小 :", img_resize.shape)

plt.title("縮放 W兩倍 H一半")
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

dH, dW = 480, 480


def resizeimg(image):
    # 將影像改變到寬高最大為480等比例縮放
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (dW, math.floor(h / (w / dW))))
    else:
        img = cv2.resize(image, (math.floor(w / (h / dH)), dH))
    return img


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image1 = cv2.imread(filename)
print("原圖大小 : ", image1.shape)

image2 = resizeimg(cv2.imread(filename))
print("將影像改變到寬高最大為480等比例縮放")
print("縮放後大小 : ", image2.shape)

plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("等比例縮放 至 480")

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

# 檔案 => cv2影像
image_original = cv2.imread(filename)  # 讀取本機圖片

# 縮放的倍率 fx fy
image_resized = cv2.resize(
    image_original, None, fx=1.50, fy=1.00, interpolation=cv2.INTER_LINEAR
)  # .resize 改變圖片大小W,H

plt.figure(figsize=(10, 6))
plt.subplot(121)
image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
plt.imshow(image_original)
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title('原圖')

plt.subplot(122)
image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(image_resized)
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title('倍率縮放')

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
rst = cv2.resize(image, size)  # .resize 改變圖片大小W,H

print("原圖大小 :", image.shape)
print("縮放後大小 :", rst.shape)

plt.figure(figsize=(10, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.xlim(0, 700)  # x軸顯示邊界
plt.ylim(700, 0)  # y軸顯示邊界
plt.title("原圖 640X480")

plt.subplot(122)
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))
plt.xlim(0, 700)  # x軸顯示邊界
plt.ylim(700, 0)  # y軸顯示邊界
plt.title("resize 480X640")

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape

print("原圖大小 :", image.shape)
print("W = ", W)
print("H = ", H)
print("D = ", D)

size = (int(W * 0.9), int(H * 1.1))  # 變瘦變高
image2 = cv2.resize(image, size)  # .resize 改變圖片大小W,H
print("縮放後大小 :", image2.shape)

plt.figure("resize", figsize=(12, 6))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("resize 變瘦1成變高1成")

image3 = cv2.resize(image, None, fx=1.5, fy=0.5)  # .resize 改變圖片大小W,H
print("縮放後大小 :", image3.shape)

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.xlim(0, 500)  # x軸顯示邊界
plt.ylim(500, 0)  # y軸顯示邊界
plt.title("resize x變1.5倍, y變一半")

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y : y + h, x : x + w]

output = np.zeros((360, 480, 3), dtype="uint8")  # 產生黑色畫布
output[x : x + w, y : y + h] = crop_img

# 檔案 => cv2影像
img = cv2.imread(filename)
output_1 = cv2.resize(img, (200, 200))  # 產生 200x200 的圖
output_2 = cv2.resize(img, (100, 300))  # 產生 100x300 的圖

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
size = img.shape  # 取得原始圖片的資訊
level = 15  # 縮小比例 ( 可當作馬賽克的等級 )
h = int(size[0] / level)  # 按照比例縮小後的高度 ( 使用 int 去除小數點 )
w = int(size[1] / level)  # 按照比例縮小後的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)  # 根據縮小尺寸縮小
mosaic = cv2.resize(
    mosaic, (size[1], size[0]), interpolation=cv2.INTER_NEAREST
)  # 放大到原本的大小

cv2.imshow("image", mosaic)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("馬賽克")
# 檔案 => cv2影像
img = cv2.imread(filename)

x = 135  # 剪裁區域左上 x 座標
y = 90  # 剪裁區域左上 y 座標
cw = 100  # 剪裁區域寬度
ch = 120  # 剪裁區域高度
mosaic = img[y : y + ch, x : x + cw]  # 取得剪裁區域
level = 15  # 馬賽克程度
h = int(ch / level)  # 縮小的高度 ( 使用 int 去除小數點 )
w = int(cw / level)  # 縮小的寬度 ( 使用 int 去除小數點 )
mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_LINEAR)
mosaic = cv2.resize(mosaic, (cw, ch), interpolation=cv2.INTER_NEAREST)
img[y : y + ch, x : x + cw] = mosaic  # 將圖片的剪裁區域，換成馬賽克的圖

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

"""

rotate


"""
print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename, 1)

print("旋轉")
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape
print("原圖大小 :", image.shape)
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

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)

H = img.shape[0]
W = img.shape[1]

aff_matrix = cv2.getRotationMatrix2D((W / 2, H / 2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (W, H))

cv2.imshow("image", img_rotate)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖片旋轉")
img_rotate = cv2.rotate(img, 1)

cv2.imshow("image", img_rotate)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
img = cv2.imread(filename)
x = 100
y = 100
w = 200
h = 200
crop_img = img[y : y + h, x : x + w]  # 取出陣列的範圍

cv2.imshow("image", crop_img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


# flip

# 檔案 => cv2影像
img = cv2.imread(filename)  # 開啟圖片
output_0 = cv2.flip(img, 0)  # 上下翻轉
output_1 = cv2.flip(img, 1)  # 左右翻轉
output_2 = cv2.flip(img, -1)  # 上下左右翻轉

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
output = cv2.transpose(img)  # 逆時針旋轉 90 度。

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
output_ROTATE_90_CLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
output_ROTATE_90_COUNTERCLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
output_ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180)

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
M = np.float32([[1, 0, 100], [0, 1, 100]])  # 2x3 矩陣，x 軸平移 100，y 軸平移 100
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
M = cv2.getRotationMatrix2D((240, 180), 45, 1)  # 中心點 (240, 180)，旋轉 45 度，尺寸 1
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
img = cv2.imread(filename)
p1 = np.float32([[100, 100], [480, 0], [0, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360]])
M = cv2.getAffineTransform(p1, p2)
output = cv2.warpAffine(img, M, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

p1 = np.float32([[100, 100], [480, 0], [0, 360], [480, 360]])
p2 = np.float32([[0, 0], [480, 0], [0, 360], [480, 360]])
m = cv2.getPerspectiveTransform(p1, p2)

# 檔案 => cv2影像
img = cv2.imread(filename)
output = cv2.warpPerspective(img, m, (480, 360))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 原图的高宽
h, w = image.shape[:2]
# 仿射变换矩阵，缩小两倍
A1 = np.array([[0.5, 0, 0], [0, 0.5, 0]], np.float32)
d1 = cv2.warpAffine(image, A1, (w, h), borderValue=125)
# 先缩小两倍，再平移
A2 = np.array([[0.5, 0, w / 4], [0, 0.5, h / 4]], np.float32)
d2 = cv2.warpAffine(image, A2, (w, h), borderValue=125)
# 在 d2 的基础上，绕图像的中心点旋转
A3 = cv2.getRotationMatrix2D((w / 2, h / 2), 30, 1)
d3 = cv2.warpAffine(d2, A3, (w, h), borderValue=125)
# 在
A4 = np.array([[math.cos(math.pi / 4), 0, 0], [math.sin(math.pi / 3), 1, 0]])
d4 = cv2.warpAffine(image, A4, (2 * w, 2 * h), borderValue=125)

cv2.imshow("image", image)
cv2.imshow("d1", d1)
cv2.imshow("d2", d2)
cv2.imshow("d3", d3)
cv2.imshow("d4", d4)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 第3章：空間變換\3.2-投影變換\perspective.py

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
image = cv2.imread(filename)

# 原图的宽高
h, w, d = image.shape
# 将原图的四个顶点投影到一个不规则的四边形中
src = np.array([[0, 0], [w - 1, 0], [0, h - 1], [w - 1, h - 1]], np.float32)
dst = np.array([[20, 50], [w / 2, 150], [50, h / 2], [w - 40, h - 40]], np.float32)
# 计算投影矩阵
p = cv2.getPerspectiveTransform(src, dst)
# 利用计算出的投影矩阵进行头像的投影变换
r = cv2.warpPerspective(image, p, (w, h), borderValue=0)

# 显示原图和投影效果
cv2.imshow("image", image)
cv2.imshow("warpPerspective", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("flip")

# 檔案 => cv2影像
I = cv2.imread(filename)

O = I.copy()

# 旋轉
O = cv2.flip(O, 1)

# 顯示原圖和輸出圖像
cv2.imshow("I", I)
cv2.imshow("O", O)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

#image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)


#图像旋转 ： cv2.ROTATE_180  cv2.ROTATE_90_COUNTERCLOCKWISE
rImg = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imwrite("lsImg.jpg",lsImg)

"""
