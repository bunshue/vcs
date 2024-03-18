"""
一本精通：OpenCV 與 AI 影像辨識


# 使用 deepface 模組
"""

import os
import sys
import time
import random

import cv2

print("------------------------------------------------------------")  # 60個

from deepface import DeepFace

filename = 'aaaa.jpg'
img = cv2.imread(filename)     # 讀取圖片
try:
    analyze = DeepFace.analyze(img)  # 辨識圖片人臉資訊
    print(analyze)
except:
    pass

cv2.imshow('ImageShow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()

'''
print("------------------------------------------------------------")  # 60個

from deepface import DeepFace

img = cv2.imread('test.jpg')     # 讀取圖片
try:
    analyze = DeepFace.analyze(img, actions=['emotion'] )  # 辨識圖片人臉資訊，取出情緒資訊
    print(analyze)
except:
    pass

cv2.imshow('ImageShow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from deepface import DeepFace

img = cv2.imread('mona.jpg')
try:
    emotion = DeepFace.analyze(img, actions=['emotion'])  # 情緒
    age = DeepFace.analyze(img, actions=['age'])          # 年齡
    race = DeepFace.analyze(img, actions=['race'])        # 人種
    gender = DeepFace.analyze(img, actions=['gender'])    # 性別

    print(emotion['dominant_emotion'])
    print(age['age'])
    print(race['dominant_race'])
    print(gender['gender'])
except:
    pass

cv2.imshow('ImageShow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

from deepface import DeepFace
from PIL import ImageFont, ImageDraw, Image

# 定義該情緒的中文字
text_obj={
    'angry': '生氣',
    'disgust': '噁心',
    'fear': '害怕',
    'happy': '開心',
    'sad': '難過',
    'surprise': '驚訝',
    'neutral': '正常'
}

# 定義加入文字函式
def putText(x,y,text,size=70,color=(255,255,255)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text, fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

img = cv2.imread('emotion.jpg')                    # 載入圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # 將圖片轉成灰階

face_cascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")   # 載入人臉模型
faces = face_cascade.detectMultiScale(gray)        # 偵測人臉

for (x, y, w, h) in faces:
    # 擴大偵測範圍，避免無法辨識情緒
    x1 = x-60
    x2 = x+w+60
    y1 = y-20
    y2 = y+h+60
    face = img[x1:x2, y1:y2]  # 取出人臉範圍
    try:
        emotion = DeepFace.analyze(face, actions=['emotion'])  # 辨識情緒
        putText(x,y,text_obj[emotion['dominant_emotion']])     # 放入文字
    except:
        pass
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

cv2.imshow('ImageShow', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
print("------------------------------------------------------------")  # 60個

from deepface import DeepFace
from PIL import ImageFont, ImageDraw, Image

# 定義該情緒的中文字
text_obj={
    'angry': '生氣',
    'disgust': '噁心',
    'fear': '害怕',
    'happy': '開心',
    'sad': '難過',
    'surprise': '驚訝',
    'neutral': '正常'
}

# 定義加入文字函式
def putText(x,y,text,size=50,color=(255,255,255)):
    global img
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text_obj[text], fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/Image_20220722_012342.jpg'
filename = 'd.jpg'

img = cv2.imread(filename)

#img = cv2.resize(img,(384,240))
try:
    analyze = DeepFace.analyze(img, actions=['emotion'])
    emotion = analyze['dominant_emotion']  # 取得情緒文字
    print("emotion = ", emotion)
    putText(0,40,emotion)                  # 放入文字
except:
    print('fail')
    pass
cv2.imshow('ImageShow', img)

sys.exit()




cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(384,240))
    try:
        analyze = DeepFace.analyze(img, actions=['emotion'])
        emotion = analyze['dominant_emotion']  # 取得情緒文字
        putText(0,40,emotion)                  # 放入文字
    except:
        pass
    cv2.imshow('ImageShow', img)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

sys.exit()

print("------------------------------------------------------------")  # 60個

from deepface import DeepFace    # 載入 deepface

cap = cv2.VideoCapture(0)        # 讀取攝影鏡頭

# 定義在畫面中放入文字的函式
def putText(source, x, y, text, scale=2.5, color=(255,255,255)):
    org = (x,y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)


a = 0        # 白色圖片透明度
n = 0        # 檔名編號
happy = 0    # 是否有 happy 的變數

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)   # 轉換成 BGRA，目的為了和白色圖片組合
    w = int(img.shape[1]*0.5)           # 取得圖片寬度的 1/2
    h = int(img.shape[0]*0.5)           # 取得圖片高度的 1/2
    img = cv2.resize(img,(w,h))         # 縮小圖片尺寸 ( 加快處理速度 )
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    key = cv2.waitKey(1)                # 每隔一毫秒取得鍵盤輸入資訊

    try:
        emotion = DeepFace.analyze(img, actions=['emotion'])               # 情緒偵測
        print(emotion['emotion']['happy'], emotion['emotion']['neutral'])  # 印出數值
        if emotion['emotion']['happy'] >0.5:
            happy = happy + 1       # 如果具有一點點 happy 的數值，就認定正在微笑，將 happy 增加 1
        else:
            happy = 0               # 如果沒有 happy，將 happy 歸零
    except:
        pass

    if happy == 1:
        a = 1                # 如果 happy 等於 1，將 a 變成 1 ，觸發拍照程式
        sec = 4              # 倒數秒數從 4 開始

    if key == 32:            # 按下空白將 a 等於 1 ( 按下空白也可以拍照 )
        a = 1
        sec = 4
    elif key == ord('q'):    # 按下 q 結束
        break

    if a == 0:
        output = img.copy()  # 如果 a 為 0，設定 output 和 photo 變數
    else:
        if happy >= 1:
            output = img.copy()
            photo = img.copy()
            sec = sec - 0.5       # 根據個人電腦效能，設定到接近倒數三秒
            putText(output, 10, 70, str(int(sec)))
            if sec < 1:
                output = cv2.addWeighted(white, a, photo, 1-a, 0)  # 計算權重，產生白色慢慢消失效果
                a = a - 0.5
                print('a', a)
                if a<=0:
                    a = 0
                    n = n + 1
                    cv2.imwrite(f'photo-{n}.jpg', photo)   # 存檔
                    print('save ok')
        else:
            a = 0
            pass
    cv2.imshow('ImageShow', output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

