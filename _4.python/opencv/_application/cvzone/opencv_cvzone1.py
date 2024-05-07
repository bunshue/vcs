"""
使用 CVZone 人臉偵測

FaceDetector
FaceMeshDetector


"""

print("------------------------------------------------------------")  # 60個

import cv2
import mediapipe as mp
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg'

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#使用 CVZone 之 FaceDetector

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg'

img = cv2.imread(filename)
detector = FaceDetector(minDetectionCon=0.5) #信心50%
img, faces = detector.findFaces(img)

if faces:
    print("偵測到人臉數:", len(faces))
else:
    print("未偵測到人臉")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

detector = FaceDetector()
img, faces = detector.findFaces(img, draw=False)
if faces:
    print("偵測到人臉數:", len(faces))
else:
    print("未偵測到人臉")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
detector = FaceDetector()
img, faces = detector.findFaces(img)
if faces:
    print("偵測到人臉數:", len(faces))
    face = faces[0]
    print("id:", face["id"])
    print("bbox:", face["bbox"])
    print("score:", face["score"])
    print("center:", face["center"])

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
detector = FaceDetector()
img, faces = detector.findFaces(img)
if faces:
    print("偵測到人臉數:", len(faces))
    face = faces[0]
    print("id:", face["id"])
    print("bbox:", face["bbox"])
    print("score:", int(face["score"][0] * 100), "%")
    print("center:", face["center"])

print("------------------------------------------------------------")  # 60個

print('取得臉部的關鍵座標, 6個')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'

img = cv2.imread(filename)
detector = FaceDetector()
img, faces = detector.findFaces(img)
if faces:
    keypoints = detector.getFaceKeypoints(img, face_idx=0)
    print(keypoints)
    for keypoint in keypoints:
        cv2.circle(img, keypoint["keypoint"], 5, (255, 0, 255), cv2.FILLED)
else:
    print("未偵測到人臉")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('裁剪出臉部的部分影像')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg'

img = cv2.imread(filename)
detector = FaceDetector()
img, faces = detector.findFaces(img)
if faces:
    for face in faces:
        x, y, w, h = face["bbox"]
        face = img[y:y+h, x:x+w]
        cv2.imshow("Non Padded", face)
        padding = 50
        padded_face = img[y-padding:y+h+padding,x-padding:x+w+padding] 
        cv2.imshow("Padded", padded_face)
        #cv2.waitKey(0)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('Webcam人臉偵測')

cap = cv2.VideoCapture(0)
detector = FaceDetector()
while cap.isOpened():
    success, img = cap.read()
    img, faces = detector.findFaces(img)
    if faces:
        center = faces[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        
    cv2.imshow("Faces", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils 
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = face_detection.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=5)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        print('aaaa')
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(image=image, landmark_list=face_landmarks, 
                connections=mp_face_mesh.FACEMESH_CONTOURS, landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#使用 CVZone 之 FaceMeshDetector 臉部網格 

print("------------------------------------------------------------")  # 60個

print('人臉偵測和匯出3D臉部網格')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates48.jpg'

img = cv2.imread(filename)
detector = FaceMeshDetector(maxFaces=2, minDetectionCon=0.5,
                            minTrackCon=0.5)
img, faces = detector.findFaceMesh(img)
if faces:
   print(len(faces[0]))
   
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('取得臉部網格的點座標')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates48.jpg'

img = cv2.imread(filename)
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
   print(len(faces[0]))
   for point in faces[0]:
       cv2.circle(img, point, 1, (255, 0, 255), cv2.FILLED)    
   
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('取得臉部特徵資訊')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates48.jpg'

img = cv2.imread(filename)
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1)  
    face_leye = detector.getFacePart(img, 0, "LEFT_EYE")
    points = np.array(face_leye, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1)     
  
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('計算臉部特徵的尺寸')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates48.jpg'
img = cv2.imread(filename)

detector = FaceMeshDetector(maxFaces=8)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_leye = detector.getFacePart(img, 0, "LEFT_EYE")
    height_leye, width_leye = detector.getFacePartSize(face_leye)
    print("LEFT_EYE:", width_leye, height_leye)
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    height_oval, width_oval = detector.getFacePartSize(face_oval)
    print("FACE OVAL:", width_oval, height_oval)
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1)  
    points = np.array(face_leye, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1)     

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('即時顯示臉部網格')

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
while cap.isOpened():
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
    cv2.imshow("Faces", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#使用 CVZone 之 FaceMeshDetector 臉部網格 

print("------------------------------------------------------------")  # 60個

print('CVZone辨識臉部表情 : 張嘴或閉嘴')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg'

img = cv2.imread(filename)
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_lips = detector.getFacePart(img, 0, "LIPS")
    height_lips, width_lips = detector.getFacePartSize(face_lips)
    print(width_lips, height_lips)
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    height_oval, width_oval = detector.getFacePartSize(face_oval)
    print(width_oval, height_oval)
    if (height_lips/height_oval)*100 > 15:
        msg = 'Mouth OPEN'
    else:
        msg = 'Mouth CLOSE'
    points = np.array(face_lips, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1) 
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1) 
    cv2.putText(img, msg, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('CVZone辨識臉部表情 : 開眼或閉眼')

filename = 'C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates17.jpg'

img = cv2.imread(filename)
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_leye = detector.getFacePart(img, 0, "LEFT_EYE")
    height_leye, width_leye = detector.getFacePartSize(face_leye)
    print(width_leye, height_leye)
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    height_oval, width_oval = detector.getFacePartSize(face_oval)
    print(width_oval, height_oval)
    if (height_leye/height_oval)*100 > 5:
        msg = 'Eye OPEN'
    else:
        msg = 'Eye CLOSE'       
    points = np.array(face_leye, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1)     
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1) 
    cv2.putText(img, msg, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



