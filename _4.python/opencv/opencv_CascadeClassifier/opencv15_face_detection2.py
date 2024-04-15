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

print("框出照片中的人臉")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/SolvayConference1927.jpg'
# filename = 'C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg'

# OpenCV 人臉識別分類器
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default333.xml"
# face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

# 讀取待檢測的圖像
image = cv2.imread(filename)
# 獲取xml文件,加載人臉檢測器
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
# 色彩轉換，轉換為灰度圖像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 調用函數detectMultiScale
faces = face_cascade_classifier.detectMultiScale(
    gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5)
)
print(faces)
# 打印輸出測試結果
print("發現{0}個人臉!".format(len(faces)))
# 逐個標記人臉
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)  # 矩形標注
    # cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)

# 顯示結果
cv2.imshow("dect", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_43 人臉識別")

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)   # 載入人臉模型
faces = face_cascade_classifier.detectMultiScale(gray)    # 偵測人臉

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('ImageShow', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_44 人臉識別 把人臉馬賽克掉")

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename) # 載入人臉偵測模型
faces = face_cascade_classifier.detectMultiScale(gray,1.2,3)  # 開始辨識影像中的人臉

for (x, y, w, h) in faces:
    mosaic = img[y:y+h, x:x+w]   # 馬賽克區域
    level = 15                   # 馬賽克程度
    mh = int(h/level)            # 根據馬賽克程度縮小的高度
    mw = int(w/level)            # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw,mh), interpolation=cv2.INTER_LINEAR) # 先縮小
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y:y+h, x:x+w] = mosaic   # 將指定區域換成馬賽克區域

cv2.imshow('ImageShow', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_45 偵測 眼 嘴 鼻")

#眼睛模型
eye_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml'

#嘴巴模型
mouth_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_mcs_mouth.xml'

#鼻子模型
nose_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_mcs_nose.xml'

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face07.jpg'
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 圖片轉灰階
#gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier(eye_filename)  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)                       # 偵測眼睛
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)      # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier(mouth_filename)  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)                           # 偵測嘴巴
for (x, y, w, h) in mouths:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)              # 標記紅色方框

nose_cascade = cv2.CascadeClassifier(nose_filename)    # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)                             # 偵測鼻子
for (x, y, w, h) in noses:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)              # 標記藍色方框

cv2.imshow('ImageShow', img)
cv2.waitKey(0)   # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_48")
""" lack file
# lack test file
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(xml_filename)  # 載入人臉追蹤模型
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

for i in range(1,31):
    img = cv2.imread(f'face01/{i}.jpg')           # 依序開啟每一張蔡英文的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄蔡英文人臉對應的 id，只能是整數，都是 1 表示蔡英文的 id 為 1

for i in range(1,16):
    img = cv2.imread(f'face02/{i}.jpg')           # 依序開啟每一張川普的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    face = detector.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in face:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄川普人臉的位置和大小內像素的數值
        ids.append(2)                             # 記錄川普人臉對應的 id，只能是整數，都是 2 表示川普的 id 為 2

print('training...')                              # 提示開始訓練
recog.train(faces,np.array(ids))                  # 開始訓練
recog.save('face.yml')                            # 訓練完成儲存為 face.yml
print('ok!')
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_46")
"""
# lack file
img = cv2.imread('cars.jpg')                    # 讀取街道影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像

car = cv2.CascadeClassifier("cars.xml")    # 讀取汽車模型
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
cars = car.detectMultiScale(gray, 1.1, 3)       # 偵測汽車
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框

cv2.imshow('ImageShow', img)
cv2.waitKey(0) # 按下任意鍵停止
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_ai_47")

""" lack file
img = cv2.imread('cars.jpg')                    # 讀取街道影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 轉換成黑白影像

car = cv2.CascadeClassifier("haarcascade_fullbody.xml")    # 讀取人體模型
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊
cars = car.detectMultiScale(gray, 1.1, 3)       # 偵測行人
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)   # 繪製外框

cv2.imshow('ImageShow', img)
cv2.waitKey(0)     # 按下任意鍵停止
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


