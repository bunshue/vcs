

print('------------------------------------------------------------')	#60個

#MediaPipe模組：Google多媒體機器學習

'''
!wget -O person1.jpg --content-disposition https://unsplash.com/photos/3g3grQaeA2o/download?force=true
!wget -O person2.jpg --content-disposition https://unsplash.com/photos/GVVsC0JG6Ak/download?force=true
'''

'''
#臉部偵測
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
cv2_imshow(image)
'''

print('------------------------------------------------------------')	#60個

#!wget -O person3.jpg --content-disposition https://unsplash.com/photos/JyVcAIUAcPM/download?force=true

#臉部特徵網
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
            connections=mp_face_mesh.FACE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)
cv2_imshow(image)

print('------------------------------------------------------------')	#60個

'''
!wget -O hand1.jpg --content-disposition https://unsplash.com/photos/33VdiGc2O9o/download?force=true
!wget -O hand2.jpg --content-disposition https://unsplash.com/photos/qKspdY9XUzs/download?force=true
'''

#手部偵測
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
cv2_imshow(image)


print('------------------------------------------------------------')	#60個

'''
!wget -O pose1.jpg --content-disposition https://unsplash.com/photos/A3MleA0jtoE/download?force=true
!wget -O pose2.jpg --content-disposition https://unsplash.com/photos/wa8o6rs22Fw/download?force=true
'''
#姿勢偵測
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
cv2_imshow(image)



print('------------------------------------------------------------')	#60個

#人體整合偵測
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
cv2_imshow(image)


print('------------------------------------------------------------')	#60個



'''
!wget -O object1.jpg --content-disposition https://unsplash.com/photos/kvmdsTrGOBM/download?force=true
!wget -O object2.jpg --content-disposition https://unsplash.com/photos/rhcllVy2zBU/download?force=true
'''
#3D物體偵測
import mediapipe as mp
import cv2
import math
from google.colab.patches import cv2_imshow

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
cv2_imshow(image) 




print('------------------------------------------------------------')	#60個

#cvzone模組：簡單易用多媒體機器學習

'''
!pip install cvzone==1.3.7
!pip install mediapipe==0.8.6
'''
#臉部偵測
from cvzone.FaceDetectionModule import FaceDetector
import cv2, math
from google.colab.patches import cv2_imshow

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
cv2_imshow(img)



print('------------------------------------------------------------')	#60個
#臉部特徵網
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2, math
from google.colab.patches import cv2_imshow

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
cv2_imshow(img)


print('------------------------------------------------------------')	#60個


#手部偵測
from cvzone.HandTrackingModule import HandDetector
import cv2, math
from google.colab.patches import cv2_imshow

dH, dW = 480, 480
def resizeimg(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (dW, math.floor(h/(w/dW))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/dH)), dH))
  return img

img = resizeimg(cv2.imread('hand1.jpg'))
# img = resizeimg(cv2.imread('hand2.jpg'))
detector = HandDetector(mode=False, detectionCon=0.5, maxHands=2)
img = detector.findHands(img)
cv2_imshow(img)





print('------------------------------------------------------------')	#60個
'''
!wget -O hand3.jpg --content-disposition https://unsplash.com/photos/fYTfOzaRVWw/download?force=true
!wget -O hand4.jpg --content-disposition https://unsplash.com/photos/Lzys6r1xFD8/download?force=true
'''
#手部狀態偵測
from cvzone.HandTrackingModule import HandDetector
import cv2, math
from google.colab.patches import cv2_imshow

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
detector = HandDetector(mode=False, detectionCon=0.5)
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

cv2_imshow(img)


print('------------------------------------------------------------')	#60個

#姿勢偵測
from cvzone.PoseModule import PoseDetector
import cv2, math
from google.colab.patches import cv2_imshow

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
cv2_imshow(img) 

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

