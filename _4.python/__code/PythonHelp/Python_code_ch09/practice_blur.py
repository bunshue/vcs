"""

webcam偵測人臉 並模糊之~~~~


"""
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
