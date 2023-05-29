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
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

image = cv2.imread(filename)
#image.shape[0]:圖片高度，image.shape[1]:圖片寬度

# 調用偵測識別人臉函式
faces = face_cascade_classifier.detectMultiScale(
    image,
    scaleFactor = 1.2,
    minNeighbors = 3,
    minSize = (32, 32),
    flags = cv2.CASCADE_SCALE_IMAGE)

print('共偵測到 ' + str(len(faces)) + ' 張人臉')

# 繪製人臉部份的方框
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x, y), (x + w, y + h), (0, 255, 255), 2)

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

