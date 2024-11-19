"""

在 28X28的方塊內 用滑鼠寫數字

按S, 用 CNN 來辨識


"""

import sys
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

# 讀取模型架構
json_file = open("data/model.json", "r")

loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

# 讀取模型權重
model.load_weights("data/model.h5")

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)


def CNN():
    img_rows = 28
    img_cols = 28
    b = img.astype(dtype=np.float32)
    # 將原始資料轉為正確的影像排列方式
    x_test = b.reshape(1, 28, 28, 1)
    # 標準化輸入資料
    x_test /= 255
    # 輸出結果

    # y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
    predict_x = model.predict(x_test)
    classes_x = np.argmax(predict_x, axis=1)
    y_pred = classes_x
    print("predict_classes:", y_pred)


img = np.full(shape=(28, 28, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow("image")

drawing = False


def draw_circle(event, x, y, flags, param):
    global img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 1, (255), -1)


cv2.setMouseCallback("image", draw_circle)

while 1:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("s"):
        print("Save")
        cv2.imwrite("tmp_1.jpg", img)
        CNN()
    elif k == ord("c"):
        print("Clear")
        img = np.full(shape=(28, 28, 1), fill_value=0, dtype=np.uint8)
    elif k == 27:
        print("ESC")
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
