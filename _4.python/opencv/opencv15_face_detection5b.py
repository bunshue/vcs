import cv2
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'

# OpenCV 人臉識別分類器
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(xml_filename)
image = cv2.imread(filename)
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
count = 1
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), (128,255,0), 2)
    filename2 = "media\\face" + str(count)+ ".jpg"
    image1 = Image.open(filename)   #使用PIL
    image2 = image1.crop((x, y, x+w, y+h))
    image3 = image2.resize((200, 200), Image.ANTIALIAS)
    image3.save(filename2)
    count += 1

cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)

cv2.waitKey(0)
cv2.destroyWindow("facedetect")# 關閉 OpenCV 視窗

