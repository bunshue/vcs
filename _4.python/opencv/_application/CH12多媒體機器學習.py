import cv2
import mediapipe as mp
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.PoseModule import PoseDetector

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

#MediaPipe模組：Google多媒體機器學習

"""
!wget -O person1.jpg --content-disposition https://unsplash.com/photos/3g3grQaeA2o/download?force=true
!wget -O person2.jpg --content-disposition https://unsplash.com/photos/GVVsC0JG6Ak/download?force=true
"""

print("臉部偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

image = resizeimg(cv2.imread('person1.jpg'))
# image = resizeimg(cv2.imread('person2.jpg'))
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils 
face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# print(results.detections)
if results.detections:
    for detection in results.detections:
        # print('鼻子:')
        # print(mp_face_detection.get_key_point(detection,mp_face_detection.FaceKeyPoint.NOSE_TIP))
        mp_drawing.draw_detection(image, detection)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

#!wget -O person3.jpg --content-disposition https://unsplash.com/photos/JyVcAIUAcPM/download?force=true

print("臉部特徵網")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

image = resizeimg(cv2.imread('person3.jpg'))
# image = resizeimg(cv2.imread('person1.jpg'))
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=5, min_detection_confidence=0.5)
results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image=image, landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

"""
!wget -O hand1.jpg --content-disposition https://unsplash.com/photos/33VdiGc2O9o/download?force=true
!wget -O hand2.jpg --content-disposition https://unsplash.com/photos/qKspdY9XUzs/download?force=true
"""

print("手部偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

# image = resizeimg(cv2.imread('hand1.jpg'))
image = resizeimg(cv2.imread('hand2.jpg'))
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, 
		min_detection_confidence=0.5)
results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        # print('姆指尖：', hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP])
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

"""
!wget -O pose1.jpg --content-disposition https://unsplash.com/photos/A3MleA0jtoE/download?force=true
!wget -O pose2.jpg --content-disposition https://unsplash.com/photos/wa8o6rs22Fw/download?force=true
"""

print("姿勢偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

image = resizeimg(cv2.imread('pose1.jpg'))
# image = resizeimg(cv2.imread('pose2.jpg'))
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, model_complexity=1, 
		min_detection_confidence=0.5)
results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if results.pose_landmarks:
    # print('鼻子：', results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE])
    mp_drawing.draw_landmarks(image, results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

print("人體整合偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

image = resizeimg(cv2.imread('pose1.jpg'))
# image = resizeimg(cv2.imread('pose2.jpg'))
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=True, model_complexity=1)
results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if results.pose_landmarks:
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

"""
!wget -O object1.jpg --content-disposition https://unsplash.com/photos/kvmdsTrGOBM/download?force=true
!wget -O object2.jpg --content-disposition https://unsplash.com/photos/rhcllVy2zBU/download?force=true
"""
"""fail

print("3D物體偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

image = resizeimg(cv2.imread('object1.jpg'))
# image = resizeimg(cv2.imread('object2.jpg'))
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
objectron = mp_objectron.Objectron(static_image_mode=True, max_num_objects=5, min_detection_confidence=0.5, model_name='Chair')

results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
if results.detected_objects:
    for detected_object in results.detected_objects:
        mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
        mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
"""
print('------------------------------------------------------------')	#60個

#cvzone模組：簡單易用多媒體機器學習

"""
!pip install cvzone==1.3.7
!pip install mediapipe==0.8.6
"""

print("臉部偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

img = resizeimg(cv2.imread('person1.jpg'))
# img = resizeimg(cv2.imread('person2.jpg'))
detector = FaceDetector()
img, bboxs = detector.findFaces(img)
# print('人臉範圍：', bboxs)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

print("臉部特徵網")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

img = resizeimg(cv2.imread('person1.jpg'))
# img = resizeimg(cv2.imread('person2.jpg'))
detector = FaceMeshDetector(staticMode=True, maxFaces=5)
img, faces = detector.findFaceMesh(img)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個

""" fail

print("手部偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

#img = resizeimg(cv2.imread('hand1.jpg'))
img = resizeimg(cv2.imread('hand2.jpg'))
detector = HandDetector(detectionCon=0.5, maxHands=2)
img = detector.findHands(img)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
"""

print('------------------------------------------------------------')	#60個

"""
!wget -O hand3.jpg --content-disposition https://unsplash.com/photos/fYTfOzaRVWw/download?force=true
!wget -O hand4.jpg --content-disposition https://unsplash.com/photos/Lzys6r1xFD8/download?force=true
"""

""" fail

print("手部狀態偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

img = resizeimg(cv2.imread('hand3.jpg'))
# img = resizeimg(cv2.imread('hand4.jpg'))
detector = HandDetector(detectionCon=0.5)
img = detector.findHands(img)
lmList, bboxInfo = detector.findPosition(img)
#print('特徵點：', lmList)
if lmList:
  bbox = bboxInfo['bbox']
  #左右手
  myHandType = detector.handType() 
  cv2.putText(img, 'Hand:{}'.format(myHandType), (bbox[0], bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

  #伸出手指數
  fingers = detector.fingersUp()
  #print(fingers)
  upFingers = fingers.count(1)
  cv2.putText(img, 'Finger:{}'.format(upFingers), (bbox[0]+100, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

  #兩特徵點距離
  distance, img, info = detector.findDistance(8, 12, img) #食指與中指
  cv2.putText(img, 'Dist:{}'.format(str(int(distance))), (bbox[0]+200, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
"""
print('------------------------------------------------------------')	#60個

print("姿勢偵測")

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

img = resizeimg(cv2.imread('pose1.jpg'))
# img = resizeimg(cv2.imread('pose2.jpg'))
detector = PoseDetector()
img = detector.findPose(img)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2
"""
cap = cv2.VideoCapture(0)
detector = PoseDetector(mode=True)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findPose(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

print('------------------------------------------------------------')	#60個

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

print('偵測手指數')

premusic = 0
count = 0

cap = cv2.VideoCapture(0)
detector = HandDetector(minTrackCon=0.5, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        bbox = bboxInfo['bbox']
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        if totalFingers>0 and totalFingers<5:  
            if (totalFingers-1) != premusic:  #手指數有改變
                if count>=3:  #連續3次手指數相同
                    print('play mp3')
                    premusic = totalFingers-1
                else:  #相同手指數加1
                    count += 1
            else:
                count = 0  #手指數歸零
        elif totalFingers==5:
            premusic = ''
            count = 0

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

sys.exit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python實戰聖經\ch12\handProperty_cam.py

from cvzone.HandTrackingModule import HandDetector
import cv2
"""
cap = cv2.VideoCapture(0)
detector = HandDetector(minTrackCon=0.5, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        bbox = bboxInfo['bbox']
        #左右手
        myHandType = detector.handType() 
        cv2.putText(img, 'Hand:{}'.format(myHandType), (bbox[0], bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
        #伸出手指數
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, 'Finger:{}'.format(totalFingers), (bbox[0]+100, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    
        #兩特徵點距離
        distance, img, info = detector.findDistance(8, 12, img) #食指與中指
        cv2.putText(img, 'Dist:{}'.format(str(int(distance))), (bbox[0]+200, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python實戰聖經\ch12\hands_cam.py

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        image_height, image_width, _ = image.shape
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
"""
#檔案 : C:\_git\vcs\_4.python\__code\Python實戰聖經\ch12\handTrack_cam.py

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(minTrackCon=0.5, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python實戰聖經\ch12\holistic_cam.py

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1)

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python實戰聖經\ch12\objectron_cam.py

import cv2
import mediapipe as mp
"""
cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
objectron = mp_objectron.Objectron(static_image_mode=False, max_num_objects=5, min_detection_confidence=0.5,
                            min_tracking_confidence=0.99, model_name='Chair')

while cap.isOpened():
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  #水平翻轉
    results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)
            mp_drawing.draw_axis(image, detected_object.rotation, detected_object.translation)
    cv2.imshow('MediaPipe Objectron', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



