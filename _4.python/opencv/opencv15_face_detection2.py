#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組

print("框出照片中的人臉")

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/ming_emperor3.jpg'

# OpenCV 人臉識別分類器
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

#image = cv2.imread(filename)	#讀取本機圖片
image = cv2.imread('demo.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 3)
faces = face_cascade_classifier.detectMultiScale(gray, 1.05, 4)

for (x, y, w, h) in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)

cv2.imshow('video', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


