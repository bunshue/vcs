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




""" 新進

import cv2
import time
from datetime import datetime


xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"


def face_add(img):
    print("稍後在此加入新增人員功能")


# -----------------------------------#


def face_who(img):
    print("稍後在此加入人臉身分辨識功能")


# -----------------------------------#


def face_shot(function):
    isCnt = False  # 用來判斷是否正在進行倒數計時中
    face_detector = cv2.CascadeClassifier(xml_filename)  # 建立臉部辨識物件
    capture = cv2.VideoCapture(0)  # 開啟編號 0 的攝影機
    while capture.isOpened():  # 判斷攝影機是否開啟成功
        sucess, img = capture.read()  # 讀取攝影機影像
        if not sucess:
            print("讀取影像失敗")
            continue
        img_copy = img.copy()  # 複製影像
        faces = face_detector.detectMultiScale(  # 從攝影機影像中偵測人臉
            img, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)
        )
        if len(faces) == 1:  # 如果偵測到一張人臉
            if isCnt == False:
                t1 = time.time()  # 紀錄現在的時間
                isCnt = True  # 告訴程式目前進入倒數狀態
            cnter = 5 - int(time.time() - t1)  # 更新倒數計時器
            for x, y, w, h in faces:  # 畫出人臉位置
                cv2.rectangle(  # 繪製矩形
                    img_copy, (x, y), (x + w, y + h), (0, 255, 255), 2
                )
                cv2.putText(  # 繪製倒數數字
                    img_copy,
                    str(cnter),
                    (x + int(w / 2), y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )
            if cnter == 0:  # 倒數結束
                isCnt = False  # 告訴程式離開倒數狀態
                filename = datetime.now().strftime("%Y-%m-%d %H.%M.%S")  # 時間格式化
                cv2.imwrite(filename + ".jpg", img)  # 存圖
                # -----------------------------------------#
                if function == "add":  # 打卡系統新增人員
                    face_add(img)
                elif function == "who":  # 進行人臉身分識別功能
                    face_who(img)
                # -----------------------------------------#
        else:  # 如果不是一張人臉
            isCnt = False  # 設定非倒數狀態

        cv2.imshow("Frame", img_copy)  # 顯示影像
        k = cv2.waitKey(1)  # 讀取按鍵輸入(若無會傳回 -1)
        if k == ord("q") or k == ord("Q"):  # 按下 q 離開迴圈, 結束程式
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break  # 離開無窮迴圈, 結束程式
    else:
        print("開啟攝影機失敗")


# -----------------------------------#
face_shot("who")  # 呼叫自訂函式


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





"""

