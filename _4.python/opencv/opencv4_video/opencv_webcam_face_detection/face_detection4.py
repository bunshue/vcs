"""

webcam臉部偵測

"""

import sys
import cv2

print("------------------------------------------------------------")  # 60個

xml_filename = r'C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml'

print("------------------------------------------------------------")  # 60個


# 建立臉部辨識物件
face_detector = cv2.CascadeClassifier(xml_filename)
capture = cv2.VideoCapture(0)                   # 開啟標號 0 的攝影機
while capture.isOpened():
    sucess, img = capture.read()            # 讀取攝影機影像
    if sucess:
        faces = face_detector.detectMultiScale(img,
                                               scaleFactor=1.1,
                                               minNeighbors=5,
                                               minSize=(200, 200))    # 從攝影機影像中偵測人臉
        for (x, y, w, h) in faces:          # 畫出人臉位置
            cv2.rectangle(img, (x, y), (x+w, y+h),
                          (0, 255, 255), 2)    # 繪製黃色線寬為 2 的矩形
        cv2.imshow('Frame', img)
    k = cv2.waitKey(1)          # 讀取按鍵輸入 (若無會傳回 -1)
    if k == ord('q') or k == ord('Q'):     # 若按下 q 結束迴圈
        print('exit')
        cv2.destroyAllWindows()
        capture.release()
        break
else:
    print('開啟攝影機失敗')



print("------------------------------------------------------------")  # 60個

import cv2

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)

while True:
    # 偵測人臉
    _, frame = cap.read()
    face_rects = face_cascade_classifier.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=4)    

    for (x, y, w, h) in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # 顯示畫面
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 退出視訊鏡頭
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#webcam偵測人臉 並模糊之

import cv2

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
# xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #偵測人臉
    face_rects = face_cascade_classifier.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors = 3)
    
    for (x, y, w, h) in face_rects:
        face = cv2.blur(frame[y:y + h, x:x + w], (25, 25))
        frame[y:y + h, x: x + w] = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
