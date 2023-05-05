#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

img = cv2.imread(filename)	#讀取本機圖片
cv2.imshow('Original Picture', img) #顯示圖片

#灰階
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#人臉辨識
faces = face_classifier.detectMultiScale(
    gray,
    scaleFactor=1.08,
    minNeighbors=6,
    minSize=(10, 10))
    
# 繪製人臉部份的方框（能不能不要方匡啊，要輪廓就好）
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# 顯示成果
#cv2.imshow(img)
cv2.imshow('New Picture', img) #顯示圖片


