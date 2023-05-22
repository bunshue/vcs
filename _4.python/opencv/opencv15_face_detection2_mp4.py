#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組
import numpy as np

print("框出照片中的人臉")

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'

# OpenCV 人臉識別分類器 Haar Cascase
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

'''
# OpenCV 人臉識別分類器 LBP Cascase
xml_filename2 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/lbpcascades/lbpcascade_frontalface.xml'
face_classifier = cv2.CascadeClassifier(xml_filename2)
'''

'''
#影片
vid = cv2.VideoCapture('spiderman.mp4')
#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 調用偵測識別人臉函式
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) == 27:
        break
vid.release()
'''

#圖片
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #設定圖片顏色, 先將圖片轉成灰階

# 調用偵測識別人臉函式
faces = face_classifier.detectMultiScale(gray, 1.2, 3)
#faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
#1.2 表示每次影像尺寸減小的比例
#3 表示每一個目標至少要被檢測到4次才算是真正的目標
#faces表示檢測到的人臉目標list

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

