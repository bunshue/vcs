import cv2
import os
import sys
import glob
import numpy as np
import matplotlib.pyplot as plt

# OpenCV 人臉識別分類器
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

print("------------------------------------------------------------")  # 60個

face_db = [] # 建立空串列

face_db.append(cv2.imread("C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk01.jpg", cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Elon_Musk03.jpg", cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg", cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates10.jpg", cv2.IMREAD_GRAYSCALE))

labels = [0,0,1,1]                                  # 建立標籤串列
faceNames = {"0":"Elon_Musk", "1":"Bill_Gates"}             # 建立對應名字的字典

recognizer = cv2.face.LBPHFaceRecognizer_create()   # 建立人臉辨識物件
recognizer.train(face_db, np.array(labels))         # 訓練人臉辨識

# 讀取要辨識的人臉
face = cv2.imread("C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates44.jpg",cv2.IMREAD_GRAYSCALE)
label,confidence = recognizer.predict(face)         # 執行人臉辨識

print(f"Name       = {faceNames[str(label)]}")
print(f"Confidence = {confidence:6.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/Bill_Gates/Bill_Gates01.jpg"

image = cv2.imread(filename, cv2.IMREAD_COLOR)    # 彩色讀取
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)                # 轉RGB

plt.subplot(121)
plt.imshow(img)                                             # 顯示人臉

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      # 轉灰階
recognizer = cv2.face.LBPHFaceRecognizer_create()   # 建立人臉辨識物件
recognizer.train([gray], np.array([0]))             # 訓練人臉辨識
histogram = recognizer.getHistograms()[0][0]
axis_values = np.array([i for i in range(0, len(histogram))])
plt.subplot(122)
plt.bar(axis_values, histogram)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('aaa')

face_db = [                                     # 人臉資料庫
            "ch29_2\\hung1.jpg",
            "ch29_2\\hung2.jpg",
            "ch29_2\\star1.jpg",
            "ch29_2\\star2.jpg"
          ]

faces = []                                      # 人臉空串列
for f in face_db:
    img = cv2.imread(f,cv2.IMREAD_GRAYSCALE)    # 讀取人臉資料庫
    faces.append(img)                           # 加入人臉空串列

# 建立標籤串列
labels = np.array([i for i in range(0, len(faces))])    

# 建立對應名字的字典            
model = cv2.face.LBPHFaceRecognizer_create()    # 建立人臉辨識物件
model.train(faces, np.array(labels))            # 訓練人臉辨識

# 儲存模型
model.save("tmp_face_model1.yml")                 # 儲存訓練的人臉數據
print("儲存訓練數據完成")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('bbb')

# 建立對應名字的字典
faceNames = {"0":"Hung", "1":"Hung", "2":"Unistar", "3":"Unistar"}

model = cv2.face.LBPHFaceRecognizer_create()    # 建立人臉辨識物件

# 讀取模型
model.read("tmp_face_model1.yml")                 # 讀取人臉辨識數據模型

# 讀取要辨識的人臉
face = cv2.imread("ch29_2\\face.jpg",cv2.IMREAD_GRAYSCALE)
label,confidence = model.predict(face)          # 執行人臉辨識
print(f"Name       = {faceNames[str(label)]}")
print(f"Confidence = {confidence:6.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('ccc')

face_db = []                                        # 建立空串列
face_db.append(cv2.imread("ch29_1\\hung1.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\hung2.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\star1.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\star2.jpg",cv2.IMREAD_GRAYSCALE))

labels = [0,0,1,1]                                  # 建立標籤串列
faceNames = {"0":"Hung", "1":"Unistar"}             # 建立對應名字的字典

# 使用EigenFaceRecognizer
recognizer = cv2.face.EigenFaceRecognizer_create()  # 建立人臉辨識物件
recognizer.train(face_db, np.array(labels))         # 訓練人臉辨識

# 讀取要辨識的人臉
face = cv2.imread("ch29_1\\face.jpg",cv2.IMREAD_GRAYSCALE)
label,confidence = recognizer.predict(face)         # 執行人臉辨識
print("使用Eigenfaces方法執行人臉辨識")
print(f"Name       = {faceNames[str(label)]}")
print(f"Confidence = {confidence:6.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('ddd')

face_db = []                                        # 建立空串列
face_db.append(cv2.imread("ch29_1\\hung1.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\hung2.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\star1.jpg",cv2.IMREAD_GRAYSCALE))
face_db.append(cv2.imread("ch29_1\\star2.jpg",cv2.IMREAD_GRAYSCALE))

labels = [0,0,1,1]                                  # 建立標籤串列
faceNames = {"0":"Hung", "1":"Unistar"}             # 建立對應名字的字典

# 使用FisherFaceRecognizer
recognizer = cv2.face.FisherFaceRecognizer_create() # 建立人臉辨識物件
recognizer.train(face_db, np.array(labels))         # 訓練人臉辨識

# 讀取要辨識的人臉
face = cv2.imread("ch29_1\\face.jpg",cv2.IMREAD_GRAYSCALE)
label,confidence = recognizer.predict(face)         # 執行人臉辨識
print("使用Fisherfaces方法執行人臉辨識")
print(f"Name       = {faceNames[str(label)]}")
print(f"Confidence = {confidence:6.2f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('eee')

total = 5                                           # 人臉取樣數
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

if not os.path.exists("ch29_6"):                    # 如果不存在ch29_6資料夾
    os.mkdir("ch29_6")                              # 就建立ch29_6
name = input("請輸入英文名字 : ")
if os.path.exists("ch29_6\\" + name):
    print("此名字的人臉資料已經存在")
else:
    os.mkdir("ch29_6\\" + name)
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
            faceName = "ch29_6\\" + name + "\\" + name + str(num) + ".jpg"
            cv2.imwrite(faceName, imageResize)      # 儲存人臉影像           
            if num >= total:                        # 拍指定人臉數後才終止               
                if num == total:
                    print(f"拍攝第 {num} 次人臉成功")
                break
            print(f"拍攝第 {num} 次人臉成功")
            num += 1
    cap.release()                                   # 關閉攝影機
    cv2.destroyAllWindows()

# 讀取人臉樣本和放入faces_db, 同時建立標籤與人名串列
nameList = []                                       # 員工姓名
faces_db = []                                       # 儲存所有人臉
labels = []                                         # 建立人臉標籤
index = 0                                           # 員工編號索引
dirs = os.listdir('ch29_6')                         # 取得所有資料夾及檔案
for d in dirs:                                      # d是所有員工人臉的資料夾
    if os.path.isdir('ch29_6\\' + d):               # 獲得資料夾
        # 撈出單層圖檔
        faces = glob.glob('ch29_6\\' + d + '\\*.jpg')  # 資料夾中所有人臉
        for face in faces:                          # 讀取人臉
            img = cv2.imread(face, cv2.IMREAD_GRAYSCALE)
            faces_db.append(img)                    # 人臉存入串列
            labels.append(index)                    # 建立數值標籤
        nameList.append(d)                          # 將英文名字加入串列
        index += 1
print(f"標籤名稱 = {nameList}")
print(f"標籤序號 ={labels}")
# 儲存人名串列，可在未來辨識人臉時使用
f = open('ch29_6\\employee.txt', 'w')
f.write(','.join(nameList))
f.close()

print('建立人臉辨識資料庫')
model = cv2.face.LBPHFaceRecognizer_create()        # 建立LBPH人臉辨識物件
model.train(faces_db, np.array(labels))             # 訓練LBPH人臉辨識

# 儲存模型
model.save('tmp_face_model2.yml')                  # 儲存LBPH訓練數據
print('人臉辨識資料庫完成')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('fff')

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識檔案物件

model = cv2.face.LBPHFaceRecognizer_create()

# 讀取模型
model.read('tmp_face_model2.yml')                  # 讀取已訓練模型
f = open('ch29_6\\employee.txt', 'r')               # 開啟姓名標籤
names = f.readline().split(',')                     # 將姓名存於串列

cap = cv2.VideoCapture(0)
while(cap.isOpened()):                              # 如果開啟攝影機成功
    ret, img = cap.read()                           # 讀取影像
    faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1,
                minNeighbors = 3, minSize=(20,20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    cv2.imshow("Face", img)                         # 顯示影像
    k = cv2.waitKey(200)                            # 0.2秒讀鍵盤一次
    if ret == True:       
        if k == ord("a") or k == ord("A"):          # 按 a 或 A 鍵
            imageCrop = img[y:y+h,x:x+w]                    # 裁切
            imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
            cv2.imwrite("ch29_6\\face.jpg", imageResize)    # 將測試人臉存檔
            break
cap.release()                                       # 關閉攝影機
cv2.destroyAllWindows()

# 讀取員工人臉
gray = cv2.imread("ch29_6\\face.jpg", cv2.IMREAD_GRAYSCALE)
val = model.predict(gray)
if val[1] < 50:                                     #人臉辨識成功
    print(f"歡迎Deepmind員工 {names[val[0]]} 登入")
    print(f"匹配值是 {val[1]:6.2f}")
else:
    print("對不起你不是員工, 請洽人事部門")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

