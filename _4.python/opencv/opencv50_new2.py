"""
opencv 集合 新進


"""

import cv2

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

# [OpenCV][Python]印出圖像中文字的位置及高寬
# 本文將說明如何去辨識出圖片文字​位置及高寬。


def read_posion(img):
    # 輸入背景黑色，物件白色的圖
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
    components = []
    # boxes_data = []
    for i in range(1, num_labels):  # 跳過背景
        x, y, w, h, _ = stats[i]
        components.append((x, y, w, h))

    components.sort(key=lambda c: c[0])  # 按 x 座標排序

    # 合併 x 軸在正負5範圍內的OCR
    merged_components = []
    current_component = list(components[0])

    for i in range(1, len(components)):
        if abs(components[i][0] - current_component[0]) <= 5:
            current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
            current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
            current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
            current_component[3] = (
                abs(components[i][1] - current_component[1]) + components[i][3]
            )  # h 取 Y2 - Y1 + H2
        else:
            merged_components.append(tuple(current_component[:4]))
            current_component = list(components[i][:4])

    # 合併最後一個OCR結果
    merged_components.append(tuple(current_component[:4]))

    return merged_components


filename = "data/captcha.png"

img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
box = read_posion(gray_img)

for i, data in enumerate(box):
    x, y, h, w = data
    # 印出OCR 位置，高寬
    print(f"第{i}個OCR，x:{x},y:{y},h:{h},w:{w}")


"""
函式詳細說明
函式定義和參數:
read_posion(img) 函式接受一個參數
img：輸入的二值化圖像，背景是黑色，物件是白色。
計算連通域:
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
使用 OpenCV 的 connectedComponentsWithStats 函數計算連通域
num_labels：連通域的數量。
labels：標籤圖，每個連通域有一個唯一的標籤。
stats：每個連通域的統計資料（x, y, w, h, area）。
_:忽略的中心點資料。
提取連通域並存入列表:
components = []
for i in range(1, num_labels):  # 跳過背景
    x, y, w, h, _ = stats[i]
    components.append((x, y, w, h))
遍歷 stats，跳過背景，提取每個連通域的位置信息和尺寸，存入 components 列表。
按 x 座標排序:
components.sort(key=lambda c: c[0])
將 components 按 x 座標進行排序。
合併相鄰的連通域:
merged_components = []
current_component = list(components[0])

for i in range(1, len(components)):
    if abs(components[i][0] - current_component[0]) <= 5:
        current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
        current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
        current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
        current_component[3] = abs(components[i][1] - current_component[1]) + components[i][3]  # h 取 Y2 - Y1 + H2
    else:
        merged_components.append(tuple(current_component[:4]))
        current_component = list(components[i][:4])

merged_components.append(tuple(current_component[:4]))
初始化 merged_components 列表和 current_component。
遍歷 components 列表，如果當前組件與前一組件的 x 座標差值在正負5範圍內，則合併它們。
合併後的結果存入 merged_components。
返回合併後的元件資訊:
return merged_components
返回合併後的元件資訊，這些資訊包括每個連通域的 x, y, w, h（左上角座標和寬高）。
"""
print("------------------------------------------------------------")  # 60個

# OpenCV如何讀取特定時間區段？

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

# 影片捕捉物件
cap = cv2.VideoCapture(video_filename)
fps = cap.get(cv2.CAP_PROP_FPS)

# 設定開始時間(秒)
start_time_sec = 3
start_frame = int(start_time_sec * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# 設定結束時間(秒)
end_time_sec = 15
end_frame = int(end_time_sec * fps)

# 如果還沒處理到結束的frame位置則...
while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
    ret, frame = cap.read()

    if not ret:
        break  # 當所有幀都被讀取完畢時退出循環

    # 在這裡處理每一幀的操作，例如顯示視頻，保存幀等
    # print('a', end = ' ')

# 釋放資源
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# [Python]使用NumPy 進行影像黑白反轉

import cv2
import numpy as np

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 讀取影像（灰階模式）
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 黑白反轉
inverted_image = 255 - image

# 顯示原影像和反轉後的影像
cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
