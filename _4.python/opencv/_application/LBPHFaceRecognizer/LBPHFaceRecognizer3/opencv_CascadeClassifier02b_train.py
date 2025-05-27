import cv2
import numpy as np

target_dir = "images"

images = []
labels = []
for index in range(10):
    filename = target_dir + "/{:03d}.jpg".format(index + 1)
    print("read " + filename)
    img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    images.append(img)
    labels.append(0)  # 第一張人臉的標籤為0

print("訓練中......")

# 人臉特徵演算法計算特徵值(LBPH演算法)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(images), np.asarray(labels))
model.save("faces.data")

print("訓練完成")
