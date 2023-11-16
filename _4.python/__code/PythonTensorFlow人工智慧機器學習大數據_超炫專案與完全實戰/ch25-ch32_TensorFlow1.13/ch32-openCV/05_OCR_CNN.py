#!/usr/bin/env python
# author: Powen Ko  柯博文老師  www.powenko.com
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

# 讀取模型架構
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# 讀取模型權重
model.load_weights("model.h5")
# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(loss=tf.contrib.keras.losses.categorical_crossentropy,
            optimizer=tf.contrib.keras.optimizers.Adadelta(),
            metrics=['accuracy'])


def CNN():
    img_rows=28
    img_cols=28
    b=img.astype(dtype=np.float32)
    # 將原始資料轉為正確的影像排列方式
    x_test = b.reshape(1, 28, 28, 1)
    # 標準化輸入資料
    x_test /= 255
    # 輸出結果
    predict = model.predict(x_test)
    print(predict[0])
    predict2 = model.predict_classes(x_test)
    print("predict_classes:", predict2)

img = np.full(shape=(28, 28, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow('image')

drawing = False
def draw_circle(event,x,y,flags,param):
    global img,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),1,(255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),1,(255),-1)
cv2.setMouseCallback('image', draw_circle)



while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite("1.jpg",img)
        CNN()
    elif k == ord('c'):
        img = np.full(shape=(28, 28, 1), fill_value=0, dtype=np.uint8)
    elif k == 27:
        break

cv2.destroyAllWindows()