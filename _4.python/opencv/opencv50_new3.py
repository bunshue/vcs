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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
