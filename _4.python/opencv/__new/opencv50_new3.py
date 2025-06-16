"""
opencv 集合 新進3

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
#Character_recognition.py

img = cv2.imread("data_new/37.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)  # 膨胀

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, 1, 5)
ret, sure_fg = cv2.threshold(
    dist_transform, 0.2 * dist_transform.max(), 255, 0
)  # 参数改小了，出现不确定区域

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)  # 减去前景

cv2.imshow("p", sure_fg)

plt.subplot(221)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(221)
plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(223)
plt.imshow(cv2.cvtColor(opening, cv2.COLOR_BGR2RGB))
plt.title("")

plt.subplot(224)
plt.imshow(cv2.cvtColor(sure_fg, cv2.COLOR_BGR2RGB))
plt.title("")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

"""
print("------------------------------------------------------------")  # 60個
# cv2.grabCut 影像擷取 ST
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

src = cv2.imread("../data2b/hung.jpg")  # 讀取影像
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
# cv2.grabCut 影像擷取 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 全景圖 ST
print("------------------------------------------------------------")  # 60個

"""
filename1 = 'C:/_git/vcs/_4.python/_data/penguin3.jpg'
filename2 = 'C:/_git/vcs/_4.python/_data/penguin4.jpg'
output_filename = 'tmp_penguin_all.jpg'
filenames = [filename1, filename2]
"""

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF2.jpg"
filename3 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF3.jpg"
filename4 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF4.jpg"
filename5 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF5.jpg"
filename6 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF6.jpg"
filename7 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF7.jpg"
filename8 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/SF8.jpg"
output_filename = "tmp_SF_all.jpg"
filenames = [
    filename1,
    filename2,
    filename3,
    filename4,
    filename5,
    filename6,
    filename7,
    filename8,
]

img_arr = []
for filename in filenames:
    image = cv2.imread(filename)
    img_arr.append(image)

stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(img_arr)
if status == cv2.Stitcher_OK:
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", pano)
    cv2.imwrite(output_filename, pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("done")
else:
    print("error: {}".format(status))

print("------------------------------------------------------------")  # 60個
# 全景圖 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.selectROI ST
print("------------------------------------------------------------")  # 60個

print("OpenCV selectROI 之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

roi = cv2.selectROI("image", image)
print("選取區域 :", roi)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.selectROI SP
print("------------------------------------------------------------")  # 60個

"""
print("------------------------------------------------------------")  # 60個
# Two Frames ST
print("------------------------------------------------------------")  # 60個

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# cap = cv2.VideoCapture(video_filename)  # 開啟影片
cap = cv2.VideoCapture("video.avi")  # 開啟影片

W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
length = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

print("W :", W)
print("H :", H)
print("frames :", frames)
print("fps :", fps)
print("length :", length)

if not cap.isOpened():
    print("開啟影片失敗")
    sys.exit()

frameNum = 0

while True:
    # 获取一帧
    ret, frame = cap.read()  # 從影片擷取一張影像
    frameNum += 1
    if ret == True:
        frame = cv2.resize(frame, (W // 3, H // 3))
        tempframe = frame
        if frameNum == 1:  # 第1張圖
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)

        if frameNum >= 2:  # 第2張圖以後
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            currentframe = cv2.absdiff(currentframe, previousframe)
            median = cv2.medianBlur(currentframe, 3)
            ret, threshold_frame = cv2.threshold(
                currentframe, 20, 255, cv2.THRESH_BINARY
            )
            gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)  # 執行高斯模糊化

            cv2.imshow("Original", frame)
            cv2.imshow("Frame", currentframe)
            cv2.imshow("medianBlur", median)

            # 按键盘上的Q键退出
            if cv2.waitKey(33) & 0xFF == ord("q"):
                break
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
    else:
        print("播放結束")
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# Two Frames SP
print("------------------------------------------------------------")  # 60個
"""

"""
#GaussianBlur

#Canny

"""

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
# cv2.inpaint 影像修復 ST
print("------------------------------------------------------------")  # 60個

# 修復影像 inpaint

lisa = cv2.imread("data_new/lisaE1.jpg")
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
print("------------------------------------------------------------")  # 60個

lisa = cv2.imread("data_new/lisaE2.jpg")
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
# cv2.inpaint 影像修復 SP
print("------------------------------------------------------------")  # 60個
'''


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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




print("------------------------------------------------------------")  # 60個

