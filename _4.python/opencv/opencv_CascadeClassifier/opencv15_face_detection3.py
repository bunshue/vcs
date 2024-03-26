# OpenCV 人臉辨識

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("框出照片中的人臉")

print("------------------------------------------------------------")  # 60個


# 人臉辨識
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"

xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
img = cv2.imread(filename)  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
print(faces)
print(len(faces))
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)

# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

xml_filename = r"C:\_git\vcs\_4.python\_data\lbpcascade_frontalface.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()

print("------------------------------------------------------------")  # 60個

xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
img = cv2.imread("data/g2.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
cv2.imshow("Face", img)  # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

if not os.path.exists("facedata"):  # 如果不存在資料夾
    os.mkdir("facedata")  # 就建立facedata

xml_filename = r"C:\opencv\data\haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
img = cv2.imread("data/g5.jpg")  # 讀取影像
faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)  # 偵測影像
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 140, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Finding " + str(len(faces)) + " face",
    (img.shape[1] - 135, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
# 同時將影像儲存在facedata資料夾, 但是必須先建立此資料夾
num = 1  # 檔名編號
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    filename = "facedata\\face" + str(num) + ".jpg"  # 路徑 + 檔名
    imageCrop = img[y : y + h, x : x + w]  # 裁切
    imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小
    cv2.imwrite(filename, imageResize)  # 儲存影像
    num += 1  # 檔案編號

cv2.imshow("Face", img)  # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()

print("------------------------------------------------------------")  # 60個

from PIL import Image

xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_faceout.jpg")  # 存圖

cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

print("檢查兩圖之差異度")

from functools import reduce
from PIL import Image
import math, operator

filename_face1 = "data/face1.jpg"
filename_face2 = "data/face1.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()
RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)

filename_face1 = "data/face1.jpg"
filename_face2 = "data/faceout.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)


print("------------------------------------------------------------")  # 60個


from PIL import Image
from functools import reduce
import math, operator

ID = input("請輸入身份證字號 = ")  # 讀取所輸入的身分證字號
face = ID + ".jpg"  # 未來的臉形檔案

xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_newface.jpg")  # 儲存檔案

print("檢查兩圖之差異度")
h1 = Image.open(face).histogram()
h2 = Image.open("tmp_newface.jpg").histogram()
RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
if RMS <= 100:
    print("歡迎出入境")
else:
    print("比對失敗")

cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

from PIL import Image

ID = input("請輸入身份證字號 = ")  # 讀取所輸入的身分證字號
print("臉形檔案將儲存在 ", ID + ".jpg")
faceFile = "tmp_" + ID + ".jpg"  # 未來的臉形檔案

xml_filename = r"C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)  # 開啟攝影機
while cap.isOpened():  # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()  # 讀取影像
    cv2.imshow("Photo", img)  # 顯示影像在OpenCV視窗
    if ret == True:  # 讀取影像如果成功
        key = cv2.waitKey(200)  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("tmp_photo.jpg", img)  # 存圖
            break
cap.release()  # 關閉攝影機

faces = face_cascade.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 標註右下角底色是黃色
cv2.rectangle(
    img,
    (img.shape[1] - 120, img.shape[0] - 20),
    (img.shape[1], img.shape[0]),
    (0, 255, 255),
    -1,
)
# 標註找到多少的人臉
cv2.putText(
    img,
    "Find " + str(len(faces)) + " face",
    (img.shape[1] - 110, img.shape[0] - 5),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 0, 0),
    1,
)
# 將人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 藍色框住人臉
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save(faceFile)  # 儲存檔案

cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
