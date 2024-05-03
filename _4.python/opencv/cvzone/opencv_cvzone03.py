#使用 CVZone xxx

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

filename = 'C:/_git/vcs/_4.python/opencv/data/_face/face03.jpg'

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

print('CVZone辨識臉部表情 : 張嘴或閉嘴')
img = cv2.imread("images/face.jpg")
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

img = cv2.imread("images/face.jpg")
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
print("作業完成")
print("------------------------------------------------------------")  # 60個






