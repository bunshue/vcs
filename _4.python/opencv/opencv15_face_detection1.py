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

image = cv2.imread(filename)	#讀取本機圖片
#image.shape[0]:圖片高度，image.shape[1]:圖片寬度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 透過轉換函式轉為灰階影像

#gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

# 調用偵測識別人臉函式
faces = face_cascade_classifier.detectMultiScale(
    gray,   #也可直接用 image 來偵測
    scaleFactor = 1.2,
    minNeighbors = 3,
    minSize = (32, 32),
    flags = cv2.CASCADE_SCALE_IMAGE)

print('共偵測到 ' + str(len(faces)) + ' 張人臉')
'''
for nn in range(len(faces)):
    print(nn)
    print(faces[nn])
    print(faces[nn][0], faces[nn][1], faces[nn][2], faces[nn][3])
'''

#參數
#image 	        待檢測圖片，一般為灰階影像，以便加快偵測速度
#scaleFactor 	在前後兩次相繼的掃描中，搜索範圍的比例係數，默認值為 1.1
#minNeighbors 	構成偵測目標的相鄰矩形的最小個數，默認值為 3
#minSize & maxSize 	用來限制得到的目標區域範圍

#1.2 表示每次影像尺寸減小的比例
#3 表示每一個目標至少要被檢測到4次才算是真正的目標
#faces表示檢測到的人臉目標list

# 繪製人臉部份的方框
color = (0, 255, 0)  # 定義框的顏色
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = image[y : y + h, x : x + w]

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')

# 釋放所有資源
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗


