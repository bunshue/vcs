"""
opencv 集合 新進

"""

import cv2

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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
'''
print("goodFeaturesToTrack 角點檢測")

filename = "C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png"

img = cv2.imread(filename)
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print(len(corners))

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


# 未知其用途 goodFeaturesToTrack


def getkpoints(imag, input1):
    mask1 = np.zeros_like(input1)
    x = 0
    y = 0
    w1, h1 = input1.shape
    input1 = input1[0:w1, 200:h1]
    try:
        w, h = imag.shape
    except:
        return None
    mask1[y : y + h, x : x + w] = 255  # 整张图片像素
    keypoints = []
    kp = cv2.goodFeaturesToTrack(input1, 200, 0.04, 7)
    if kp is not None and len(kp) > 0:
        for x, y in np.float32(kp).reshape(-1, 2):
            keypoints.append((x, y))
    return keypoints


def process(image):
    grey1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey1)
    cv2.imshow("frame", grey)
    keypoints = getkpoints(grey, grey1)
    if keypoints is not None and len(keypoints) > 0:
        for x, y in keypoints:
            cv2.circle(image, (int(int(x) + 200), int(y)), 3, (0, 0, 255))
    return image


video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"
# video_filename = 'D:/內視鏡影片/_ims影片2/180824-1025.mp4'

cap = cv2.VideoCapture(video_filename)
# cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    # cv2.imshow('frame', frame)
    if cv2.waitKey(27) & 0xFF == ord("q"):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.resize(cv2.imread("images/soccer_practice.jpg", 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread("images/shoe.PNG", 0), (0, 0), fx=0.8, fy=0.8)
print(img.shape)
print(template.shape)
h, w = template.shape

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
]

for method in methods:
    print("matchTemplate, method = ", method)
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("製作毛玻璃效果")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

import numpy as np

img = cv2.imread(filename)
result = img.copy()
H, W = result.shape[:2]
print(H, W)

for y in range(H-5):
    for x in range(W-5):
        random_num = np.random.randint(0, 5)
        result[y, x] = img[y+random_num, x+random_num]

cv2.imshow('src', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('OpenCV之控件 Trackbar')
print('滑桿 ( Trackbar ) 又稱作滑動條、Slider bar，是一種可以用滑鼠調整數值的 UI 介面')

print("測試cv2視窗的Trackbar")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#image = cv2.imread(filename)

# 調整對比度後，圖像的效果顯示窗口
cv2.namedWindow("TrackbarTest", cv2.WND_PROP_AUTOSIZE)

cv2.imshow("TrackbarTest", image)

MAX_VALUE = 80
MIN_VALUE = 30  # 無效，看起來最小值一定要0
initial_value = 40


def callback_trackbar_test(_value):
    print(_value, end=" ")

callback_trackbar_test(initial_value)  # 做一次

# cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式
cv2.createTrackbar(
    "value", "TrackbarTest", MIN_VALUE, MAX_VALUE, callback_trackbar_test
)  # callback function
cv2.setTrackbarPos("value", "TrackbarTest", initial_value)

cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------------------------------

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

img = cv2.imread(filename)
cv2.imshow('opencv', img)

def get_trackbar_value(val):
    print(val, end = " ")

cv2.createTrackbar('Trackbar', 'opencv', 0, 255, get_trackbar_value)
cv2.setTrackbarPos('Trackbar', 'opencv', 50)#預設值

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np

def setup_bg_color(x):
  r = cv2.getTrackbarPos('R','image')
  g = cv2.getTrackbarPos('G','image')
  b = cv2.getTrackbarPos('B','image')
  s = cv2.getTrackbarPos(switch,'image')

  if s == 0:
   img[:] = 0
  else:
   img[:] = [b,g,r]
  cv2.imshow('image',img)


# Create a black image, a window
img = np.zeros((240,180,3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,setup_bg_color)
cv2.createTrackbar('G','image',0,255,setup_bg_color)
cv2.createTrackbar('B','image',0,255,setup_bg_color)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,setup_bg_color)

while(1):
 k = cv2.waitKey(1) & 0xFF
 if k == 27:
  break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#boxPoints返回四个点顺序：右下→左下→左上→右上

import cv2
import numpy as np

image = cv2.imread("data/cc.bmp")

imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(imagegray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
rect = cv2.minAreaRect(contours[0]) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
print(rect)
points = cv2.boxPoints(rect) # 获取最小外接矩形的4个顶点坐标
print(points)  # 
points = np.int0(points)

# 畫出來
cv2.drawContours(image, [points], 0, (0, 0, 255), 3)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
  
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")

cv2.imshow("original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n", rect)
points = cv2.boxPoints(rect)
print("\n轉換后的points：\n", points)
points = np.int0(points)  # 取整

# 畫出來
cv2.drawContours(image, [points], 0, (0, 0, 255), 3)

cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
print("------------------------------------------------------------")  # 60個

rotating_angle = 0#順時針
# 旋轉矩形

W, H = 400, 400
cx, cy = 200, 200
points = cv2.boxPoints(((cx, cy), (350, 100), rotating_angle))
# 四個頂點
print(points.dtype)  # 打印數據類型
print(points)  # 打印四個頂點

# 根據四個頂點在黑色畫板上畫出該矩形
image = np.zeros((H, W), np.uint8)

for i in range(4):
    # 相鄰的點
    p1 = points[i, :]
    j = (i + 1) % 4
    p2 = points[j, :]
    # 畫出直線
    cv2.line(
        image,
        (int(p1[0]), int(p1[1])),
        (int(p2[0]), int(p2[1])),
        (255, 255, 255),
        5,
        lineType=cv2.LINE_AA,
    )

cv2.circle(image, (100,100), 100, (255, 255, 255), 5)
#cv2.circle(image, (cx, cy), radius, color, line_width)  # 繪製圓形

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
