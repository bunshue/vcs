"""
opencv 集合 新進2

"""

import cv2

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/ims01.bmp"

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

maxval = 255  # 定義像素最大值, 閾值
width, height = 640, 480  # 影像寬, 影像高

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

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def show():
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


print("------------------------------------------------------------")  # 60個

# 01loadimg.py

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
img = cv2.imread(filename, 0)  # 0 黑白图片；1 原色图片
cv2.imshow(win_name, img)  # 显示图片
cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁创建的对象

cv2.imwrite("tmp_picture1.mono.pgm", img)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 02opencvmatplotlib.py

# 读取图片
img = cv2.imread("tmp_picture1.mono.pgm", 0)  # 黑白图片
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # 隐藏 X Y 坐标
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03drawrectangle.py

# Create a black image
img = np.zeros((512, 512, 3))
# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色:( 255,0,0)，宽度:2
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04drawGeometry.py

img = np.zeros((512, 512, 3))
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 矩形
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)  # 圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)  # 椭圆
# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, (0, 255, 255), 1)
# 写入文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05drawcirlcle.py

img = np.zeros((512, 512, 3))
# 绘制圆：圆心(255, 255), 半径60, 颜色( 0, 255, 255), 像素1
cv2.circle(img, (255, 150), 60, (0, 255, 255), 2)  # 圆
# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100
# 360表示整个椭圆；颜色 0, 255, 255；像素2；
cv2.ellipse(img, (255, 350), (100, 50), 0, 0, 360, (255, 255, 0), 2)  # 椭圆
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt_tree.xml"
picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("_tmp_face1.jpg", img)  # 存圖

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
)

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("_tmp_face2.jpg", img)  # 存圖

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
