# OpenCV 人臉辨識

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

print("框出照片中的人臉, 轉成灰階再辨識, 畫框畫在原圖並顯示")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/SolvayConference1927.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg'

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

image = cv2.imread(filename)  # 讀取本機圖片
# image.shape[0]:圖片高度，image.shape[1]:圖片寬度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 透過轉換函式轉為灰階影像

# gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

# 調用偵測識別人臉函式
faces = face_cascade_classifier.detectMultiScale(
    gray,  # 也可直接用 image 來偵測
    scaleFactor=1.2,
    minNeighbors=3,
    minSize=(32, 32),
    flags=cv2.CASCADE_SCALE_IMAGE,
)

print("共偵測到 " + str(len(faces)) + " 張人臉")
"""
for nn in range(len(faces)):
    print(nn)
    print(faces[nn])
    print(faces[nn][0], faces[nn][1], faces[nn][2], faces[nn][3])
"""
# 參數
# image 	        待檢測圖片，一般為灰階影像，以便加快偵測速度
# scaleFactor 	在前後兩次相繼的掃描中，搜索範圍的比例係數，默認值為 1.1
# minNeighbors 	構成偵測目標的相鄰矩形的最小個數，默認值為 3
# minSize & maxSize 	用來限制得到的目標區域範圍

# 1.2 表示每次影像尺寸減小的比例
# 3 表示每一個目標至少要被檢測到4次才算是真正的目標
# faces表示檢測到的人臉目標list

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = image[y : y + h, x : x + w]

"""
for (x, y, w, h) in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
"""

# cv2.namedWindow('video', cv2.WINDOW_NORMAL)

# 顯示結果
# cv2.imshow(image)
cv2.imshow("New Picture", image)  # 顯示圖片

print("wait here")
cv2.waitKey(0)
print("收到按鍵")

# 釋放所有資源
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"

# face_cascade_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_cascade_classifier = cv2.CascadeClassifier("haarcascade_eye.xml")

xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename1)

xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"
eye_cascade_classifier = cv2.CascadeClassifier(xml_filename2)

# save the image(i) in the same directory

img = cv2.imread(filename)  # 讀取本機圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

for ex, ey, ew, eh in eyes:
    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# 顯示結果
# cv2.imshow(image)
cv2.imshow("New Picture", img)  # 顯示圖片

print("wait here")
cv2.waitKey(0)
print("收到按鍵")

# 釋放所有資源
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"

filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

import cv2

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(filename)

#轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#臉部偵測
faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)

#標示出來
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

