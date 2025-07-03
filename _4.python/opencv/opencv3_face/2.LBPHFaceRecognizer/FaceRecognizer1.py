"""
FaceRecognizer1


人臉辨識
1.LBPH人臉辨識
2.Eigenfaces(特徵臉)人臉辨識
3.Fisherfaces人臉辨識

Local Binary Pattern Histogram	區域二值模式直方圖

face.LBPHFaceRecognizer_create()	建立LBPH人臉便是物件
.train					訓練LBPH人臉辨識
.predict				執行LBPH人臉辨識

"""

import cv2
import os
import numpy as np

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/a1.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/a2.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/b1.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/b2.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/a3.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/e01.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e02.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e11.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/e12.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.EigenFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/eTest.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個

images = []
images.append(cv2.imread("data/f01.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f02.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f11.png", cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread("data/f12.png", cv2.IMREAD_GRAYSCALE))
labels = [0, 0, 1, 1]
# print(labels)
recognizer = cv2.face.FisherFaceRecognizer_create()
recognizer.train(images, np.array(labels))
predict_image = cv2.imread("data/fTest.png", cv2.IMREAD_GRAYSCALE)
label, confidence = recognizer.predict(predict_image)
print("label=", label)
print("confidence=", confidence)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("OpenCV_ai_48")

""" lack file
# lack test file
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

for i in range(1,31):
    img = cv2.imread(f'face01/{i}.jpg')  # 彩色讀取 # 依序開啟每一張蔡英文的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉灰階
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    faces = face_cascade_classifier.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in faces:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄蔡英文人臉對應的 id，只能是整數，都是 1 表示蔡英文的 id 為 1

for i in range(1,16):
    img = cv2.imread(f'face02/{i}.jpg')  # 彩色讀取 # 依序開啟每一張川普的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉灰階
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    faces = face_cascade_classifier.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in faces:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄川普人臉的位置和大小內像素的數值
        ids.append(2)                             # 記錄川普人臉對應的 id，只能是整數，都是 2 表示川普的 id 為 2

print('training...')                              # 提示開始訓練
recog.train(faces,np.array(ids))                  # 開始訓練
recog.save('tmp_face.yml')                            # 訓練完成儲存為 tmp_face.yml
print('ok!')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 face.yml 人臉模型檔
print("OpenCV_ai_71")

recognizer = cv2.face.LBPHFaceRecognizer_create()  # 啟用訓練人臉模型方法

# NG 無檔案
# recognizer.read('face.yml')                               # 讀取人臉模型檔

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #轉灰階
    
    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(gray)

    # 建立姓名和 id 的對照表
    name = {"1": "David", "2": "John", "3": "Chris"}

    # 依序判斷每張臉屬於哪個 id
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)  # 標記人臉外框
        idnum, confidence = recognizer.predict(
            gray[y : y + h, x : x + w]  # 裁切, 取出 ROI
        )  # 取出 id 號碼以及信心指數 confidence
        if confidence < 60:
            text = name[str(idnum)]  # 如果信心指數小於 60，取得對應的名字
        else:
            text = "???"  # 不然名字就是 ???
        # 在人臉外框旁加上名字
        cv2.putText(
            img,
            text,
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            GREEN,
            2,
            cv2.LINE_AA,
        )

    cv2.imshow("WebCam", img)
    
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
