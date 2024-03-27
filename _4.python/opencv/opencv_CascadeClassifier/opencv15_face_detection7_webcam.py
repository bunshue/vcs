"""
WebCam 使用
一般使用

人臉辨識

目前 webcam 僅 x64 電腦可用
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

ESC = 27

import time

print("按 ESC 或 Q 離開")
print("按 S 存圖")

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)  # 建立攝影機物件

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print("Could not open video device")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像

    if ret == False:
        print("無影像, 離開")
        break

    # frame = cv2.resize(frame,(int(frame.shape[1] / 2), int(frame.shape[0] / 2))) #調整畫面大小
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 調用偵測識別人臉函式
    """
    faces = face_cascade_classifier.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 3,
        minSize = (200, 200))
    """
    faces = face_cascade_classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3
    )

    # print('共偵測到 ' + str(len(faces)) + ' 張人臉')
    # 繪製人臉部份的方框
    color = (0, 255, 0)  # 定義框的顏色
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    cv2.imshow("WebCam", frame)  # 顯示圖片, 彩色

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:  # ESC
        break
    elif k == ord("Q") or k == ord("q"):  # 按下 Q(q) 結束迴圈
        break
    elif k == ord("S") or k == ord("s"):  # 按下 S(s), 存圖
        image_filename = (
            "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
        )
        cv2.imwrite(image_filename, frame)
        print("已存圖, 檔案 :", filename)

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

