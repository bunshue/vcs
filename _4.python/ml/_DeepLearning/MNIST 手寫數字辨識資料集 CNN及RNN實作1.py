"""
MNIST 手寫數字辨識資料集 CNN及RNN實作1


https://github.com/SweetornotspicyMarathon/Learn-Tensorflow-Keras-Note/blob/main/U4%2BU6%2BU7.ipynb?source=post_page-----9327366cc838---------------------------------------



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

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from tensorflow.keras.utils import to_categorical  # One-Hot Encoding
from matplotlib.colors import ListedColormap

from sklearn import tree

import warnings

warnings.filterwarnings("ignore")


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# U6 MNIST 手寫數字辨識
# 1.查看資料集 train data 和test data

np.random.seed(10)

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
print("train data= ", len(x_train_image))
print("test data=", len(x_test_image))

# train data=  60000
# test data= 10000


def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap="binary")
    plt.show()


plot_image(x_train_image[0])


y_train_label[0]

# 5


# 建立函數要來畫多圖的
def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    # 設定顯示圖形的大小
    fig = plt.gcf()
    fig.set_size_inches(12, 14)

    # 最多25張
    if num > 25:
        num = 25

    # 一張一張畫
    for i in range(0, num):
        # 建立子圖形5*5(五行五列)
        ax = plt.subplot(5, 5, i + 1)

        # 畫出子圖形
        ax.imshow(images[idx], cmap="binary")

        # 標題和label
        title = "label=" + str(labels[idx])

        # 如果有傳入預測結果也顯示
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        # 設定子圖形的標題大小
        ax.set_title(title, fontsize=10)

        # 設定不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_train_image, y_train_label, [], 0, 10)


print("train data= ", len(x_train_image))
print("test data=", len(x_test_image))

print("x_test_image:", x_test_image.shape)
print("y_test_label:", y_test_label.shape)

x_test_image: (10000, 28, 28)
y_test_label: (10000,)

plot_images_labels_prediction(x_test_image, y_test_label, [], 0, 25)


# 2.清理資料 data cleaning
# 查看資料的型態
print("x_train_image:", x_train_image.shape)
print("y_train_label:", y_train_label.shape)


# 影像資料--------------------------------------
# 代表 train image 總共有6萬張，每一張是28*28的圖片
# label 也有6萬個
# 所以要把二維的圖片矩陣先轉換成一維
# 這裡的784是因為 28*28
x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

# 轉換後的資料型態，壓扁變成一維了
print(x_Train.shape)
print(x_Test.shape)

print(x_Train[0])

# 3.影像標準化(normailze)

# 由於是圖片最大的是255，所以全部除以255
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

print(x_Train_normalize[0])

# 4.label 前處理 使用one-hot encoding

# 查看原本的 label 型態
# 他是0~9的數字
y_train_label[:5]

y_TrainOneHot = to_categorical(y_train_label)
y_TestOneHot = to_categorical(y_test_label)

# 來看轉換好的
# 這個就是第一筆資料，他是數字5
print(y_TrainOneHot[:1])

# 5.建立模型 多元感知器Multilayer perceptron 模型

# 建立模型
model = Sequential()

# 建立輸入層和隱藏層
model.add(
    Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu")
)
# 定義隱藏層神經元個數256
# 輸入為28*28=784 個float 數字
# 使用 normal distribution 常態分布的亂數，初始化 weight權重 bias 偏差
# 定義激活函數為 relu


# 建立輸出層
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))
# 定義輸出層為10個 (數字0~9)
# 也是使用常態分佈初始化
# 定義激活函數是 softmax
# 這裡建立的Dense 層，不用設定 input dim ，因為keras 會自動照上一層的256設定

print(model.summary())

# 從這個 summary 可以看出 這一個模型是兩層的模型
# 然後隱藏層有256個神經元
# 輸出層有10個神經元

# 另外是 param 參數
# 參數的計算方式第一個是 200960=256*784+256
# 另外一個是2570=256*10+10=2570
# 下面有一個全部訓練 total params=200960+2570=203530

# 6.開始訓練

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# 模型訓練之前要用 compele 對模型進行設定
# loss 深度學習通常用 cross entropy 交叉嫡，訓練效果較好
# optimizer 設定訓練時依優化的方法，在深度學習使用 adam 最優化方法，最快收斂提高準確度
# metrics 設定評估模型的方式是 accuracy 準確率

# 開始訓練

train_history = model.fit(
    x=x_Train_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)
# x 是訓練資料
# y 是label 資料
# 設定參數 validation 切0.2起來驗證
# epoch=10 是訓練週期為10
# batch_size=200 每一批訓練200筆資料
# verbose =2 顯示訓練過程

# 所以以上的程式會執行10次
# 每一次執行200筆資料 ，總共訓練資料原本有60000*0.8=48000
# 48000/200=24 要跑240批次
# epoch 每一次訓練週期紀錄結果在 train_history 裡面


# 來把訓練過程畫出來


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train history")
    plt.ylabel("train")
    plt.xlabel("epoch")

    # 設置圖例在左上角
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")

# 7.評估測試資料準確率

scores = model.evaluate(x_Test_normalize, y_TestOneHot)
print()
print("111 accuracy", scores[1])

# accuracy 0.9782999753952026

# 8.執行預測

# prediction = model.predict_classes(x_Test)  # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_Test)
classes_x = np.argmax(predict_x, axis=1)
prediction = classes_x

prediction

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)


# 9.顯示混淆矩陣 confussion table

pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["prediction"])

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
df[:10]


df[(df.label == 5) & (df.predict == 3)]

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

# 10. 隱藏層增加為1000個神經元

model = Sequential()

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="softmax")
)
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 開始訓練
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
train_history = model.fit(
    x=x_Train_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

show_train_history(train_history, "accuracy", "val_accuracy")

# 11.加入 dropout 避免overfitting

model = Sequential()

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="softmax")
)
model.add(Dropout(0.5))
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))
print(model.summary())

# 開始訓練
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=20,
    batch_size=200,
    verbose=2,
)
show_train_history(train_history, "accuracy", "val_accuracy")

scores = model.evaluate(x_Test_normalize, y_TestOneHot)
print()
print("222 accuracy", scores[1])

# accuracy 0.9362999796867371

# 12.建立多層感知模型包含2 個隱藏層

model = Sequential()

print("先到此")

# 以下NG

sys.exit()


model(Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(units=1000, kernel_initializer="normal", activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))


# 開始訓練
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=20,
    batch_size=200,
    verbose=2,
)
show_train_history(train_history, "accuracy", "val_accuracy")

scores = model.evaluate(x_Test_normalize, y_TestOneHot)
print()
print("333 accuracy", scores[1])

print(model.summary())

# accuracy 0.9800999760627747


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
