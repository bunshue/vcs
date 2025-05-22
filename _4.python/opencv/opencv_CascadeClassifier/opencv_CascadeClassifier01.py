# OpenCV 人臉辨識

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

print("------------------------------------------------------------")  # 60個

# OpenCV 人臉識別分類器 Haar Cascase
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
# xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml"


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/SolvayConference1927.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg"

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/SolvayConference1927.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg"

print("------------------------------------------------------------")  # 60個

print("人臉辨識 圖片")

print("框出照片中的人臉, 轉成灰階再辨識, 畫框畫在原圖並顯示")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

image = cv2.imread(filename)  # 讀取本機圖片

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

print("共找到 " + str(len(faces)) + " 張人臉")

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

# cv2.imshow(image)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

# 應改用 "E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

#filename = "C:/_git/vcs/_4.python/opencv/data/_face/YaltaSummit1945.jpg"

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(filename)

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 臉部偵測
faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("框出照片中的人臉")

# OpenCV 人臉識別分類器
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

print("共找到 " + str(len(faces)) + " 張人臉")

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    # cv2.circle(image,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),(0,255,0),2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_43 人臉識別")

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 將圖片轉成灰階

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 載入人臉模型
faces = face_cascade_classifier.detectMultiScale(gray)  # 偵測人臉

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(filename)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)
# faces = face_cascade_classifier.detectMultiScale(
# gray,
# scaleFactor=1.1,
# minNeighbors=5,
# minSize=(30, 30),
# )

# Draw a rectangle around the faces
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個






# 以上為單純圖片的人臉辨識
#sys.exit()

print("OpenCV_ai_44 人臉識別 把人臉馬賽克掉")

img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 影像轉換成灰階

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 載入人臉偵測模型

faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)  # 開始辨識影像中的人臉

for x, y, w, h in faces:
    mosaic = img[y : y + h, x : x + w]  # 馬賽克區域
    level = 15  # 馬賽克程度
    mh = int(h / level)  # 根據馬賽克程度縮小的高度
    mw = int(w / level)  # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)  # 先縮小
    mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y : y + h, x : x + w] = mosaic  # 將指定區域換成馬賽克區域

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("人臉辨識 圖片 臉 眼")

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

# 繪製人臉部份的方框
color = (255, 0, 0)  # 定義框的顏色
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

# 繪製眼睛部份的方框
color = (0, 255, 0)  # 定義框的顏色
for ex, ey, ew, eh in eyes:
    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), color, 2)

# cv2.imshow(image)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("人臉辨識 圖片 眼 嘴 鼻")

# 眼睛模型
eye_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"

# 嘴巴模型
mouth_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_mcs_mouth.xml"

# 鼻子模型
nose_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_mcs_nose.xml"

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face07.jpg"
img = cv2.imread(filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 圖片轉灰階
# gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

eye_cascade = cv2.CascadeClassifier(eye_filename)  # 使用眼睛模型
eyes = eye_cascade.detectMultiScale(gray)  # 偵測眼睛

for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 標記綠色方框

mouth_cascade = cv2.CascadeClassifier(mouth_filename)  # 使用嘴巴模型
mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴
for x, y, w, h in mouths:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 標記紅色方框

nose_cascade = cv2.CascadeClassifier(nose_filename)  # 使用鼻子模型
noses = nose_cascade.detectMultiScale(gray)  # 偵測鼻子
for x, y, w, h in noses:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 標記藍色方框

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_48")
""" lack file
# lack test file
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
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗
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
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
img = cv2.imread(filename)  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
#print(faces)
print("共找到 " + str(len(faces)) + " 張人臉")

# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Image", img)  # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print('bbb')
#xml_filename = r"C:\_git\vcs\_4.python\_data\lbpcascade_frontalface.xml"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print('ccc')
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

img = cv2.imread(filename)  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉

cv2.imshow("Image", img)  # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print('ddd')
if not os.path.exists("facedata"):  # 如果不存在資料夾
    os.mkdir("facedata")  # 就建立facedata

#xml_filename = r"haarcascade_frontalface_alt2.xml"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
img = cv2.imread(filename)  # 讀取影像
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)  # 偵測影像
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
# 同時將影像儲存在facedata資料夾, 但是必須先建立此資料夾
num = 1  # 檔名編號
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    filename = "facedata\\face" + str(num) + ".jpg"  # 路徑 + 檔名
    imageCrop = img[y : y + h, x : x + w]  # 裁切
    imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
    cv2.imwrite(filename, imageResize)  # 存圖
    num += 1  # 檔案編號

cv2.imshow("Image", img)  # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

print("檢查兩圖之差異度")

from functools import reduce
import operator

filename_face1 = "C:/_git/vcs/_4.python/opencv/opencv_CascadeClassifier/facedata/face1.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/opencv_CascadeClassifier/facedata/face1.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()
RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)

filename_face1 = "C:/_git/vcs/_4.python/opencv/opencv_CascadeClassifier/facedata/face1.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/opencv_CascadeClassifier/facedata/face2.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# OpenCV 人臉辨識 影片

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

"""
# OpenCV 人臉識別分類器 LBP Cascase
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/lbpcascades/lbpcascade_frontalface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
"""

# 影片
vid = cv2.VideoCapture(video_filename)

# In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    if ret == True:
        # frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2))) #調整畫面大小
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 調用偵測識別人臉函式
        faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Video", frame)  # 顯示圖片, 彩色

        k = cv2.waitKey(1)
        if k == 27:  # ESC
            break
        elif k == ord("q"):  # 若按下 q 鍵則離開迴圈
            break
        elif k == ord("s"):  # 若按下 s 鍵則存圖
            image_filename = (
                "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
            )
            cv2.imwrite(image_filename, frame)  # 存圖
            print("已存圖")
    else:
        break

# 釋放所有資源
vid.release()
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('用到 Webcam')
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Image")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Image", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_faceout.jpg")  # 存圖

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from functools import reduce
import operator

ID = input("請輸入身份證字號 = ")  # 讀取所輸入的身分證字號
face = ID + ".jpg"  # 未來的臉形檔案

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Image")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Image", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_newface.jpg")  # 儲存檔案

print("檢查兩圖之差異度")
h1 = Image.open(face).histogram()
h2 = Image.open("tmp_newface.jpg").histogram()
RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
if RMS <= 100:
    print("歡迎出入境")
else:
    print("比對失敗")

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個

ID = input("請輸入身份證字號 = ")  # 讀取所輸入的身分證字號
print("臉形檔案將儲存在 ", ID + ".jpg")
faceFile = "tmp_" + ID + ".jpg"  # 未來的臉形檔案

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Image")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Image", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save(faceFile)  # 儲存檔案

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
WebCam 使用
一般使用
人臉辨識
"""
print("按 ESC 或 Q 離開")
print("按 S 存圖")

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

    # print("共找到 " + str(len(faces)) + " 張人臉")
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
        cv2.imwrite(image_filename, frame)  # 存圖
        print("已存圖, 檔案 :", filename)

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import operator
from functools import reduce

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

target_dir = "images"

# 準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    # os.makedirs(target_dir, exist_ok = True)

user_filename = "images/recogface.jpg"  # 使用者人臉檔案
user_filename2 = "images/recogface2.jpg"  # 使用者人臉檔案
login_filename = "images/loginface.jpg"  # 登入者人臉檔案
login_filename2 = "images/loginface2.jpg"  # 登入者人臉檔案

cap = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    cv2.imshow("Image", frame)  # 顯示圖片, 原圖

    # k = cv2.waitKey(100)  #每0.1秒讀一次鍵盤
    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break
    elif k == ord("C"):
        print("建立使用者資料")
        cv2.imwrite(user_filename, frame)  # 存檔
        image = cv2.imread(user_filename)  # 讀檔做人臉辨識
        faces = face_cascade_classifier.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉
        image1 = Image.open(user_filename).crop((x, y, x + w, y + h))  # 擷取人臉
        # image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  # 轉為解析度200x200
        image1.save(user_filename2)  # 存檔

    elif k == ord("c"):
        print("比對登入者")
        if not os.path.exists(user_filename2):  # 如果使用者人臉檔案不存在
            print("請先建立使用者資料")
            continue
        cv2.imwrite(login_filename, frame)  # 存檔
        image = cv2.imread(login_filename)  # 讀檔做人臉辨識
        faces = face_cascade_classifier.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉
        image1 = Image.open(login_filename).crop((x, y, x + w, y + h))  # 擷取人臉
        # image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  # 轉為解析度200x200
        image1.save(login_filename2)  # 存檔

        pic1 = Image.open(user_filename2)  # 開啟使用者人臉檔案
        pic2 = Image.open(login_filename2)  # 開啟登入者人臉檔案
        h1 = pic1.histogram()  # 計算圖形差異度
        h2 = pic2.histogram()
        diff = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
        )
        if diff <= 100:  # 若差度在100內視為通過驗證
            print("通過驗證，歡迎使用本系統！ diff=%4.2f" % diff)
        else:
            print("臉譜不正確，無法使用本系統！ diff=%4.2f" % diff)


# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# webcam臉部偵測

# 建立臉部辨識物件
face_detector = cv2.CascadeClassifier(xml_filename)
capture = cv2.VideoCapture(0)  # 開啟標號 0 的攝影機
while capture.isOpened():
    sucess, img = capture.read()  # 讀取攝影機影像
    if sucess:
        faces = face_detector.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)
        )  # 從攝影機影像中偵測人臉
        for x, y, w, h in faces:  # 畫出人臉位置
            cv2.rectangle(
                img, (x, y), (x + w, y + h), (0, 255, 255), 2
            )  # 繪製黃色線寬為 2 的矩形
        cv2.imshow("Frame", img)
    k = cv2.waitKey(1)  # 讀取按鍵輸入 (若無會傳回 -1)
    if k == ord("q") or k == ord("Q"):  # 若按下 q 結束迴圈
        print("exit")
        cv2.destroyAllWindows()
        capture.release()
        break
else:
    print("開啟攝影機失敗")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# webcam偵測人臉 並模糊之

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # 偵測人臉
    face_rects = face_cascade_classifier.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=3
    )

    for x, y, w, h in face_rects:
        face = cv2.blur(frame[y : y + h, x : x + w], (25, 25))
        frame[y : y + h, x : x + w] = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測閉眼, 按 ESC 離開")

from functools import wraps

lastsave = 0


def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        global lastsave
        if time.time() - lastsave > 3:
            # this is in seconds, so 5 minutes = 300 seconds
            lastsave = time.time()
            tmp.count = 0
        return func(*args, **kwargs)

    tmp.count = 0
    return tmp


xml_filename1 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename1)

xml_filename2 = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml"
eye_cascade_classifier = cv2.CascadeClassifier(xml_filename2)

cap = cv2.VideoCapture(0)


@counter
def closed():
    print("Eye Closed")


def openeye():
    print("Eye is Open")


def warning():
    print("Sleeping~~~~")


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]

        eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

        if eyes is not ():
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                openeye()
        else:
            closed()
            if closed.count == 3:
                warning()

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == 27:  # ESC
        break
    elif k == ord("s"):  # 若按下 s 鍵則存圖
        image_filename = (
            "Image_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".jpg"
        )
        cv2.imwrite(image_filename, frame)  # 存圖
        print("已存圖")

# 釋放所有資源
cap.release()  # 釋放攝影機
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
face_cascade_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y : y + w, x : x + w]
        roi_color = frame[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()  # 關閉所有 OpenCV 視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_63 偵測人臉")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)
# faces = face_cascade_classifier.detectMultiScale(gray)

while True:
    ret, frame = cap.read()

    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 將鏡頭影像轉換成灰階
    faces = face_cascade_classifier.detectMultiScale(gray)  # 偵測人臉
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 標記人臉

    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_65 偵測人臉 將其馬賽克")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，避免尺寸過大導致效能不好
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

    cv2.imshow("WebCam", frame)

    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

eye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_eye.xml"
nose_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_mcs_nose.xml"
mouth_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_mcs_mouth.xml"

print("OpenCV_ai_67 偵測眼睛R鼻子G嘴巴B")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

eye_cascade = cv2.CascadeClassifier(eye_xml_filename)  # 使用眼睛模型
nose_cascade = cv2.CascadeClassifier(nose_xml_filename)  # 使用鼻子模型
mouth_cascade = cv2.CascadeClassifier(mouth_xml_filename)  # 使用嘴巴模型

while True:
    ret, frame = cap.read()

    # img = cv2.resize(frame, (640//2, 480//2))
    img = frame

    gray = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    eyes = eye_cascade.detectMultiScale(gray)  # 偵測眼睛R
    for x, y, w, h in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    noses = nose_cascade.detectMultiScale(gray)  # 偵測鼻子G
    for x, y, w, h in noses:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    mouths = mouth_cascade.detectMultiScale(gray)  # 偵測嘴巴B
    for x, y, w, h in mouths:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

""" NG 無檔案 face.yml 人臉模型檔
print("OpenCV_ai_71")

recognizer = cv2.face.LBPHFaceRecognizer_create()  # 啟用訓練人臉模型方法

# NG 無檔案
# recognizer.read('face.yml')                               # 讀取人臉模型檔

xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascade_frontalface_default.xml"
)

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 啟用人臉追蹤

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    #img = cv2.resize(img, (640//2, 480//2))  # 縮小尺寸，加快辨識效率
    
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

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測右轉指示牌")

img = cv2.imread("pic_turnR.jpg")
detector = cv2.CascadeClassifier("haar_turnR.xml")
signs = detector.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30)
)
if len(signs) > 0:
    for x, y, w, h in signs:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
else:
    print("nothing")

cv2.imshow("Frame", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個

#若有多個視窗 要指名視窗名稱

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)


'''

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

    face_rects = face_cascade_classifier.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=4
    )

    for x, y, w, h in face_rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

'''
