"""
TensorFlow+Keras深度學習人工智慧實務應用

http://www.drmaster.com.tw/download/example/MP21710_example.zip


"""
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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sklearn
import tensorflow as tf
from sklearn import datasets
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法
from sklearn.cluster import MeanShift  # 均值偏移_聚類演算法
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. 全连接mnist数字识别
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import mnist

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255
y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)
model = Sequential()
model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)
model.add(Dropout(0.5))
model.add(Dense(units=1000, kernel_initializer="normal", activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))
print(model.summary())
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)
"""
show_train_history(train_history, "acc", "val_acc")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])
prediction = model.predict_classes(x_Test)
plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)
# pd.crosstab(y_test_label,prediction,rownames=['label'],
#             colnames=['predict'])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 2. cnn on mnist


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import mnist

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()
x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28, 1).astype("float32")
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype("float32")
x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255
y_TrainOneHot = tf.keras.utils.to_categorical(y_Train)
y_TestOneHot = tf.keras.utils.to_categorical(y_Test)
model = Sequential()
model.add(
    Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
print(model.summary())
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
train_history = model.fit(
    x=x_Train4D_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=300,
    verbose=2,
)
"""
show_train_history(train_history, "acc", "val_acc")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_Test4D_normalize, y_TestOneHot)
print(scores[1])
prediction = model.predict_classes(x_Test4D_normalize)
pd.crosstab(y_Test, prediction, rownames=["label"], colnames=["predict"])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3. cnn on cifar10

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import cifar10

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0
y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)
model = Sequential()
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)
model.add(Dropout(rate=0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(rate=0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(rate=0.25))
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
""" 久
train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)
show_train_history(train_history, "acc", "val_acc")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_img_train_normalize, y_label_train_OneHot, verbose=0)
print(scores[1])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
