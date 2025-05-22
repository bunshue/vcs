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


print("------------------------------------------------------------")  # 60個
# OpenCV_16_輪廓擬合與凸包的相關應用
print("------------------------------------------------------------")  # 60個

# ch16_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 輸出矩形格式使用元組(tuple)
rect = cv2.boundingRect(contours[0])
print(f"元組 rect = {rect}")
# 輸出矩形格式, 列出所有細項
x, y, w, h = cv2.boundingRect(contours[0])
print(f"左上角 x = {x}, 左上角 y = {y}")
print(f"矩形寬度     = {w}")
print(f"矩形高度     = {h}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_3.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_4.py

src = cv2.imread("explode2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

box = cv2.minAreaRect(contours[0])  # 建構最小矩形
print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)  # 獲取頂點座標
points = np.int0(points)  # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")
dst = cv2.drawContours(src, [points], 0, (0, 255, 0), 2)  # 繪製輪廓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_5.py

src = cv2.imread("explode3.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_6.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, (0, 255, 255), 2)  # 繪圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_7.py

src = cv2.imread("cloud.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得圓中心座標和圓半徑
ellipse = cv2.fitEllipse(contours[0])  # 取得最優擬合橢圓數據
print(f"資料類型   = {type(ellipse)}")
print(f"橢圓中心   = {ellipse[0]}")
print(f"長短軸直徑 = {ellipse[1]}")
print(f"旋轉角度   = {ellipse[2]}")
dst = cv2.ellipse(src, ellipse, (0, 255, 0), 2)  # 繪橢圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_8.py

src = cv2.imread("heart.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 取得三角形面積與頂點座標
area, triangle = cv2.minEnclosingTriangle(contours[0])
print(f"三角形面積   = {area}")
print(f"三角形頂點座標資料類型 = {type(triangle)}")
print(f"三角頂點座標 = \n{triangle}")
triangle = np.int0(triangle)  # 轉整數
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), (0, 255, 0), 2)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_9.py

src = cv2.imread("multiple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 近似多邊形包圍
n = len(contours)  # 輪廓數量
src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
for i in range(n):
    approx = cv2.approxPolyDP(contours[i], 3, True)  # epsilon=3
    dst1 = cv2.polylines(src1, [approx], True, (0, 255, 0), 2)  # dst1
    approx = cv2.approxPolyDP(contours[i], 15, True)  # epsilon=15
    dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # dst2
cv2.imshow("dst1 - epsilon = 3", dst1)
cv2.imshow("dst2 - epsilon = 15", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_10.py

src = cv2.imread("unregular.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 擬合一條線
rows, cols = src.shape[:2]  # 輪廓大小
vx, vy, x, y = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
print(f"共線正規化向量 = {vx}, {vy}")
print(f"直線經過的點   = {x}, {y}")
lefty = int((-x * vy / vx) + y)  # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)  # 右邊點的 y 座標
dst = cv2.line(src, (0, lefty), (cols - 1, righty), (0, 255, 0), 2)  # 左到右繪線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_11.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_12_1.py

src = cv2.imread("hand1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
print(f"凸包面積 = {convex_area}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_13.py

src = cv2.imread("hand2.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
n = len(contours)  # 輪廓數量
for i in range(n):
    hull = cv2.convexHull(contours[i])  # 獲得凸包頂點座標
    dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_14.py

src = cv2.imread("star.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包 -> 凸包缺陷
contour = contours[0]  # 輪廓
hull = cv2.convexHull(contour, returnPoints=False)  # 獲得凸包
defects = cv2.convexityDefects(contour, hull)  # 獲得凸包缺陷
n = defects.shape[0]  # 缺陷數量
print(f"缺陷數量 = {n}")
for i in range(n):
    # s是startPoint, e是endPoint, f是farPoint, d是depth
    s, e, f, d = defects[i, 0]
    start = tuple(contour[s][0])  # 取得startPoint座標
    end = tuple(contour[e][0])  # 取得endPoint座標
    far = tuple(contour[f][0])  # 取得farPoint座標
    dst = cv2.line(src, start, end, [0, 255, 0], 2)  # 凸包連線
    dst = cv2.circle(src, far, 3, [0, 0, 255], -1)  # 繪製farPoint
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_15.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
src1 = src.copy()  # 複製src影像
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst1 = cv2.polylines(src1, [hull], True, (0, 255, 0), 2)  # 將凸包連線
cv2.imshow("dst1", dst1)
isConvex = cv2.isContourConvex(hull)  # 是否凸形
print(f"凸包是凸形       = {isConvex}")
# 近似多邊形包圍
src2 = src.copy()  # 複製src影像
approx = cv2.approxPolyDP(contours[0], 10, True)  # epsilon=10
dst2 = cv2.polylines(src2, [approx], True, (0, 255, 0), 2)  # 近似多邊形連線
cv2.imshow("dst2 - epsilon = 10", dst2)
isConvex = cv2.isContourConvex(approx)  # 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_16.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch16_17.py

src = cv2.imread("heart1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 0), 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點
# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, (0, 255, 255), 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")
# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, (255, 0, 0), 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")
# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, (0, 255, 255), 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_17_輪廓的特徵
print("------------------------------------------------------------")  # 60個

# ch17_1.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
aspectratio = w / h  # 計算寬高比
print(f"寬高比 = {aspectratio}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_2.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
print(f"資料格式 = {type(cnt)}")
print(f"資料維度 = {cnt.ndim}")
print(f"資料長度 = {len(cnt)}")
for i in range(3):  # 列印 3 個座標點
    print(cnt[i])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_3.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_4.py

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個

# ch17_5.py

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")

print("------------------------------------------------------------")  # 60個

# ch17_6.py

data = np.array([[[186, 39]], [[181, 44]], [[180, 44]]])
print(f"原始資料data = \n{data}")
n = len(data)
print("取3維內的陣列資料")
for i in range(n):  # 列印 3 個座標點
    print(data[i])
print(f"資料維度   = {data.ndim}")  # 維度
max_i = data[:, :, 0].argmax()  # x 最大值索引索引
print(f"x 最大值索引 = {max_i}")  # 列印 x 最大值索引
right = tuple(data[data[:, :, 0].argmax()][0])  # 最大值元組
print(f"最大值元組 = {right}")  # 列印最大值元組
min_i = data[:, :, 0].argmin()  # x 最小值索引索引
print(f"x 最小值索引 = {min_i}")  # 列印 x 最小值索引
left = tuple(data[data[:, :, 0].argmin()][0])  # 最小值元組
print(f"最小值元組 = {left}")  # 列印最小值元組

print("------------------------------------------------------------")  # 60個

# ch17_7.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 建立輪廓變數
left = tuple(cnt[cnt[:, :, 0].argmin()][0])  # left
right = tuple(cnt[cnt[:, :, 0].argmax()][0])  # right
top = tuple(cnt[cnt[:, :, 1].argmin()][0])  # top
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])  # bottom
print(f"最左點 = {left}")
print(f"最右點 = {right}")
print(f"最上點 = {top}")
print(f"最下點 = {bottom}")
dst = cv2.circle(src, left, 5, [0, 255, 0], -1)
dst = cv2.circle(src, right, 5, [0, 255, 0], -1)
dst = cv2.circle(src, top, 5, [0, 255, 255], -1)
dst = cv2.circle(src, bottom, 5, [0, 255, 255], -1)
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_8.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 255), 2)
cv2.imshow("dst", dst)
square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print(f"Extent = {extent}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_9.py

src = cv2.imread("explode1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, (0, 255, 255), 2)  # 將凸包連線
cv2.imshow("dst", dst)
convex_area = cv2.contourArea(hull)  # 凸包面積
solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_10.py

src = cv2.imread("star1.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, (0, 255, 0), 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
dst = cv2.circle(src, (260, 110), int(ed / 2), (0, 255, 0), 3)  # 繪製圓
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_11.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個

# ch17_12.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_13.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = np.transpose(np.nonzero(dst1))
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = np.transpose(np.nonzero(dst2))
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_14.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個

# ch17_15.py

src = cv2.imread("simple.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray, 127, 255, cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]  # 取得輪廓數據
mask1 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst1 = cv2.drawContours(mask1, [cnt], 0, 255, 1)  # 繪製空心輪廓
points1 = cv2.findNonZero(dst1)
mask2 = np.zeros(src_gray.shape, np.uint8)  # 建立畫布
dst2 = cv2.drawContours(mask2, [cnt], 0, 255, -1)  # 繪製實心輪廓
points2 = cv2.findNonZero(dst2)
print(f"空心像素點長度 = {len(points1)},   實心像素點長度 = {len(points2)}")
print("空心像素點")
print(points1)
print("實心像素點")
print(points2)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_16.py

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(256, size=(height, width))  # 建立矩陣
print(f"矩陣內容 = \n{img}")
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)
print(f"最小值 = {minVal},  位置 = {minLoc}")  # 最小值與其位置
print(f"最大值 = {maxVal},  位置 = {maxLoc}")  # 最大值與其位置

print("------------------------------------------------------------")  # 60個

# ch17_17.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask", mask)
# 在src_gray影像的mask遮罩區域找尋最大像素與最小像素值
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(src_gray, mask=mask)
print(f"最小像素值 = {minVal}")
print(f"最小像素值座標 = {minLoc}")
print(f"最大像素值 = {maxVal}")
print(f"最大像素值座標 = {maxLoc}")
cv2.circle(src, minLoc, 20, [0, 255, 0], 3)  # 最小像素值用綠色圓
cv2.circle(src, maxLoc, 20, [0, 0, 255], 3)  # 最大像素值用紅色圓
# 建立遮罩未來可以顯示此感興趣的遮罩區域
mask1 = np.zeros(src.shape, np.uint8)  # 建立遮罩
mask1 = cv2.drawContours(mask1, [cnt], -1, (255, 255, 255), -1)
cv2.imshow("mask1", mask1)
dst = cv2.bitwise_and(src, mask1)  # 顯示感興趣區域
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_18.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)

channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_19.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)

channels = cv2.mean(src)  # 計算均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_20.py

src = cv2.imread("hand.jpg")
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]
# 在src_gray影像的mask遮罩區域計算均值
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, (255, 255, 255), -1)
channels = cv2.mean(src, mask=mask)  # 計算遮罩的均值
print(channels)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch17_21.py

src = cv2.imread("forest.png")
cv2.imshow("src", src)

mean, std = cv2.meanStdDev(src)  # 計算標準差
print(f"均值   = \n{mean}")
print(f"標準差 = \n{std}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_18_從直線檢測到無人駕駛車道檢測
print("------------------------------------------------------------")  # 60個

# ch18_1.py

src = cv2.imread("calendar.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)  # 檢測直線
# 繪製直線
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
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_2.py

src = cv2.imread("lane.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 100, 200)  # 使用Canny邊緣檢測
# cv2.imshow("Canny", edges)                         # 顯示Canny邊緣線條
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)  # 檢測直線
# 繪製直線
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

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_3.py

src = cv2.imread("roadtest.jpg", cv2.IMREAD_COLOR)
cv2.imshow("src", src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 轉成灰階
edges = cv2.Canny(src_gray, 50, 200)  # 使用Canny邊緣檢測
cv2.imshow("Canny", edges)  # 顯示Canny邊緣線條
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=10, maxLineGap=100)
# 繪製檢測到的直線
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(src, (x1, y1), (x2, y2), (255, 0, 0), 3)  # 繪製藍色線條
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch18_4.py

src = cv2.imread("shapes.jpg")
cv2.imshow("src", src)

image = cv2.medianBlur(src, 5)  # 過濾雜訊

src_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉成灰階
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
# 繪製檢測到的直線
for c in circles[0]:
    x, y, r = c
    cv2.circle(src, (x, y), r, (0, 255, 0), 3)  # 綠色繪圓外圈
    cv2.circle(src, (x, y), 2, (0, 0, 255), 2)  # 紅色繪圓中心
cv2.imshow("dst", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_19_直方圖均衡化—增強影像對比度
print("------------------------------------------------------------")  # 60個

# ch19_1.py

seq = [1, 2, 3, 4, 5]  # 像素值
times = [2, 1, 2, 1, 3]  # 出現次數
plt.plot(seq, times, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 4])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_2.py

times = [2, 1, 2, 1, 3]  # 出現次數
N = len(times)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, times, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Times")  # 出現次數
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_3.py

seq = [1, 2, 3, 4, 5]  # 像素值
freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
plt.plot(seq, freq, "-o")  # 繪含標記的圖
plt.axis([0, 6, 0, 0.5])  # 建立軸大小
plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Frequency")  # 出現頻率
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_4.py

freq = [2 / 9, 1 / 9, 2 / 9, 1 / 9, 3 / 9]  # 出現頻率
N = len(freq)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, freq, width)  # 繪製長條圖

plt.xlabel("Pixel Value")  # 像素值
plt.ylabel("Freqency")  # 出現頻率
plt.xticks(x, ("1", "2", "3", "4", "5"))
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_5.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_6.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

plt.hist(src.ravel(), 20)  # 降維再繪製直方圖
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_7.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
print(f"資料內容 \n{hist}")

print("------------------------------------------------------------")  # 60個

# ch19_8.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

hist = cv2.calcHist([src], [0], None, [256], [0, 258])  # 直方圖統計資料
plt.plot(hist)  # 用plot()繪直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_9.py

src = cv2.imread("macau.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

b = cv2.calcHist([src], [0], None, [256], [0, 256])  # B 通道統計資料
g = cv2.calcHist([src], [1], None, [256], [0, 256])  # G 通道統計資料
r = cv2.calcHist([src], [2], None, [256], [0, 256])  # R 通道統計資料
plt.plot(b, color="blue", label="B channel")  # 用plot()繪 B 通道
plt.plot(g, color="green", label="G channel")  # 用plot()繪 G 通道
plt.plot(r, color="red", label="R channel")  # 用plot()繪 R 通道
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_10.py

src = np.zeros([200, 400], np.uint8)  # 建立影像
src[50:150, 100:300] = 255  # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_11.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)  # And運算
cv2.imshow("After Mask", masked)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_12.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
plt.plot(hist, color="blue", label="Src Image")  # 用plot()繪影像直方圖
plt.plot(hist_mask, color="red", label="Mask")  # 用plot()繪遮罩直方圖
plt.legend(loc="best")
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_13.py

src = cv2.imread("macau.jpg", cv2.IMREAD_GRAYSCALE)
# 建立遮罩
mask = np.zeros(src.shape[:2], np.uint8)  # 建立影像遮罩影像
mask[20:200, 50:400] = 255  # 在遮罩影像內建立遮罩
aftermask = cv2.bitwise_and(src, src, mask=mask)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 灰階統計資料
hist_mask = cv2.calcHist([src], [0], mask, [256], [0, 256])  # 遮罩統計資料
# subplot()第一個 2 是代表垂直有 2 張圖, 第二個 2 是代表左右有 2 張圖
# subplot()第三個參數是代表子圖編號
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.imshow(mask, "gray")  # 灰階顯示第2張圖
plt.subplot(223)  # 建立子圖 3
plt.imshow(aftermask, "gray")  # 灰階顯示第3張圖
plt.subplot(224)  # 建立子圖 4
plt.plot(hist, color="blue", label="Src Image")
plt.plot(hist_mask, color="red", label="Mask")
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_14.py

src = cv2.imread("snow1.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_15.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_16.py

src = cv2.imread("highway1.png", cv2.IMREAD_GRAYSCALE)
plt.subplot(221)  # 建立子圖 1
plt.imshow(src, "gray")  # 灰階顯示第1張圖
plt.subplot(222)  # 建立子圖 2
plt.hist(src.ravel(), 256)  # 降維再繪製直方圖
plt.subplot(223)  # 建立子圖 3
dst = cv2.equalizeHist(src)  # 均衡化處理
plt.imshow(dst, "gray")  # 顯示執行均衡化的結果影像
plt.subplot(224)  # 建立子圖 4
plt.hist(dst.ravel(), 256)  # 降維再繪製直方圖
plt.show()

print("------------------------------------------------------------")  # 60個

# ch19_17.py

src = cv2.imread("springfield.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

(b, g, r) = cv2.split(src)  # 拆開彩色影像通道
blue = cv2.equalizeHist(b)  # 均衡化 B 通道
green = cv2.equalizeHist(g)  # 均衡化 G 通道
red = cv2.equalizeHist(r)  # 均衡化 R 通道
dst = cv2.merge((blue, green, red))  # 合併通道
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_18.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

equ = cv2.equalizeHist(src)  # 直方圖均衡化
cv2.imshow("euualizeHist", equ)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch19_19.py

src = cv2.imread("office.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)

# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
dst = clahe.apply(src)  # 灰度影像與clahe物件關聯
cv2.imshow("CLAHE", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_20_模板匹配 Template Matching
print("------------------------------------------------------------")  # 60個

# ch20_1.py

src = cv2.imread("macau_hotel.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

H, W = src.shape[:2]
print(f"原始影像高 H = {H}, 寬 W = {W}")
temp1 = cv2.imread("head.jpg")
cv2.imshow("Temp1", temp1)  # 顯示模板影像
h, w = temp1.shape[:2]
print(f"模板影像高 h = {h}, 寬 w = {w}")
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_2.py

src = cv2.imread("shapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_3.py

src = cv2.imread("g5.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("face1.jpg", cv2.IMREAD_COLOR)
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_SQDIFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
upperleft = minLoc  # 左上角座標
lowerright = (minLoc[0] + width, minLoc[1] + height)  # 右下角座標
dst = cv2.rectangle(src, upperleft, lowerright, (0, 255, 0), 3)  # 繪置最相似外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_4.py

src = []  # 建立原始影像陣列
src1 = cv2.imread("knight0.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列
src2 = cv2.imread("knight1.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列
temp1 = cv2.imread("knight.jpg", cv2.IMREAD_COLOR)
# 使用cv2.TM_SQDIFF_NORMED執行模板匹配
minValue = 1  # 設定預設的最小值
index = -1  # 設定最小值的索引
# 採用歸一化平方匹配法
for i in range(len(src)):
    result = cv2.matchTemplate(src[i], temp1, cv2.TM_SQDIFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if minValue > minVal:
        minValue = minVal  # 紀錄目前的最小值
        index = i  # 紀錄目前的索引
seq = "knight" + str(index) + ".jpg"
print(f"{seq} 比較類似")
cv2.imshow("Dst", src[index])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_5.py

src = cv2.imread("mutishapes.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Src", src)

temp1 = cv2.imread("heart.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Temp1", temp1)  # 顯示模板影像
height, width = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(
                src, (col, row), (col + width, row + height), (0, 255, 0), 3
            )
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_6.py

src = cv2.imread("baidu.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("mountain_mark.jpg", cv2.IMREAD_COLOR)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.95:  # 值大於0.95就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (0, 0, 255), 3)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_7.py

start_x = 450  # 目前位置 x
start_y = 180  # 目前位置 y
src = cv2.imread("airport.jpg", cv2.IMREAD_COLOR)
temp1 = cv2.imread("airport_mark.jpg", cv2.IMREAD_COLOR)
dst = cv2.circle(src, (start_x, start_y), 10, (255, 0, 0), -1)
h, w = temp1.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), (255, 0, 0), 2)
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
    cv2.line(src, (start_x, start_y), (ul_x[0], ul_y[0]), (255, 0, 0), 2)
else:
    cv2.line(src, (start_x, start_y), (ul_x[1], ul_y[1]), (255, 0, 0), 2)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch20_8.py


def myMatch(image, tmp):
    """執行匹配"""
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像
temps = []
temp1 = cv2.imread("heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp1)  # 加入匹配串列temps
temp2 = cv2.imread("star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(temp2)  # 加入匹配串列temps
match = []  # 符合匹配的圖案
for t in temps:
    myMatch(src, t)  # 調用 myMatch
for img in match:
    dst = cv2.rectangle(src, (img[0]), (img[1]), (0, 255, 0), 1)  # 繪外框
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# OpenCV_21_傅立葉變換
print("------------------------------------------------------------")  # 60個

# ch21_1.py

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 時間值
water = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 水
sugar = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]  # 糖
grass = [4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0]  # 仙草
pearl = [3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]  # 黑珍珠
plt.plot(seq, water, "-o", label="水")  # 繪含標記的water折線圖
plt.plot(seq, sugar, "-x", label="糖")  # 繪含標記的sugar折線圖
plt.plot(seq, grass, "-s", label="仙草")  # 繪含標記的grass折線圖
plt.plot(seq, pearl, "-p", label="黑珍珠")  # 繪含標記的pearl折線圖
plt.legend(loc="best")
plt.axis([0, 12, 0, 5])  # 建立軸大小
plt.xlabel("時間軸")  # 時間軸
plt.ylabel("份數")  # 份數
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_10.py

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
# 執行逆傅立葉
idftshift = np.fft.ifftshift(dftshift)
tmp = cv2.idft(idftshift)
dst = cv2.magnitude(tmp[:, :, 0], tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊逆傅立葉圖
plt.imshow(dst, cmap="gray")  # 灰階顯示
plt.title("逆傅立葉影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_11.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 低通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
mask = np.zeros((rows, cols, 2), np.uint8)
mask[row - 30 : row + 30, col - 30 : col + 30] = 1  # 設定區塊為低頻率分量是1

fshift = dftshift * mask
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("低通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.imshow(src_back)  # 顯示
plt.title("低通濾波影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_2.py

copies = [1, 2, 4, 3]  # 份數
N = len(copies)
x = np.arange(N)
width = 0.35
plt.bar(x, copies, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("份數")  # 份數
plt.xticks(x, ("1", "2", "3", "4"))
plt.grid(axis="y")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_3.py

start = 0
end = 1
x = np.linspace(start, end, 500)  # x 軸區間
y = np.sin(2 * np.pi * 4 * x)  # 建立正弦曲線
plt.plot(x, y)
plt.xlabel("時間(秒)")  # 時間
plt.ylabel("振幅")  # 振幅
plt.title("正弦曲線", fontsize=16)  # 標題
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_4.py

amplitude = [0, 0, 0, 1, 0, 0, 0]
N = len(amplitude)
x = np.arange(N)
width = 0.3
plt.bar(x, amplitude, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("振幅")  # 振幅
plt.xticks(x, ("1", "2", "3", "4", "5", "6", "7"))
plt.grid(axis="y")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_5.py

start = 0
# 起始時間
end = 5
# 結束時間
# 兩個正弦波的訊號頻率
freq1 = 5
# 頻率是 5 Hz
freq2 = 8
# 頻率是 8 Hz
# 建立時間軸的Numpy陣列, 用500個點
time = np.linspace(start, end, 500)
# 建立2個正弦波
amplitude1 = np.sin(2 * np.pi * freq1 * time)
amplitude2 = np.sin(2 * np.pi * freq2 * time)
# 建立子圖
figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
# 時間域的 sin 波 1
axis[0].set_title("頻率是 5 Hz的 sin 波")
axis[0].plot(time, amplitude1)
axis[0].set_xlabel("時間")
axis[0].set_ylabel("振幅")
# 時間域的 sin 波 2
axis[1].set_title("頻率是 8 Hz的 sin 波")
axis[1].plot(time, amplitude2)
axis[1].set_xlabel("時間")
axis[1].set_ylabel("振幅")
# 加總sin波
amplitude = amplitude1 + amplitude2
axis[2].set_title("2個不同頻率正弦波的結果")
axis[2].plot(time, amplitude)
axis[2].set_xlabel("時間")
axis[2].set_ylabel("振幅")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_1.py

src = cv2.imread("shape1.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape1.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_2.py

src = cv2.imread("shape2.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像shape2.jpg")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_6_3.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(src)  # 轉成頻率域
# fshift = np.fft.fftshift(f)            # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(f))  # 轉成頻譜
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_7.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率頻率移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊逆運算圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("逆變換影像")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_8.py

src = cv2.imread("snow.jpg", cv2.IMREAD_GRAYSCALE)
# 傅立葉變換
f = np.fft.fft2(src)  # 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
# 高通濾波器
rows, cols = src.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
fshift[row - 30 : row + 30, col - 30 : col + 30] = 0  # 設定區塊為低頻率分量是0
# 逆傅立葉變換
ifshift = np.fft.ifftshift(fshift)  # 0 頻率分量移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(131)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(132)  # 繪製中間圖
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("高通濾波灰階影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(133)  # 繪製右邊圖
plt.title("高通濾波影像")
plt.imshow(src_back)  # 顯示影像
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個

# ch21_9.py

src = cv2.imread("jk.jpg", cv2.IMREAD_GRAYSCALE)
# 轉成頻率域
dft = cv2.dft(np.float32(src), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(dft)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))
plt.subplot(121)  # 繪製左邊原圖
plt.imshow(src, cmap="gray")  # 灰階顯示
plt.title("原始影像")
plt.axis("off")  # 不顯示座標軸
plt.subplot(122)  # 繪製右邊頻譜圖
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")
plt.axis("off")  # 不顯示座標軸
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_22_影像分割使用分水嶺演算法
print("------------------------------------------------------------")  # 60個

# ch22_1.py

src = cv2.imread("coin1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch22_1.py

src = cv2.imread("coin2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
ret, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow("Dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch22_2.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_2_1.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_2_2.py

src = cv2.imread("coin1.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(133)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_3.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
plt.subplot(141)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(142)
plt.title("距離變換影像")
plt.imshow(dst)
plt.axis("off")
plt.subplot(143)
plt.title("閾值化影像")
plt.imshow(sure_fg)
plt.axis("off")
plt.subplot(144)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_4.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
plt.subplot(131)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(132)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(133)
plt.title("標記區")
plt.imshow(markers)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_5.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1  # 標記修訂
markers_new[unknown == 255] = 0
plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")
plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis("off")
plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch22_6.py

src = cv2.imread("opencv_coin.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 因為在matplotlib模組顯示, 所以必須轉成 RGB 色彩
rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案
# 計算未知區域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 標記
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
# 正式執行分水嶺函數
dst = rgb_src.copy()
markers = cv2.watershed(dst, markers)
dst[markers == -1] = [255, 0, 0]  # 使用紅色
plt.subplot(121)
plt.title("原始影像")
plt.imshow(rgb_src)
plt.axis("off")
plt.subplot(122)
plt.title("分割結果")
plt.imshow(dst)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_23_影像擷取
print("------------------------------------------------------------")  # 60個

# ch23_1.py

src = cv2.imread("hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

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
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
maskpict_rgb = cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB)
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(maskpict_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_3.py

src = cv2.imread("lena.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch23_4.py

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
src_rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(121)
plt.title("原始影像")
plt.imshow(src_rgb)
plt.axis("off")
plt.subplot(122)
plt.title("擷取影像")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_24_影像修復
print("------------------------------------------------------------")  # 60個

# ch24_1.py

lisa = cv2.imread("lisaE1.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_NS)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch24_2.py

lisa = cv2.imread("lisaE2.jpg")
ret, mask = cv2.threshold(lisa, 250, 255, cv2.THRESH_BINARY)
# 遮罩處理, 適度增加要處理的表面
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
mask = cv2.dilate(mask, kernal)
dst = cv2.inpaint(lisa, mask[:, :, -1], 5, cv2.INPAINT_TELEA)
# 輸出執行結果
lisa_rgb = cv2.cvtColor(lisa, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)  # 將BGR轉RGB
plt.subplot(131)
plt.title("原始影像")
plt.imshow(lisa_rgb)
plt.axis("off")
plt.subplot(132)
plt.title("遮罩影像")
plt.imshow(mask_rgb)
plt.axis("off")
plt.subplot(133)
plt.title("影像修復結果")
plt.imshow(dst_rgb)
plt.axis("off")
plt.show()

print("------------------------------------------------------------")  # 60個
# OpenCV_25_辨識手寫數字
print("------------------------------------------------------------")  # 60個

# ch25_1.py

data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")

print("------------------------------------------------------------")  # 60個

# ch25_10.py

data = np.arange(16).reshape(2, 2, 2, 2)
print(f"data = \n {data}")
print(f"data = \n {np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_11.py

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.hsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_11_1.py

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)
print(f"After repeat = \n{x}")

print("------------------------------------------------------------")  # 60個

# ch25_11_2.py

data = np.array([[1, 2], [3, 4]])
print(f"data = \n {data}")
x1 = np.repeat(data, 3, axis=1)
print(f"After axis=1 repeat  = \n{x1}")
x2 = np.repeat(data, 3, axis=0)
print(f"After axis=0 repeat = \n{x2}")

print("------------------------------------------------------------")  # 60個

# ch25_11_3.py

data = np.arange(3)
print(f"data = \n {data}")
x = np.repeat(data, 3)[:, np.newaxis]
print(f"After repeat = \n{x}")

print("------------------------------------------------------------")  # 60個

# ch25_12.py

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")

print("------------------------------------------------------------")  # 60個

# ch25_13.py

img = cv2.imread("digits.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 將digits拆成 5000 張, 20 x 20 的數字影像
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
# 將 cells 轉成 50 x 100 x 20 x 20 的陣列
x = np.array(cells)
# 將數據轉為訓練數據 size=(2500,400)和測試數據 size=(2500,400)
train = x[:, :50].reshape(-1, 400).astype(np.float32)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)
# 建立訓練數據和測試數據的分類 labels
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]
test_labels = train_labels.copy()
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)
# 統計辨識結果
matches = result == test_labels  # 執行匹配
correct = np.count_nonzero(matches)  # 正確次數
accuracy = correct * 100.0 / result.size  # 精確度
print(f"測試數據辨識成功率 = {accuracy}")
np.savez("knn_digit.npz", train=train, train_labels=train_labels)

print("------------------------------------------------------------")  # 60個

# ch25_14.py

# 下載數據
with np.load("knn_digit.npz") as data:
    train = data["train"]
    train_labels = data["train_labels"]
# 讀取數字影像
test_img = cv2.imread("8.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img", test_img)
img = cv2.resize(test_img, (20, 20)).reshape((1, 400))
test_data = img.astype(np.float32)  # 將資料轉成foat32
# 最初化KNN或稱建立KNN物件，訓練數據、使用 k=5 測試KNN演算法
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test_data, k=5)
print(f"識別的數字是 = {int(result[0,0])}")

print("------------------------------------------------------------")  # 60個

# ch25_2.py

np.random.seed(5)
data1 = np.random.randint(0, 10, size=5)
print(f"陣列外形 = {data1.shape}")
print(f"輸出陣列 = {data1}")
print(f"data1[0] = {data1[0]}")
data2 = np.random.randint(0, 10, size=(5, 1))
print(f"矩陣外形 = {data2.shape}")
print(f"輸出矩陣 = \n{data2}")
print(f"data2[0] = {data2[0]}")
print(f"data2[0,0] = {data2[0,0]}")

print("------------------------------------------------------------")  # 60個

# ch25_3.py

data = np.random.randint(0, 10, size=(5, 1))
print(f"輸出二維陣列 = \n{data}")
print(f"轉成一維陣列 = \n{data.ravel()}")

print("------------------------------------------------------------")  # 60個

# ch25_4.py

np.random.seed(1)
trains = np.random.randint(0, 10, size=(5, 2))
print(f"列出二維陣列 \n{trains}")
np.random.seed(5)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (5, 1))
print(f"列出顏色分類陣列 \n{labels}")
# 列出 0 代表的紅色
red = trains[labels.ravel() == 0]
print(f"輸出紅色的二維陣列 \n{red}")
print(f"配對取出 \n{red[:,0], red[:,1]}")
# 列出 1 代表的藍色
blue = trains[labels.ravel() == 1]
print(f"輸出藍色的二維陣列 \n{blue}")
print(f"配對取出 \n{blue[:,0], blue[:,1]}")

print("------------------------------------------------------------")  # 60個

# ch25_5.py

num = 30  # 數據數量
np.random.seed(5)
trains = np.random.randint(0, 100, size=(num, 2))
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_6.py

num = 30  # 數據數量
np.random.seed(5)
# 建立訓練數據 train, 需轉為 32位元浮點數
trains = np.random.randint(0, 100, size=(num, 2)).astype(np.float32)
np.random.seed(1)
# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (num, 1)).astype(np.float32)
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(10)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")
plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_7.py

num = 30  # 數據數量
np.random.seed(5)
# 建立 0 - 50 間的訓練數據 train0, 需轉為 32位元浮點數
train0 = np.random.randint(0, 50, (num // 2, 2)).astype(np.float32)
# 建立 50 - 100 間的訓練數據 train1, 需轉為 32位元浮點數
train1 = np.random.randint(50, 100, (num // 2, 2)).astype(np.float32)
trains = np.vstack((train0, train1))  # 合併訓練數據
# 建立分類, 未來 0 代表 red,  1 代表 blue
label0 = np.zeros((num // 2, 1)).astype(np.float32)
label1 = np.ones((num // 2, 1)).astype(np.float32)
labels = np.vstack((label0, label1))
# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小
# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
# test 為測試數據, 需轉為 32位元浮點數
np.random.seed(8)
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:, 0], test[:, 1], 50, "g", "o")  # 50大小的綠色圓
# 建立 KNN 物件
knn = cv2.ml.KNearest_create()
knn.train(trains, cv2.ml.ROW_SAMPLE, labels)  # 訓練數據
# 執行 KNN 分類
ret, results, neighbours, dist = knn.findNearest(test, k=3)
print(f"最後分類              result = {results}")
print(f"最近鄰3個點的分類 neighbours = {neighbours}")
print(f"與最近鄰的距離      distance = {dist}")

plt.show()

print("------------------------------------------------------------")  # 60個

# ch25_8.py

data = np.arange(16).reshape(4, 4)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個

# ch25_9.py

data = np.arange(8).reshape(2, 2, 2)
print(f"data = \n {data}")
print(f"split = \n{np.vsplit(data,2)}")

print("------------------------------------------------------------")  # 60個
# OpenCV_26_OpenCV的攝影功能
print("------------------------------------------------------------")  # 60個

# ch26_1.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_10.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.namedWindow("myVideo", 0)
        cv2.resizeWindow("myVideo", 300, 200)
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_11.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
print(f"Frame 的寬度 = {width}")  # 輸出Frame 的寬度
print(f"Frame 的高度 = {height}")  # 輸出Frame 的高度
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_12.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    cv2.imshow("Frame", frame)  # 顯示影像
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬度
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
    video_fps = video.get(cv2.CAP_PROP_FPS)  # 速度
    video_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)  # 幀數
    c = cv2.waitKey(50)  # 等待時間
    if c == 27:  # 按 Esc 键
        break
print(f"Video 的寬度    = {width}")  # 輸出 Video 的寬度
print(f"Video 的高度    = {height}")  # 輸出 Video 的高度
print(f"Video 的速度    = {video_fps}")  # 輸出 Video 的速度
print(f"Video 的幀數    = {video_frames}")  # 輸出 Video 的幀數
video.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_13.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 設定寬度
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)  # 設定高度
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_14.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 影片高度
counter = 1  # 幀數計數器
font = cv2.FONT_HERSHEY_SIMPLEX  # 字型
while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        y = int(height - 50)  # Frames計數器位置
        cv2.putText(
            frame, "Frames  : " + str(counter), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示幀數
        seconds = round(counter / video_fps, 2)  # 計算秒數
        y = int(height - 10)  # Seconds計數器位置
        cv2.putText(
            frame, "Seconds : " + str(seconds), (0, y), font, 1, (255, 0, 0), 2
        )  # 顯示秒數
        cv2.imshow("myVideo", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    counter += 1  # 幀數加 1
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_15.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案
video_fps = video.get(cv2.CAP_PROP_FPS)  # 計算速度
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))  # 寬度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度
# 建立裁剪影片物件
fourcc = cv2.VideoWriter_fourcc(*"I420")  # 編碼
new_video = cv2.VideoWriter("out26_15.avi", fourcc, video_fps, (width, height))
counter = video_fps * 5  # 影片長度
while video.isOpened() and counter >= 0:
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        new_video.write(frame)  # 寫入新影片
        counter -= 1  # 幀數減 1

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_2.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像
    # 轉灰階顯示
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Frame", gray_frame)  # 顯示灰階影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_3.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示彩色影像

    h_frame = cv2.flip(frame, 1)  # 水平翻轉
    cv2.imshow("Flip Frame", h_frame)  # 顯示水平翻轉
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_4.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
while capture.isOpened():
    ret, frame = capture.read()  # 讀取設請鏡頭的影像
    cv2.imshow("Frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 13:  # 按 Enter 鍵
        cv2.imwrite("mypict.png", frame)  # 拍照
        cv2.imshow("My Picture", frame)  # 開視窗顯示
    if c == 27:  # 按 Esc 键
        break
capture.release()  # 關閉攝影功能
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_5.py

capture = cv2.VideoCapture(0)  # 初始化攝影功能
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # MPEG-4
# 建立輸出物件
video_out = cv2.VideoWriter("out26_5.avi", fourcc, 20.0, (640, 480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        video_out.write(frame)  # 寫入影片物件
        cv2.imshow("frame", frame)  # 顯示攝影鏡頭的影像
    c = cv2.waitKey(1)  # 等待時間 1 毫秒 ms
    if c == 27:  # 按 Esc 键, 結束
        break
capture.release()  # 關閉攝影功能
video_out.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_6.py

video = cv2.VideoCapture("out26_5.avi")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_7.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_8.py

video = cv2.VideoCapture("iceocean2.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret == True:
        cv2.imshow("frame", frame)  # 顯示彩色影片
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray_frame", gray_frame)  # 顯示灰階影片
    else:
        break
    c = cv2.waitKey(50)  # 可以控制撥放速度
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch26_9.py

video = cv2.VideoCapture("iceocean.mov")  # 開啟影片檔案

while video.isOpened():
    ret, frame = video.read()  # 讀取影片檔案
    if ret:
        cv2.imshow("frame", frame)  # 顯示影片
        c = cv2.waitKey(50)  # 可以控制撥放速度
    else:
        break
    if c == 32:  # 是否按 空白鍵
        cv2.waitKey()  # 等待按鍵發生
        continue
    if c == 27:  # 按 Esc 键, 結束
        break

video.release()  # 關閉輸出物件
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# OpenCV_27_物件偵測
print("------------------------------------------------------------")  # 60個

# ch27_1.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("jk.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_10.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_upperbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_11.py

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立雙眼物件
xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

face_cascade_classifier = cv2.CascadeClassifier(pictPath1)  # 建立人臉物件
img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測人臉
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 偵測雙眼
face_cascade_classifier2 = cv2.CascadeClassifier(pictPath2)
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_12.py

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立雙眼物件
xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測雙眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將雙眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_13.py

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立左眼物件
xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_lefteye_2splits.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測左眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將左眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_14.py

# 建立人臉物件
xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier1 = cv2.CascadeClassifier(xml_filename1)  # 建立辨識檔案物件

# 建立右眼物件
xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_righteye_2splits.xml"
face_cascade_classifier2 = cv2.CascadeClassifier(xml_filename2)  # 建立辨識檔案物件

img = cv2.imread("jk.jpg")  # 讀取影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade_classifier1.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測右眼
eyes = face_cascade_classifier2.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

# 將右眼框起來, 由於有可能找到好幾個眼睛所以用迴圈繪出來
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 綠色框住眼睛

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_15.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalcatface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("cat1.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將貓臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住貓臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_16.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalcatface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("cat2.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_17.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_18.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car1.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_19.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_russian_plate_number.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("car2.jpg")  # 讀取影像
plates = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將車牌框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住車牌

cv2.imshow("Car Plate", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_2.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("g5.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_3.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_3_1.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

# ch27_4.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_4_1.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_5.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt_tree.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("solvay1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6_1.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.02, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_6_2.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_profileface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("s_1927.jpg")  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_7.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_fullbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_8.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_fullbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people2.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch27_9.py

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_lowerbody.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("people1.jpg")  # 讀取影像
bodies = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 標註身體
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住身體

cv2.imshow("Body", img)  # 顯示影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
