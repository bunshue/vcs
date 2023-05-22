import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'

# OpenCV 人臉識別分類器
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'

faceCascade = cv2.CascadeClassifier(xml_filename)
image = cv2.imread(filename)
faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
#image.shape[0]:圖片高度，image.shape[1]:圖片寬度
cv2.rectangle(image, (10,image.shape[0]-20), (110,image.shape[0]), (0,0,0), -1)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(128,255,0),2)

print('共找到 : ' + str(len(faces)) + ' 張圖')

cv2.namedWindow("facedetect")
cv2.imshow("facedetect", image)

cv2.waitKey(0)
cv2.destroyWindow("facedetect")# 關閉 OpenCV 視窗

