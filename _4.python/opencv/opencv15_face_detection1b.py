#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/______test_files1/_emgu/lena.jpg'
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
img = cv2.imread(filename)	#讀取本機圖片
cv2.imshow('Original Picture', img) #顯示圖片

#灰階
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#人臉辨識
faces = face_cascade.detectMultiScale(
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


