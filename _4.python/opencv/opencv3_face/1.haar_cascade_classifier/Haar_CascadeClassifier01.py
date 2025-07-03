"""
OpenCV 人臉辨識
OpenCV 人臉識別分類器 Haar Cascade Classifier
Haar-like features 哈爾特徵
匈牙利 Afred Haar

haarcascade_frontalface_default.xml		偵測正面人臉 預設
haarcascade_frontalface_alt_tree.xml		偵測正面人臉
haarcascade_frontalface_alt.xml			偵測正面人臉
haarcascade_frontalface_alt2.xml		偵測正面人臉

cv2內建xml位置:
cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# 參數
# img    	        待檢測圖片，一般為灰階影像，以便加快偵測速度
# scaleFactor 	        在前後兩次相繼的掃描中，搜索範圍的比例係數，默認值為 1.1
# minNeighbors 	        構成偵測目標的相鄰矩形的最小個數，默認值為 3
# minSize & maxSize 	用來限制得到的目標區域範圍

# 1.2 表示每次影像尺寸減小的比例
# 3 表示每一個目標至少要被檢測到4次才算是真正的目標
# faces表示檢測到的人臉目標list

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列

"""

import cv2
from PIL import Image

ESC = 27

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
    # pass
    plt.show()


def cvshow(title, img):
    # pass
    cv2.imshow(title, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# OpenCV_顏色共同
RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測正面人臉 haarcascade_frontalface_default.xml
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

# 眼睛模型
eye_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
)

# 左眼模型
lefteye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lefteye_2splits.xml"

# 右眼模型
righteye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_righteye_2splits.xml"

# 嘴巴模型
mouth_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_mouth.xml"
)

# 鼻子模型
nose_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_nose.xml"
)

# 偵測上半身 haarcascade_upperbody.xml
upperbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_upperbody.xml"
)

# 正面的貓臉 haarcascade_frontalcatface.xml
frontalcatface_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalcatface.xml"
)

# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml
russian_plate_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"

# 偵測側面的人臉 haarcascade_profileface.xml
profileface_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_profileface.xml"
)

# 偵測身形 路人偵測 haarcascade_fullbody.xml
fullbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_fullbody.xml"
)

# 下半身
lowerbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lowerbody.xml"
)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face17.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/yalta1945.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/solvay1927a.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 共同 建立辨識物件

# 人臉偵測
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件 人臉

# 眼睛
eye_cascade_classifier = cv2.CascadeClassifier(eye_xml_filename)  # 建立辨識物件 眼睛

# 鼻子
nose_cascade_classifier = cv2.CascadeClassifier(nose_xml_filename)  # 建立辨識物件 鼻子

# 嘴巴
mouth_cascade_classifier = cv2.CascadeClassifier(mouth_xml_filename)  # 建立辨識物件 嘴巴

# 左眼
lefteye_cascade_classifier = cv2.CascadeClassifier(lefteye_xml_filename)  # 建立辨識物件 左眼

# 右眼
righteye_cascade_classifier = cv2.CascadeClassifier(righteye_xml_filename)  # 建立辨識物件 右眼

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def detect_face(img):
    # 圖形轉換 處理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

    # 人臉偵測
    # faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
    # faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)
    # faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)
    # faces = face_cascade_classifier.detectMultiScale(gray)
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200))
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (200, 200))
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # faces = face_cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200))

    """
    faces = face_cascade_classifier.detectMultiScale(
        # gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5)
        # gray, scaleFactor=1.15, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
        # gray, scaleFactor=1.15, minNeighbors=5, minSize=(20, 20)
        gray,
        scaleFactor=1.02,
        minNeighbors=3,
        minSize=(20, 20),
    )
    """

    faces = face_cascade_classifier.detectMultiScale(
        gray,  # 也可直接用 img 來偵測
        scaleFactor=1.2,
        minNeighbors=3,
        minSize=(32, 32),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    print("共找到 " + str(len(faces)) + " 張人臉")

    """
    for nn in range(len(faces)):
        print(nn)
        print(faces[nn])
        print(faces[nn][0], faces[nn][1], faces[nn][2], faces[nn][3])
    """

    # 把人臉框起來
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)  # 綠色框住人臉

    cv2.imshow("Image1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("人臉辨識 圖片")

img = cv2.imread(filename)  # 彩色讀取

detect_face(img)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多重偵測 臉 眼 鼻 嘴 左眼 右眼")

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face07.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"

img = cv2.imread(filename3)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 偵測人臉
faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
# 把人臉框起來
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    roi_gray = gray[y : y + h, x : x + w]  # 裁切, 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 裁切, 取出 ROI
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

# 偵測眼睛
eyes = eye_cascade_classifier.detectMultiScale(gray)  # 偵測眼睛
# 把眼睛框起來 G
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    # cv2.rectangle(roi_color, (x, y), (x + w, y + h), GREEN, 2)

# 偵測鼻子
noses = nose_cascade_classifier.detectMultiScale(gray)  # 偵測鼻子
# 把鼻子框起來 B
for x, y, w, h in noses:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

# 偵測嘴巴
mouths = mouth_cascade_classifier.detectMultiScale(gray)  # 偵測嘴巴
# 把嘴巴框起來 R
for x, y, w, h in mouths:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

# 偵測左眼
left_eyes = lefteye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 把左眼框起來 GREEN
for x, y, w, h in left_eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

# 偵測右眼
right_eyes = righteye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)
# 把右眼框起來 GREEN
for x, y, w, h in right_eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測右轉指示牌")

img = cv2.imread("data/traffic_sign1.jpg")  # 彩色讀取

turnR_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haar_turnR.xml"
turnR_cascade_classifier = cv2.CascadeClassifier(turnR_xml_filename)  # 建立辨識物件 右轉指示牌

turnRs = turnR_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30)
)
if len(turnRs) > 0:
    for x, y, w, h in turnRs:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
else:
    print("找不到 右轉指示牌")

plt.title("偵測右轉指示牌")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測上半身 haarcascade_upperbody.xml

upperbody_cascade_classifier = cv2.CascadeClassifier(
    upperbody_xml_filename
)  # 建立辨識物件 上半身

# pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"
# pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face02.jpg"

img = cv2.imread("data2/people1.jpg")  # 彩色讀取

bodies = upperbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Upperbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 正面的貓臉 haarcascade_frontalcatface.xml

frontalcatface_cascade_classifier = cv2.CascadeClassifier(
    frontalcatface_xml_filename
)  # 建立辨識物件 正面的貓臉

img = cv2.imread("data2/cat2.jpg")  # 彩色讀取

# 貓臉偵測
faces = frontalcatface_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 把貓臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Cat Face", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread("testCar/cartest1.jpg")

carplate_xml_filename = "haar_carplate.xml"  # 哈爾特徵檔路徑
carplate_cascade_classifier = cv2.CascadeClassifier(carplate_xml_filename)  # 讀哈爾特徵檔

# 執行辨識
plates = carplate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)

if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 裁切, 取出 ROI, 車牌影像
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
else:
    print("偵測車牌失敗")

cv2.imshow("Car1", img)  # 顯示所讀取的車輛
cv2.imshow("Car2", carplate)  # 顯示所讀取的車輛

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml

russian_plate_cascade_classifier = cv2.CascadeClassifier(
    russian_plate_xml_filename
)  # 建立辨識物件 俄羅斯車牌

img = cv2.imread("data2/car1.jpg")  # 彩色讀取
img = cv2.imread("data2/car2.jpg")  # 彩色讀取

plates = russian_plate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把車牌框起來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Car Plate", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測側面的人臉 haarcascade_profileface.xml

profileface_cascade_classifier = cv2.CascadeClassifier(
    profileface_xml_filename
)  # 建立辨識物件

img = cv2.imread("data2/s_1927.jpg")  # 彩色讀取

# 人臉偵測
faces = profileface_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)
print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Profile Face", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測身形 路人偵測 haarcascade_fullbody.xml

# img = cv2.imread("cars.jpg")# 彩色讀取
img = cv2.imread("data2/people2.jpg")  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

fullbody_cascade_classifier = cv2.CascadeClassifier(fullbody_xml_filename)  # 建立辨識物件 全身

# 偵測全身
# bodies = fullbody_cascade_classifier.detectMultiScale(gray, 1.1, 3)
bodies = fullbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Fullbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 下半身
lowerbody_cascade_classifier = cv2.CascadeClassifier(
    lowerbody_xml_filename
)  # 建立辨識物件 下半身

img = cv2.imread("data2/people1.jpg")  # 彩色讀取
bodies = lowerbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Lowerbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

# OpenCV 人臉識別分類器 LBP Cascase
lbpcascade_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
)
lbp_cascade_classifier = cv2.CascadeClassifier(lbpcascade_xml_filename)  # 建立辨識物件

img = cv2.imread(picture_filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

faces = lbp_cascade_classifier.detectMultiScale(gray, 1.2, 3)
print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/video1.avi"
# video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/video2.avi"

# 汽車模型
cars_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/cars.xml"
car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車

cap = cv2.VideoCapture(video_filename)

while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

    cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 1)

    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

    cv2.imshow("Video", img)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread("cars.jpg")# 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉灰階

car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車
cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 3)       # 偵測汽車

# 把汽車框起來
for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)   # 繪製外框

cv2.imshow("ImageShow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pytesseract

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(Image.open("data/atq9305.jpg"), config=config)
print(f"車號是 : {text}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

img = cv2.imread("car_plate/cartest1.jpg")

carplate_xml_filename = "haar_carplate.xml"  # 哈爾特徵檔路徑
carplate_cascade_classifier = cv2.CascadeClassifier(carplate_xml_filename)  # 讀哈爾特徵檔

# 執行辨識
plates = carplate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 裁切, 取出 ROI, 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛
text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

img = cv2.imread("car_plate/cartest3.jpg")

carplate_xml_filename = "haar_carplate.xml"  # 哈爾特徵檔路徑
carplate_cascade_classifier = cv2.CascadeClassifier(carplate_xml_filename)  # 讀哈爾特徵檔

# 執行辨識
plates = carplate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 裁切, 取出 ROI, 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛

text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

img = cv2.imread("car_plate/cartest3.jpg")

carplate_xml_filename = "haar_carplate.xml"  # 哈爾特徵檔路徑
carplate_cascade_classifier = cv2.CascadeClassifier(carplate_xml_filename)  # 讀哈爾特徵檔

# 執行辨識
plates = carplate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 裁切, 取出 ROI, 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛

ret, dst = cv2.threshold(carplate, 100, 255, cv2.THRESH_BINARY)  # 二值化
cv2.imshow("Car binary", dst)  # 顯示二值化車牌

text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

img = cv2.imread("car_plate/cartest3.jpg")

carplate_xml_filename = "haar_carplate.xml"  # 哈爾特徵檔路徑
carplate_cascade_classifier = cv2.CascadeClassifier(carplate_xml_filename)  # 讀哈爾特徵檔

# 執行辨識
plates = carplate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 裁切, 取出 ROI, 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛

ret, dst = cv2.threshold(carplate, 100, 255, cv2.THRESH_BINARY)  # 二值化
cv2.imshow("Car binary", dst)  # 顯示二值化車牌

kernel = np.ones((3, 3), np.uint8)
dst1 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)  # 執行開運算
text = pytesseract.image_to_string(dst1, config=config)  # 執行辨識
print(f"車號是 : {text}")

cv2.imwrite(carFile, dst)  # 寫入儲存
print("已存圖, 檔案 :", carFile)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("檢查兩圖之差異度")
# histogram() 計算圖形差異度

from PIL import Image
from functools import reduce
import operator

filename_face1 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("相同檔案, RMS = ", RMS)

filename_face1 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/data/_face/face02.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("不同檔案, RMS = ", RMS)

if RMS <= 100:  # 若差度在100內視為通過驗證
    print("通過驗證, RMS=%4.2f" % RMS)
else:
    print("臉譜不正確, RMS=%4.2f" % RMS)

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 若有多個視窗 要指名視窗名稱

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

# ----------------------------

key = cv2.waitKey(200)  # 0.2秒檢查一次
if key == ord("a") or key == ord("A"):  # 如果按A或a
    cv2.imwrite("tmp_photo.jpg", img)  # 存圖

# 把人臉框起來
for x, y, w, h in faces:
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測人臉 並模糊之

# 把人臉框起來
for x, y, w, h in faces:
    face = cv2.blur(frame[y : y + h, x : x + w], (25, 25))
    frame[y : y + h, x : x + w] = face

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測人臉 將其馬賽克")

# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(gray)
for x, y, w, h in faces:
    mosaic = frame[y : y + h, x : x + w]  # 裁切, 取出 ROI
    level = 15
    mh = int(h / level)
    mw = int(w / level)
    mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)
    mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y : y + h, x : x + w] = mosaic

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cv2.imwrite("tmp_atq9305.jpg", carplate)
print("已存圖, 檔案 : tmp_atq9305.jpg")

target_dir = "images"

# 準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    # os.makedirs(target_dir, exist_ok = True)

login_filename = "images/loginface.jpg"  # 登入者人臉檔案
login_filename2 = "images/loginface2.jpg"  # 登入者人臉檔案

cap = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

"""
while True:

    # k = cv2.waitKey(100)  #每0.1秒讀一次鍵盤
    k = cv2.waitKey(1)

        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉
        
        image1 = Image.open(user_filename).crop((x, y, x + w, y + h))  # 擷取人臉

        # 人臉偵測
        faces = face_cascade_classifier.detectMultiScale(
            img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉

        image1 = Image.open(login_filename).crop((x, y, x + w, y + h))  # 擷取人臉

# -----------------------------

            # 把人臉框起來
            for x, y, w, h in faces:
                cv2.rectangle(img_copy, (x, y), (x + w, y + h), GREEN, 2)  # 繪製矩形
                cv2.putText(  # 繪製倒數數字
                    img_copy,
                    str(cnter),
                    (x + int(w / 2), y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    YELLOW,
                    2,
                )
                filename = datetime.now().strftime("%Y-%m-%d %H.%M.%S")  # 時間格式化
                cv2.imwrite(filename + ".jpg", img)  # 存圖
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像直接存檔
# image.save("tmp_newface.jpg")  # 儲存檔案

# ------------------------------------------------------------------------------

# 眼睛
eyes = eye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

# 眼睛
eyes = eye_cascade_classifier.detectMultiScale(gray)  # 偵測眼睛

# 鼻子
noses = nose_cascade_classifier.detectMultiScale(gray)  # 偵測鼻子

# 嘴巴
mouths = mouth_cascade_classifier.detectMultiScale(gray)  # 偵測嘴巴

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測閉眼, 按 ESC 離開")

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    roi_gray = gray[y : y + h, x : x + w]  # 裁切, 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 裁切, 取出 ROI

    # 偵測到人臉再去偵測眼睛
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

    if eyes != ():
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), GREEN, 2)
            print("有睜眼")
    else:
        print("有閉眼")
        if closed.count == 3:
            print("警告 睡覺")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

for x, y, w, h in faces:
    mosaic = img[y : y + h, x : x + w]  # 取出 ROI  # 馬賽克區域

    img[y : y + h, x : x + w] = mosaic  # 將指定區域換成馬賽克區域

cv2.imshow("Image8", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) #彩色讀取直接轉灰階

gray = cv2.medianBlur(gray, 5)  # 模糊化去除雜訊

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.resize(img, (160, 160))  # 重製大小
image = cv2.resize(img, (int(frame.shape[1] / 2), int(frame.shape[0] / 2)))  # 調整畫面大小
image = cv2.resize(img, (640 // 2, 480 // 2))  # 縮小尺寸，加快辨識效率
image = img.resize((200, 200), Image.ANTIALIAS)  # 轉為解析度200x200
image = img.resize((200, 200), Image.LANCZOS)  # 轉為解析度200x200
image = img.resize((150, 150), Image.Resampling.LANCZOS)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cv2.circle(img, (int((x + x + w) / 2), int((y + y + h) / 2)), int(w / 2), RED, 2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

roi_color = img[y : y + h, x : x + w]  # 裁切, 取出 ROI
roi_gray = gray[y : y + h, x : x + w]  # 裁切, 取出 ROI

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
