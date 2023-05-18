#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

image = cv2.imread(filename)	#讀取本機圖片
#cv2.imshow('Original Picture', image) #顯示圖片

#灰階
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#人臉辨識
faces = face_classifier.detectMultiScale(
    gray,
    scaleFactor=1.08,
    minNeighbors=6,
    minSize=(25, 25))

print('共偵測到 ' + str(len(faces)) + ' 張人臉')
for nn in range(len(faces)):
    print(nn)
    print(faces[nn])
    print(faces[nn][0], faces[nn][1], faces[nn][2], faces[nn][3])


color = (0, 255, 0)  # 定義框的顏色

# 大於 0 則檢測到人臉
if len(faces):  
    # 繪製人臉部份的方框
    for face in faces: 
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x + h, y + w), color, 2)

''' 不知道是否筆誤
# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + h, y + w), (0, 255, 255), 2)
'''

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

