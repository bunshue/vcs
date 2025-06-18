"""

"""

import os
import cv2
import numpy as np
import pytesseract
from PIL import Image

print("------------------------------------------------------------")  # 60個

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

print("------------------------------------------------------------")  # 60個

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread(filename)

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)  # 偵測影像

# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
num = 1  # 檔名編號
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    filename = "tmp_face" + str(num) + ".jpg"  # 路徑 + 檔名
    imageCrop = img[y : y + h, x : x + w]  # 裁切
    imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
    # cv2.imwrite(filename, imageResize)              # 儲存影像
    num += 1  # 檔案編號

cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

name = "david1"
faceName = "tmp_" + name + ".jpg"  # 人臉影像
facePhoto = "tmp_" + name + "photo.jpg"  # 拍攝影像

print("按 A 存圖")
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

cap = cv2.VideoCapture(1)
while cap.isOpened():  # 攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite(facePhoto, img)  # 將影像寫入facePhoto
            print("已存圖, 檔案 :", facePhoto)
            break

cap.release()

img = cv2.imread(facePhoto)

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    imageCrop = img[y : y + h, x : x + w]  # 裁切
    imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
    cv2.imwrite(faceName, imageResize)  # 儲存人臉影像
    print("已存圖, 檔案 :", faceName)

cv2.imshow("FaceRecognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

name = "david2"
faceName = "tmptmp_" + name + ".jpg"  # 人臉影像

print("按 A 存圖")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cap = cv2.VideoCapture(1)
while cap.isOpened():  # 攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
    )
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            imageCrop = img[y : y + h, x : x + w]  # 裁切
            imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
            cv2.imwrite(faceName, imageResize)  # 儲存人臉影像
            print("已存圖, 檔案 :", faceName)
            break

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

name = "david3"

print("按 A 存圖")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cap = cv2.VideoCapture(1)
num = 1  # 影像編號
while cap.isOpened():  # 攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
    )
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            imageCrop = img[y : y + h, x : x + w]  # 裁切
            imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
            faceName = "tmptmptmp_" + name + str(num) + ".jpg"  # 儲存影像
            cv2.imwrite(faceName, imageResize)  # 儲存人臉影像
            print("已存圖, 檔案 :", faceName)
            if num >= 5:  # 拍 5 張人臉後才終止
                if num == 5:
                    print(f"拍攝第 {num} 次人臉成功")
                break
            print(f"拍攝第 {num} 次人臉成功")
            num += 1

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

name = "david4"
total = 10  # eval(input("請輸入人臉需求數量 : "))

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

cap = cv2.VideoCapture(1)
num = 1  # 影像編號
while cap.isOpened():  # 攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
    )
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    key = cv2.waitKey(200)
    if ret == True:  # 讀取影像如果成功
        imageCrop = img[y : y + h, x : x + w]  # 裁切
        imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
        faceName = "tmptmptmptmp_" + name + str(num) + ".jpg"  # 儲存影像
        cv2.imwrite(faceName, imageResize)  # 儲存人臉影像
        print("已存圖, 檔案 :", faceName)
        if num >= total:  # 拍指定人臉數後才終止
            if num == total:
                print(f"拍攝第 {num} 次人臉成功")
            break
        print(f"拍攝第 {num} 次人臉成功")
        num += 1

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# ch31_1.py

pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("testCar/cartest1.jpg")

car_cascade = cv2.CascadeClassifier(pictPath)  # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛

cv2.imwrite("tmp_atq9305.jpg", carplate)
print("已存圖, 檔案 : tmp_atq9305.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch31_2.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(Image.open("atq9305.jpg"), config=config)
print(f"車號是 : {text}")

print("------------------------------------------------------------")  # 60個

# ch31_3.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("testCar/cartest1.jpg")

car_cascade = cv2.CascadeClassifier(pictPath)  # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛
text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch31_4.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("testCar/cartest3.jpg")

car_cascade = cv2.CascadeClassifier(pictPath)  # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛

text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch31_5.py

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("testCar/cartest3.jpg")

car_cascade = cv2.CascadeClassifier(pictPath)  # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛
ret, dst = cv2.threshold(carplate, 100, 255, cv2.THRESH_BINARY)  # 二值化
cv2.imshow("Car binary", dst)  # 顯示二值化車牌
text = pytesseract.image_to_string(carplate, config=config)  # OCR辨識
print(f"車號是 : {text}")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ch31_6.py

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("testCar/cartest3.jpg")

car_cascade = cv2.CascadeClassifier(pictPath)  # 讀哈爾特徵檔

# 執行辨識
plates = car_cascade.detectMultiScale(
    img, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), maxSize=(155, 50)
)
if len(plates) > 0:  # 有偵測到車牌
    for x, y, w, h in plates:  # 標記車牌
        carplate = img[y : y + h, x : x + w]  # 車牌影像
else:
    print("偵測車牌失敗")

cv2.imshow("Car", carplate)  # 顯示所讀取的車輛
ret, dst = cv2.threshold(carplate, 100, 255, cv2.THRESH_BINARY)  # 二值化

cv2.imshow("Car binary", dst)  # 顯示二值化車牌
kernel = np.ones((3, 3), np.uint8)
dst1 = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel)  # 執行開運算
text = pytesseract.image_to_string(dst1, config=config)  # 執行辨識
print(f"車號是 : {text}")

cv2.imwrite(carFile, dst)  # 寫入儲存
print("已存圖, 檔案 :", carFile)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
