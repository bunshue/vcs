"""
模板匹配 Template Matching
matchTemplate
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

filename1 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46.jpg"
filename2 = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates46_head.jpg"

src = cv2.imread(filename1, cv2.IMREAD_COLOR)

plt.subplot(311)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
# plt.axis("off")

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
# plt.axis("off")

plt.subplot(313)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = []  # 建立原始影像陣列

src1 = cv2.imread("data/matchTemplate/tennis1.jpg", cv2.IMREAD_COLOR)
src.append(src1)  # 加入原始影像串列

src2 = cv2.imread("data/matchTemplate/tennis2.jpg", cv2.IMREAD_COLOR)
src.append(src2)  # 加入原始影像串列

src3 = cv2.imread("data/matchTemplate/tennis3.jpg", cv2.IMREAD_COLOR)
src.append(src3)  # 加入原始影像串列

template = cv2.imread("data/matchTemplate/tennis0.jpg", cv2.IMREAD_COLOR)

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
# plt.axis("off")

plt.subplot(222)
plt.imshow(cv2.cvtColor(src2, cv2.COLOR_BGR2RGB))
plt.title("src2")
# plt.axis("off")

plt.subplot(223)
plt.imshow(cv2.cvtColor(src3, cv2.COLOR_BGR2RGB))
plt.title("src3")
# plt.axis("off")

plt.subplot(224)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/Angry-Birds01.jpg"
)
filename_small = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"

src = cv2.imread(filename_big, cv2.IMREAD_COLOR)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("src")
# plt.axis("off")

template = cv2.imread(filename_small, cv2.IMREAD_COLOR)

height, width = template.shape[:2]  # 獲得模板影像的高與寬

# 使用 cv2.TM_CCOEFF_NORMED 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.85:  # 值大於0.95就算找到了
            dst = cv2.rectangle(src, (col, row), (col + width, row + height), RED, 3)

plt.subplot(132)
plt.imshow(cv2.cvtColor(template, cv2.COLOR_BGR2RGB))
plt.title("template")
# plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")
# plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename_big = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/Angry-Birds01.jpg"
)
filename_small = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg"


def myMatch(image, tmp):
    # 執行匹配
    h, w = tmp.shape[0:2]  # 回傳height, width
    result = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    for row in range(len(result)):  # 找尋row
        for col in range(len(result[row])):  # 找尋column
            if result[row][col] > 0.95:  # 值大於0.95就算找到了
                match.append([(col, row), (col + w, row + h)])  # 左上與右下點加入串列
    return


src = cv2.imread("data/matchTemplate/mutishapes1.jpg", cv2.IMREAD_COLOR)  # 讀取原始影像

temps = []
template = cv2.imread("data/matchTemplate/heart1.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
temps.append(template)  # 加入匹配串列temps

temp2 = cv2.imread("data/matchTemplate/star.jpg", cv2.IMREAD_COLOR)  # 讀取匹配影像
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
print("------------------------------------------------------------")  # 60個

filename_big = "data/matchTemplate/tmrt_map.jpg"
filename_small = "data/matchTemplate/tmrt_logo1.jpg"

start_x = 1250  # 目前位置 x
start_y = 560  # 目前位置 y
src = cv2.imread(filename_big, cv2.IMREAD_COLOR)

template = cv2.imread(filename_small, cv2.IMREAD_COLOR)

dst = cv2.circle(src, (start_x, start_y), 10, BLUE, -1)  # 實心圓

h, w = template.shape[:2]  # 獲得模板影像的高與寬
# 使用cv2.TM_CCOEFF_NORMED執行模板匹配
ul_x = []  # 最佳匹配左上角串列 x
ul_y = []  # 最佳匹配左上較串列 y
result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
for row in range(len(result)):  # 找尋row
    for col in range(len(result[row])):  # 找尋column
        if result[row][col] > 0.9:  # 值大於0.9就算找到了
            dst = cv2.rectangle(src, (col, row), (col + w, row + h), RED, 2)  # 空心長方形
            ul_x.append(col)  # 加入最佳匹配串列 x
            ul_y.append(row)  # 加入最佳匹配串列 y

print("共找到 :", len(ul_x), "個捷運站")

length = len(ul_x)
for i in range(length):
    sub_x = start_x - ul_x[i]  # 計算 x 座標差距
    sub_y = start_y - ul_y[i]  # 計算 y 座標差距
    distance = math.hypot(sub_x, sub_y)  # 計算距離
    print(f"目前位置到此捷運站的距離 = {distance:8.2f}")
    cv2.line(src, (start_x, start_y), (ul_x[i], ul_y[i]), colors[i], 2)

plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("附近的捷運站")
plt.axis("off")

show()

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
