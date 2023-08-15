filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

import numpy as np
import cv2

#face_cascade_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#eye_cascade_classifier = cv2.CascadeClassifier("haarcascade_eye.xml")

xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename1)

xml_filename2 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_eye.xml'
eye_cascade_classifier = cv2.CascadeClassifier(xml_filename2)

#save the image(i) in the same directory

img = cv2.imread(filename)	#讀取本機圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


