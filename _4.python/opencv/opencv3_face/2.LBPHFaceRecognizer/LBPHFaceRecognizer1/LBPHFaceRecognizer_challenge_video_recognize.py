import os
import sys
import cv2 as cv
import numpy as np
from datetime import datetime

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

print("------------------------------------------------------------")  # 60個

# 1_capture.py

face_detector = cv.CascadeClassifier(xml_filename)

# 打開視訊鏡頭
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Could not open video device.")
cap.set(3, 640)  # 畫面寬度
cap.set(4, 480)  # 畫面高度

# 向使用者解釋程序
print(
    """當螢幕提示時，請輸入你的訊息。\n
      然後取下眼鏡，直視攝影鏡頭。\n
      請做出多種不同的表情，包括正常的、快樂的、悲傷的、疲倦的，\n
      直到聽到提示喊停為止。"""
)

name = input("\nEnter last name: ")
user_id = input("Enter assigned ID Number: ")
print("\nCapturing face. Look at the camera now!")

# 新建資料夾用於放置影像
if not os.path.isdir("trainer"):
    os.mkdir("trainer")
os.chdir("trainer")

frame_count = 0

while True:
    # 獲取畫面影像，共 30 張
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rects = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for x, y, w, h in face_rects:
        frame_count += 1  # 增加畫面數計數
        cv.imwrite(
            str(name) + "." + str(user_id) + "." + str(frame_count) + ".jpg",
            gray[y : y + h, x : x + w],
        )  # 儲存影像至資料夾
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 畫出矩形
        cv.imshow("image", frame)  # 顯示影像
        cv.waitKey(400)  # 視窗停滯 0.4 秒
    if frame_count >= 30:
        break

print("\nImage collection complete. Exiting...")

cap.release()
cv.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 2_train.py

face_detector = cv.CascadeClassifier(xml_filename)

# train_path = './trainer' # 若使用的是你的臉，請取消註解
train_path = "./demming_trainer"  # 使用提供的 Demming 臉部影像
image_paths = [os.path.join(train_path, f) for f in os.listdir(train_path)]
images, labels = [], []

# 讀取灰階影像，並顯示使用者 ID、影像的名稱、影像的畫面號碼
for image in image_paths:
    print(image)
    train_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    label = int(os.path.split(image)[-1].split(".")[1])
    name = os.path.split(image)[-1].split(".")[0]
    frame_num = os.path.split(image)[-1].split(".")[2]
    faces = face_detector.detectMultiScale(train_image)
    for x, y, w, h in faces:
        images.append(train_image[y : y + h, x : x + w])
        labels.append(label)
        print(f"Preparing training images for {name}.{label}.{frame_num}")
        cv.imshow("Training Image", train_image[y : y + h, x : x + w])
        cv.waitKey(50)

cv.destroyAllWindows()

# 訓練影像
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
recognizer.write("tmp_lbph_trainer.yml")
print("Training complete. Exiting...")

print("------------------------------------------------------------")  # 60個

# 3_predict.py

face_detector = cv.CascadeClassifier(xml_filename)

names = {1: "Demming"}  # 將使用者 ID 聯結到使用者名稱

# 初始化辨識器物件，並載入訓練資料
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("tmp_lbph_trainer.yml")

# test_path = './tester'  # 若使用的是你的臉，請取消註解
test_path = "./demming_tester"  # 使用提供的臉部影像
image_paths = [os.path.join(test_path, f) for f in os.listdir(test_path)]

# 執行人臉辨識並更新存取日誌檔案
for image in image_paths:
    predict_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    faces = face_detector.detectMultiScale(
        predict_image, scaleFactor=1.05, minNeighbors=5
    )
    for x, y, w, h in faces:
        print(f"\nAccess requested at {datetime.now()}.")
        face = cv.resize(predict_image[y : y + h, x : x + w], (100, 100))
        predicted_id, dist = recognizer.predict(face)
        if predicted_id == 1 and dist <= 95:
            name = names[predicted_id]
            print(
                "{} identified as {} with distance={}".format(
                    image, name, round(dist, 1)
                )
            )
            print(
                f"Access granted to {name} at {datetime.now()}.",
                file=open("lab_access_log.txt", "a"),
            )
        else:
            name = "unknown"
            print(f"{image} is {name}.")

        cv.rectangle(predict_image, (x, y), (x + w, y + h), 255, 2)  # 繪製矩形
        cv.putText(
            predict_image,
            name,
            (x + 1, y + h - 5),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,
            255,
            1,
        )  # 標示使用者名稱
        cv.imshow("ID", predict_image)  # 顯示影像
        cv.waitKey(2000)  # 視窗停滯 2 秒
        cv.destroyAllWindows()  # 關閉視窗

print("------------------------------------------------------------")  # 60個

# challenge_video_recognize.py

names = {1: "Demming"}  # 將使用者 ID 聯結到使用者名稱

detector = cv.CascadeClassifier(xml_filename)

# 初始化辨識器物件，並載入訓練資料
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("tmp_lbph_trainer.yml")

# 設定視訊鏡頭
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cloud not open video device.")
# cap.set(3,320) # 設定螢幕寬度
# cap.set(4,240) # 設定螢幕高度

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rects = detector.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5)

    for x, y, w, h in face_rects:
        # 縮放影像使它變成能訓練的大小
        gray_resize = cv.resize(gray[y : y + h, x : x + w], (100, 100), cv.INTER_LINEAR)
        predicted_id, dist = recognizer.predict(gray_resize)
        if predicted_id == 1 and dist <= 110:
            name = names[predicted_id]
        else:
            name = "unknown"
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv.putText(
            frame,
            name,
            (x + 1, y + h - 5),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 0),
            1,
        )
        # 顯示畫面
        cv.imshow("frame", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# 退出視訊鏡頭
cap.release()
cv.destroyAllWindows()
