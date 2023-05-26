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

face_cascade = cv2.CascadeClassifier(xml_filename)
# Read the image
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 調用偵測識別人臉函式
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.25,
    minNeighbors=2,
    minSize=(30, 30),
)
print('Found {0} faces!'.format(len(faces)))
# Draw a rectangle around the faces
# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

print('共找到 : ' + str(len(faces)) + ' 張圖')

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

