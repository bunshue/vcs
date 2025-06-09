"""
#GaussianBlur

#Canny

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


RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]


def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階處理
    blur = cv2.GaussianBlur(gray, (13, 13), 0)  # 高斯模糊
    canny = cv2.Canny(blur, 50, 150)  # 邊緣偵測
    return canny


def get_roi(img):
    mask = np.zeros_like(img)  # 全黑遮罩
    points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊形座標
    cv2.fillPoly(mask, points, 255)  # 多邊三角形
    roi = cv2.bitwise_and(img, mask)
    return roi


def draw_lines(img, lines):  # 建立自訂函式
    for line in lines:
        points = line.reshape(
            4,
        )  # 降成一維 shape = (4,)
        x1, y1, x2, y2 = points  # 取出直線座標
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)  # 繪製直線
    return img  # 回傳繪製直線後的影像


def get_avglines(lines):
    if lines is None:  # 如果有找到線段
        print("偵測不到直線線段")
        return None
    # -----↓先依斜率分到左組或右組↓
    lefts = []
    rights = []
    for line in lines:
        points = line.reshape(
            4,
        )
        x1, y1, x2, y2 = points
        slope, b = np.polyfit((x1, x2), (y1, y2), 1)  # y = slope*x + b
        # print(f'y = {slope} x + {b}')  #若有需要可將斜率與截距印出
        if slope > 0:  # 斜率 > 0, 右邊的直線函數
            rights.append([slope, b])  # 以 list 存入
        else:  # 斜率 < 0, 左邊的直線函數
            lefts.append([slope, b])  # 以 list 存入

    # -----↓再計算左組與右組的平圴線↓
    if rights and lefts:  # 必須同時有左右兩邊的直線函數
        right_avg = np.average(rights, axis=0)  # 取得右邊的平均直線
        left_avg = np.average(lefts, axis=0)  # 取得左邊的平均直線
        return np.array([right_avg, left_avg])
    else:
        print("無法同時偵測到左右邊緣")
        return None


def get_sublines(img, avglines):
    sublines = []  # 用於儲存線段座標
    for line in avglines:  # 一一取出所有直線函數
        slope, b = line  # y = slope*x + b
        y1 = img.shape[0]  # 影像高度 (即影像的最底部位
        y2 = int(y1 * (3 / 5))  # 取影像高度的 3/5 位置為線段
        x1 = int((y1 - b) / slope)  # x = (y-b/m), 取得線段 x 座標
        x2 = int((y2 - b) / slope)
        sublines.append([x1, y1, x2, y2])  # 座標存入串列中
    return np.array(sublines)  # 將串列轉為陣列回傳


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "road.jpg"

print("------------------------------------------------------------")  # 60個

# 彩色讀取
img = cv2.imread(filename)  # 讀取圖片

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (3, 3), 0)

plt.figure(figsize=(12, 8))
plt.subplot(311)
plt.title("原圖")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(312)
plt.title("灰階")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(313)
plt.title("高斯模糊")
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

cv2.imshow("Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(edge, cv2.COLOR_BGR2RGB))
plt.title("顯示邊緣圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

edge = get_edge(img)  # Canny邊緣檢測

mask = np.zeros_like(edge)  # 全黑遮罩
points = np.array([[[146, 539], [781, 539], [515, 417], [296, 397]]])  # 建立多邊座標
cv2.fillPoly(mask, points, 255)  # 繪製三角形
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("顯示mask圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.title("顯示ROI圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
print(lines)
if lines is not None:  # 如果有找到線段
    img = draw_lines(img, lines)  # 在原圖繪製線段
else:
    print("偵測不到直線線段")
cv2.imshow("Line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("顯示直線線段圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 讀取圖片

edge = get_edge(img)  # Canny邊緣檢測

roi = get_roi(edge)  # 取得 ROI

lines = cv2.HoughLinesP(
    image=roi,  # Hough 轉換取得線段座標陣列
    rho=3,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=40,
    maxLineGap=50,
)
avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
if avglines is not None:
    lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
    img = draw_lines(img, lines)  # 畫出線段
    cv2.imshow("Line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("顯示直線圖")
    show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

video_filename = (
    "C:/_git/__大檔與暫存區/GRENZEL 雲創 E3W WiFi 行車記錄器 1080 30fps 日間測試 高速公路 - Mobile01.mp4"
)
video_filename = "C:/_git/__大檔與暫存區/DOD行車記錄器-LS300W 日間高速公路實拍.mp4"
video_filename = "C:/_git/__大檔與暫存區/響尾蛇行車記錄器高解析度1080P - 高速公路白天行駛記錄 -.mp4"
video_filename = "road.mp4"

capture = cv2.VideoCapture(video_filename)  # 建立 VideoCapture 物件
if capture.isOpened():
    while True:
        sucess, img = capture.read()  # 讀取影像
        if sucess:
            edge = get_edge(img)  # 邊緣偵測
            roi = get_roi(edge)  # 取得 ROI
            lines = cv2.HoughLinesP(
                image=roi,  # Hough 轉換
                rho=3,
                theta=np.pi / 180,
                threshold=30,
                minLineLength=50,
                maxLineGap=40,
            )
            avglines = get_avglines(lines)  # 取得左右 2 條平均線方程式
            if avglines is not None:
                lines = get_sublines(img, avglines)  # 取得要畫出的左右 2 條線段
                img = draw_lines(img, lines)  # 畫出線段
            cv2.imshow("Frame", img)  # 顯示影像
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ord("q") or k == ord("Q"):  # 按下 Q(q) 結束迴圈
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break
else:
    print("開啟攝影機失敗")


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
