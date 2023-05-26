'''
WebCam 使用
一般使用

人臉辨識

目前 webcam 僅 x64 電腦可用
'''

import cv2
import sys

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

name = "webcam"
number = 0

cap = cv2.VideoCapture(0)

# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

if not cap.isOpened():
    print('Could not open video device')
    sys.exit()
else:
    print('Video device opened')

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像

    if ret == False:
      print('無影像, 離開')
      break

    #frame = cv2.resize(frame,(int(frame.shape[1] / 2), int(frame.shape[0] / 2))) #調整畫面大小
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5, minSize = (200, 200))
    faces = face_classifier.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)
    #將抓到的人像標記並存檔
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        number += 1
        cv2.imwrite("{}.{}.jpg".format(name, number), gray[y:y + h, x:x + w])
        cv2.waitKey(100)

    cv2.imshow('WebCam', frame)    # 顯示圖片, 彩色
    cv2.waitKey(1)

    if number >= 10:
        break

    k = cv2.waitKey(1)
    if k == 27:     #ESC
        break
    elif k == ord('q'): # 若按下 q 鍵則離開迴圈
        break
    elif k == ord('s'): # 若按下 s 鍵則存圖
        image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
        cv2.imwrite(image_filename, frame)
        print('已存圖')

# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

