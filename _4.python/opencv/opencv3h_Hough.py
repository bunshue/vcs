"""
霍夫變換

HoughLines
HoughLinesP
HoughCircles

"""

import cv2

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


def show():
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


# OpenCV_顏色共同
RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/Hough/computer.jpg")  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oShow = orgb.copy()

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 140)
print("共找到 :", len(lines), "條直線")

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(orgb, (x1, y1), (x2, y2), (0, 0, 255), 2)

plt.subplot(121)
plt.imshow(oShow)
plt.axis("off")

plt.subplot(122)
plt.imshow(orgb)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/Hough/computer.jpg", -1)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oShow = orgb.copy()

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=100, maxLineGap=10)
print("共找到 :", len(lines), "條直線")

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(orgb, (x1, y1), (x2, y2), (255, 255, 255), 2)

plt.subplot(121)
plt.imshow(oShow)
plt.axis("off")

plt.subplot(122)
plt.imshow(orgb)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/Hough/chess.jpg", 0)
imgo = cv2.imread("data/Hough/chess.jpg", -1)

o = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
oshow = o.copy()
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(
    img, cv2.HOUGH_GRADIENT, 1, 300, param1=50, param2=30, minRadius=100, maxRadius=200
)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(o, (i[0], i[1]), i[2], (255, 0, 0), 12)
    cv2.circle(o, (i[0], i[1]), 2, (255, 0, 0), 12)

plt.subplot(121)
plt.imshow(oshow)
plt.axis("off")

plt.subplot(122)
plt.imshow(o)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

print("這個做很久~~~~~~~")

img = cv2.imread("data/Hough/chess.jpg", 0)
imgo = cv2.imread("data/Hough/chess.jpg", -1)

o = cv2.cvtColor(imgo, cv2.COLOR_BGR2RGB)
oshow = o.copy()
img = cv2.medianBlur(img, 5)
circles = cv2.HoughCircles(
    img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0
)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(o, (i[0], i[1]), i[2], (255, 0, 0), 12)  # 注意如果是白色，会显示满屏白色，不仔细分析还会以为程序错了呢
    cv2.circle(o, (i[0], i[1]), 2, (255, 0, 0), 12)

plt.subplot(121)
plt.imshow(oshow)
plt.axis("off")

plt.subplot(122)
plt.imshow(o)
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread("data/Hough/jianzhu.png")  # 彩色讀取

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(gray, 50, 200)

plt.figure("霍夫變換 HoughLines", figsize=(12, 10))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("灰階")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("Canny邊緣檢測")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

lines1 = lines[:, 0, :]  # 提取为为二维
for rho, theta in lines1[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

plt.subplot(224)
plt.title("霍夫變換 HoughLines")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

lane1 = cv2.imread("data/Hough/lane.jpg")  # 彩色讀取

# 高斯模糊，Canny边缘检测需要的
lane2 = cv2.GaussianBlur(lane1, (5, 5), 0)  # 執行高斯模糊化

# Canny邊緣檢測，减少图像空间中需要检测的点数量
lane3 = cv2.Canny(lane2, 50, 150)

plt.figure("霍夫變換 HoughLinesP", figsize=(12, 10))

plt.subplot(221)
plt.imshow(cv2.cvtColor(lane1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(lane2, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊")

plt.subplot(223)
plt.imshow(cv2.cvtColor(lane3, cv2.COLOR_BGR2RGB))
plt.title("Canny邊緣檢測")

rho = 1  # 距离分辨率
theta = np.pi / 180  # 角度分辨率
threshold = 10  # 霍夫空间中多少个曲线相交才算作正式交点
min_line_len = 10  # 最少多少个像素点才构成一条直线
max_line_gap = 50  # 线段之间的最大间隔像素

lines = cv2.HoughLinesP(lane3, rho, theta, threshold, maxLineGap=max_line_gap)
print("共找到 :", len(lines), "條直線")

lane4 = np.zeros_like(lane3)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(lane4, (x1, y1), (x2, y2), 255, 1)

plt.subplot(224)
plt.imshow(cv2.cvtColor(lane4, cv2.COLOR_BGR2RGB))
plt.title("霍夫變換 HoughLinesP")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img1 = cv2.imread("data/Hough/4.png", 0)  # 灰階讀取
img2 = cv2.medianBlur(img1, 5)
img3 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

plt.figure("霍夫變換 HoughCircles", figsize=(12, 10))
plt.subplot(221)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("medianBlur")

plt.subplot(223)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("COLOR_GRAY2BGR")

circles = cv2.HoughCircles(
    img2,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=100,
    param2=30,
    minRadius=100,
    maxRadius=200,
)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # 画外圆
    cv2.circle(img3, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 画出圆心
    cv2.circle(img3, (i[0], i[1]), 2, (0, 0, 255), 3)

plt.subplot(224)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("霍夫變換 HoughCircles")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 霍夫圓形檢測

filename = "data/Hough/cup.jpg"

image = cv2.imread(filename, -1)  # 彩色讀取

plt.subplot(211)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

shape = image.shape
h = shape[0]  # 高
w = shape[1]  # 寬
h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

image = cv2.resize(image, (int(w / 10), int(h / 10)))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray = cv2.GaussianBlur(gray, (5, 5), 0)  # 執行高斯模糊化
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,  # 偵測方法目前只支援這個參數
    1,  # 1代表偵測圖與輸入圖大小一致，填1即可
    20,  # 各圓心間的最小距離，設太小容易誤判，太大會將數個圓當成一個
    None,  # 固定填 None
    10,  # canny演算法的高閾值，此值一半為低閾值
    75,  # 超過此閾值才會被當作圓
    3,  # 最小圓半徑
    75,  # 最大圓半徑
)

print(circles)

"""
if circles == None:
    print('找不到圓形, 離開')
    sys.exit()
"""

circles = circles.astype(int)
print(circles)

if len(circles) > 0:
    out = image.copy()
    for x, y, r in circles[0]:
        # 畫圓
        cv2.circle(out, (x, y), r, (0, 0, 255), 3)
        # 畫圓心
        cv2.circle(out, (x, y), 2, (0, 255, 0), 3)
    image = cv2.hconcat([image, out])


plt.subplot(212)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("霍夫圓形檢測")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# add_collection 只能用 ax

# 使用HoughLinesP()檢驗圖形中的直線
img = cv2.imread("data/Hough/building.jpg", cv2.IMREAD_GRAYSCALE)

# Canny邊緣檢測，减少图像空间中需要检测的点数量
img_binary = cv2.Canny(img, 100, 255)

lines = cv2.HoughLinesP(
    img_binary,
    rho=1,
    theta=np.deg2rad(0.1),
    threshold=96,
    minLineLength=33,
    maxLineGap=4,
)
print("共找到 :", len(lines), "條直線")

fig, ax = plt.subplots(figsize=(12, 10))
plt.imshow(img, cmap="gray")

from matplotlib.collections import LineCollection

lc = LineCollection(lines.reshape(-1, 2, 2))
ax.add_collection(lc)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檢驗圓形

# 使用HoughCircles()檢驗圖形中的圓形
img = cv2.imread("data/Hough/coins.png", cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (0, 0), 1.8)
circles = cv2.HoughCircles(
    img_blur,
    cv2.HOUGH_GRADIENT,
    dp=2.0,
    minDist=20.0,
    param1=170,
    param2=44,
    minRadius=16,
    maxRadius=40,
)

x, y, r = circles[0].T

fig, ax = plt.subplots(figsize=(12, 10))
plt.imshow(img, cmap="gray")

from matplotlib.collections import EllipseCollection

ec = EllipseCollection(
    widths=2 * r,
    heights=2 * r,
    angles=0,
    units="xy",
    facecolors="none",
    edgecolors="red",
    transOffset=ax.transData,
    offsets=np.c_[x, y],
)
ax.add_collection(ec)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_18_從直線檢測到無人駕駛車道檢測
print("------------------------------------------------------------")  # 60個

filename = "data/Hough/japanese_schedule.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 100, 200)

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 220)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

# 繪製直線 在 src 上
index = 0
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 繪製綠色線條
    # cv2.line(src, (x1, y1), (x2, y2), colors[index%6], 2)  # 繪製綠色線條
    index += 1

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("邊緣檢測")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/Hough/lane2.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 100, 200)
cv2.imshow("edges", edges)

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("邊緣檢測")
plt.axis("off")

# 尋找霍夫直線
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
print("共找到 :", len(lines), "條直線")

# 繪製直線, 畫在src上
for line in lines:
    rho, theta = line[0]  # lines回傳
    a = np.cos(theta)  # cos(theta)
    b = np.sin(theta)  # sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))  # 建立 x1
    y1 = int(y0 + 1000 * (a))  # 建立 y1
    x2 = int(x0 - 1000 * (-b))  # 建立 x2
    y2 = int(y0 - 1000 * (a))  # 建立 y2
    cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 繪製紅色線條

cv2.imshow("dst", src)

plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")
plt.axis("off")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/Hough/roadtest.jpg", cv2.IMREAD_COLOR)

cv2.imshow("src", src)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
edges = cv2.Canny(src_gray, 50, 200)

cv2.imshow("Canny", edges)

plt.subplot(132)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("Canny")
plt.axis("off")

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
print("共找到 :", len(lines), "條直線")

# 繪製檢測到的直線, 畫在src上
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 3)  # 繪製藍色線條
cv2.imshow("dst", src)


plt.subplot(133)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughLines")
plt.axis("off")

show()


cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/Hough/shapes.jpg")
cv2.imshow("src", src)

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

src = cv2.medianBlur(src, 5)  # 過濾雜訊

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉灰階
circles = cv2.HoughCircles(
    src_gray,
    cv2.HOUGH_GRADIENT,
    1,
    100,
    param1=50,
    param2=30,
    minRadius=70,
    maxRadius=200,
)
circles = np.uint(np.around(circles))  # 轉成整數

# 繪製檢測到的直線, 畫在src上
for c in circles[0]:
    x, y, r = c
    cv2.circle(src, (x, y), r, (0, 255, 0), 3)  # 綠色繪圓外圈
    cv2.circle(src, (x, y), 2, (0, 0, 255), 2)  # 紅色繪圓中心
cv2.imshow("dst", src)


plt.subplot(122)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("HoughCircles")
plt.axis("off")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 參數使用
# 尋找霍夫直線
lines = cv2.HoughLines(canny_image, 1, np.pi/180, 180)
canny_image：经过图像边缘处理后的图像
1：像素之间的距离为1
np.pi/180：直线角度范围，2pi/(pi/180) = 360°
180：一条预选直线上的最少像素点个数
注意：
如果距离是1，180个像素即可生成直线，
如果距离是2，至少360个像素才可以生成直线。
"""
"""
霍夫直线的返回参数
cv2.HoughLines 的返回参数 line == [\rho ,\Theta ]，
其中，第一个参数表示图像原点距离直线的长度，第二个参数表示沿着x轴的角度大小。
如下图所示，首先通过 cv.HoughLines 得到 line，
此时已经确定了直线的位置，然后需要确定直线上的两个坐标点来充当 cv.line 的输入参数，
最后，在源图像上通过 cv.line 来绘制直线。
"""

"""
图解cv2.HoughLines的返回参数
        # 延长直线的长度，保证在整幅图像上绘制直线
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))
前面讲到， 霍夫直线值仅仅返回两个参数，并不会直接返回直线上的坐标点，
我们在选取直线坐标点的时候，需要尽量选取图像外部的点（即负数），
这样才会过整幅图像绘制直线。
"""

img = cv2.imread("data/Hough/FerrisWheel4.png")  # 彩色讀取

cv2.imshow("src", img)

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

img_gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)  # 轉灰階

# Canny邊緣檢測，减少图像空间中需要检测的点数量
canny_image = cv2.Canny(img, 200, 200)

cv2.imshow("canny_image", canny_image)

# 尋找霍夫直線
lines = cv2.HoughLines(canny_image, 1, np.pi / 180, 180)
print("共找到 :", len(lines), "條直線")

# 绘画霍夫直线
if lines is not None:
    for n, line in enumerate(lines):
        # 沿着左上角的原点，作目标直线的垂线得到长度和角度
        rho = line[0][0]
        theta = line[0][1]
        # if np.pi / 3 < theta < np.pi * (3 / 4):
        a = np.cos(theta)
        b = np.sin(theta)
        # 得到目标直线上的点
        x0 = a * rho
        y0 = b * rho

        # 延长直线的长度，保证在整幅图像上绘制直线
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))

        # 连接两点画直线
        cv2.line(img, (x1, y1), (x2, y2), WHITE, 1)

plt.subplot(312)
plt.title("Canny")
plt.imshow(cv2.cvtColor(canny_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(313)
plt.title("result")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

show()


cv2.imshow("result", img)
cv2.imshow("canny", canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
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


print("------------------------------------------------------------")  # 60個
