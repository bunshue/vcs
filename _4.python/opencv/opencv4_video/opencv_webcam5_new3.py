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

# simple color
"""
色彩辨識與追蹤
"""
color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print("Could not open video device")
    sys.exit()
else:
    print("Video device opened")

ratio = w / h
WIDTH = 320
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

    #### 在while中
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)  # 執行高斯模糊化

    #### 在while中
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #### 在while中
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt) < 100:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (x - 2, y - 2)
        p2 = (x + w + 4, y + h + 4)

        out = cv2.bitwise_and(hsv, hsv, mask=mask)

        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2)  # B G R
        cv2.rectangle(hsv, p1, p2, (0, 255, 0), 2)
        cv2.rectangle(out, p1, p2, (255, 0, 0), 2)

        frame = cv2.hconcat([frame, hsv, out])

    #### 在while中
    cv2.imshow("frame", frame)

    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
