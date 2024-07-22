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
