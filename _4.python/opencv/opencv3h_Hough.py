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

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/computer.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oShow = orgb.copy()
lines = cv2.HoughLines(edges, 1, np.pi / 180, 140)
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

plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/computer.jpg", -1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oShow = orgb.copy()
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 160, minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(orgb, (x1, y1), (x2, y2), (255, 255, 255), 2)

plt.subplot(121)
plt.imshow(oShow)
plt.axis("off")

plt.subplot(122)
plt.imshow(orgb)
plt.axis("off")

plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/chess.jpg", 0)
imgo = cv2.imread("images/chess.jpg", -1)
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

plt.show()

print("------------------------------------------------------------")  # 60個

print("這個做很久~~~~~~~")

img = cv2.imread("images/chess.jpg", 0)
imgo = cv2.imread("images/chess.jpg", -1)
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

plt.show()

print("------------------------------------------------------------")  # 60個

"""
霍夫變換

HoughLines
HoughLinesP
HoughCircles

"""
img = cv2.imread("images/jianzhu.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
edges = cv2.Canny(gray, 50, 200)

plt.figure("霍夫變換 HoughLines", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("灰階")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("Canny")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

# hough变换
lines = cv2.HoughLines(edges, 1, np.pi / 180, 180)
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

plt.show()

print("------------------------------------------------------------")  # 60個

lane1 = cv2.imread("images/lane.jpg")
# 高斯模糊，Canny边缘检测需要的
lane2 = cv2.GaussianBlur(lane1, (5, 5), 0)  # 執行高斯模糊化
# 进行边缘检测，减少图像空间中需要检测的点数量
lane3 = cv2.Canny(lane2, 50, 150)
cv2.imshow("lane3", lane3)
cv2.waitKey()

plt.figure("霍夫變換 HoughLinesP", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lane1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("高斯模糊")
plt.imshow(cv2.cvtColor(lane2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("Canny")
plt.imshow(cv2.cvtColor(lane3, cv2.COLOR_BGR2RGB))

rho = 1  # 距离分辨率
theta = np.pi / 180  # 角度分辨率
threshold = 10  # 霍夫空间中多少个曲线相交才算作正式交点
min_line_len = 10  # 最少多少个像素点才构成一条直线
max_line_gap = 50  # 线段之间的最大间隔像素
lines = cv2.HoughLinesP(lane3, rho, theta, threshold, maxLineGap=max_line_gap)
lane4 = np.zeros_like(lane3)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(lane4, (x1, y1), (x2, y2), 255, 1)

cv2.imshow("lane4", lane4)

plt.subplot(224)
plt.title("霍夫變換 HoughLinesP")
plt.imshow(cv2.cvtColor(lane4, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey()

print("------------------------------------------------------------")  # 60個

img1 = cv2.imread("images/4.png", 0)
img2 = cv2.medianBlur(img1, 5)
img3 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

plt.figure("霍夫變換 HoughCircles", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("medianBlur")
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("COLOR_GRAY2BGR")
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))

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

cv2.imshow("detected circles", img3)

plt.subplot(224)
plt.title("霍夫變換 HoughCircles")
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

"""
霍夫圓形檢測

"""
filename = "images/cup.jpg"

print("顯示圖片")
image = cv2.imread(filename, -1)

shape = image.shape
h = shape[0]  # 高
w = shape[1]  # 寬
h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

image = cv2.resize(image, (int(w / 10), int(h / 10)))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", image)  # 顯示圖片

print("在此等待任意鍵繼續, 繼續後刪除本視窗")
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("作業完成")
