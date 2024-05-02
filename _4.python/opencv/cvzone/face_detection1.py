#使用 CVZone 人臉偵測

print("------------------------------------------------------------")  # 60個

import cv2
from cvzone.FaceDetectionModule import FaceDetector

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face03.jpg'

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
detector = FaceDetector(minDetectionCon=0.5)#信心
img, faces = detector.findFaces(img)

if faces:
    print("偵測到人臉數:", len(faces))
else:
    print("未偵測到人臉")

cv2.imshow("Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)

detector = FaceDetector()
img, faces = detector.findFaces(img, draw=False)
if faces:
    print("偵測到人臉數:", len(faces))
else:
    print("未偵測到人臉")

cv2.imshow("Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

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

from cvzone.FaceDetectionModule import FaceDetector
import cv2

print('取得臉部的關鍵座標, 6個')

img = cv2.imread("images/face.jpg")
detector = FaceDetector()
img, faces = detector.findFaces(img)
if faces:
    keypoints = detector.getFaceKeypoints(img, face_idx=0)
    print(keypoints)
    for keypoint in keypoints:
        cv2.circle(img, keypoint["keypoint"], 5, (255, 0, 255), cv2.FILLED)
else:
    print("未偵測到人臉")

cv2.imshow("Face", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.FaceDetectionModule import FaceDetector
import cv2

print('裁剪出臉部的部分影像')

img = cv2.imread("images/face.jpg")
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

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print('Webcam人臉偵測')
from cvzone.FaceDetectionModule import FaceDetector
import cv2

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



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



