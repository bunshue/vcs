import os
import sys
import cv2

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cv2.namedWindow("Peony1")                       # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)    # 可以調整大小
img1 = cv2.imread(filename)                         # 彩色讀取
img2 = cv2.imread(filename, 0)                      # 灰色讀取
cv2.imshow("Peony1", img1)                      # 顯示影像img1
cv2.imshow("Peony2", img2)                      # 顯示影像img2
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyWindow("Peony1")                     # 刪除Peony1
cv2.waitKey(3000)                                   # 等待3秒
cv2.destroyAllWindows()                             # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cv2.namedWindow("Peony")        # 使用預設
img = cv2.imread(filename)          # 彩色讀取
cv2.imshow("Peony", img)        # 顯示影像img
cv2.imwrite("tmp_pic01.jpg", img)     # 將檔案寫入 tmp_pic01.jpg
cv2.waitKey(3000)                   # 等待3秒
cv2.destroyAllWindows()             # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

img = cv2.imread("mountain.jpg")                # BGR 讀取
cv2.imshow("mountain.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("street.jpg")                  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cv2.namedWindow("Peony")                            # 使用預設
img = cv2.imread("antarctica3.jpg")                     # 彩色讀取
cv2.line(img,(100,100),(1200,100),(255,0,0),2)          # 輸出線條
cv2.rectangle(img,(100,200),(1200,400),(0,0,255),2)     # 輸出矩陣
cv2.putText(img,"I Like Python",(400,350),              # 輸出文字
            cv2.FONT_ITALIC,3,(255,0,0),8)
cv2.imshow("Peony", img)                            # 顯示影像img
cv2.waitKey(3000)                                       # 等待3秒
cv2.destroyAllWindows()                                 # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)          # 建立辨識物件
img = cv2.imread(filename)                              # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
cv2.imshow("Face", img)                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)          # 建立辨識物件
img = cv2.imread("g2.jpg")                              # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
cv2.imshow("Face", img)                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

if not os.path.exists("facedata"):                  # 如果不存在資料夾
    os.mkdir("facedata")                            # 就建立facedata

pictPath = r'C:\opencv\data\haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(pictPath)      # 建立辨識檔案物件
img = cv2.imread("g5.jpg")                          # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))          # 偵測影像
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
# 同時將影像儲存在facedata資料夾, 但是必須先建立此資料夾
num = 1                                             # 檔名編號
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    filename = "facedata\\face" + str(num) + ".jpg" # 路徑 + 檔名
    imageCrop = img[y:y+h,x:x+w]                    # 裁切
    imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
    cv2.imwrite(filename, imageResize)              # 儲存影像
    num += 1                                        # 檔案編號                                
    
cv2.imshow("Face", img)                             # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import Image

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("photo.jpg", img)       # 將影像寫入photo.jpg           
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_faceout.jpg")                       # 儲存檔案
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

from functools import reduce
from PIL import Image
import math, operator
h1 = Image.open("face1.jpg").histogram()
h2 = Image.open("face1.jpg").histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
print("RMS = ", RMS)

print("------------------------------------------------------------")  # 60個

from functools import reduce
from PIL import Image
import math, operator
h1 = Image.open("face1.jpg").histogram()
h2 = Image.open("faceout.jpg").histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
print("RMS = ", RMS)

print("------------------------------------------------------------")  # 60個

from PIL import Image
from functools import reduce
import math, operator

ID = input("請輸入身份證字號 = ")               # 讀取所輸入的身分證字號
face = ID + ".jpg"                              # 未來的臉形檔案

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("photo.jpg", img)       # 將影像寫入photo.jpg           
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_newface.jpg")                       # 儲存檔案

h1 = Image.open(face).histogram()
h2 = Image.open("newface.jpg").histogram()
RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
if RMS <= 100:
    print("歡迎出入境")
else:
    print("比對失敗")       
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

from PIL import Image

ID = input("請輸入身份證字號 = ")               # 讀取所輸入的身分證字號
print("臉形檔案將儲存在 ", ID + ".jpg")
faceFile = "tmp_" + ID + ".jpg"                          # 未來的臉形檔案

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("photo.jpg", img)       # 將影像寫入photo.jpg           
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.Resampling.LANCZOS)
    imgResize.save(faceFile)                            # 儲存檔案
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)

print("------------------------------------------------------------")  # 60個

