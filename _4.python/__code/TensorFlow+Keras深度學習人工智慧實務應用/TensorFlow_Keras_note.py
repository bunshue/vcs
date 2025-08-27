"""
TensorFlow_Keras_note

TensorFlow+Keras 深度學習人工智慧實務應用 書籍(作者:林大貴)學習筆記

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation

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

"""
結論
多層感知器 Multilayer perceptron 模型，辨識手寫字
嘗試將模型加寬加深，加入 drop 以提高準確度，避免 overfitting
但多層感知器有其極限，若要提高準確度，就要使用卷積神經網路 CNN
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# U8

"""
CNN來了喔
多層感知器VS CVV卷積神經網路
最大的差異在 :
CNN增加了卷積層、池化層、來處理提取特徵
CNN介紹 ，可以分成兩部分:
1. 影像的特徵提取，透過卷積層、池化層 (擷取影像特徵很像是加入濾鏡的效果)
2. 完全連結神經網路，包含平坦層、隱藏層、輸出層
卷積層的意義
將原本一個影像，經過卷積運算，產生多影像，像是照片卷積起來
卷積算不改變原影像大小，卷積的效果很類似濾鏡效果，可以提取不同特徵，EX:邊緣、線條、和角
使用Max-pool 做下採樣(downsampling)
有的好處是
1.減少需處理的資料點
2.讓影像位置差異變小
3.參數的數量和計算量下降=>控制overfitting
1.資料前處理
這裡和之前多層感知器(MLP)的資料型態不同
因為MLP 直接送進神經元處理 原本28*28的圖片把它壓扁成784
但CNN必須要通過卷積跟池化所以要維持影像的維度，也就是28X81
"""

np.random.seed(10)

(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()
print(x_Train.shape)

# (60000, 28, 28)

# 將feature 轉換成4維度 ，也就是6000*28*28*1
x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28, 1).astype("float32")
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype("float32")

print(x_Train.shape)

# 數值標準化
x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255

# label 用one hot enconding 轉換
y_TrainOneHot = to_categorical(y_Train)
y_TestOneHot = to_categorical(y_Test)

# (60000, 28, 28)

# 2.建立模型

model = Sequential()

# 建立卷積層1=>28*28大小，但是產生16個影像
model.add(
    Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)

# 建立池化層1
# 執行第一次降採樣，原本的28*28變成14*14=>16個14*14
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立卷積層2=>將原本的16個影像轉換成36，大小還是14*14
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding="same", activation="relu"))

# 建立池化層2=>原本36個14*14變成，36個7*7
model.add(MaxPooling2D(pool_size=(2, 2)))

# 加入dropout 避免 overfitting，這裡的0.25，是在每一次捨棄25%的神經元
model.add(Dropout(0.25))

# --------------------------------
# 建立神經網路
# 建立平坦層=>把他們壓扁，所以是36個*14*14=1764對應1764個神經元
model.add(Flatten())

# 建立隱藏層
model.add(Dense(128, activation="relu"))

# 捨棄50%神經元
model.add(Dropout(0.5))

# 建立輸出層
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 3.訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train4D_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=300,
    verbose=2,
)


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

# 4.評估模型準確率

scores = model.evaluate(x_Test4D_normalize, y_TestOneHot)
print(scores[1])

# 5.執行預測

# prediction=model.predict_classes(x_Test4D_normalize)  # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_Test4D_normalize)
classes_x = np.argmax(predict_x, axis=1)
prediction = classes_x

prediction[:10]


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)

    if num > 25:
        num = 25

    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])

        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_Test, y_Test, prediction, idx=0)

# 6.混淆矩陣

pd.crosstab(y_Test, prediction, rownames=["label"], colnames=["predict"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# U9 + U10

# U9
"""
這一單元要使用 CIFAR-10 的資料庫
資料庫中有十種分類，分別是: 飛機、汽車、鳥、貓、鹿、狗、青蛙、船、卡車
"""

# 1.下載Cifar10資料
from keras.datasets import cifar10

np.random.seed(10)

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train :", len(x_img_train))
print("test :", len(x_img_test))

# 有5萬筆訓練;1萬筆測試

print("train image shape :", x_img_train.shape)
# 總共有5萬張影像，每一張影像是32*32*3，最後一個3表示為RGB彩色影像

print("trian label shape :", y_label_train.shape)

# 來看第0筆資料長甚麼樣子

print(x_img_test[0])
print(y_label_test[0])

# 來看多筆的image and label

# 先把分類轉換成文字

label_dict = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}


def plot_image_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(16, 8)

    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_image_labels_prediction(x_img_train, y_label_train, [], 0)

# 2.資料前處理

print(x_img_train[0][0][0])

# 影像正規化
# normalize all/255
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

print(x_img_train_normalize[0][0][0])


cc = y_label_train[:5]
print(cc)

# label 正規化 one hot

print(y_label_train[:5])

y_label_train_OneHot = to_categorical(y_label_train)
y_label_test_OneHot = to_categorical(y_label_test)

print(y_label_train_OneHot)
print(y_label_train_OneHot.shape)


# U10
# 開始使用CNN

# 建立模型
model = Sequential()

# 建立卷積層1
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)

# 加入dropout
model.add(Dropout(rate=0.25))

# 建立池化層1
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立卷積層2
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.25))

# 建立平坦層
model.add(Flatten())
model.add(Dropout(rate=0.25))

# 建立隱藏層
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

# 建立輸出層
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 開始訓練

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)

# 底下跑10個 epoch
# 每一個epoch 每一批資料因為為128筆，所以是總共40000筆資料/128一次=313


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

# 評估模型準確率

scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
scores[1]


# 0.6955000162124634


# 進行預測

# prediction = model.predict_classes(x_img_test_normalize)  # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_img_test_normalize)
classes_x = np.argmax(predict_x, axis=1)
prediction = classes_x
prediction[:10]

# array([3, 8, 8, 0, 4, 6, 1, 6, 3, 1])

plot_image_labels_prediction(x_img_test, y_label_test, prediction, 0, 10)


Predicted_Probability = model.predict(x_img_test_normalize)


def show_Predicted_Probability(y, prediction, x_img, Predicted_Probability, i):
    print("label:", label_dict[y[i][0]], "predict", label_dict[prediction[i]])
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(x_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + "Probability: %1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 0
)

"""
label: cat predict cat

airplaneProbability: 0.000368072
automobileProbability: 0.000068074
birdProbability: 0.003527550
catProbability: 0.852452576
deerProbability: 0.005850250
dogProbability: 0.134105921
frogProbability: 0.000298286
horseProbability: 0.002257990
shipProbability: 0.001003677
truckProbability: 0.000067636
"""

show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 3
)

"""
label: airplane predict airplane

airplaneProbability: 0.688755810
automobileProbability: 0.002678981
birdProbability: 0.016130244
catProbability: 0.000126020
deerProbability: 0.005111547
dogProbability: 0.000000309
frogProbability: 0.000008707
horseProbability: 0.000031111
shipProbability: 0.287136942
truckProbability: 0.000020297
"""

# 混淆矩陣 confusion table

cc = prediction.shape
print(cc)

# (10000,)

cc = y_label_test.shape
print(cc)

# (10000, 1)

cc = y_label_test.reshape(-1)
print(cc)

# array([3, 8, 8, ..., 5, 1, 7], dtype=uint8)

print(label_dict)
pd.crosstab(
    y_label_test.reshape(-1), prediction, rownames=["label"], colnames=["predict"]
)


# 建立3次的卷積運算神經網路

# 建立模型
model = Sequential()

# 建立卷積層1
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)

# 加入dropout
model.add(Dropout(rate=0.25))

# 建立池化層1
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立卷積層2
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.25))

# 建立卷積層3
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.5))


# 建立平坦層
model.add(Flatten())
model.add(Dropout(rate=0.25))

# 建立隱藏層
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

# 建立輸出層
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 開始訓練

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)

# 底下跑10個 epoch
# 每一個epoch 每一批資料因為為128筆，所以是總共40000筆資料/128一次=313


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


scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
scores[1]


# 0.732699990272522

# 優化模型 1

# 建立模型
model = Sequential()

# 建立卷積層1
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)

# 加入dropout
model.add(Dropout(rate=0.25))

# 建立池化層1
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立卷積層2
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.5))

# 建立卷積層3
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.5))

# 建立卷積層4
model.add(Conv2D(filters=256, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.25))

# 建立平坦層
model.add(Flatten())
model.add(Dropout(rate=0.25))

# 建立隱藏層
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

# 建立輸出層
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 開始訓練

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)

# 底下跑10個 epoch
# 每一個epoch 每一批資料因為為128筆，所以是總共40000筆資料/128一次=313


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


scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
scores[1]


# 0.6970000267028809

# 優化模型 2

# 建立模型
model = Sequential()

# 建立卷積層1
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)

# 加入dropout
model.add(Dropout(rate=0.25))

# 建立池化層1
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立卷積層2
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.5))

# 建立卷積層3
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.5))

# 建立卷積層4
model.add(Conv2D(filters=256, kernel_size=(3, 3), activation="relu", padding="same"))

# 加入dropout
model.add(Dropout(0.25))


# 建立平坦層
model.add(Flatten())
model.add(Dropout(rate=0.25))

# 建立隱藏層
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

# 建立輸出層
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 開始訓練

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=30,
    batch_size=128,
    verbose=1,
)

# 底下跑10個 epoch
# 每一個epoch 每一批資料因為為128筆，所以是總共40000筆資料/128一次=313


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


scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
scores[1]

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
