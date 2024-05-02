#使用 CVZone 臉部網格

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face03.jpg'

print("------------------------------------------------------------")  # 60個

print('人臉偵測和匯出3D臉部網格')

img = cv2.imread("images/face4.jpg")
detector = FaceMeshDetector(maxFaces=2, minDetectionCon=0.5,
                            minTrackCon=0.5)
img, faces = detector.findFaceMesh(img)
if faces:
   print(len(faces[0]))
   
cv2.imshow("Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('取得臉部網格的點座標')

img = cv2.imread("images/face4.jpg")
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
   print(len(faces[0]))
   for point in faces[0]:
       cv2.circle(img, point, 1, (255, 0, 255), cv2.FILLED)    
   
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('取得臉部特徵資訊')

img = cv2.imread("images/face.jpg")
detector = FaceMeshDetector(maxFaces=2)
img, faces = detector.findFaceMesh(img, draw=False)
if faces:
    face_oval = detector.getFacePart(img, 0, "FACE_OVAL")
    points = np.array(face_oval, np.int32)
    cv2.polylines(img, [points], True, (0, 0, 255), 1)  
    face_leye = detector.getFacePart(img, 0, "LEFT_EYE")
    points = np.array(face_leye, np.int32)
    cv2.polylines(img, [points], True, (0, 255, 255), 1)     
  
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('計算臉部特徵的尺寸')

img = cv2.imread("images/face.jpg")
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

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


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


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




