"""




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

print("OpenCV_ai_63")

cap = cv2.VideoCapture(0)

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
# faces = face_cascade_classifier.detectMultiScale(gray)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (540, 320))  # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 將鏡頭影像轉換成灰階
    faces = face_cascade_classifier.detectMultiScale(gray)  # 偵測人臉
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 標記人臉

    cv2.imshow("ImageShow", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_65")

cap = cv2.VideoCapture(0)

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (480, 300))  # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 影像轉轉灰階
    faces = face_cascade_classifier.detectMultiScale(gray)  # 偵測人臉
    for x, y, w, h in faces:
        mosaic = frame[y : y + h, x : x + w]
        level = 15
        mh = int(h / level)
        mw = int(w / level)
        mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)
        mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y : y + h, x : x + w] = mosaic

    cv2.imshow("ImageShow", frame)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


eye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_eye.xml"
mouth_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_mcs_mouth.xml"
nose_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_mcs_nose.xml"

print("OpenCV_ai_67")

cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(eye_xml_filename)  # 使用眼睛模型
mouth_cascade = cv2.CascadeClassifier(mouth_xml_filename)  # 使用嘴巴模型
nose_cascade = cv2.CascadeClassifier(nose_xml_filename)  # 使用鼻子模型
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame, (540, 320))
    gray = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    eyes = eye_cascade.detectMultiScale(gray)  # 偵測眼睛
    for x, y, w, h in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴
    for x, y, w, h in mouths:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    noses = nose_cascade.detectMultiScale(gray)  # 偵測鼻子
    for x, y, w, h in noses:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_71")

recognizer = cv2.face.LBPHFaceRecognizer_create()  # 啟用訓練人臉模型方法

# 缺檔案
# recognizer.read('face.yml')                               # 讀取人臉模型檔

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 啟用人臉追蹤

cap = cv2.VideoCapture(0)  # 開啟攝影機
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (540, 300))  # 縮小尺寸，加快辨識效率
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換成黑白
    faces = face_cascade_classifier.detectMultiScale(gray)  # 追蹤人臉 ( 目的在於標記出外框 )

    # 建立姓名和 id 的對照表
    name = {"1": "David", "2": "John", "3": "Chris"}

    # 依序判斷每張臉屬於哪個 id
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 標記人臉外框
        idnum, confidence = recognizer.predict(
            gray[y : y + h, x : x + w]
        )  # 取出 id 號碼以及信心指數 confidence
        if confidence < 60:
            text = name[str(idnum)]  # 如果信心指數小於 60，取得對應的名字
        else:
            text = "???"  # 不然名字就是 ???
        # 在人臉外框旁加上名字
        cv2.putText(
            img,
            text,
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

    cv2.imshow("ImageShow", img)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_72")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break
    # 按下 a 開始選取
    if k == ord("a"):
        # 選取區域
        area = cv2.selectROI("ImageShow", frame, showCrosshair=False, fromCenter=False)
        print(area)

    cv2.imshow("ImageShow", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_73")

tracker = cv2.TrackerCSRT_create()  # 創建追蹤器
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (540, 300))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

    if k == ord("a"):
        area = cv2.selectROI("ImageShow", frame, showCrosshair=False, fromCenter=False)
        tracker.init(frame, area)  # 初始化追蹤器
        tracking = True  # 設定可以開始追蹤
    if tracking:
        success, point = tracker.update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
        if success:
            p1 = [int(point[0]), int(point[1])]
            p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
            cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

    cv2.imshow("ImageShow", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_74 影片")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

tracker_list = []
for i in range(3):
    tracker = cv2.TrackerCSRT_create()  # 創建三組追蹤器
    tracker_list.append(tracker)
colors = [(0, 0, 255), (0, 255, 255), (255, 255, 0)]  # 設定三個外框顏色
tracking = False  # 設定 False 表示尚未開始追蹤

cap = cv2.VideoCapture(video_filename)  # 讀取某個影片
a = 0  # 刪減影片影格使用
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (400, 230))  # 縮小尺寸，加快速度

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

    # 為了避免影片影格太多，所以採用 10 格取一格，加快處理速度
    if a % 10 == 0:
        if tracking == False:
            # 如果尚未開始追蹤，就開始標記追蹤物件的外框
            for i in tracker_list:
                area = cv2.selectROI(
                    "ImageShow", frame, showCrosshair=False, fromCenter=False
                )
                i.init(frame, area)  # 初始化追蹤器
            tracking = True  # 設定可以開始追蹤
        if tracking:
            for i in range(len(tracker_list)):
                success, point = tracker_list[i].update(frame)  # 追蹤成功後，不斷回傳左上和右下的座標
                if success:
                    p1 = [int(point[0]), int(point[1])]
                    p2 = [int(point[0] + point[2]), int(point[1] + point[3])]
                    cv2.rectangle(frame, p1, p2, colors[i], 3)  # 根據座標，繪製四邊形，框住要追蹤的物件

        cv2.imshow("ImageShow", frame)
    a = a + 1

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_75")

multiTracker = cv2.legacy.MultiTracker_create()  # 建立多物件追蹤器
tracking = False  # 設定追蹤尚未開始
colors = [(0, 0, 255), (0, 255, 255)]  # 建立外框色彩清單

cap = cv2.VideoCapture(0)  # 讀取攝影鏡頭
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (400, 230))  # 縮小尺寸加快速度

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

    # 按下 a 的時候開始標記物件外框
    if k == ord("a"):
        for i in range(2):
            area = cv2.selectROI(
                "ImageShow", frame, showCrosshair=False, fromCenter=False
            )
            # 標記外框後設定該物件的追蹤演算法
            tracker = cv2.legacy.TrackerCSRT_create()
            # 將該物件加入 multiTracker
            multiTracker.add(tracker, frame, area)
        # 設定 True 開始追蹤
        tracking = True
    if tracking:
        # 更新 multiTracker
        success, points = multiTracker.update(frame)
        a = 0
        if success:
            for i in points:
                p1 = (int(i[0]), int(i[1]))
                p2 = (int(i[0] + i[2]), int(i[1] + i[3]))
                # 標記物件外框
                cv2.rectangle(frame, p1, p2, colors[a], 3)
                a = a + 1
    cv2.imshow("ImageShow", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_77")

lower = np.array([30, 40, 200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90, 100, 255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    mask = cv2.inRange(frame, lower, upper)  # 使用 inRange
    output = cv2.bitwise_and(frame, frame, mask=mask)  # 套用影像遮罩

    cv2.imshow("ImageShow", output)

    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_78")

lower = np.array([30, 40, 200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90, 100, 255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (640, 360))  # 縮小尺寸，加快處理速度
    output = cv2.inRange(img, lower, upper)  # 取得顏色範圍的顏色
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))  # 設定膨脹與侵蝕的參數
    output = cv2.dilate(output, kernel)  # 膨脹影像，消除雜訊
    output = cv2.erode(output, kernel)  # 縮小影像，還原大小

    cv2.imshow("ImageShow", output)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_79")

lower = np.array([30, 40, 200])
upper = np.array([90, 100, 255])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (640, 360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    # cv2.findContours 抓取顏色範圍的輪廓座標
    # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列，cv2.CHAIN_APPROX_SIMPLE 為取值的演算法
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    """
    # 使用 for 迴圈印出座標長相
    for contour in contours:
        print(contour)
    """

    cv2.imshow("ImageShow", output)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_80")

lower = np.array([30, 40, 200])
upper = np.array([90, 100, 255])
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (640, 360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)

    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    for contour in contours:
        area = cv2.contourArea(contour)  # 取得範圍內的面積
        color = (0, 0, 255)  # 設定外框顏色
        # 如果面積大於 300 再標記，避免標記到背景中太小的東西
        if area > 300:
            for i in range(len(contour)):
                if i > 0 and i < len(contour) - 1:
                    # 從第二個點開始畫線
                    img = cv2.line(
                        img,
                        (contour[i - 1][0][0], contour[i - 1][0][1]),
                        (contour[i][0][0], contour[i][0][1]),
                        color,
                        3,
                    )
                elif i == len(contour) - 1:
                    # 如果是最後一個點，與第一個點連成一線
                    img = cv2.line(
                        img,
                        (contour[i][0][0], contour[i][0][1]),
                        (contour[0][0][0], contour[0][0][1]),
                        color,
                        3,
                    )

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_81")

lower = np.array([30, 40, 200])  # 轉換成 NumPy 陣列，範圍稍微變小 ( 55->30, 70->40, 252->200 )
upper = np.array([90, 100, 255])  # 轉換成 NumPy 陣列，範圍稍微加大 ( 70->90, 80->100, 252->255 )
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (640, 360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0, 0, 255)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)  # 取得座標與長寬尺寸
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)  # 繪製四邊形

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_82")

lower = np.array([30, 40, 200])
upper = np.array([90, 100, 255])

blue_lower = np.array([90, 100, 0])  # 設定藍色最低值範圍
blue_upper = np.array([200, 160, 100])  # 設定藍色最高值範圍

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (640, 360))
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    contours, hierarchy = cv2.findContours(
        output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (0, 0, 255)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    # 設定選取藍色的程式
    blue_output = cv2.inRange(img, blue_lower, blue_upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    blue_output = cv2.dilate(blue_output, kernel)
    blue_output = cv2.erode(blue_output, kernel)
    contours, hierarchy = cv2.findContours(
        blue_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        area = cv2.contourArea(contour)
        color = (255, 255, 0)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_83")

import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
) as face_detection:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break

        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.detections:
            print(len(results.detections))
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_84")

import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection  # 建立偵測方法
mp_drawing = mp.solutions.drawing_utils  # 建立繪圖方法

with mp_face_detection.FaceDetection(  # 開始偵測人臉
    model_selection=0, min_detection_confidence=0.5
) as face_detection:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 將 BGR 顏色轉換成 RGB
        results = face_detection.process(img2)  # 偵測人臉

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)  # 標記人臉

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_85")

import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
) as face_detection:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        size = img.shape  # 取得攝影機影像尺寸
        w = size[1]  # 取得畫面寬度
        h = size[0]  # 取得畫面高度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img2)

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)
                s = detection.location_data.relative_bounding_box  # 取得人臉尺寸
                eye = int(s.width * w * 0.1)  # 計算眼睛大小 ( 人臉尺寸*0.1 )
                a = detection.location_data.relative_keypoints[0]  # 取得左眼座標
                b = detection.location_data.relative_keypoints[1]  # 取得右眼座標
                ax, ay = int(a.x * w), int(a.y * h)  # 計算左眼真正的座標
                bx, by = int(b.x * w), int(b.y * h)  # 計算右眼真正的座標
                cv2.circle(
                    img, (ax, ay), (eye + 10), (255, 255, 255), -1
                )  # 畫左眼白色大圓 ( 白眼球 )
                cv2.circle(
                    img, (bx, by), (eye + 10), (255, 255, 255), -1
                )  # 畫右眼白色大圓 ( 白眼球 )
                cv2.circle(img, (ax, ay), eye, (0, 0, 0), -1)  # 畫左眼黑色大圓 ( 黑眼球 )
                cv2.circle(img, (bx, by), eye, (0, 0, 0), -1)  # 畫右眼黑色大圓 ( 黑眼球 )
                cv2.circle(
                    img, (ax - 8, ay - 8), (eye - 15), (255, 255, 255), -1
                )  # 畫左眼白色小圓 ( 反光 )
                cv2.circle(
                    img, (bx - 8, by - 8), (eye - 15), (255, 255, 255), -1
                )  # 畫右眼白色小圓 ( 反光 )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_86")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_face_mesh = mp.solutions.face_mesh  # mediapipe 人臉網格方法
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)  # 繪圖參數設定

cap = cv2.VideoCapture(0)

# 啟用人臉網格偵測，設定相關參數
with mp_face_mesh.FaceMesh(
    max_num_faces=1,  # 一次偵測最多幾個人臉
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as face_mesh:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 顏色 BGR 轉換為 RGB
        results = face_mesh.process(img2)  # 取得人臉網格資訊
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 繪製網格
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                )
                # 繪製輪廓
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
                )
                # 繪製眼睛
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style(),
                )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_87")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as face_mesh:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (480, 320))  # 調整影像尺寸為 480x320
        output = np.zeros((320, 480, 3), dtype="uint8")  # 繪製 480x320 的黑色畫布
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img2)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 繪製網格
                mp_drawing.draw_landmarks(
                    image=output,  # 繪製到 output
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                )
                # 繪製輪廓
                mp_drawing.draw_landmarks(
                    image=output,  # 繪製到 output
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
                )
                # 繪製眼睛
                mp_drawing.draw_landmarks(
                    image=output,  # 繪製到 output
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style(),
                )

        cv2.imshow("ImageShow", output)  # 顯示 output
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_88")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_hands = mp.solutions.hands  # mediapipe 偵測手掌方法

cap = cv2.VideoCapture(0)

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0,
    # max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 將 BGR 轉換成 RGB
        results = hands.process(img2)  # 偵測手掌
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 將節點和骨架繪製到影像中
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_89")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_hands = mp.solutions.hands  # mediapipe 偵測手掌方法

cap = cv2.VideoCapture(0)

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    run = True  # 設定是否更動觸碰區位置
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (540, 320))  # 調整畫面尺寸
        size = img.shape  # 取得攝影機影像尺寸
        w = size[1]  # 取得畫面寬度
        h = size[0]  # 取得畫面高度
        if run:
            run = False  # 如果沒有碰到，就一直是 False ( 不會更換位置 )
            rx = random.randint(50, w - 50)  # 隨機 x 座標
            ry = random.randint(50, h - 100)  # 隨機 y 座標
            print(rx, ry)
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 將 BGR 轉換成 RGB
        results = hands.process(img2)  # 偵測手掌
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x = hand_landmarks.landmark[7].x * w  # 取得食指末端 x 座標
                y = hand_landmarks.landmark[7].y * h  # 取得食指末端 y 座標
                print(x, y)
                if x > rx and x < (rx + 80) and y > ry and y < (ry + 80):
                    run = True
                # 將節點和骨架繪製到影像中
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

        cv2.rectangle(img, (rx, ry), (rx + 80, ry + 80), (0, 0, 255), 5)  # 畫出觸碰區
        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_90")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_pose = mp.solutions.pose  # mediapipe 姿勢偵測

cap = cv2.VideoCapture(0)

# 啟用姿勢偵測
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (520, 300))  # 縮小尺寸，加快演算速度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 將 BGR 轉換成 RGB
        results = pose.process(img2)  # 取得姿勢偵測結果
        # 根據姿勢偵測結果，標記身體節點和骨架
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
        )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_91")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
bg = cv2.imread("windows-bg.jpg")  # 載入 windows 經典背景

with mp_pose.Pose(
    min_detection_confidence=0.5,
    enable_segmentation=True,  # 額外設定 enable_segmentation 參數
    min_tracking_confidence=0.5,
) as pose:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (520, 300))
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img2)
        try:
            # 使用 try 避免抓不到姿勢時發生錯誤
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
            # 如果滿足模型判斷條件 ( 表示要換成背景 )，回傳 True
            img = np.where(condition, img, bg)
            # 將主體與背景合成，如果滿足背景條件，就更換為 bg 的像素，不然維持原本的 img 的像素
        except:
            pass
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
        )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_92")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic  # mediapipe 全身偵測方法

cap = cv2.VideoCapture(0)

# mediapipe 啟用偵測全身
with mp_holistic.Holistic(
    min_detection_confidence=0.5, min_tracking_confidence=0.5
) as holistic:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (520, 300))
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 將 BGR 轉換成 RGB
        results = holistic.process(img2)  # 開始偵測全身
        # 面部偵測，繪製臉部網格
        mp_drawing.draw_landmarks(
            img,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
        )
        # 身體偵測，繪製身體骨架
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style(),
        )

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_93")

""" fail
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils  # mediapipe 繪圖方法
mp_objectron = mp.solutions.objectron    # mediapipe 物體偵測

cap = cv2.VideoCapture(0)

# 啟用物體偵測，偵測鞋子 Shoe
with mp_objectron.Objectron(static_image_mode=False,
                            max_num_objects=5,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.99,
                            model_name='Shoe') as objectron:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))               # 縮小尺寸，加快演算速度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = objectron.process(img2)             # 取得物體偵測結果
        # 標記所偵測到的物體
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                  img, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
                mp_drawing.draw_axis(img, detected_object.rotation,
                                    detected_object.translation)

        cv2.imshow('ImageShow', img)
        k = cv2.waitKey(1) # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_94")

""" 缺檔案
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils                    # mediapipe 繪圖功能
mp_selfie_segmentation = mp.solutions.selfie_segmentation  # mediapipe 自拍分割方法

cap = cv2.VideoCapture(0)
bg = cv2.imread('windows-bg.jpg')   # 載入 windows 經典背景

# mediapipe 啟用自拍分割
with mp_selfie_segmentation.SelfieSegmentation(
    model_selection=1) as selfie_segmentation:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))               # 縮小尺寸，加快演算速度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = selfie_segmentation.process(img2)   # 取得自拍分割結果
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1 # 如果滿足模型判斷條件 ( 表示要換成背景 )，回傳 True
        output_image = np.where(condition, img, bg)
        # 將主體與背景合成，如果滿足背景條件，就更換為 bg 的像素，不然維持原本的 img 的像素

        cv2.imshow('ImageShow', output_image)
        k = cv2.waitKey(1) # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_95")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(
            math.acos(
                (v1_x * v2_x + v1_y * v2_y)
                / (((v1_x**2 + v1_y**2) ** 0.5) * ((v2_x**2 + v2_y**2) ** 0.5))
            )
        )
    except:
        angle_ = 180
    return angle_


# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1]))),
    )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1]))),
    )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[10][0])),
            (int(hand_[0][1]) - int(hand_[10][1])),
        ),
        (
            (int(hand_[11][0]) - int(hand_[12][0])),
            (int(hand_[11][1]) - int(hand_[12][1])),
        ),
    )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[14][0])),
            (int(hand_[0][1]) - int(hand_[14][1])),
        ),
        (
            (int(hand_[15][0]) - int(hand_[16][0])),
            (int(hand_[15][1]) - int(hand_[16][1])),
        ),
    )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[18][0])),
            (int(hand_[0][1]) - int(hand_[18][1])),
        ),
        (
            (int(hand_[19][0]) - int(hand_[20][0])),
            (int(hand_[19][1]) - int(hand_[20][1])),
        ),
    )
    angle_list.append(angle_)
    return angle_list


# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]  # 大拇指角度
    f2 = finger_angle[1]  # 食指角度
    f3 = finger_angle[2]  # 中指角度
    f4 = finger_angle[3]  # 無名指角度
    f5 = finger_angle[4]  # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "good"
    elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "no!!!"
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "ROCK!"
    elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "0"
    elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "pink"
    elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "1"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "2"
    elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "ok"
    elif f1 < 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "ok"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 > 50:
        return "3"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "4"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "5"
    elif f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "6"
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "7"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "8"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 >= 50:
        return "9"
    else:
        return ""


cap = cv2.VideoCapture(0)  # 讀取攝影機
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA  # 印出文字的邊框

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    w, h = 540, 310  # 影像尺寸
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w, h))  # 縮小尺寸，加快處理效率
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 轉換成 RGB 色彩
        results = hands.process(img2)  # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []  # 記錄手指節點座標的串列
                for i in hand_landmarks.landmark:
                    # 將 21 個節點換算成座標，記錄到 finger_points
                    x = i.x * w
                    y = i.y * h
                    finger_points.append((x, y))
                if finger_points:
                    finger_angle = hand_angle(finger_points)  # 計算手指角度，回傳長度為 5 的串列
                    # print(finger_angle)                     # 印出角度 ( 有需要就開啟註解 )
                    text = hand_pos(finger_angle)  # 取得手勢所回傳的內容
                    cv2.putText(
                        img, text, (30, 120), fontFace, 5, (255, 255, 255), 10, lineType
                    )  # 印出文字

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_96")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(
            math.acos(
                (v1_x * v2_x + v1_y * v2_y)
                / (((v1_x**2 + v1_y**2) ** 0.5) * ((v2_x**2 + v2_y**2) ** 0.5))
            )
        )
    except:
        angle_ = 180
    return angle_


# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1]))),
    )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1]))),
    )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[10][0])),
            (int(hand_[0][1]) - int(hand_[10][1])),
        ),
        (
            (int(hand_[11][0]) - int(hand_[12][0])),
            (int(hand_[11][1]) - int(hand_[12][1])),
        ),
    )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[14][0])),
            (int(hand_[0][1]) - int(hand_[14][1])),
        ),
        (
            (int(hand_[15][0]) - int(hand_[16][0])),
            (int(hand_[15][1]) - int(hand_[16][1])),
        ),
    )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[18][0])),
            (int(hand_[0][1]) - int(hand_[18][1])),
        ),
        (
            (int(hand_[19][0]) - int(hand_[20][0])),
            (int(hand_[19][1]) - int(hand_[20][1])),
        ),
    )
    angle_list.append(angle_)
    return angle_list


# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]  # 大拇指角度
    f2 = finger_angle[1]  # 食指角度
    f3 = finger_angle[2]  # 中指角度
    f4 = finger_angle[3]  # 無名指角度
    f5 = finger_angle[4]  # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "good"
    elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "no!!!"
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "ROCK!"
    elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "0"
    elif f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "pink"
    elif f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "1"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "2"
    elif f1 >= 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "ok"
    elif f1 < 50 and f2 >= 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "ok"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 > 50:
        return "3"
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "4"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50:
        return "5"
    elif f1 < 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 < 50:
        return "6"
    elif f1 < 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "7"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50:
        return "8"
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 >= 50:
        return "9"
    else:
        return ""


cap = cv2.VideoCapture(0)  # 讀取攝影機
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA  # 印出文字的邊框

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    w, h = 540, 310  # 影像尺寸
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w, h))  # 縮小尺寸，加快處理效率
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 轉換成 RGB 色彩
        results = hands.process(img2)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []  # 記錄手指節點座標的串列
                fx = []  # 記錄所有 x 座標的串列
                fy = []  # 記錄所有 y 座標的串列
                for i in hand_landmarks.landmark:
                    # 將 21 個節點換算成座標，記錄到 finger_points
                    x = i.x * w  # 計算 x 座標
                    y = i.y * h  # 計算 y 座標
                    finger_points.append((x, y))
                    fx.append(int(x))  # 記錄 x 座標
                    fy.append(int(y))  # 記錄 y 座標
                if finger_points:
                    finger_angle = hand_angle(finger_points)  # 計算手指角度，回傳長度為 5 的串列
                    # print(finger_angle)             # 印出角度 ( 有需要就開啟註解 )
                    text = hand_pos(finger_angle)  # 取得手勢所回傳的內容
                    if text == "no!!!":
                        x_max = max(fx)  # 如果是比中指，取出 x 座標最大值
                        y_max = max(fy)  # 如果是比中指，取出 y 座標最大值
                        x_min = min(fx) - 10  # 如果是比中指，取出 x 座標最小值
                        y_min = min(fy) - 10  # 如果是比中指，取出 y 座標最小值
                        if x_max > w:
                            x_max = w  # 如果最大值超過邊界，將最大值等於邊界
                        if y_max > h:
                            y_max = h  # 如果最大值超過邊界，將最大值等於邊界
                        if x_min < 0:
                            x_min = 0  # 如果最小值超過邊界，將最小值等於邊界
                        if y_min < 0:
                            y_min = 0  # 如果最小值超過邊界，將最小值等於邊界
                        mosaic_w = x_max - x_min  # 計算四邊形的寬
                        mosaic_h = y_max - y_min  # 計算四邊形的高
                        mosaic = img[y_min:y_max, x_min:x_max]  # 取出四邊形區域
                        mosaic = cv2.resize(
                            mosaic, (8, 8), interpolation=cv2.INTER_LINEAR
                        )  # 根據縮小尺寸縮小
                        mosaic = cv2.resize(
                            mosaic,
                            (mosaic_w, mosaic_h),
                            interpolation=cv2.INTER_NEAREST,
                        )  # 放大到原本的大小
                        img[y_min:y_max, x_min:x_max] = mosaic  # 馬賽克區域
                    else:
                        cv2.putText(
                            img,
                            text,
                            (30, 120),
                            fontFace,
                            5,
                            (255, 255, 255),
                            10,
                            lineType,
                        )  # 印出文字

        cv2.imshow("ImageShow", img)
        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_97")

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(
            math.acos(
                (v1_x * v2_x + v1_y * v2_y)
                / (((v1_x**2 + v1_y**2) ** 0.5) * ((v2_x**2 + v2_y**2) ** 0.5))
            )
        )
    except:
        angle_ = 180
    return angle_


# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1]))),
    )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1]))),
    )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[10][0])),
            (int(hand_[0][1]) - int(hand_[10][1])),
        ),
        (
            (int(hand_[11][0]) - int(hand_[12][0])),
            (int(hand_[11][1]) - int(hand_[12][1])),
        ),
    )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[14][0])),
            (int(hand_[0][1]) - int(hand_[14][1])),
        ),
        (
            (int(hand_[15][0]) - int(hand_[16][0])),
            (int(hand_[15][1]) - int(hand_[16][1])),
        ),
    )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        (
            (int(hand_[0][0]) - int(hand_[18][0])),
            (int(hand_[0][1]) - int(hand_[18][1])),
        ),
        (
            (int(hand_[19][0]) - int(hand_[20][0])),
            (int(hand_[19][1]) - int(hand_[20][1])),
        ),
    )
    angle_list.append(angle_)
    return angle_list


# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]  # 大拇指角度
    f2 = finger_angle[1]  # 食指角度
    f3 = finger_angle[2]  # 中指角度
    f4 = finger_angle[3]  # 無名指角度
    f5 = finger_angle[4]  # 小拇指角度

    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1 >= 50 and f2 < 50 and f3 >= 50 and f4 >= 50 and f5 >= 50:
        return "1"
    else:
        return ""


cap = cv2.VideoCapture(0)  # 讀取攝影機
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA  # 印出文字的邊框

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    w, h = 540, 310  # 影像尺寸
    draw = np.zeros((h, w, 4), dtype="uint8")  # 繪製全黑背景，尺寸和影像相同
    dots = []  # 使用 dots 空串列記錄繪圖座標點
    cv2.rectangle(draw, (20, 20), (60, 60), (0, 0, 255, 255), -1)  # 在畫面上方放入紅色正方形
    cv2.rectangle(draw, (80, 20), (120, 60), (0, 255, 0, 255), -1)  # 在畫面上方放入綠色正方形
    cv2.rectangle(draw, (140, 20), (180, 60), (255, 0, 0, 255), -1)  # 在畫面上方放入藍色正方形
    color = (0, 0, 255, 255)  # 設定預設顏色為紅色
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w, h))  # 縮小尺寸，加快處理效率
        img = cv2.flip(img, 1)
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 偵測手勢的影像轉換成 RGB 色彩
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 畫圖的影像轉換成 BGRA 色彩
        results = hands.process(img2)  # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []  # 記錄手指節點座標的串列
                for i in hand_landmarks.landmark:
                    # 將 21 個節點換算成座標，記錄到 finger_points
                    x = i.x * w
                    y = i.y * h
                    finger_points.append((x, y))
                if finger_points:
                    finger_angle = hand_angle(finger_points)  # 計算手指角度，回傳長度為 5 的串列
                    text = hand_pos(finger_angle)  # 取得手勢所回傳的內容
                    if text == "1":
                        fx = int(finger_points[8][0])  # 如果手勢為 1，記錄食指末端的座標
                        fy = int(finger_points[8][1])
                        if fy >= 20 and fy <= 60 and fx >= 20 and fx <= 60:
                            color = (0, 0, 255, 255)  # 如果食指末端碰到紅色，顏色改成紅色
                        elif fy >= 20 and fy <= 60 and fx >= 80 and fx <= 120:
                            color = (0, 255, 0, 255)  # 如果食指末端碰到綠色，顏色改成綠色
                        elif fy >= 20 and fy <= 60 and fx >= 140 and fx <= 180:
                            color = (255, 0, 0, 255)  # 如果食指末端碰到藍色，顏色改成藍色
                        else:
                            dots.append([fx, fy])  # 記錄食指座標
                            dl = len(dots)
                            if dl > 1:
                                dx1 = dots[dl - 2][0]
                                dy1 = dots[dl - 2][1]
                                dx2 = dots[dl - 1][0]
                                dy2 = dots[dl - 1][1]
                                cv2.line(
                                    draw, (dx1, dy1), (dx2, dy2), color, 5
                                )  # 在黑色畫布上畫圖
                    else:
                        dots = []  # 如果換成別的手勢，清空 dots

        # 將影像和黑色畫布合成
        for j in range(w):
            img[:, j, 0] = img[:, j, 0] * (1 - draw[:, j, 3] / 255) + draw[:, j, 0] * (
                draw[:, j, 3] / 255
            )
            img[:, j, 1] = img[:, j, 1] * (1 - draw[:, j, 3] / 255) + draw[:, j, 1] * (
                draw[:, j, 3] / 255
            )
            img[:, j, 2] = img[:, j, 2] * (1 - draw[:, j, 3] / 255) + draw[:, j, 2] * (
                draw[:, j, 3] / 255
            )

        cv2.imshow("ImageShow", img)

        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

        # 按下 r 重置畫面
        if k == ord("r"):
            draw = np.zeros((h, w, 4), dtype="uint8")
            cv2.rectangle(
                draw, (20, 20), (60, 60), (0, 0, 255, 255), -1
            )  # 在畫面上方放入紅色正方形
            cv2.rectangle(
                draw, (80, 20), (120, 60), (0, 255, 0, 255), -1
            )  # 在畫面上方放入綠色正方形
            cv2.rectangle(
                draw, (140, 20), (180, 60), (255, 0, 0, 255), -1
            )  # 在畫面上方放入藍色正方形
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_98")

cap = cv2.VideoCapture(0)  # 讀取攝影鏡頭
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

dots = []  # 記錄座標
mask_b = np.zeros((height, width, 3), dtype="uint8")  # 產生黑色遮罩 -> 套用清楚影像
mask_b[:, :] = 255  # 設定黑色遮罩底色為白色
mask_b[80:280, 220:420] = 0  # 設定黑色遮罩哪個區域是黑色

mask_w = np.zeros((height, width, 3), dtype="uint8")  # 產生白色遮罩 -> 套用模糊影像
mask_w[80:280, 220:420] = 255  # 設定白色遮罩哪個區域是白色

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    img = cv2.flip(img, 1)  # 翻轉影像
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
    img2 = img.copy()  # 複製影像
    img2 = cv2.blur(img, (55, 55))  # 套用模糊

    mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    img = cv2.bitwise_and(img, img, mask=mask1)  # 清楚影像套用黑遮罩

    mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
    img2 = cv2.bitwise_and(img2, img2, mask=mask2)  # 模糊影像套用白遮罩

    output = cv2.add(img, img2)  # 合併影像

    cv2.imshow("ImageShow", output)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)  # 讀取攝影機

# mediapipe 啟用偵測手掌
with mp_hands.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    w = 640  # 定義影片寬度
    h = 360  # 定義影像高度
    dots = []  # 記錄座標
    mask_b = np.zeros((h, w, 3), dtype="uint8")  # 產生黑色遮罩 -> 套用清楚影像
    mask_w = np.zeros((h, w, 3), dtype="uint8")  # 產生白色遮罩 -> 套用模糊影像
    mask_w[0:h, 0:w] = 255  # 白色遮罩背景為白色

    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (w, h))  # 縮小尺寸，加快處理效率
        img = cv2.flip(img, 1)  # 翻轉影像
        img_hand = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 偵測手勢使用
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)  # 轉換顏色為 BGRA ( 計算時需要用到 Alpha 色版 )
        img2 = img.copy()  # 複製影像
        img2 = cv2.blur(img, (55, 55))  # 套用模糊

        if not ret:
            print("Cannot receive frame")
            break
        results = hands.process(img_hand)  # 偵測手勢
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_points = []  # 記錄手指節點位置的串列
                for i in hand_landmarks.landmark:
                    x = i.x
                    y = i.y
                    finger_points.append((x, y))  # 記錄手指節點位置
                if finger_points:
                    fx1 = finger_points[8][0]
                    fy1 = finger_points[8][1]
                    fx2 = finger_points[12][0]
                    fy2 = finger_points[12][1]
                    d = (
                        (fx1 - fx2) * (fx1 - fx2) + (fy1 - fy2) * (fy1 - fy2)
                    ) ** 0.5  # 計算食指和中指分開的距離
                    if d < 0.15:
                        dots.append([fx1, fy1])
                        dl = len(dots)
                        if dl > 1:
                            x1 = int(dots[dl - 2][0] * w)  # 計算出真正的座標
                            y1 = int(dots[dl - 2][1] * h)
                            x2 = int(dots[dl - 1][0] * w)
                            y2 = int(dots[dl - 1][1] * h)
                            cv2.line(
                                mask_w, (x1, y1), (x2, y2), (0, 0, 0), 50
                            )  # 在白色遮罩上畫出黑色線條
                            cv2.line(
                                mask_b, (x1, y1), (x2, y2), (255, 255, 255), 50
                            )  # 在黑色遮罩上畫出白色線條
                    else:
                        dots = []

        mask1 = cv2.cvtColor(mask_b, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
        img = cv2.bitwise_and(img, img, mask=mask1)  # 清楚影像套用黑遮罩
        mask2 = cv2.cvtColor(mask_w, cv2.COLOR_BGR2GRAY)  # 轉換遮罩為灰階
        img2 = cv2.bitwise_and(img2, img2, mask=mask2)  # 模糊影像套用白遮罩

        output = cv2.add(img, img2)  # 合併影像

        cv2.imshow("ImageShow", output)

        k = cv2.waitKey(1)  # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" 缺檔案
import mediapipe as mp

cap = cv2.VideoCapture(0)                          # 讀取攝影鏡頭
mp_face_detection = mp.solutions.face_detection    # 使用人臉偵測方法

h, w = 360, 640                                    # 輸出時的影像長寬
mask = np.zeros((h, w, 3), dtype='uint8')          # 建立遮罩
cv2.ellipse(mask, (260,100),(55,35),0,0,360,(255,255,255),-1)   # 繪製左眼的橢圓形遮罩
cv2.ellipse(mask, (380,100),(55,35),0,0,360,(255,255,255),-1)   # 繪製右眼的橢圓形遮罩
cv2.ellipse(mask, (320,212),(115,66),0,0,360,(255,255,255),-1)  # 繪製嘴巴的橢圓形遮罩
mask = cv2.GaussianBlur(mask,(35,35),0)            # 將遮罩進行高斯模糊
mask = mask/255                                    # 轉換成比例

orange = cv2.imread('orange.jpg')                  # 讀取橘子圖片背景

# 人臉偵測模組啟用成功後，執行相關內容
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()                        # 讀取攝影機畫面
        if not ret:
            print("Cannot receive frame")
            break
        img = cv2.resize(img, (w, h))                # 縮小尺寸加快速度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 轉換成 RGB 才能夠在 mediapipe 中使用
        results = face_detection.process(img2)       # 讀取人臉偵測資訊

        if results.detections:
            for detection in results.detections:
                s = detection.location_data.relative_bounding_box      # 取得人臉尺寸
                eye_w = int(s.width*w*0.24/2)                          # 計算眼睛寬度 ( 除以 2 計算座標使用 )
                eye_h = int(s.width*w*0.16/2)                          # 計算眼睛高度 ( 除以 2 計算座標使用 )
                mouth_w = int(s.width*w*0.5/2)                         # 計算嘴巴寬度 ( 除以 2 計算座標使用 )
                mouth_h = int(s.width*w*0.3/2)                         # 計算嘴巴高度 ( 除以 2 計算座標使用 )

                eye_r = detection.location_data.relative_keypoints[0]  # 左眼中心點座標
                eye_l = detection.location_data.relative_keypoints[1]  # 右眼中心點座標
                mouth = detection.location_data.relative_keypoints[3]  # 嘴巴中心點座標

                rcx, rcy = int(eye_r.x*w), int(eye_r.y*h)              # 計算左眼真正的座標
                lcx, lcy = int(eye_l.x*w), int(eye_l.y*h)              # 計算右眼真正的座標
                mx, my = int(mouth.x*w), int(mouth.y*h)                # 計算嘴巴真正的座標

                eye_r_img = img[rcy-eye_h:rcy+eye_h, rcx-eye_w:rcx+eye_w]      # 取出右眼的區域
                eye_r_img = cv2.resize(eye_r_img, (120,80))                    # 改變尺寸為 180x120
                eye_l_img = img[lcy-eye_h:lcy+eye_h, lcx-eye_w:lcx+eye_w]      # 取出左眼的區域
                eye_l_img = cv2.resize(eye_l_img, (120,80))                    # 改變尺寸為 180x120
                mouth_img = img[my-mouth_h:my+mouth_h, mx-mouth_w:mx+mouth_w]  # 取出嘴巴的區域
                mouth_img = cv2.resize(mouth_img, (240,144))                   # 改變尺寸為 360x216

                face = np.zeros((h, w, 3), dtype='uint8')  # 建立空白全黑畫布
                bg = orange.copy()                         # 複製 orange 圖片當作背景
                face[60:140, 200:320] =  eye_l_img         # 貼上左眼
                face[60:140, 320:440] =  eye_r_img         # 貼上右眼
                face[140:284, 200:440] =  mouth_img        # 貼上嘴巴
                face = face + 30                           # 增加亮度
                face = face/255                            # 轉換成比例
                bg = bg/255                                # 轉換成比例
                out  = bg * (1 - mask) + face * mask       # 根據比例混合
                out = (out * 255).astype('uint8')          # 轉換成數字

        cv2.imshow('ImageShow', out)
        k = cv2.waitKey(1) # 等待按鍵輸入
        if k == ESC:
            break

cap.release()
cv2.destroyAllWindows()

"""

print("------------------------------------------------------------")  # 60個


""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)   # 載入 model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)           # 設定資料陣列

cap = cv2.VideoCapture(0)         # 設定攝影機鏡頭
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()       # 讀取攝影機影像
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))   # 改變尺寸
    img = img[0:224, 80:304]               # 裁切為正方形，符合 model 大小
    image_array = np.asarray(img)          # 去除換行符號和結尾空白，產生文字陣列
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # 轉換成預測陣列
    data[0] = normalized_image_array
    prediction = model.predict(data)       # 預測結果
    a,b= prediction[0]                     # 取得預測結果
    if a>0.9:
        print('oxxo')
    if b>0.9:
        print('維他命')
        
    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個


""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 2.5                      # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 5                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text('a')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('b')
    if c>0.9:
        text('c')
        
    cv2.imshow('ImageShow', img)
    
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 50)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text('剪刀')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('石頭')
    if c>0.9:
        text('布')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 1                        # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 2                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]    # 印出每個項目的數值資訊
    print(a,b,bg)
    if a>0.999:              # 判斷有戴口罩
        text('ok~')
    if b>0.001:              # 判斷沒戴口罩
        text('no mask!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model_3.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 30)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame , (398, 224))
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]
    print(a,b,bg)
    if a>0.999:
        text('很乖')
    if b>0.001:
        text('沒戴口罩!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1) # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist
from keras import utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 載入訓練集

# 訓練集資料
x_train = x_train.reshape(x_train.shape[0], -1)  # 轉換資料形狀
x_train = x_train.astype("float32") / 255  # 轉換資料型別
y_train = y_train.astype(np.float32)

# 測試集資料
x_test = x_test.reshape(x_test.shape[0], -1)  # 轉換資料形狀
x_test = x_test.astype("float32") / 255  # 轉換資料型別
y_test = y_test.astype(np.float32)

knn = cv2.ml.KNearest_create()  # 建立 KNN 訓練方法
knn.setDefaultK(5)  # 參數設定
knn.setIsClassifier(True)

print("training...")
knn.train(x_train, cv2.ml.ROW_SAMPLE, y_train)  # 開始訓練
knn.save("mnist_knn.xml")  # 儲存訓練模型
print("ok")

print("testing...")
test_pre = knn.predict(x_test)  # 讀取測試集並進行辨識
test_ret = test_pre[1]
test_ret = test_ret.reshape(
    -1,
)
test_sum = test_ret == y_test
acc = test_sum.mean()  # 得到準確率
print(acc)

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)  # 啟用攝影鏡頭
print("loading...")
knn = cv2.ml.KNearest_load("mnist_knn.xml")  # 載入模型
print("start...")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (540, 300))  # 改變影像尺寸，加快處理效率
    x, y, w, h = 400, 200, 60, 60  # 定義擷取數字的區域位置和大小
    img_num = img.copy()  # 複製一個影像作為辨識使用
    img_num = img_num[y : y + h, x : x + w]  # 擷取辨識的區域

    img_num = cv2.cvtColor(img_num, cv2.COLOR_BGR2GRAY)  # 顏色轉成灰階
    # 針對白色文字，做二值化黑白轉換，轉成黑底白字
    ret, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
    output = cv2.cvtColor(img_num, cv2.COLOR_GRAY2BGR)  # 顏色轉成彩色
    img[0:60, 480:540] = output  # 將轉換後的影像顯示在畫面右上角

    img_num = cv2.resize(img_num, (28, 28))  # 縮小成 28x28，和訓練模型對照
    img_num = img_num.astype(np.float32)  # 轉換格式
    img_num = img_num.reshape(
        -1,
    )  # 打散成一維陣列資料，轉換成辨識使用的格式
    img_num = img_num.reshape(1, -1)
    img_num = img_num / 255
    img_pre = knn.predict(img_num)  # 進行辨識
    num = str(int(img_pre[1][0][0]))  # 取得辨識結果

    text = num  # 印出的文字內容
    org = (x, y - 20)  # 印出的文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出的文字字體
    fontScale = 2  # 印出的文字大小
    color = (0, 0, 255)  # 印出的文字顏色
    thickness = 2  # 印出的文字邊框粗細
    lineType = cv2.LINE_AA  # 印出的文字邊框樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)  # 印出文字

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 標記辨識的區域

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)  # 等待按鍵輸入
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
