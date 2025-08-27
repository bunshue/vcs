# 人臉識別

#!pip install face_recognition

print("------------------------------------------------------------")  # 60個

import cv2
import face_recognition

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("人臉偵測")

filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg"
img = cv2.imread(filename)

faces = face_recognition.face_locations(img, number_of_times_to_upsample=1, model="hog")

print("臉數=", len(faces))
for face in faces:
    top, right, bottom, left = face
    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("臉部資料編碼")

filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg"
img = cv2.imread(filename)

faces = face_recognition.face_locations(img)

print("臉數=", len(faces))
img_encodings = face_recognition.face_encodings(
    img, known_face_locations=faces, num_jitters=10
)
print("128維度的編碼=", len(img_encodings))
print(img_encodings[0])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("人臉識別")

filename1 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"
filename2 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates03.jpg"

img = cv2.imread(filename1)
known_encoding = face_recognition.face_encodings(img)[0]

new_img = cv2.imread(filename2)
new_encoding = face_recognition.face_encodings(new_img)[0]

result = face_recognition.compare_faces([known_encoding], new_encoding, tolerance=0.6)
print(type(result))
print(result)
if result == [True]:
    print("是同一個人")
else:
    print("不是同一人")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("計算兩張人臉之間差異的距離")

filename1 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"
filename2 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg"
filename3 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Steve_Jobs_01.jpg"

filename_new = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates03.jpg"

img = cv2.imread(filename1)
known1_encoding = face_recognition.face_encodings(img)[0]

img = cv2.imread(filename2)
known2_encoding = face_recognition.face_encodings(img)[0]

img = cv2.imread(filename3)
known3_encoding = face_recognition.face_encodings(img)[0]

new_img = cv2.imread(filename_new)
new_encoding = face_recognition.face_encodings(new_img)[0]

know_encodings = [known1_encoding, known2_encoding, known3_encoding]
distance = face_recognition.face_distance(know_encodings, new_encoding)
print(distance)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("識別和繪出臉部特徵")

filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates02.jpg"

img = cv2.imread(filename)

faces = face_recognition.face_locations(img)
landmarks = face_recognition.face_landmarks(img, face_locations=faces)
features = [
    "chin",  # 下巴
    "left_eyebrow",  # 左眉
    "right_eyebrow",  # 右眉
    "nose_bridge",  # 鼻樑
    "nose_tip",  # 鼻尖
    "left_eye",  # 左眼
    "right_eye",  # 右眼
    "top_lip",  # 上嘴唇
    "bottom_lip",
]  # 下嘴唇

for landmark in landmarks:
    for feature in features:
        points = np.array(landmark[feature], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], False, (255, 255, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def get_encoded_faces():
    # looks through the faces folder and encodes all the faces
    # :return: dict of (name, image encoded)
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./member"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = face_recognition.load_image_file("member/" + f)
                encoding = face_recognition.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    # encode a face given the file name
    face = face_recognition.load_image_file("member/" + img)
    encoding = face_recognition.face_encodings(face)[0]

    return encoding


def classify_face(filename):
    # will find all of the faces in a given image and label
    # them if it knows what they are
    # :param filename: str of file path
    # :return: list of face names
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(filename, 1)
    # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    # img = img[:,:,::-1]

    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            print("best_match_index : ", best_match_index)
            print("name : ", name)

        face_names.append(name)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            print("top", top)
            print("right", right)
            print("bottom", bottom)
            print("left", left)
            print("name", name)

            # Draw a box around the face
            cv2.rectangle(
                img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2
            )

            # Draw a label with a name below the face
            cv2.rectangle(
                img,
                (left - 20, bottom - 15),
                (right + 20, bottom + 20),
                (255, 0, 0),
                cv2.FILLED,
            )
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                img, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2
            )
    return img


filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"
image = classify_face(filename)

cv2.imshow("Result", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("face-recognition：效果絕佳的人臉辨識")

from PIL import Image, ImageDraw

filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates21.jpg"

image = face_recognition.load_image_file(filename)
boxes = face_recognition.face_locations(image)
print(boxes)

img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for i in range(len(boxes)):
    drawing.rectangle(
        (boxes[i][3], boxes[i][0], boxes[i][1], boxes[i][2]), outline="red", width=2
    )
plt.imshow(img)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"

image = face_recognition.load_image_file(filename)
landmarks = face_recognition.face_landmarks(image)
print(landmarks)
print("鼻樑位置：{}".format(landmarks[0]["nose_bridge"]))

img = Image.open(filename)
drawing = ImageDraw.Draw(img)
for landmark in landmarks:
    for feature in landmark.keys():
        drawing.line(landmark[feature], width=5)
plt.imshow(img)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("把人員圖片資料先存起來, 並註記人名")
file1 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"
file2 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg"
file3 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Steve_Jobs_01.jpg"
filename1 = face_recognition.load_image_file(file1)
filename2 = face_recognition.load_image_file(file2)
filename3 = face_recognition.load_image_file(file3)
encoding1 = face_recognition.face_encodings(filename1)[0]
encoding2 = face_recognition.face_encodings(filename2)[0]
encoding3 = face_recognition.face_encodings(filename3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ["Bill Gates", "Elon Musk", "Steve Jobs"]

file_new = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates32.jpg"
unknown = face_recognition.load_image_file(file_new)
encoding_unknown = face_recognition.face_encodings(unknown)[0]

print("使用辨識功能")
results = face_recognition.compare_faces(known_faces, encoding_unknown)
print(results)

face = ""
for i in range(len(results)):
    if results[i]:
        face = face + names[i] + "  "
if face == "":
    print("圖片中辨識不到資料庫中人臉！aaa")
else:
    print("圖片中的人臉：" + face)

print()

print("把人員圖片資料先存起來, 並註記人名")
file1 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"
file2 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg"
file3 = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Steve_Jobs_01.jpg"
filename1 = face_recognition.load_image_file(file1)
filename2 = face_recognition.load_image_file(file2)
filename3 = face_recognition.load_image_file(file3)
encoding1 = face_recognition.face_encodings(filename1)[0]
encoding2 = face_recognition.face_encodings(filename2)[0]
encoding3 = face_recognition.face_encodings(filename3)[0]
known_faces = [encoding1, encoding2, encoding3]
names = ["Bill Gates", "Elon Musk", "Steve Jobs"]

file_new = "D:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates32.jpg"
unknown = face_recognition.load_image_file(file_new)
encoding_unknown = face_recognition.face_encodings(unknown)[0]

print("使用距離功能")
distances = face_recognition.face_distance(known_faces, encoding_unknown)
print(distances)

face = ""
for i in range(len(distances)):
    if distances[i] < 0.5:
        face = face + names[i] + "  "

if face == "":
    print("圖片中辨識不到資料庫中人臉！bbb")
else:
    print("圖片中的人臉：" + face)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
