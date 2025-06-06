"""

findContours

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.findContours ST
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
# contours, hierarchy = cv2.findContours(dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

dst = cv2.drawContours(src, contours, -1, GREEN, 5)  # 繪製圖形輪廓

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("lake.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 150  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

#外輪廓
dst = cv2.drawContours(src, contours, -1, GREEN, 2)  # 繪製圖形輪廓

#填滿輪廓
# dst = cv2.drawContours(src, contours, -1, GREEN, -1)  # 繪製圖形輪廓

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("lake.jpg")

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(222)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
mask = np.zeros(src.shape, np.uint8)
dst = cv2.drawContours(mask, contours, -1, WHITE, -1)  # 繪製圖形輪廓

plt.subplot(223)
plt.title("繪製圖形輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

dst_result = cv2.bitwise_and(src, mask)

plt.subplot(224)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst_result, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy2.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
"""
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
"""
dst = cv2.drawContours(src, contours, -1, GREEN, 5)  # 繪製圖形輪廓
print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

plt.subplot(313)
plt.title("繪製圖形輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy3.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
)
"""
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
"""
dst = cv2.drawContours(src, contours, -1, GREEN, 3)  # 繪製圖形輪廓

print(f"hierarchy 資料類型 : {type(hierarchy)}")
print(f"列印層級 \n {hierarchy}")

plt.subplot(313)
plt.title("繪製圖形輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

print("資料類型 :", type(contours))
print("輪廓數量 :", len(contours))

# 一次把全部輪廓都畫完 (參數 -1)
# dst = cv2.drawContours(src, contours, -1, GREEN, 5)  # 繪製圖形輪廓

# 依序畫每個輪廓
n = len(contours)  # 回傳輪廓數

for i in range(n):  # 輸出輪廓的屬性
    print(f"編號 = {i}")
    print(f"輪廓點的數量 = {len(contours[i])}")
    print(f"輪廓點的外形 = {contours[i].shape}")

print(contours[1])  # 列印編號1的輪廓點

dst = np.ones(src.shape, dtype=np.uint8) * 100

n = len(contours)  # 回傳輪廓數
for i in range(n):  # 依次繪製輪廓
    img = np.zeros(src.shape, np.uint8)  # 建立輪廓影像
    img = np.ones(src.shape, dtype=np.uint8) * 127
    # 依序畫每個輪廓 (參數 i)
    print('第', i+1, '個輪廓')
    dst = cv2.drawContours(dst, contours, i, colors[i], 5)

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

for i in range(n):  # 列印輪廓面積
    area = cv2.moments(contours[i])
    print(f"輪廓面積 str(i) = {area['m00']}")
""" many
for i in range(n):  # 列印影像矩
    M = cv2.moments(contours[i])
    print(f"列印影像矩 {str(i)} \n {M}")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, GREEN, 5)  # 繪製圖形輪廓

for c in contours:  # 繪製中心點迴圈
    M = cv2.moments(c)  # 影像矩
    Cx = int(M["m10"] / M["m00"])  # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])  # 質心 y 座標
    cv2.circle(dst, (Cx, Cy), 5, BLUE, -1)  # 繪製中心點

plt.subplot(313)
plt.title("繪製圖形輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

print("輪廓數量 :", len(contours))
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.contourArea(contours[i])  # 計算輪廓面積
    print(f"輪廓 {i} 面積 = {area}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("easy.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

print("輪廓數量 :", len(contours))
n = len(contours)
for i in range(n):  # 繪製中心點迴圈
    M = cv2.moments(contours[i])  # 影像矩
    area = cv2.arcLength(contours[i], True)  # 計算輪廓周長
    print(f"輪廓 {i} 周長 = {area}")

show()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart.jpg")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
M = cv2.moments(src_gray)  # 影像矩
nu20 = M["nu20"]
print(f"歸一化中心矩 nu20 = {nu20}")
nu02 = M["nu02"]
print(f"歸一化中心矩 nu02 = {nu02}")

Hu = cv2.HuMoments(M)  # Hu矩
print(f"Hu \n {Hu}")  # 列印Hu矩

result = Hu[0][0] - (nu20 + nu02)  # 驗證Hu矩 0, h0
print(f"驗證結果 h0 - nu20 - nu02 = {result}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("3heart.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("3shapes.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

M0 = cv2.moments(contours[0])  # 計算編號 0 影像矩
M1 = cv2.moments(contours[1])  # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])  # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)  # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)  # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)  # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

show()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("myheart.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

match0 = cv2.matchShapes(contours[0], contours[0], 1, 0)  # 輪廓0和0比較
print(f"輪廓0和0比較 = {match0}")

match1 = cv2.matchShapes(contours[0], contours[1], 1, 0)  # 輪廓0和1比較
print(f"輪廓0和1比較 = {match1}")

match2 = cv2.matchShapes(contours[0], contours[2], 1, 0)  # 輪廓0和2比較
print(f"輪廓0和2比較 = {match2}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")

plt.subplot(311)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]

# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")

plt.subplot(312)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]

# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")

plt.subplot(313)
plt.title("原圖3")
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
sd = cv2.createShapeContextDistanceExtractor()  # 建立形狀場景運算子
match0 = sd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")

match1 = sd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")

match2 = sd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")

plt.subplot(311)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(src1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src1_gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray, 127, 255, cv2.THRESH_BINARY)

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt1 = contours[0]

# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")

plt.subplot(312)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt2 = contours[0]

# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")

plt.subplot(313)
plt.title("原圖3")
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src3_gray = cv2.cvtColor(src3, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
cnt3 = contours[0]
hd = cv2.createHausdorffDistanceExtractor()  # 建立Hausdorff
match0 = hd.computeDistance(cnt1, cnt1)  # 影像1和1比較
print(f"影像1和1比較 = {match0}")

match1 = hd.computeDistance(cnt1, cnt2)  # 影像1和2比較
print(f"影像1和2比較 = {match1}")

match2 = hd.computeDistance(cnt1, cnt3)  # 影像1和3比較
print(f"影像1和3比較 = {match2}")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# OpenCV_16_輪廓擬合與凸包的相關應用
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(313)
plt.title("建構矩形")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode2.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(313)
plt.title("建構矩形")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode2.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

box = cv2.minAreaRect(contours[0])  # 建構最小矩形
print(f"轉換前的矩形頂角 = \n {box}")
points = cv2.boxPoints(box)  # 獲取頂點座標
points = np.int0(points)  # 轉為整數
print(f"轉換後的矩形頂角 = \n {points}")
dst = cv2.drawContours(src, [points], 0, GREEN, 2)  # 繪製輪廓


plt.subplot(313)
plt.title("繪製輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode3.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, YELLOW, 2)  # 繪圓

plt.subplot(313)
plt.title("圓圈框選")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 取得圓中心座標和圓半徑
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))  # 圓中心座標取整數
radius = int(radius)  # 圓半徑取整數
dst = cv2.circle(src, center, radius, YELLOW, 2)  # 繪圓

plt.subplot(313)
plt.title("圓圈框選")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("cloud.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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
dst = cv2.ellipse(src, ellipse, GREEN, 2)  # 繪橢圓

plt.subplot(313)
plt.title("最優擬合橢圓框選")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[1][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[1][0]), tuple(triangle[2][0]), GREEN, 2)
dst = cv2.line(src, tuple(triangle[0][0]), tuple(triangle[2][0]), GREEN, 2)

plt.subplot(313)
plt.title("三角形框選")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("multiple.jpg")

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(222)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 近似多邊形包圍
print("輪廓數量 :", len(contours))
n = len(contours)  # 輪廓數量
src1 = src.copy()  # 複製src影像
src2 = src.copy()  # 複製src影像
for i in range(n):
    approx = cv2.approxPolyDP(contours[i], 3, True)  # epsilon=3
    dst1 = cv2.polylines(src1, [approx], True, GREEN, 2)  # dst1
    approx = cv2.approxPolyDP(contours[i], 15, True)  # epsilon=15
    dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # dst2

plt.subplot(223)
plt.title("多邊形框選 3") # epsilon = 3
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(224)
plt.title("多邊形框選 15") # epsilon = 15
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("unregular.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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
dst = cv2.line(src, (0, lefty), (cols - 1, righty), GREEN, 2)  # 左到右繪線

plt.subplot(313)
plt.title("擬合一條線")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(313)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("hand1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(313)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("hand1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(313)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

convex_area = cv2.contourArea(hull)  # 凸包面積
print(f"凸包面積 = {convex_area}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("hand2.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
print("輪廓數量 :", len(contours))
n = len(contours)  # 輪廓數量
for i in range(n):
    hull = cv2.convexHull(contours[i])  # 獲得凸包頂點座標
    dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線

plt.subplot(313)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("star.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


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

plt.subplot(313)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart1.jpg")

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(222)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
src1 = src.copy()  # 複製src影像
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst1 = cv2.polylines(src1, [hull], True, GREEN, 2)  # 將凸包連線
isConvex = cv2.isContourConvex(hull)  # 是否凸形
print(f"凸包是凸形       = {isConvex}")

plt.subplot(223)
plt.title("凸包")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 近似多邊形包圍
src2 = src.copy()  # 複製src影像
approx = cv2.approxPolyDP(contours[0], 10, True)  # epsilon=10
dst2 = cv2.polylines(src2, [approx], True, GREEN, 2)  # 近似多邊形連線
isConvex = cv2.isContourConvex(approx)  # 是否凸形
print(f"近似多邊形是凸形 = {isConvex}")

plt.subplot(224)
plt.title("近似多邊形包圍") # epsilon = 10
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, True)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(313)
plt.title("點在凸包外")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("heart1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, GREEN, 2)  # 將凸包連線
# print(hull)   可以用這個指令了解凸包座標點

# 點在凸包線上
pointa = (231, 85)  # 點在凸包線上
dist_a = cv2.pointPolygonTest(hull, pointa, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_a = (236, 95)  # 文字輸出位置
dst = cv2.circle(src, pointa, 3, [0, 0, 255], -1)  # 用圓標記點 A
cv2.putText(dst, "A", pos_a, font, 1, YELLOW, 2)  # 輸出文字 A
print(f"dist_a = {dist_a}")

# 點在凸包內
pointb = (150, 100)  # 點在凸包線上
dist_b = cv2.pointPolygonTest(hull, pointb, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_b = (160, 110)  # 文字輸出位置
dst = cv2.circle(src, pointb, 3, [0, 0, 255], -1)  # 用圓標記點 B
cv2.putText(dst, "B", pos_b, font, 1, BLUE, 2)  # 輸出文字 B
print(f"dist_b = {dist_b}")

# 點在凸包外
pointc = (80, 85)  # 點在凸包線上
dist_c = cv2.pointPolygonTest(hull, pointc, False)  # 檢測距離
font = cv2.FONT_HERSHEY_SIMPLEX
pos_c = (50, 95)  # 文字輸出位置
dst = cv2.circle(src, pointc, 3, [0, 0, 255], -1)  # 用圓標記點 C
cv2.putText(dst, "C", pos_c, font, 1, YELLOW, 2)  # 輸出文字 C
print(f"dist_c = {dist_c}")

plt.subplot(313)
plt.title("點在凸包外")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
# OpenCV_17_輪廓的特徵
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)

x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

aspectratio = w / h  # 計算寬高比
print(f"寬高比 = {aspectratio}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = np.argmax(data)
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = np.argmin(data)
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([3, 9, 8, 5, 2])
print(f"data = {data}")
max_i = data.argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i]}")
min_i = data.argmin()
print(f"最小值索引 = {min_i}")
print(f"最小值     = {data[min_i]}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = np.array([[3, 9], [8, 2], [5, 3]])
print(f"data = {data}")
max_i = data[:, 0].argmax()
print(f"最大值索引 = {max_i}")
print(f"最大值     = {data[max_i][0]}")
print(f"對應值     = {data[max_i][1]}")
max_val = tuple(data[data[:, 0].argmax()])
print(f"最大值配對 = {max_val}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, GREEN, 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
x, y, w, h = cv2.boundingRect(contours[0])  # 建構矩形
dst = cv2.rectangle(src, (x, y), (x + w, y + h), YELLOW, 2)

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

square_area = w * h  # 計算矩形面積
extent = con_area / square_area  # 計算Extent
print(f"Extent = {extent}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("explode1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, GREEN, 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
# 凸包
hull = cv2.convexHull(contours[0])  # 獲得凸包頂點座標
dst = cv2.polylines(src, [hull], True, YELLOW, 2)  # 將凸包連線

plt.subplot(313)
plt.title("找尋影像內的輪廓")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

convex_area = cv2.contourArea(hull)  # 凸包面積
solidity = con_area / convex_area  # 計算solidity
print(f"Solidity = {solidity}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("star1.jpg")

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(312)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(
    dst_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
)
dst = cv2.drawContours(src, contours, -1, GREEN, 3)  # 繪製輪廓
con_area = cv2.contourArea(contours[0])  # 輪廓面積
ed = np.sqrt(4 * con_area / np.pi)  # 計算等效面積
print(f"等效面積 = {ed}")
dst = cv2.circle(src, (260, 110), int(ed / 2), GREEN, 3)  # 繪製圓

plt.subplot(313)
plt.title("等效面積")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")

nonzero_img = np.nonzero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{nonzero_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度
img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")
nonzero_img = np.nonzero(img)  # 獲得非0元素座標
loc_img = np.transpose(nonzero_img)  # 執行矩陣轉置
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("simple.jpg")

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(222)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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

plt.subplot(223)
plt.title("空心像素點")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(224)
plt.title("實心像素點")
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

height = 3  # 矩陣高度
width = 5  # 矩陣寬度

img = np.random.randint(2, size=(height, width))  # 建立0, 1矩陣
print(f"矩陣內容 = \n{img}")

loc_img = cv2.findNonZero(img)  # 獲得非0元素座標
print(f"非0元素的座標 \n{loc_img}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("simple.jpg")

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 影像轉成灰階

# 二值化處理影像
thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, dst_binary = cv2.threshold(src_gray, thresh, maxval, cv2.THRESH_BINARY)

plt.subplot(222)
plt.title("二值化")
plt.imshow(cv2.cvtColor(dst_binary, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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

plt.subplot(223)
plt.title("空心像素點")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

plt.subplot(224)
plt.title("實心像素點")
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("hand.jpg")  # 手上有一黑點與一白點

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]

# 製作mask
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, WHITE, -1)

plt.subplot(222)
plt.title("mask")
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

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
mask1 = cv2.drawContours(mask1, [cnt], -1, WHITE, -1)

plt.subplot(223)
plt.title("mask1")
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

dst = cv2.bitwise_and(src, mask1)  # 顯示感興趣區域

plt.subplot(224)
plt.title("顯示感興趣區域")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("hand.jpg")  # 手上有一黑點與一白點

plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.axis("off")


src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(src_gray, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
cnt = contours[0]

# 在src_gray影像的mask遮罩區域計算均值
# 製作mask
mask = np.zeros(src_gray.shape, np.uint8)  # 建立遮罩
mask = cv2.drawContours(mask, [cnt], -1, WHITE, -1)

channels = cv2.mean(src, mask=mask)  # 計算遮罩的均值
print(channels)

show()

print("------------------------------------------------------------")  # 60個
# cv2.findContours SP
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


