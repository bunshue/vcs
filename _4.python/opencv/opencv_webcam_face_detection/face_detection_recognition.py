import os
import cv2

ESC = 27

import math, operator
from PIL import Image
from functools import reduce

# OpenCV 人臉識別分類器
xml_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
face_cascade_classifier = cv2.CascadeClassifier(xml_filename)   #建立辨識物件

target_dir = 'images'

#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    #os.makedirs(target_dir, exist_ok = True)

user_filename = 'images/recogface.jpg'  #使用者人臉檔案
user_filename2 = 'images/recogface2.jpg'  #使用者人臉檔案
login_filename = 'images/loginface.jpg'  #登入者人臉檔案
login_filename2 = 'images/loginface2.jpg'  #登入者人臉檔案

cap = cv2.VideoCapture(0)
cv2.namedWindow('WebCam', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()   # 從攝影機擷取一張影像
    cv2.imshow('WebCam', frame)    # 顯示圖片, 原圖

    #k = cv2.waitKey(100)  #每0.1秒讀一次鍵盤
    k = cv2.waitKey(1)
    if k == ESC:     #ESC
        break
    elif k == ord('C'):
        print('建立使用者資料')
        cv2.imwrite(user_filename, frame)  #存檔
        image = cv2.imread(user_filename)  #讀檔做人臉辨識
        faces = face_cascade_classifier.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #只取第一張人臉
        image1 = Image.open(user_filename).crop((x, y, x + w, y + h))  #擷取人臉
        #image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  #轉為解析度200x200
        image1.save(user_filename2)  #存檔
        
    elif k == ord('c'):
        print('比對登入者')
        if(not os.path.exists(user_filename2)):  #如果使用者人臉檔案不存在
            print('請先建立使用者資料')
            continue
        cv2.imwrite(login_filename, frame)  #存檔
        image = cv2.imread(login_filename)  #讀檔做人臉辨識
        faces = face_cascade_classifier.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #只取第一張人臉
        image1 = Image.open(login_filename).crop((x, y, x + w, y + h))  #擷取人臉
        #image1 = image1.resize((200, 200), Image.ANTIALIAS)  #轉為解析度200x200
        image1 = image1.resize((200, 200), Image.LANCZOS)  #轉為解析度200x200
        image1.save(login_filename2)  #存檔

        pic1 = Image.open(user_filename2)  #開啟使用者人臉檔案
        pic2 = Image.open(login_filename2)  #開啟登入者人臉檔案
        h1 = pic1.histogram()  #計算圖形差異度
        h2 = pic2.histogram()
        diff = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
        if(diff <= 100):  #若差度在100內視為通過驗證
            print("通過驗證，歡迎使用本系統！ diff=%4.2f" % diff)
        else:
            print("臉譜不正確，無法使用本系統！ diff=%4.2f" % diff)


# 釋放所有資源
cap.release()   # 釋放攝影機
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗
