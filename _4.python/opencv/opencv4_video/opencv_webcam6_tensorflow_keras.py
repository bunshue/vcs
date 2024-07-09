"""
使用 tensorflow + keras



"""

import os
import sys
import time
import math
import random

print("------------------------------------------------------------")  # 60個

ESC = 27

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個



""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)   # 載入 model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)           # 設定資料陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()       # 讀取攝影機影像
    #img = cv2.resize(frame , (640//2, 480//2))   # 改變尺寸
    img = frame
    img = img[0:224, 80:304]               # 裁切為正方形，符合 model 大小
    image_array = np.asarray(img)          # 去除換行符號和結尾空白，產生文字陣列
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # 轉換成預測陣列
    data[0] = normalized_image_array
    prediction = model.predict(data)       # 預測結果
    a,b= prediction[0]                     # 取得預測結果
    if a>0.9:
        print('oxxo')
    if b>0.9:
        print('維他命')
        
    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個


""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 2.5                      # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 5                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    #img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text('a')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('b')
    if c>0.9:
        text('c')
        
    cv2.imshow('ImageShow', img)
    
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 50)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    #img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text('剪刀')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('石頭')
    if c>0.9:
        text('布')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 1                        # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 2                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame , (640//2, 480//2))
    img frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]    # 印出每個項目的數值資訊
    print(a,b,bg)
    if a>0.999:              # 判斷有戴口罩
        text('ok~')
    if b>0.001:              # 判斷沒戴口罩
        text('no mask!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

""" 缺檔案
import tensorflow as tf

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model_3.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 30)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]
    print(a,b,bg)
    if a>0.999:
        text('很乖')
    if b>0.001:
        text('沒戴口罩!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist
from keras import utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 載入訓練集

# 訓練集資料
x_train = x_train.reshape(x_train.shape[0], -1)  # 轉換資料形狀
x_train = x_train.astype("float32") / 255  # 轉換資料型別
y_train = y_train.astype(np.float32)

# 測試集資料
x_test = x_test.reshape(x_test.shape[0], -1)  # 轉換資料形狀
x_test = x_test.astype("float32") / 255  # 轉換資料型別
y_test = y_test.astype(np.float32)

knn = cv2.ml.KNearest_create()  # 建立 KNN 訓練方法
knn.setDefaultK(5)  # 參數設定
knn.setIsClassifier(True)

print("training...")
knn.train(x_train, cv2.ml.ROW_SAMPLE, y_train)  # 開始訓練
knn.save("mnist_knn.xml")  # 儲存訓練模型
print("ok")

print("testing...")
test_pre = knn.predict(x_test)  # 讀取測試集並進行辨識
test_ret = test_pre[1]
test_ret = test_ret.reshape(
    -1,
)
test_sum = test_ret == y_test
acc = test_sum.mean()  # 得到準確率
print(acc)

print("------------------------------------------------------------")  # 60個

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

print("loading...")
knn = cv2.ml.KNearest_load("mnist_knn.xml")  # 載入模型
print("start...")

while True:
    ret, img = cap.read()
    #img = cv2.resize(img, (640//2, 480//2))  # 改變影像尺寸，加快處理效率
    x, y, w, h = 400, 200, 60, 60  # 定義擷取數字的區域位置和大小
    img_num = img.copy()  # 複製一個影像作為辨識使用
    img_num = img_num[y : y + h, x : x + w]  # 擷取辨識的區域

    img_num = cv2.cvtColor(img_num, cv2.COLOR_BGR2GRAY)  # 顏色轉成灰階
    # 針對白色文字，做二值化黑白轉換，轉成黑底白字
    ret, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
    output = cv2.cvtColor(img_num, cv2.COLOR_GRAY2BGR)  # 顏色轉成彩色
    img[0:60, 480:540] = output  # 將轉換後的影像顯示在畫面右上角

    img_num = cv2.resize(img_num, (28, 28))  # 縮小成 28x28，和訓練模型對照
    img_num = img_num.astype(np.float32)  # 轉換格式
    img_num = img_num.reshape(
        -1,
    )  # 打散成一維陣列資料，轉換成辨識使用的格式
    img_num = img_num.reshape(1, -1)
    img_num = img_num / 255
    img_pre = knn.predict(img_num)  # 進行辨識
    num = str(int(img_pre[1][0][0]))  # 取得辨識結果

    text = num  # 印出的文字內容
    org = (x, y - 20)  # 印出的文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出的文字字體
    fontScale = 2  # 印出的文字大小
    color = (0, 0, 255)  # 印出的文字顏色
    thickness = 2  # 印出的文字邊框粗細
    lineType = cv2.LINE_AA  # 印出的文字邊框樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)  # 印出文字

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 標記辨識的區域

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

