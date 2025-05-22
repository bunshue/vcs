import cv2
import os

# OpenCV 人臉識別分類器
# xml_filename = "C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml"
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_alt2.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

print("------------------------------------------------------------")  # 60個

# ch28_1.py

if not os.path.exists("facedata"):                  # 如果不存在資料夾
    os.mkdir("facedata")                            # 就建立facedata

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

img = cv2.imread("g5.jpg")                          # 讀取影像
faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
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
print("------------------------------------------------------------")  # 60個

# ch28_2.py

if not os.path.exists("ch28_2"):                # 如果不存在ch28_2資料夾
    os.mkdir("ch28_2")                          # 就建立ch28_2
name = input("請輸入英文名字 : ")
faceName = "ch28_2\\" + name + ".jpg"           # 人臉影像
facePhoto = "ch28_2\\" + name + "photo.jpg"     # 拍攝影像

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite(facePhoto, img)         # 將影像寫入facePhoto           
            break
cap.release()                                   # 關閉攝影機

img = cv2.imread(facePhoto)                     # 讀取影像facePhoto
faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))

# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    imageCrop = img[y:y+h,x:x+w]                    # 裁切
    imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
    cv2.imwrite(faceName, imageResize)              # 儲存人臉影像 
    
cv2.imshow("FaceRecognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch28_3.py

if not os.path.exists("ch28_3"):                # 如果不存在ch28_3資料夾
    os.mkdir("ch28_3")                          # 就建立ch28_3
name = input("請輸入英文名字 : ")
faceName = "ch28_3\\" + name + ".jpg"           # 人臉影像

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 攝影機有開啟就執行迴圈   
    ret, img = cap.read()                       # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
            minNeighbors = 3, minSize=(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            imageCrop = img[y:y+h,x:x+w]                    # 裁切
            imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
            cv2.imwrite(faceName, imageResize)  # 儲存人臉影像           
            break
cap.release()                                   # 關閉攝影機

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch28_4.py

if not os.path.exists("ch28_4"):                # 如果不存在ch28_4資料夾
    os.mkdir("ch28_4")                          # 就建立ch28_4
name = input("請輸入英文名字 : ")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件
cap = cv2.VideoCapture(0)                       # 開啟攝影機
num = 1                                         # 影像編號
while(cap.isOpened()):                          # 攝影機有開啟就執行迴圈   
    ret, img = cap.read()                       # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
            minNeighbors = 3, minSize=(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            imageCrop = img[y:y+h,x:x+w]                      # 裁切
            imageResize = cv2.resize(imageCrop,(160,160))     # 重製大小
            faceName = "ch28_4\\" + name + str(num) + ".jpg"  # 儲存影像
            cv2.imwrite(faceName, imageResize)  # 儲存人臉影像           
            if num >= 5:                        # 拍 5 張人臉後才終止               
                if num == 5:
                    print(f"拍攝第 {num} 次人臉成功")
                break
            print(f"拍攝第 {num} 次人臉成功")
            num += 1
cap.release()                                   # 關閉攝影機
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch28_5.py

if not os.path.exists("ch28_5"):                # 如果不存在ch28_5資料夾
    os.mkdir("ch28_5")                          # 就建立ch28_5
name = input("請輸入英文名字     : ")
total = eval(input("請輸入人臉需求數量 : "))

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

cap = cv2.VideoCapture(0)                       # 開啟攝影機
num = 1                                         # 影像編號
while(cap.isOpened()):                          # 攝影機有開啟就執行迴圈   
    ret, img = cap.read()                       # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
            minNeighbors = 3, minSize=(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    key = cv2.waitKey(200)
    if ret == True:                             # 讀取影像如果成功
        imageCrop = img[y:y+h,x:x+w]                      # 裁切
        imageResize = cv2.resize(imageCrop,(160,160))     # 重製大小
        faceName = "ch28_5\\" + name + str(num) + ".jpg"  # 儲存影像
        cv2.imwrite(faceName, imageResize)      # 儲存人臉影像           
        if num >= total:                        # 拍指定人臉數後才終止               
            if num == total:
                print(f"拍攝第 {num} 次人臉成功")
            break
        print(f"拍攝第 {num} 次人臉成功")
        num += 1
cap.release()                                   # 關閉攝影機
cv2.destroyAllWindows()



print("------------------------------------------------------------")  # 60個




