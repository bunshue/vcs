"""

新進  未歸類


"""

import os
import sys
import time
import math
import random

print("------------------------------------------------------------")  # 60個

ESC = 27

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個

#未知其用途 goodFeaturesToTrack

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
    mask1[y:y + h, x:x + w] = 255          # 整张图片像素
    keypoints = []    
    kp = cv2.goodFeaturesToTrack(input1, 200, 0.04, 7)
    if kp is not None and len(kp) > 0:
        for x, y in np.float32(kp).reshape(-1, 2):
            keypoints.append((x, y))
    return keypoints

def process(image):
    grey1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey1)
    cv2.imshow('frame', grey)
    keypoints = getkpoints(grey, grey1)
    if keypoints is not None and len(keypoints) > 0:
        for x, y in keypoints:
            cv2.circle(image, (int(int(x) + 200), int(y)), 3, (0, 0, 255))
    return image

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
#video_filename = 'D:/內視鏡影片/_ims影片2/180824-1025.mp4'

cap = cv2.VideoCapture(video_filename)
#cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    #cv2.imshow('frame', frame)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# simple color
"""
色彩辨識與追蹤
"""
import sys
import cv2 
import time
import numpy as np

ESC = 27

color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype = 'uint8')
upper = np.array(color[1], dtype = 'uint8')

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')

ratio = w / h
WIDTH = 320
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

#### 在while中
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)    #執行高斯模糊化

#### 在while中
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)

#### 在while中
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key = cv2.contourArea)
        if cv2.contourArea(cnt) < 100:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (x - 2, y - 2)
        p2 = (x + w + 4, y + h + 4)

        out = cv2.bitwise_and(hsv, hsv, mask = mask)
        
        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2)  #B G R
        cv2.rectangle(hsv, p1, p2, (0, 255, 0), 2)
        cv2.rectangle(out, p1, p2, (255, 0, 0), 2)
        
        frame = cv2.hconcat([frame, hsv, out])

#### 在while中
    cv2.imshow("frame", frame)
    
    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


