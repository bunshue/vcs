"""
OpenCV 人臉辨識
OpenCV 人臉識別分類器 Haar Cascade Classifier
Haar-like features 哈爾特徵
匈牙利 Afred Haar

haarcascade_frontalface_default.xml		偵測正面人臉 預設
haarcascade_frontalface_alt_tree.xml		偵測正面人臉
haarcascade_frontalface_alt.xml			偵測正面人臉
haarcascade_frontalface_alt2.xml		偵測正面人臉

cv2內建xml位置:
cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# 參數
# img    	        待檢測圖片，一般為灰階影像，以便加快偵測速度
# scaleFactor 	        在前後兩次相繼的掃描中，搜索範圍的比例係數，默認值為 1.1
# minNeighbors 	        構成偵測目標的相鄰矩形的最小個數，默認值為 3
# minSize & maxSize 	用來限制得到的目標區域範圍

# 1.2 表示每次影像尺寸減小的比例
# 3 表示每一個目標至少要被檢測到4次才算是真正的目標
# faces表示檢測到的人臉目標list

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列

"""
import cv2
from PIL import Image

ESC = 27

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # pass
    plt.show()


def cvshow(title, img):
    # pass
    cv2.imshow(title, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# OpenCV_顏色共同
RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測正面人臉 haarcascade_frontalface_default.xml
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"

# 眼睛模型
eye_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
)

# 左眼模型
lefteye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lefteye_2splits.xml"

# 右眼模型
righteye_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_righteye_2splits.xml"

# 嘴巴模型
mouth_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_mouth.xml"
)

# 鼻子模型
nose_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades_mcs/haarcascade_mcs_nose.xml"
)

# 偵測上半身 haarcascade_upperbody.xml
upperbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_upperbody.xml"
)

# 正面的貓臉 haarcascade_frontalcatface.xml
frontalcatface_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalcatface.xml"
)

# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml
russian_plate_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_russian_plate_number.xml"

# 偵測側面的人臉 haarcascade_profileface.xml
profileface_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_profileface.xml"
)

# 偵測身形 路人偵測 haarcascade_fullbody.xml
fullbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_fullbody.xml"
)

# 下半身
lowerbody_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_lowerbody.xml"
)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename = "C:/_git/vcs/_4.python/opencv/data/_face/face17.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/yalta1945.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/solvay1927a.jpg"
# filename = "C:/_git/vcs/_4.python/opencv/data/_face/ming_emperor3.jpg"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("人臉辨識 圖片")

print("框出照片中的人臉, 轉成灰階再辨識, 畫框畫在原圖並顯示")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

img = cv2.imread(filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 人臉偵測
# faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)
# faces = face_cascade_classifier.detectMultiScale(gray, 1.1, 4)
# faces = face_cascade_classifier.detectMultiScale(gray)
# faces = face_cascade_classifier.detectMultiScale(
# gray,
# scaleFactor=1.1,
# minNeighbors=5,
# minSize=(30, 30),
# )
# faces = face_cascade_classifier.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))
"""
faces = face_cascade_classifier.detectMultiScale(
    # gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5)
    # gray, scaleFactor=1.15, minNeighbors=3, minSize=(20, 20), maxSize=(50, 50)
    # gray, scaleFactor=1.15, minNeighbors=5, minSize=(20, 20)
    gray,
    scaleFactor=1.02,
    minNeighbors=3,
    minSize=(20, 20),
)
"""
faces = face_cascade_classifier.detectMultiScale(
    gray,  # 也可直接用 img 來偵測
    scaleFactor=1.2,
    minNeighbors=3,
    minSize=(32, 32),
    flags=cv2.CASCADE_SCALE_IMAGE,
)
"""
# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
"""
print("共找到 " + str(len(faces)) + " 張人臉")

"""
for nn in range(len(faces)):
    print(nn)
    print(faces[nn])
    print(faces[nn][0], faces[nn][1], faces[nn][2], faces[nn][3])
"""

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)  # 綠色框住人臉
    roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 取出 ROI
    # cv2.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2), GREEN,2)

cv2.imshow("Image1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以上為單純圖片的人臉辨識

print("OpenCV_ai_44 人臉識別, 把人臉馬賽克掉, 縮小放大法")

img = cv2.imread(filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)  # 開始辨識影像中的人臉

for x, y, w, h in faces:
    mosaic = img[y : y + h, x : x + w]  # 取出 ROI  # 馬賽克區域
    level = 15  # 馬賽克程度
    mh = int(h / level)  # 根據馬賽克程度縮小的高度
    mw = int(w / level)  # 根據馬賽克程度縮小的寬度
    mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)  # 先縮小
    mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)  # 然後放大
    img[y : y + h, x : x + w] = mosaic  # 將指定區域換成馬賽克區域

cv2.imshow("Image8", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多重偵測 臉 眼 鼻 嘴 左眼 右眼")

filename = "C:/_git/vcs/_4.python/opencv/data/_face/face07.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"

img = cv2.imread(filename3)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# gray = cv2.medianBlur(gray, 5)                # 如果一直偵測到雜訊，可使用模糊的方式去除雜訊

# 人臉偵測
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件 人臉
faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
# 把人臉框起來
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 取出 ROI
    eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

# 眼睛
eye_cascade_classifier = cv2.CascadeClassifier(eye_xml_filename)  # 建立辨識物件 眼睛
eyes = eye_cascade_classifier.detectMultiScale(gray)  # 偵測眼睛
# 把眼睛框起來 G
for x, y, w, h in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    # cv2.rectangle(roi_color, (x, y), (x + w, y + h), GREEN, 2)

# 鼻子
nose_cascade_classifier = cv2.CascadeClassifier(nose_xml_filename)  # 建立辨識物件 鼻子
noses = nose_cascade_classifier.detectMultiScale(gray)  # 偵測鼻子
# 把鼻子框起來 B
for x, y, w, h in noses:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

# 嘴巴
mouth_cascade_classifier = cv2.CascadeClassifier(mouth_xml_filename)  # 建立辨識物件 嘴巴
mouths = mouth_cascade_classifier.detectMultiScale(gray)  # 偵測嘴巴
# 把嘴巴框起來 R
for x, y, w, h in mouths:
    cv2.rectangle(img, (x, y), (x + w, y + h), RED, 2)

# 偵測左眼
lefteye_cascade_classifier = cv2.CascadeClassifier(lefteye_xml_filename)  # 建立辨識物件 左眼
left_eyes = lefteye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)
# 把左眼框起來 GREEN
for x, y, w, h in left_eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

# 偵測右眼
righteye_cascade_classifier = cv2.CascadeClassifier(righteye_xml_filename)  # 建立辨識物件 右眼
right_eyes = righteye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=7, minSize=(20, 20)
)
# 把右眼框起來 GREEN
for x, y, w, h in right_eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("OpenCV_ai_48")
""" lack file
# lack test file
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法
faces = []   # 儲存人臉位置大小的串列
ids = []     # 記錄該人臉 id 的串列

for i in range(1,31):
    img = cv2.imread(f'face01/{i}.jpg')# 彩色讀取           # 依序開啟每一張蔡英文的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉灰階
    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列
    faces = face_cascade_classifier.detectMultiScale(gray)        # 擷取人臉區域
    for(x,y,w,h) in faces:
        faces.append(img_np[y:y+h,x:x+w])         # 記錄蔡英文人臉的位置和大小內像素的數值
        ids.append(1)                             # 記錄蔡英文人臉對應的 id，只能是整數，都是 1 表示蔡英文的 id 為 1

for i in range(1,16):
    img = cv2.imread(f'face02/{i}.jpg')# 彩色讀取           # 依序開啟每一張川普的照片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉灰階
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

import operator
from functools import reduce

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

target_dir = "images"

# 準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    # os.makedirs(target_dir, exist_ok = True)

user_filename = "images/recogface.jpg"  # 使用者人臉檔案
user_filename2 = "images/recogface2.jpg"  # 使用者人臉檔案
login_filename = "images/loginface.jpg"  # 登入者人臉檔案
login_filename2 = "images/loginface2.jpg"  # 登入者人臉檔案

cap = cv2.VideoCapture(0)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()  # 從攝影機擷取一張影像
    cv2.imshow("Image", frame)  # 顯示圖片, 原圖

    # k = cv2.waitKey(100)  #每0.1秒讀一次鍵盤
    k = cv2.waitKey(1)
    if k == ESC:  # ESC
        break
    elif k == ord("C"):
        print("建立使用者資料")
        cv2.imwrite(user_filename, frame)  # 存檔
        img = cv2.imread(user_filename)  # 彩色讀取
        # 人臉偵測
        faces = face_cascade_classifier.detectMultiScale(
            img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉
        image1 = Image.open(user_filename).crop((x, y, x + w, y + h))  # 擷取人臉
        # image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  # 轉為解析度200x200
        image1.save(user_filename2)  # 存檔

    elif k == ord("c"):
        print("比對登入者")
        if not os.path.exists(user_filename2):  # 如果使用者人臉檔案不存在
            print("請先建立使用者資料")
            continue
        cv2.imwrite(login_filename, frame)  # 存檔
        img = cv2.imread(login_filename)  # 彩色讀取
        # 人臉偵測
        faces = face_cascade_classifier.detectMultiScale(
            img,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  # 只取第一張人臉
        image1 = Image.open(login_filename).crop((x, y, x + w, y + h))  # 擷取人臉
        # image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  # 轉為解析度200x200
        image1.save(login_filename2)  # 存檔

        pic1 = Image.open(user_filename2)  # 開啟使用者人臉檔案
        pic2 = Image.open(login_filename2)  # 開啟登入者人臉檔案
        h1 = pic1.histogram()  # 計算圖形差異度
        h2 = pic2.histogram()
        diff = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
        )
        if diff <= 100:  # 若差度在100內視為通過驗證
            print("通過驗證，歡迎使用本系統！ diff=%4.2f" % diff)
        else:
            print("臉譜不正確，無法使用本系統！ diff=%4.2f" % diff)


cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測閉眼, 按 ESC 離開")

from functools import wraps

lastsave = 0


def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        global lastsave
        if time.time() - lastsave > 3:
            # this is in seconds, so 5 minutes = 300 seconds
            lastsave = time.time()
            tmp.count = 0
        return func(*args, **kwargs)

    tmp.count = 0
    return tmp


face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

eye_cascade_classifier = cv2.CascadeClassifier(eye_xml_filename)  # 建立辨識物件 眼睛

cap = cv2.VideoCapture(0)


@counter
def closed():
    print("Eye Closed")


def openeye():
    print("Eye is Open")


def warning():
    print("Sleeping~~~~")


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    # 把人臉框起來
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
        roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
        roi_color = img[y : y + h, x : x + w]  # 取出 ROI

        eyes = eye_cascade_classifier.detectMultiScale(roi_gray)

        if eyes != ():
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), GREEN, 2)
                openeye()
        else:
            closed()
            if closed.count == 3:
                warning()

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 face.yml 人臉模型檔
print("OpenCV_ai_71")

recognizer = cv2.face.LBPHFaceRecognizer_create()  # 啟用訓練人臉模型方法

# NG 無檔案
# recognizer.read('face.yml')                               # 讀取人臉模型檔

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, img = cap.read()

    #img = cv2.resize(img, (640//2, 480//2))  # 縮小尺寸，加快辨識效率
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉灰階
    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(gray)

    # 建立姓名和 id 的對照表
    name = {"1": "David", "2": "John", "3": "Chris"}

    # 依序判斷每張臉屬於哪個 id
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)  # 標記人臉外框
        idnum, confidence = recognizer.predict(
            gray[y : y + h, x : x + w]  # 取出 ROI
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

print("偵測右轉指示牌")

img = cv2.imread("data/traffic_sign1.jpg")  # 彩色讀取

turnR_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haar_turnR.xml"

turnR_cascade_classifier = cv2.CascadeClassifier(turnR_xml_filename)  # 建立辨識物件 右轉指示牌

turnRs = turnR_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30)
)
if len(turnRs) > 0:
    for x, y, w, h in turnRs:
        cv2.rectangle(img, (x, y), (x + w, y + h), RED, 2)
else:
    print("nothing")

plt.title("偵測右轉指示牌")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測上半身 haarcascade_upperbody.xml

upperbody_cascade_classifier = cv2.CascadeClassifier(
    upperbody_xml_filename
)  # 建立辨識物件 上半身

# pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"
# pic_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face02.jpg"

img = cv2.imread("data2/people1.jpg")  # 彩色讀取

bodies = upperbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)

cv2.imshow("Upperbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 正面的貓臉 haarcascade_frontalcatface.xml

frontalcatface_cascade_classifier = cv2.CascadeClassifier(
    frontalcatface_xml_filename
)  # 建立辨識物件 正面的貓臉

img = cv2.imread("data2/cat2.jpg")  # 彩色讀取

# 貓臉偵測
faces = frontalcatface_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=9, minSize=(20, 20)
)

# 把貓臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Cat Face", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
        cv2.rectangle(img, (x, y), (x + w, y + h), RED, 2)
else:
    print("偵測車牌失敗")

cv2.imshow("Car1", img)  # 顯示所讀取的車輛
cv2.imshow("Car2", carplate)  # 顯示所讀取的車輛

cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測車牌, 適用於俄羅斯車牌 haarcascade_russian_plate_number.xml

russian_plate_cascade_classifier = cv2.CascadeClassifier(
    russian_plate_xml_filename
)  # 建立辨識物件 俄羅斯車牌

img = cv2.imread("data2/car1.jpg")  # 彩色讀取
img = cv2.imread("data2/car2.jpg")  # 彩色讀取

plates = russian_plate_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把車牌框起來
for x, y, w, h in plates:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Car Plate", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測側面的人臉 haarcascade_profileface.xml

profileface_cascade_classifier = cv2.CascadeClassifier(
    profileface_xml_filename
)  # 建立辨識物件

img = cv2.imread("data2/s_1927.jpg")  # 彩色讀取

# 人臉偵測
faces = profileface_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.3, minNeighbors=4, minSize=(20, 20)
)
print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Profile Face", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測身形 路人偵測 haarcascade_fullbody.xml

# img = cv2.imread("cars.jpg")# 彩色讀取
img = cv2.imread("data2/people2.jpg")  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray = cv2.medianBlur(gray, 5)  # 模糊化去除雜訊

fullbody_cascade_classifier = cv2.CascadeClassifier(fullbody_xml_filename)  # 建立辨識物件 全身

# 偵測全身
# bodies = fullbody_cascade_classifier.detectMultiScale(gray, 1.1, 3)
bodies = fullbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Fullbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 下半身
lowerbody_cascade_classifier = cv2.CascadeClassifier(
    lowerbody_xml_filename
)  # 建立辨識物件 下半身

img = cv2.imread("data2/people1.jpg")  # 彩色讀取
bodies = lowerbody_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把身體框起來
for x, y, w, h in bodies:
    cv2.rectangle(img, (x, y), (x + w, y + h), BLUE, 2)

cv2.imshow("Lowerbody", img)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

img = cv2.imread(picture_filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列

faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)

print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 取出 ROI

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

lbpcascade_xml_filename = (
    "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
)

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

lbp_cascade_classifier = cv2.CascadeClassifier(lbpcascade_xml_filename)  # 建立辨識物件

img = cv2.imread(picture_filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

faces = lbp_cascade_classifier.detectMultiScale(gray, 1.2, 3)
print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), WHITE, 4)
    roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
    roi_color = img[y : y + h, x : x + w]  # 取出 ROI

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 汽車模型
cars_xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/cars.xml"

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/video1.avi"
# video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/video2.avi"

car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車

cap = cv2.VideoCapture(video_filename)

while True:
    ret, img = cap.read()
    if type(img) == type(None):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 1)

    for x, y, w, h in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), RED, 2)

    cv2.imshow("video", img)

    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
img = cv2.imread("cars.jpg")# 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉灰階
gray = cv2.medianBlur(gray, 5)                  # 模糊化去除雜訊

car_cascade_classifier = cv2.CascadeClassifier(cars_xml_filename)  # 建立辨識物件 汽車

cars = car_cascade_classifier.detectMultiScale(gray, 1.1, 3)       # 偵測汽車

# 把汽車框起來
for x, y, w, h in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)   # 繪製外框

cv2.imshow("ImageShow", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import os
import cv2
import numpy as np
import pytesseract
from PIL import Image

print("------------------------------------------------------------")  # 60個

# ch31_2.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text = pytesseract.image_to_string(Image.open("data/atq9305.jpg"), config=config)
print(f"車號是 : {text}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ch31_3.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("car_plate/cartest1.jpg")

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
print("------------------------------------------------------------")  # 60個

# ch31_4.py

config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("car_plate/cartest3.jpg")

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
print("------------------------------------------------------------")  # 60個

# ch31_5.py

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("car_plate/cartest3.jpg")

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
print("------------------------------------------------------------")  # 60個

# ch31_6.py

carFile = "car_plate.jpg"
config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pictPath = "haar_carplate.xml"  # 哈爾特徵檔路徑

img = cv2.imread("car_plate/cartest3.jpg")

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

from datetime import datetime


def face_add(img):
    print("稍後在此加入新增人員功能")


# -----------------------------------#


def face_who(img):
    print("稍後在此加入人臉身分辨識功能")


# -----------------------------------#


def face_shot(function):
    isCnt = False  # 用來判斷是否正在進行倒數計時中
    face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        sucess, img = capture.read()
        if not sucess:
            print("讀取影像失敗")
            continue
        img_copy = img.copy()  # 複製影像
        # 人臉偵測
        faces = face_cascade_classifier.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)
        )
        if len(faces) == 1:  # 如果偵測到一張人臉
            if isCnt == False:
                t1 = time.time()  # 紀錄現在的時間
                isCnt = True  # 告訴程式目前進入倒數狀態
            cnter = 5 - int(time.time() - t1)  # 更新倒數計時器
            # 把人臉框起來
            for x, y, w, h in faces:
                cv2.rectangle(img_copy, (x, y), (x + w, y + h), YELLOW, 2)  # 繪製矩形
                cv2.putText(  # 繪製倒數數字
                    img_copy,
                    str(cnter),
                    (x + int(w / 2), y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    YELLOW,
                    2,
                )
            if cnter == 0:  # 倒數結束
                isCnt = False  # 告訴程式離開倒數狀態
                filename = datetime.now().strftime("%Y-%m-%d %H.%M.%S")  # 時間格式化
                cv2.imwrite(filename + ".jpg", img)  # 存圖
                # -----------------------------------------#
                if function == "add":  # 打卡系統新增人員
                    face_add(img)
                elif function == "who":  # 進行人臉身分識別功能
                    face_who(img)
                # -----------------------------------------#
        else:  # 如果不是一張人臉
            isCnt = False  # 設定非倒數狀態

        cv2.imshow("Frame", img_copy)
        k = cv2.waitKey(1)  # 讀取按鍵輸入(若無會傳回 -1)
        if k == ord("q") or k == ord("Q"):  # 按下 q 離開迴圈, 結束程式
            print("exit")
            cv2.destroyAllWindows()  # 關閉視窗
            capture.release()  # 關閉攝影機
            break  # 離開無窮迴圈, 結束程式
    else:
        print("開啟攝影機失敗")


# -----------------------------------#
face_shot("who")  # 呼叫自訂函式


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 若有多個視窗 要指名視窗名稱

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)


"""
# 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=4
    )
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)
"""

img = cv2.imread(filename)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

# gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) #彩色讀取直接轉灰階


# ----------------------------

imageCrop = img[y : y + h, x : x + w]  # 裁切  # 取出 ROI
imageCrop = img[y : y + h, x : x + w]  # 裁切  # 取出 ROI
imageCrop = img[y : y + h, x : x + w]  # 裁切  # 取出 ROI
imageResize = cv2.resize(imageCrop, (160, 160))  # 重製大小

"""
# OpenCV 人臉識別分類器 LBP Cascase
xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
"""

# frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2))) #調整畫面大小
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)
# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)

cap = cv2.VideoCapture(0)  # 開啟攝影機

key = cv2.waitKey(200)  # 0.2秒檢查一次
if key == ord("a") or key == ord("A"):  # 如果按A或a
    cv2.imwrite("tmp_photo.jpg", img)  # 存圖


# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save("tmp_faceout.jpg")  # 存圖


"""
# 取得影像的尺寸大小
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Image Size: %d x %d" % (w, h))

    # frame = cv2.resize(frame,(int(frame.shape[1] / 2), int(frame.shape[0] / 2))) #調整畫面大小
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階

    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 3,
        minSize = (200, 200))

    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3
    )

    # print("共找到 " + str(len(faces)) + " 張人臉")
    # 把人臉框起來
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
        # 人臉偵測
        faces = face_cascade_classifier.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=5, minSize=(200, 200)
        )

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# webcam偵測人臉 並模糊之

    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=3
    )
    # 把人臉框起來
    for x, y, w, h in faces:
        face = cv2.blur(frame[y : y + h, x : x + w], (25, 25))
        frame[y : y + h, x : x + w] = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 偵測到人臉再去偵測眼睛
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(gray, 1.3, 5)

    # 把人臉框起來
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 5)
        roi_gray = gray[y : y + h, x : x + w]  # 取出 ROI
        roi_color = frame[y : y + h, x : x + w]  # 取出 ROI
        eyes = eye_cascade_classifier.detectMultiScale(roi_gray, 1.3, 5)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), GREEN, 5)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

# 人臉偵測
# faces = face_cascade_classifier.detectMultiScale(gray)

    # frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，避免尺寸過大導致效能不好
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
    # 人臉偵測
    faces = face_cascade_classifier.detectMultiScale(gray)

    # 把人臉框起來
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

    # img = cv2.resize(frame, (640//2, 480//2))
    gray = cv2.medianBlur(img, 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)  # 轉灰階
    gray = cv2.medianBlur(gray, 5)

    # 眼睛
    eyes = eye_cascade_classifier.detectMultiScale(gray)  # 偵測眼睛

    # 鼻子
    noses = nose_cascade_classifier.detectMultiScale(gray)  # 偵測鼻子

    # 嘴巴
    mouths = mouth_cascade_classifier.detectMultiScale(gray)  # 偵測嘴巴

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(gray, 1.2, 3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 偵測人臉
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

# 偵測雙眼
eyes = eye_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from functools import reduce
import operator

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件
# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)
print("共找到 " + str(len(faces)) + " 張人臉")

# 把人臉框起來
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), GREEN, 2)
    myimg = Image.open("tmp_photo.jpg")  # PIL模組開啟
    imgCrop = myimg.crop((x, y, x + w, y + h))  # 裁切
    imgResize = imgCrop.resize((150, 150), Image.Resampling.LANCZOS)
    imgResize.save(faceFile)  # 儲存檔案


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("偵測人臉 將其馬賽克")

face_cascade_classifier = cv2.CascadeClassifier(xml_filename)  # 建立辨識物件

# frame = cv2.resize(frame, (640//2, 480//2))  # 縮小尺寸，避免尺寸過大導致效能不好
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 轉灰階
# 人臉偵測
faces = face_cascade_classifier.detectMultiScale(gray)
for x, y, w, h in faces:
    mosaic = frame[y : y + h, x : x + w]  # 取出 ROI
    level = 15
    mh = int(h / level)
    mw = int(w / level)
    mosaic = cv2.resize(mosaic, (mw, mh), interpolation=cv2.INTER_LINEAR)
    mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)
    frame[y : y + h, x : x + w] = mosaic

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("檢查兩圖之差異度")

from functools import reduce
import operator

filename_face1 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()
RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)

filename_face1 = "C:/_git/vcs/_4.python/opencv/data/_face/face01.jpg"
filename_face2 = "C:/_git/vcs/_4.python/opencv/data/_face/face02.jpg"

h1 = Image.open(filename_face1).histogram()
h2 = Image.open(filename_face2).histogram()

RMS = math.sqrt(
    reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1)
)
print("RMS = ", RMS)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

faces = face_cascade_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cv2.imwrite("tmp_atq9305.jpg", carplate)
print("已存圖, 檔案 : tmp_atq9305.jpg")
