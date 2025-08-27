"""

偵測人臉 自動存檔

"""

import os
import cv2

ESC = 27

# 存檔檔名用
index = 1
# 人臉取樣總數
total = 10

target_dir = "images"

# 準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    # os.makedirs(target_dir, exist_ok = True)


def saveImage(face_image, index):
    filename = target_dir + "/{:03d}.jpg".format(index)
    cv2.imwrite(filename, face_image)
    print(filename)


# OpenCV 人臉識別分類器
xml_filename = "D:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)

cap = cv2.VideoCapture(0)
cv2.namedWindow("video", cv2.WINDOW_NORMAL)

cnt = 0
while True:
    ret, frame = cap.read()  # 讀取影像
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if index < total + 1:
        faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 3)
        for x, y, w, h in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if cnt % 5 == 0:
                face_img = gray[y : y + h, x : x + w]
                face_img = cv2.resize(face_img, (400, 400))  # 調整大小
                saveImage(face_img, index)  # 存圖
                index += 1
                if index == total + 1:
                    print("已存檔", index - 1, "張")
            cnt += 1

    #### 在while內
    cv2.imshow("video", frame)  # 顯示影像
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
