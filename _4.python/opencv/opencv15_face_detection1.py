#OpenCV 人臉辨識

import cv2	#導入 OpenCV 模組

print("框出照片中的人臉")

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/human1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/YaltaSummit1945.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/SolvayConference1927.jpg'

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

#取得將使用的檔案名稱，並讀取圖檔，接著把圖檔透過轉換函式轉為灰階影像，定義框出人臉時的框顏色
print(filename)
filename1 = filename.split(".")[0] # 取得檔案名稱(不添加副檔名)
print(filename1)
image = cv2.imread(filename)	#讀取本機圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 透過轉換函式轉為灰階影像

# 調用偵測識別人臉函式
faces = face_classifier.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors = 3,
    minSize = (32, 32))

'''
print('共偵測到 ' + str(len(faces)) + ' 張人臉')
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

color = (0, 255, 0)  # 定義框的顏色

# 大於 0 則檢測到人臉
if len(faces):  
    # 繪製人臉部份的方框
    for face in faces: 
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x + h, y + w), color, 2)

# 顯示結果
#cv2.imshow(image)
cv2.imshow('New Picture', image) #顯示圖片

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

