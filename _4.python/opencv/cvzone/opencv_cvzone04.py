#人臉識別

print("------------------------------------------------------------")  # 60個

import cv2
import numpy as np
import face_recognition

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

print('人臉偵測')

img = cv2.imread("images/faces2.jpg")
faces = face_recognition.face_locations(img,
                         number_of_times_to_upsample=1,
                         model="hog")
print("臉數=", len(faces))
for face in faces:
    top, right, bottom, left = face
    cv2.rectangle(img, (left, top), (right, bottom),
                                    (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print('臉部資料編碼')
img = cv2.imread("images/faces2.jpg")
faces = face_recognition.face_locations(img)
print("臉數=", len(faces))
img_encodings = face_recognition.face_encodings(img,
                known_face_locations=faces, num_jitters=10)
print("128維度的編碼=", len(img_encodings))
print(img_encodings[0])

print("------------------------------------------------------------")  # 60個

print('人臉識別')
img = cv2.imread("images/mary1.jpg")
known_encoding = face_recognition.face_encodings(img)[0]
new_img = cv2.imread("images/mary2.jpg")
new_encoding = face_recognition.face_encodings(new_img)[0]

result = face_recognition.compare_faces([known_encoding],
                                new_encoding, tolerance=0.6)
print(result)

print("------------------------------------------------------------")  # 60個

print('計算兩張人臉之間差異的距離')

img = cv2.imread("images/mary1.jpg")
known1_encoding = face_recognition.face_encodings(img)[0]
img = cv2.imread("images/jane.jpg")
known2_encoding = face_recognition.face_encodings(img)[0]
new_img = cv2.imread("images/mary2.jpg")
new_encoding = face_recognition.face_encodings(new_img)[0]

know_encodings = [known1_encoding, known2_encoding]
distance = face_recognition.face_distance(know_encodings,
                                          new_encoding)
print(distance)

print("------------------------------------------------------------")  # 60個

print('識別和繪出臉部特徵')

img = cv2.imread("images/faces2.jpg")
faces = face_recognition.face_locations(img)
landmarks = face_recognition.face_landmarks(img, face_locations=faces)
features = ["chin",            # 下巴
            "left_eyebrow",    # 左眉
            "right_eyebrow",   # 右眉
            "nose_bridge",     # 鼻樑
            "nose_tip",        # 鼻尖
            "left_eye",        # 左眼
            "right_eye",       # 右眼
            "top_lip",         # 上嘴唇
            "bottom_lip"]      # 下嘴唇
for landmark in landmarks:
    for feature in features:
        points = np.array(landmark[feature], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], False, (255, 255, 0), 2)        

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個    


print("------------------------------------------------------------")  # 60個    


print("------------------------------------------------------------")  # 60個    


print("------------------------------------------------------------")  # 60個    




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




