"""
OpenCV影像創意邁向AI視覺王者歸來

"""

print("------------------------------------------------------------")  # 60個

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


maxval = 255  # 定義像素最大值, 閾值
width, height = 640, 480  # 影像寬, 影像高

RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]
'''
print("------------------------------------------------------------")  # 60個

print("製作影像")

width, height = 640, 480  # 影像寬, 影像高

# 建立 640 X 480 之黑圖
fig = np.zeros((height, width), dtype=np.uint8)

# 建立 640 X 480 之白圖
fig = np.ones((height, width), dtype=np.uint8) * 255

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

# 某塊塗為白色
image[40:120, 70:210] = 255  # 高在40至120之間,寬在70至210之間,設為255

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)

print("某些塗為白色")

for y in range(0, height, 20):
    image[y : y + 10, :] = 255  # 白色厚度是10
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)
image[:, :, 0] = 255  # 建立 B 通道像素值
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

height = 160  # 影像高
width = 280  # 影像寬
width, height = 640, 480  # 影像寬, 影像高

# 建立BGR影像陣列
image = np.zeros((height, width, 3), np.uint8)

# R
red_image = image.copy()
red_image[:, :, 2] = 255  # 建立 R 通道像素值

# G
green_image = image.copy()
green_image[:, :, 1] = 255  # 建立 G 通道像素值

# B
blue_image = image.copy()
blue_image[:, :, 0] = 255  # 建立 B 通道像素值

# Y
yellow_image = image.copy()
yellow_image[:, :, 2] = 255  # 建立 R 通道像素值
yellow_image[:, :, 1] = 255  # 建立 G 通道像素值

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

image = np.zeros((height, width, 3), np.uint8)
image[0:50, :, 0] = 255  # blue
image[50:100, :, 1] = 255  # green
image[100:150, :, 2] = 255  # red
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("製作隨機影像")

# 使用random.randint()建立GRAY影像陣列
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)  # 灰階, 1維
# src = np.random.randint(256, size=[height, width, 3], dtype=np.uint8)  # 彩色, 3維

cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

src = np.random.randint(256, size=(height, width))  # 建立矩陣
# print(f"矩陣內容 = \n{src}")

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# 製作隨機影像
width, height = 64, 48  # 影像寬, 影像高
src = np.random.randint(0, 256, size=[height, width], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個
# OpenCV_05_建立空影像
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立GRAY影像陣列, 黑色
image = np.zeros((height, width), np.uint8)
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.zeros((height, width), np.uint8)
image.fill(255)  # 元素內容改為白色 255
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

# 建立GRAY影像陣列, 白色
image = np.ones((height, width), np.uint8) * 255
cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("-------------------- ----------------------------------------")  # 60個
# OpenCV 運算
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)

channels = cv2.mean(src)  # 計算影像各通道的均值
print(f"均值   = \n{channels}")

mean, std = cv2.meanStdDev(src)  # 計算影像各通道的標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(5000)  # 等待 5 秒
cv2.destroyWindow("Peony")  # 關閉視窗

ret_value = cv2.waitKey(0)  # 無限等待
if ret_value == ord("Q") or ret_value == ord("q"):
    cv2.destroyWindow("Peony")  # 關閉視窗

print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread(filename1)
cv2.imshow("Peony", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 設定 cv 視窗
cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小

img1 = cv2.imread(filename1)  # 彩色讀取
img2 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
# img2 = cv2.imread(filename1, 0)  # 灰色讀取 same

cv2.imshow("Peony1", img1)
cv2.imshow("Peony2", img2)

cv2.waitKey()
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取某點的灰階/RGB值

pt_y = 169
pt_x = 118

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
px = img[pt_y, pt_x]  # 讀px點

print(type(px))
print(f"BGR = {px}")

img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀px點
print(type(px))
print(f"BGR = {px}")

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
blue = img[pt_y, pt_x, 0]  # 讀 B 通道值
green = img[pt_y, pt_x, 1]  # 讀 G 通道值
red = img[pt_y, pt_x, 2]  # 讀 R 通道值
print(f"BGR = {blue}, {green}, {red}")

print("------------------------------------------------------------")  # 60個

# 修改影像的RGB值

pt_y = 169
pt_x = 118
img = cv2.imread(filename1)  # 彩色讀取
px = img[pt_y, pt_x]  # 讀取 px 點
print(f"更改前BGR = {px}")
px = [255, 255, 255]  # 修改 px 點
print(f"更改後BGR = {px}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_06_影像處理
print("------------------------------------------------------------")  # 60個

print("修改圖片的像素值 灰階")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = 127

plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階")
plt.axis("off")

print("修改圖片的像素值 彩色")

img = cv2.imread(filename1)  # 彩色讀取
print(img.shape)

for y in range(0, img.shape[0], 5):
    for x in range(0, img.shape[1], 5):
        img[y, x] = [255, 0, 0]

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("彩色")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

width, height = 640, 480  # 影像寬, 影像高

# 建立紅色red底的彩色影像陣列
red_image = np.zeros((height, width, 3), np.uint8)
red_image[:, :, 2] = 255  # 填滿紅色

# 建立綠色green底的彩色影像陣列
green_image = np.zeros((height, width, 3), np.uint8)
green_image[:, :, 1] = 255  # 填滿綠色

# 建立藍色blue底的彩色影像陣列
blue_image = np.zeros((height, width, 3), np.uint8)
blue_image[:, :, 0] = 255  # 填滿藍色

# 建立黃色yellow底的彩色影像陣列
yellow_image = np.zeros((height, width, 3), np.uint8)
yellow_image[:, :, 2] = 255  # 填滿紅色
yellow_image[:, :, 1] = 255  # 填滿綠色

plt.subplot(221)
plt.imshow(cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(yellow_image, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("Y")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1] = {blue[0,1]}")

blue[0, 1] = [50, 100, 150]  # 修訂像素點
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue[0,1,2]}")

blue[0, 1, 2] = 50  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue[0,1,2]}")

print("------------------------------------------------------------")  # 60個

# 取出像素值, 修改之

img = cv2.imread(filename1)  # 彩色讀取

print(f"修改前img[115,110] = {img[115,110]}")
print(f"修改前img[125,110] = {img[125,110]}")
print(f"修改前img[135,110] = {img[135,110]}")

# 紫色長條
img[115:125, 110:210] = [255, 0, 255]

# 白色長條
for z in range(125, 135):  # 修改影像:一次一個通道值
    for y in range(110, 210):
        for x in range(0, 3):  # 一次一個通道值
            img[z, y, x] = 255  # 白色取代

# 黃色長條
for y in range(135, 145):  # 修改影像
    for x in range(110, 210):
        img[y, x] = [0, 255, 255]  # 黃色取代

cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110] = {img[115,110]}")
print(f"修改後img[125,110] = {img[125,110]}")
print(f"修改後img[135,110] = {img[135,110]}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("修改alpha通道值 255=>127")

# 4通道的PNG圖
filename5 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"

img = cv2.imread(filename5, cv2.IMREAD_UNCHANGED)  # PNG讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(img.shape)
print(f"修改前img[210,150] = {img[210,150]}")
print(f"修改前img[250,199] = {img[250,199]}")

for z in range(0, img.shape[1]):  # 一次一個修改alpha通道值
    for y in range(0, img.shape[0]):
        img[z, y, 3] = 127  # 修改alpha通道值

img[0:200, 0:200, 3] = 127  # 修改alpha通道值

print(f"修改後img[210,150] = {img[210,150]}")
print(f"修改後img[250,199] = {img[250,199]}")

cv2.imshow("After", img)  # 顯示修改前影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = np.random.randint(0, 200, size=[3, 5], dtype=np.uint8)
print(f"image = \n{image}")
print(f"修改前image.item(1,3) = {image.item(1,3)}")

image.itemset((1, 3), 255)  # 修訂內容為 255

print(f"修改後image =\n{image}")
print(f"修改後image.item(1,3) = {image.item(1,3)}")

print("------------------------------------------------------------")  # 60個

print("灰階讀取, 部分塗成灰色")

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img

for y in range(30, 100):  # 修改影像
    for x in range(180, 280):
        img.itemset((y, x), 127)
cv2.imshow("After", img)  # 顯示修改後影像img

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 建立藍色blue底的彩色影像陣列
blue = np.zeros((2, 3, 3), np.uint8)
blue[:, :, 0] = 255  # 填滿藍色
print(f"blue =\n{blue}")  # 列印影像陣列
# 列印修訂前的像素點
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

blue.itemset((0, 1, 2), 50)  # 修訂像素點的單一通道
print("修訂後")
# 列印修訂後的像素點
print(f"blue =\n{blue}")  # 列印影像陣列
print(f"blue[0,1,2] = {blue.item(0,1,2)}")

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Before", img)  # 顯示修改前影像img
print(f"修改前img[115,110,1] = {img.item(115,110,1)}")
print(f"修改前img[125,110,1] = {img.item(125,110,1)}")
print(f"修改前img[135,110,1] = {img.item(135,110,1)}")

# 白色長條
for z in range(30, 100):  # 修改影像:一次一個通道值
    for y in range(180, 280):
        for x in range(0, 3):  # 一次一個通道值
            img.itemset((z, y, x), 127)  # 白色取代
cv2.imshow("After", img)  # 顯示修改後影像img

print(f"修改後img[115,110,1] = {img.item(115,110,1)}")
print(f"修改後img[125,110,1] = {img.item(125,110,1)}")
print(f"修改後img[135,110,1] = {img.item(135,110,1)}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony", img)

# ROI大小區塊建立馬賽克
w, h = 100, 70
face = np.random.randint(0, 256, size=(h, w, 3))  # 馬賽克效果
img[30 : 30 + h, 180 : 180 + w] = face  # ROI, 先高後寬
cv2.imshow("Face", img)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

big = cv2.imread(filename2)  # 彩色讀取, 大圖

small = cv2.imread(filename1)  # 彩色讀取, 小圖

roi = small[110:200, 130:220]  # ROI, 先高後寬

big[110:200, 70:160] = roi  # 小圖貼到大圖上

cv2.imshow("Image", big)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_08_影像計算
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = cv2.add(src1, src2)
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 灰階/彩色影像相加, 變得更白/更亮
# 用相加的，像素值會破表

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰色讀取
# img = cv2.imread(filename1)  # 彩色讀取
cv2.imshow("Peony0", img)

res = cv2.add(img, img)
cv2.imshow("Peony_by_cv2.add", res)

res2 = img + img
cv2.imshow("Peony_by_+", res2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

value = 60  # 亮度調整值
img = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("Elephant1", img)

coff = np.ones(img.shape, dtype=np.uint8) * value
res = cv2.add(img, coff)  # 調整亮度結果
cv2.imshow("Elephant2", res)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 像素質直接相加會破表

src1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
src2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
res = src1 + src2
print(f"src1 = \n {src1}")
print(f"src2 = \n {src2}")
print(f"dst = \n {src1+src2}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

b = np.zeros((height, width, 3), np.uint8)  # b影像
g = np.zeros((height, width, 3), np.uint8)  # g影像
r = np.zeros((height, width, 3), np.uint8)  # r影像
b[:, :, 0] = 255  # 設定藍色
g[:, :, 1] = 255  # 設定綠色
r[:, :, 2] = 255  # 設定紅色

img1 = cv2.add(b, g)  # b + g影像
img2 = cv2.add(g, r)  # g + r影像
img3 = cv2.add(img1, r)  # b + g + r影像

plt.subplot(231)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B+G")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G+R")
plt.axis("off")

plt.subplot(236)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("B+G+R")
plt.axis("off")

show()

""" size error
# 製作mask
# mask = np.zeros((4, 5), dtype=np.uint8)
mask = np.zeros((height, width, 3), np.uint8)
mask[100:300, 100:, -1] = 255  # 設定mask, 先高後寬

img4 = cv2.add(b, g, mask=mask)  # b + g影像 + mask

cv2.imshow("img4", img4)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add
# 影像相加 影像取mask

img1 = np.ones((4, 5), dtype=np.uint8) * 8
img2 = np.ones((4, 5), dtype=np.uint8) * 9

# 製作mask
mask = np.zeros((4, 5), dtype=np.uint8)
mask[1:3, 1:4] = 255  # 設定mask, 先高後寬

print("img1 = \n", img1)
print("img2 = \n", img2)
print("mask = \n", mask)

dst = cv2.add(img1, img2, mask=mask)
print("結果值 dst =\n", dst)

print("------------------------------------------------------------")  # 60個

# 影像計算 影像相加 cv2.add

width, height = 640, 480  # 影像寬, 影像高

img1 = np.zeros((height, width, 3), np.uint8)  # 建立img1影像
img1[:, :, 2] = 255  # 紅色

img2 = np.zeros((height, width, 3), np.uint8)  # 建立img2影像
img2[:, :, 1] = 255  # 綠色

# 製作mask
m = np.zeros((height, width, 1), np.uint8)  # 建立mask(m)影像
m[50:350, 100:300, :] = 255  # 建立 ROI, 白色

# 使用cv2.add相加
img3 = cv2.add(img1, img2)  # 不含mask的影像相加

# 使用cv2.add相加, 使用mask
img4 = cv2.add(img1, img2, mask=m)  # 含mask的影像相加

plt.subplot(231)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(232)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(233)
plt.imshow(cv2.cvtColor(m, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("mask")
plt.axis("off")

plt.subplot(234)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G by cv2.add")
plt.axis("off")

plt.subplot(235)
plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G+mask by cv2.add")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# 加權和 alpha beta gamma

# 全 10 影像
src1 = np.ones((2, 3), dtype=np.uint8) * 10
print(f"src1 = \n {src1}")

# 全 50 影像
src2 = np.ones((2, 3), dtype=np.uint8) * 50
print(f"src2 = \n {src2}")

alpha = 1
beta = 0.5
gamma = 5
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和
print(f"dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

# 要一樣大的影像才可以做 加權和 addWeighted

filename_rgb_r = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename_rgb_g = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

src1 = cv2.imread(filename_rgb_r)
src2 = cv2.imread(filename_rgb_g)

alpha = 1
beta = 0.2
gamma = 1
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)  # 加權和

plt.subplot(131)
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("G")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("R+G")
plt.axis("off")

plt.suptitle("addWeighted")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)

plt.subplot(331)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

row, column = img.shape
x = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    x[:, :, i] = 2**i  # 填上權重

result = np.zeros((row, column, 8), dtype=np.uint8)

for i in range(8):
    result[:, :, i] = cv2.bitwise_and(img, x[:, :, i])
    mask = result[:, :, i] > 0  # 影像邏輯值
    result[mask] = 255  # True的位置填255
    plt.subplot(3, 3, i + 2)
    plt.imshow(cv2.cvtColor(result[:, :, i], cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
    plt.title(str(i))
    plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# cv2.bitwise_and

src = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)
row, column = src.shape  # 取得列高和欄寬

h100 = np.ones((row, column), dtype=np.uint8) * 100  # 建立像素值是100的影像

new_src = cv2.bitwise_and(src, h100)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(h100, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("灰階100")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(new_src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title("原圖取出灰階100")
plt.axis("off")

plt.suptitle("cv2.bitwise_and")
show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_20_模板匹配 Template Matching
print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46.jpg"
filename2 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46_head.jpg"

src = cv2.imread(filename1, cv2.IMREAD_COLOR)

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
#plt.axis("off")

template = cv2.imread(filename2, cv2.IMREAD_COLOR)
height, width = template.shape[:2]  # 獲得模板影像的高與寬

# 使用 cv2.TM_SQDIFF_NORMED 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, GREEN, 3)  # 繪置最相似外框
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

plt.subplot(312)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
#plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
#plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
src = []  # 建立原始影像陣列

src1 = cv2.imread("tennis1.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列

src2 = cv2.imread("tennis2.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列

src3 = cv2.imread("tennis3.jpg", cv2.IMREAD_COLOR)
src.append(src3)  # 加入原始影像串列

template = cv2.imread("tennis0.jpg", cv2.IMREAD_COLOR)

# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
minValue = 1  # 設定預設的最小值
index = -1  # 設定最小值的索引
# 採用歸一化平方匹配法
for i in range(len(src)):
    result = cv2.matchTemplate(src[i], template, cv2.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    # print(i, minVal, maxVal, minLoc, maxLoc, "\t比較小", minVal)
    print("圖 :", i, "值 :", minVal)
    if minValue > minVal:
        minValue = minVal  # 紀錄目前的最小值
        index = i  # 紀錄目前的索引

seq = "tennis" + str(index) + ".jpg"
print(f"{seq} 比較類似")

plt.subplot(221)
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))
plt.title("src1")
#plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))
plt.title("src2")
#plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))
plt.title("src3")
#plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
#plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/Angry-Birds01.jpg"
filename_small = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"

src = cv2.imread(filename_big, cv2.IMREAD_COLOR)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("src")
#plt.axis("off")

template = cv2.imread(filename_small, cv2.IMREAD_COLOR)

height, width = template.shape[:2]  # 獲得模板影像的高與寬

# 使用 cv2.TM_CCOEFF_NORMED 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.85:  # 值大於0.95就算找到了
            dst = cv2.rectangle(
                src, (col, row), (col + width, row + height), RED, 3
            )

plt.subplot(132)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
#plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
#plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

start_x = 450  # 目前位置 x
start_y = 180  # 目前位置 y
src = cv2.imread("airport.jpg", cv2.IMREAD_COLOR)

template = cv2.imread("airport_mark.jpg", cv2.IMREAD_COLOR)

dst = cv2.circle(src, (start_x, start_y), 10, BLUE, -1) # 實心圓

h, w = template.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), RED, 2)#空心長方形
            ul_x.append(col)  # 加入最佳匹配串列 x
            ul_y.append(row)  # 加入最佳匹配串列 y

# 計算目前位置到台北機場的距離
sub_x = start_x - ul_x[0]  # 計算 x 座標差距
sub_y = start_y - ul_y[0]  # 計算 y 座標差距
start_taipei = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到台北機場的距離 = {start_taipei:8.2f}")

# 計算目前位置到桃園機場的距離
sub_x = start_x - ul_x[1]  # 計算 x 座標差距
sub_y = start_y - ul_y[1]  # 計算 y 座標差距
start_taoyuan = math.hypot(sub_x, sub_y)  # 計算距離
print(f"目前位置到桃園機場的距離 = {start_taoyuan:8.2f}")

# 計算最短距離
if start_taipei > start_taoyuan:  # 距離比較
    print('桃園機場 較近')
else:
    print('台北機場 較近')

cv2.line(src, (start_x, start_y), (ul_x[0], ul_y[0]), RED, 2)
cv2.line(src, (start_x, start_y), (ul_x[1], ul_y[1]), GREEN, 2)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def myMatch(image, tmp):
    # 執行匹配
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像

temps = []
template = cv2.imread("heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(template)  # 加入匹配串列temps

temp2 = cv2.imread("star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp2)  # 加入匹配串列temps

match = []  # 符合匹配的圖案
for t in temps:
    myMatch(src, t)  # 調用 myMatch
for img in match:
    dst = cv2.rectangle(src, (img[0]), (img[1]), GREEN, 1)  # 繪外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_23_影像擷取
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)  # 讀取影像

mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (150, 50, 200, 480)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1

# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)

# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

dst = cv2.rectangle(dst, rect, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# ch23_2.py

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)

maskpict = cv2.imread("hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# OpenCV_24_影像修復
print("------------------------------------------------------------")  # 60個

# ch24_1.py

# 修復影像 inpaint

lisa = cv2.imread("lisaE1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# ch24_2.py

lisa = cv2.imread("lisaE2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)

# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)

plt.subplot(131)
plt.imshow(cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("影像修復結果")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#print(f"輸出二維陣列 = \n{data}")
#print(f"轉成一維陣列 = \n{data.ravel()}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

num = 30  # 數據數量

trains = np.random.randint(0, 100, size=(num, 2))

# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1))

# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小

# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
show()

print("------------------------------------------------------------")  # 60個
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

cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()

ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
cv2.imwrite("a32.png", a32_image)  # 儲存alpha=32影像

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img = cv2.imread(filename1)  # 彩色讀取

# 影像的屬性

print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# np.vsplit(data, 2) 垂直方向分割數據
# np.hsplit(data, 2) 水平方向分割數據
# np.repeat(data, N) 元素重複, 每個元素重複N次
# np.repeat(data, 3, axis=1)
# np.repeat(data, 3, axis=0)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
陣列垂直合併 vstack()
陣列水平合併 hstack()
"""

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Peony", img)

# 準備搬出

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

print("------------------------------------------------------------")  # 60個

# 取出圖片的一塊
face = img[70:220, 90:240]  # ROI, 先高後寬
cv2.imshow("Face", face)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
src = cv2.imread(filename2)
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個

# 使用 cv2.TM_SQDIFF 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")



"""
待清除本地檔案
.jpg
.bmp
.png


"""

