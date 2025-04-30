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
show_train_history(train_history, "accuracy", "val_accuracy")
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
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

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
show_train_history(train_history, "accuracy", "val_accuracy")
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
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import ZeroPadding2D


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

# 久
train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)
show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_img_train_normalize, y_label_train_OneHot, verbose=0)
print(scores[1])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 5.1 建立Computational Graph

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

# 建立 const

ts_c = tf.constant(2, name="ts_c")

print(ts_c)

# <tf.Tensor 'ts_c:0' shape=() dtype=int32>

# 建立 Variable

ts_x = tf.Variable(ts_c + 5, name="ts_x")

print(ts_x)

# <tf.Variable 'ts_x:0' shape=() dtype=int32_ref>

# 5.2 建立Session執行Computational Graph

init = tf.global_variables_initializer()

ts_c = 2

ts_x = 7

# --------------------------------------

# Session open close

# import tensorflow as tf
ts_c = tf.constant(2, name="ts_c")
ts_x = tf.Variable(ts_c + 5, name="ts_x")

sess = tf.Session()
init = tf.global_variables_initializer()

sess.close()

# With語法開啟Session

ts_c = tf.constant(2, name="ts_c")
ts_x = tf.Variable(ts_c + 5, name="ts_x")
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# --------------------------------------

# Create dim 1 tensor

ts_X = tf.Variable([0.4, 0.2, 0.4])

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# Create dim 2 tensor

ts_X = tf.Variable([[0.4, 0.2, 0.4]])

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# shape: (1, 3)

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])

with tf.Session() as sess:
    init = tf.global_variables_initializer()

# matmul

X = tf.Variable([[1.0, 1.0, 1.0]])

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])

XW = tf.matmul(X, W)

with tf.Session() as sess:
    init = tf.global_variables_initializer()

tf.add

b = tf.Variable([[0.1, 0.2]])
XW = tf.Variable([[-1.3, 0.4]])

Sum = XW + b
with tf.Session() as sess:
    init = tf.global_variables_initializer()

X = tf.Variable([[1.0, 1.0, 1.0]])

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])


b = tf.Variable([[0.1, 0.2]])

XWb = tf.matmul(X, W) + b


with tf.Session() as sess:
    init = tf.global_variables_initializer()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

size = 500
W = tf.random_normal([size, size], name="W")
X = tf.random_normal([size, size], name="X")
mul = tf.matmul(W, X, name="mul")
sum_result = tf.reduce_sum(mul, name="sum")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_Introduce

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

print("train data=", len(x_train_image))
print(" test data=", len(x_test_image))

# train data= 60000
# test data= 10000

print("x_train_image:", x_train_image.shape)
print("y_train_label:", y_train_label.shape)

# x_train_image: (60000, 28, 28)
# y_train_label: (60000,)


def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap="binary")
    show()


plot_image(x_train_image[0])

print(y_train_label[0])
# 5


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
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_train_image, y_train_label, [], 0, 10)

print("x_test_image:", x_test_image.shape)
print("y_test_label:", y_test_label.shape)

# x_test_image: (10000, 28, 28)
# y_test_label: (10000,)

plot_images_labels_prediction(x_test_image, y_test_label, [], 0, 10)

# 將images進行預處理

print("x_train_image:", x_train_image.shape)
print("y_train_label:", y_train_label.shape)

# x_train_image: (60000, 28, 28)
# y_train_label: (60000,)

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

print("x_train:", x_Train.shape)
print("x_test:", x_Test.shape)

# x_train: (60000, 784)
# x_test: (10000, 784)

print(x_train_image[0])

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

print(x_Train_normalize[0])

# one hot encode outputs

print(y_train_label[:5])

y_TrainOneHot = tf.keras.utils.to_categorical(y_train_label)
y_TestOneHot = tf.keras.utils.to_categorical(y_test_label)

print(y_TrainOneHot[:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_CNN

from keras.datasets import mnist

# from tensorflow.keras.utils import to_categorical

np.random.seed(10)

# 資料預處理

(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()

x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28, 1).astype("float32")
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype("float32")

x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255

y_TrainOneHot = tf.keras.utils.to_categorical(y_Train)
y_TestOneHot = tf.keras.utils.to_categorical(y_Test)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

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

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train4D_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=2,
    batch_size=300,
    verbose=2,
)

print(type(train_history))
print(train_history)

print(train_history.history.keys())

# summarize history for accuracy
plt.plot(train_history.history["accuracy"])
plt.plot(train_history.history["val_accuracy"])
plt.title("model accuracy")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
show()

# summarize history for loss
plt.plot(train_history.history["loss"])
plt.plot(train_history.history["val_loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
show()


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率
# 久
print("aaaaaaa 久")
scores = model.evaluate(x_Test4D_normalize, y_TestOneHot)
print(scores[1])

print("bbbbbbb 久")
# 預測結果
# prediction = model.predict_classes(x_Test4D_normalize) # old
predict_x = model.predict(x_Test4D_normalize)
prediction = np.argmax(predict_x, axis=1)

print("ccccccc")

# 9888/10000 [============================>.] - ETA: 0s

cc = prediction[:10]
print(cc)

# array([7, 2, 1, 0, 4, 1, 4, 9, 5, 9], dtype=int64)

# 查看預測結果


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        ax.set_title(
            "label=" + str(labels[idx]) + ",predict=" + str(prediction[idx]),
            fontsize=10,
        )

        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


print("ddddd")

plot_images_labels_prediction(x_Test, y_Test, prediction, idx=0)

# confusion matrix

cc = pd.crosstab(y_Test, prediction, rownames=["label"], colnames=["predict"])
print(cc)

df = pd.DataFrame({"label": y_Test, "predict": prediction})

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h256

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(
    Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=2,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])

# 進行預測

# prediction=model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)

print(prediction)


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
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=0)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
print(df[:2])

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets(
    "C:/_git/vcs/_4.python/ml/data/MNIST_data/", one_hot=True
)

print(
    "train images     :", mnist.train.images.shape, "labels:", mnist.train.labels.shape
)
print(
    "validation images:",
    mnist.validation.images.shape,
    " labels:",
    mnist.validation.labels.shape,
)
print("test images      :", mnist.test.images.shape, "labels:", mnist.test.labels.shape)


# 建立模型
def layer(output_dim, input_dim, inputs, activation=None):
    W = tf.Variable(tf.random_normal([input_dim, output_dim]))
    b = tf.Variable(tf.random_normal([1, output_dim]))
    XWb = tf.matmul(inputs, W) + b
    if activation is None:
        outputs = XWb
    else:
        outputs = activation(XWb)
    return outputs


# 建立輸入層 x

import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

tf.disable_v2_behavior()

x = tf.placeholder("float", [None, 784])

# 建立隱藏層h1

h1 = layer(output_dim=1000, input_dim=784, inputs=x, activation=tf.nn.relu)

# 建立輸出層

y_predict = layer(output_dim=10, input_dim=1000, inputs=h1, activation=None)

# 建立訓練資料label真實值 placeholder

y_label = tf.placeholder("float", [None, 10])

# 定義訓練方式

loss_function = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(logits=y_predict, labels=y_label)
)

optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss_function)

# 定義評估模型的準確率

# 計算每一筆資料是否正確預測

correct_prediction = tf.equal(tf.argmax(y_label, 1), tf.argmax(y_predict, 1))

# 將計算預測正確結果，加總平均

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 開始訓練

trainEpochs = 15
batchSize = 100
totalBatchs = int(mnist.train.num_examples / batchSize)
epoch_list = []
accuracy_list = []
loss_list = []
from time import time

startTime = time()
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(trainEpochs):
    for i in range(totalBatchs):
        batch_x, batch_y = mnist.train.next_batch(batchSize)
        sess.run(optimizer, feed_dict={x: batch_x, y_label: batch_y})

    loss, acc = sess.run(
        [loss_function, accuracy],
        feed_dict={x: mnist.validation.images, y_label: mnist.validation.labels},
    )

    epoch_list.append(epoch)
    loss_list.append(loss)
    accuracy_list.append(acc)

    print(
        "Train Epoch:",
        "%02d" % (epoch + 1),
        "Loss=",
        "{:.9f}".format(loss),
        " Accuracy=",
        acc,
    )

duration = time() - startTime
print("Train Finished takes:", duration)

fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.plot(epoch_list, loss_list, label="loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["loss"], loc="upper left")
show()

plt.plot(epoch_list, accuracy_list, label="accuracy")
fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.ylim(0.8, 1)
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend()
show()

# 評估模型準確率

print(
    "Accuracy:",
    sess.run(accuracy, feed_dict={x: mnist.test.images, y_label: mnist.test.labels}),
)

# Accuracy: 0.9577

# 進行預測

prediction_result = sess.run(tf.argmax(y_predict, 1), feed_dict={x: mnist.test.images})

cc = prediction_result[:10]
print(cc)

# array([7, 2, 1, 0, 4, 1, 8, 9, 4, 9])


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)

        ax.imshow(np.reshape(images[idx], (28, 28)), cmap="binary")

        title = "label=" + str(np.argmax(labels[idx]))
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(
    mnist.test.images, mnist.test.labels, prediction_result, 0
)

y_predict_Onehot = sess.run(y_predict, feed_dict={x: mnist.test.images})

cc = y_predict_Onehot[8]
print(cc)

# sess.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000_DropOut

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

# 將「輸入層」與「隱藏層」加入模型

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dropout(0.5))

# 將「輸出層」加入模型

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

# 久
scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print("accuracy=", scores[1])

# accuracy= 0.9808

# 進行預測

# prediction = model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)

print(prediction)

# array([7, 2, 1, ..., 4, 5, 6], dtype=int64)


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
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
cc = df[:2]
print(cc)

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000_DropOut_h1000_DropOut

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

# 將「輸入層」與「隱藏層1」加入模型

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dropout(0.5))

# 將「隱藏層2」加入模型

model.add(Dense(units=1000, kernel_initializer="normal", activation="relu"))

model.add(Dropout(0.5))

# 將「輸出層」加入模型

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])

# accuracy= 0.9802

# 進行預測
# prediction = model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)
print(prediction)


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
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
cc = df[:2]
print(cc)

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Taianic_Introduce


# 下載鐵達尼號旅客資料集

import urllib.request
import os

url = "http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls"  # old
url = "https://hbiostat.org/data/repo/titanic3.xls"
filename = "tmp_titanic3.xls"
if not os.path.isfile(filename):
    result = urllib.request.urlretrieve(url, filename)
    print("downloaded:", result)

# 使用Pandas dataframe讀取資料並進行處理

all_df = pd.read_excel(filename)

print(all_df.shape)

# 1309筆資料, 14欄位

# 查看前2筆資料
cc = all_df[:2]
print(cc)


"""
1	2		3	4	5	6	7
pclass	survived	name	sex	age	sibsp	parch
8	9	10	11		12	13	14
ticket	fare	cabin	embarked	boat	body	home.dest
	
資料欄位包含:
艙等:pclass
是否生存:survival
姓名:name
性別:sex
年齡:age
手足、配偶也在船上數量:sibsp
雙親或子女也在船上數量:parch
車票號碼:ticket
旅客費用:fare
艙位號碼:cabin
登船港口embarked
"""

# 選取所需的欄位, 只抓取需要的欄位至dataframe
cols = [
    "survived",
    "name",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]
all_df = all_df[cols]


"""
資料欄位包含:
是否生存:survival
艙等:pclass
姓名:name
性別:sex
年齡:age
手足、配偶也在船上數量:sibsp
雙親或子女也在船上數量:parch
旅客費用:fare
登船港口embarked
"""

# 4) 開始資料處理
"""
姓名先移除，訓練時不需要
性別:sex，欄位為文字，將轉為0、1
年齡:age，為null值，將填入平均值
旅客費用:fare，為null值，將填入平均值
登船港口embarked(有3類C、Q、S)，用onehot encoding 轉換
"""


cc = all_df[:2]
print(cc)

# 找出含有null值的欄位
cc = all_df.isnull().sum()
print(cc)

# 將name欄位移除
df = all_df.drop(["name"], axis=1)
# axis=0，指删除index，因此删除columns时要指定axis=1

# 資料都填上平均值 把age為null值的欄位補上平均值
age_mean = df["age"].mean()

df["age"] = df["age"].fillna(age_mean)

# 把fare為null值的欄位補上平均值
fare_mean = df["fare"].mean()
df["fare"] = df["fare"].fillna(fare_mean)

# 性別欄位轉換 轉換性別為0,1 需要將文字轉成數字才能進行訓練
df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)

cc = df[:2]
print(cc)

# 用Onehot Enconding轉換
# 登船港口embarked 轉換
# data為要轉換的dataframe  columns為要轉換的欄位
x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

cc = x_OneHot_df[:2]
print(cc)

# 4) dataframe轉換為array 。之後資料處理需要用到
# 轉換為array

ndarray = x_OneHot_df.values

print(ndarray.shape)

# (1309, 10)

print(ndarray[:2])

# 擷取features 和 label

Label = ndarray[:, 0]
Features = ndarray[:, 1:]

# 5) features 標準化，標準化之後的數字。都介顧0–1之間

print(Features.shape)

print(Features[:2])

print(Label.shape)

print(Label[:2])

# 將array進行標準化  將特徵欄位進行標準化

from sklearn import preprocessing

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

scaledFeatures = minmax_scale.fit_transform(Features)

print(scaledFeatures[:2])  # 查看前兩筆資料

print(Label[:5])

# 6) 將資料80% 為訓練資料、20 % 為測試資料
# 將資料分為訓練資料與測試資料
# 使用隨機方式分類並顯示
msk = np.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]

print("total:", len(all_df), "train:", len(train_df), "test:", len(test_df))

# total: 1309 train: 1043 test: 266

# 7)預處理function


def PreprocessData(raw_df):
    df = raw_df.drop(["name"], axis=1)
    age_mean = df["age"].mean()
    df["age"] = df["age"].fillna(age_mean)
    fare_mean = df["fare"].mean()
    df["fare"] = df["fare"].fillna(fare_mean)
    df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

    ndarray = x_OneHot_df.values
    Features = ndarray[:, 1:]
    Label = ndarray[:, 0]

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures = minmax_scale.fit_transform(Features)

    return scaledFeatures, Label


# 8) 進行資料預處理

train_Features, train_Label = PreprocessData(train_df)
test_Features, test_Label = PreprocessData(test_df)

print(train_Features[:2])  # 訓練資料特徵欄位

print(train_Label[:2])  # 訓練資料標籤欄位

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Taianic_MLP

from sklearn import preprocessing

np.random.seed(10)

filename = "tmp_titanic3.xls"

all_df = pd.read_excel(filename)

cols = [
    "survived",
    "name",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]
all_df = all_df[cols]

msk = np.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]

print("total:", len(all_df), "train:", len(train_df), "test:", len(test_df))

# total: 1309 train: 1034 test: 275


def PreprocessData(raw_df):
    df = raw_df.drop(["name"], axis=1)
    age_mean = df["age"].mean()
    df["age"] = df["age"].fillna(age_mean)
    fare_mean = df["fare"].mean()
    df["fare"] = df["fare"].fillna(fare_mean)
    df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

    ndarray = x_OneHot_df.values
    Features = ndarray[:, 1:]
    Label = ndarray[:, 0]

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures = minmax_scale.fit_transform(Features)

    return scaledFeatures, Label


train_Features, train_Label = PreprocessData(train_df)
test_Features, test_Label = PreprocessData(test_df)

# 3. Create Model

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

model.add(Dense(units=40, input_dim=9, kernel_initializer="uniform", activation="relu"))

model.add(Dense(units=30, kernel_initializer="uniform", activation="relu"))

model.add(Dense(units=1, kernel_initializer="uniform", activation="sigmoid"))

# 4. Train model

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

"""
train_history = model.fit(
    x=train_Features,
    y=train_Label,
    validation_split=0.1,
    epochs=30,
    batch_size=30,
    verbose=2,
)

# 6. Print History


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x=test_Features, y=test_Label)

print(scores[1])

# 預測資料
# 加入Jack & Rose資料

Jack = pd.Series([0, "Jack", 3, "male", 23, 1, 0, 5.0000, "S"])
Rose = pd.Series([1, "Rose", 1, "female", 20, 1, 0, 100.0000, "S"])

JR_df = pd.DataFrame(
    [list(Jack), list(Rose)],
    columns=[
        "survived",
        "name",
        "pclass",
        "sex",
        "age",
        "sibsp",
        "parch",
        "fare",
        "embarked",
    ],
)

all_df = pd.concat([all_df, JR_df])

print(all_df[-2:])

# 進行預測

all_Features, Label = PreprocessData(all_df)

all_probability = model.predict(all_Features)

cc = all_probability[:10]
print(cc)

pd = all_df
pd.insert(len(all_df.columns), "probability", all_probability)

# 預測Jack & Rose資料的生存機率

print(pd[-2:])

# 查看生存機率高，卻沒有存活

cc = pd[(pd["survived"] == 0) & (pd["probability"] > 0.9)]
print(cc)

print(pd[:5])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Cifar_CNN-Introduce.ipynb

from keras.datasets import cifar10

np.random.seed(10)

# 資料準備

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train:", len(x_img_train))
print("test :", len(x_img_test))

print(x_img_train.shape)

print(y_label_train.shape)

print(x_img_test.shape)

print(x_img_test[0])

print(y_label_test.shape)

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


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_train, y_label_train, [], 0)

print("x_img_test:", x_img_test.shape)
print("y_label_test :", y_label_test.shape)

# Image normalize

print(x_img_train[0][0][0])

# array([59, 62, 63], dtype=uint8)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

print(x_img_train_normalize[0][0][0])

# array([ 0.23137255,  0.24313726,  0.24705882], dtype=float32)

# 轉換label 為OneHot Encoding

print(y_label_train.shape)

# (50000, 1)

print(y_label_train[:5])

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_train_OneHot.shape)

print(y_label_train_OneHot[:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Cifar_CNN

from keras.datasets import cifar10

np.random.seed(10)

# 資料準備

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", x_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", x_img_test.shape, " labels:", y_label_test.shape)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import ZeroPadding2D

model = Sequential()

# 卷積層1

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

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

model.add(Dropout(0.25))

model.add(MaxPooling2D(pool_size=(2, 2)))

# Step3	建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(rate=0.25))

model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModelnew1.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.7339

# 進行預測

prediction = model.predict_classes(x_img_test_normalize)

print(prediction[:10])

# 查看預測結果

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


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_test, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(x_img_test_normalize)


def show_Predicted_Probability(y, prediction, x_img, Predicted_Probability, i):
    print("label:", label_dict[y[i][0]], "predict:", label_dict[prediction[i]])
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(x_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 0
)

show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 3
)

print("confusion matrix")

print(prediction.shape)

print(y_label_test.shape)

print(y_label_test)

print(y_label_test.reshape(-1))

print(label_dict)
cc = pd.crosstab(
    y_label_test.reshape(-1), prediction, rownames=["label"], colnames=["predict"]
)
print(cc)

print(label_dict)

# Save model to JSON

model_json = model.to_json()
with open("SaveModel/cifarCnnModelnew.json", "w") as json_file:
    json_file.write(model_json)

# Save Model to YAML

model_yaml = model.to_yaml()
with open("SaveModel/cifarCnnModelnew.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Cifar_CNN_Continue_Train

from keras.datasets import cifar10

np.random.seed(10)

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", x_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", x_img_test.shape, " labels:", y_label_test.shape)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

model = Sequential()

# 卷積層1

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

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

model.add(Dropout(0.25))

model.add(MaxPooling2D(pool_size=(2, 2)))

# Step3	建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(rate=0.25))

model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModel.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 載入模型失敗!開始訓練一個新模型

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=1,
    batch_size=128,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.57869999999999999

# 進行預測

prediction = model.predict_classes(x_img_test_normalize)

print(prediction[:10])

# 查看預測結果

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


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_test, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(x_img_test_normalize)


def show_Predicted_Probability(y, prediction, x_img, Predicted_Probability, i):
    print("label:", label_dict[y[i][0]], "predict:", label_dict[prediction[i]])
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(x_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 0
)

show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 3
)

print("confusion matrix")

print(prediction.shape)

print(y_label_test.shape)

print(y_label_test)

print(y_label_test.reshape(-1))

print(label_dict)
cc = pd.crosstab(
    y_label_test.reshape(-1), prediction, rownames=["label"], colnames=["predict"]
)

print(cc)

print(label_dict)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModel.h5")
print("Saved model to disk")

# Saved model to disk

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Cifar_CNN_Deeper_Conv3

# Simple CNN model for the CIFAR-10 Dataset

from keras.datasets import cifar10

np.random.seed(10)

(X_img_train, y_label_train), (X_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", X_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", X_img_test.shape, " labels:", y_label_test.shape)

X_img_train_normalize = X_img_train.astype("float32") / 255.0
X_img_test_normalize = X_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

model = Sequential()

# 卷積層1與池化層1

model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)
model.add(Dropout(0.3))
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 卷積層3與池化層3

model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(2500, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(1500, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModelnew.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 載入模型失敗!開始訓練一個新模型

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    X_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=1,
    batch_size=300,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(X_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.10000000000000001

# 進行預測

prediction = model.predict_classes(X_img_test_normalize)

print(prediction[:10])

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


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(X_img_test_normalize, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(X_img_test_normalize)


def show_Predicted_Probability(X_img, Predicted_Probability, i):
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(X_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(X_img_test, Predicted_Probability, 0)

show_Predicted_Probability(X_img_test, Predicted_Probability, 3)

# Save model to JSON

model_json = model.to_json()
with open("SaveModel/cifarCnnModelnew.json", "w") as json_file:
    json_file.write(model_json)

# Save Model to YAML

model_yaml = model.to_yaml()
with open("SaveModel/cifarCnnModelnew.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

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


"""
# from keras.utils import np_utils
# np_utils.to_categorical(y_Train)
改成
y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
# from keras.utils import np_utils
# np_utils.to_categorical(y_Train)
"""


""" 解决 placeholder
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0
tf.disable_v2_behavior()

x = tf.placeholder("float", [None, 784])
"""
