import cv2
import numpy as np

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

vid = cv2.VideoCapture(video_filename)

#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) == 27:
        break

vid.release()
cv2.destroyAllWindows()
    

    


