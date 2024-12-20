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

import tensorflow as tf
from sklearn import datasets
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score
from time import time


def show():
    # return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MLPClassifier（多層感知器分類器）

X = [[0.0, 0.0], [1.0, 1.0]]
y = [0, 1]
mlp = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 5), random_state=1
)
mlp.fit(X, y)

print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)

print("------------------------------------------------------------")  # 60個

# MLPClassifier（多層感知器分類器）

iris = datasets.load_iris()
data = iris.data
labels = iris.target

# We add max_iter=1000 becaue the default is max_iter=200 and
# it is not enough for full convergence
mlp = MLPClassifier(random_state=1, max_iter=1000)
mlp.fit(data, labels)

pred = mlp.predict(data)

print()
print("Accuracy: %.2f" % accuracy_score(labels, pred))

print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
data = iris.data
labels = iris.target

data_train, data_test, labels_train, labels_test = train_test_split(
    data, labels, test_size=0.5, random_state=1
)

scaler = StandardScaler()
scaler.fit(data)
data_train_std = scaler.transform(data_train)
data_test_std = scaler.transform(data_test)

data_train = data_train_std
data_test = data_test_std

# We add max_iter=1000 becaue the default is max_iter=200 and
# it is not enough for full convergence
mlp = MLPClassifier(random_state=1, max_iter=1000)
mlp.fit(data, labels)
mlp.fit(data_train, labels_train)
pred = mlp.predict(data_test)

print()
print("Misclassified samples: %d" % (labels_test != pred).sum())
print("Accuracy: %.2f" % accuracy_score(labels_test, pred))

print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap

# Apply standardization
standardised = True

# 0萼長 1萼寬 2瓣長 3瓣寬
M = {0: "sepal length", 1: "sepal width", 2: "petal length", 3: "petal width"}

# Choose two features
x = 1  # 1 corresponds to the sepal width 萼寬
y = 3  # 3 corresponds to the petal width 瓣寬

iris = datasets.load_iris()
data = iris.data[:, [x, y]]

labels = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.5, random_state=1
)

reg = StandardScaler()
reg.fit(data)
X_train_std = reg.transform(X_train)
X_test_std = reg.transform(X_test)

if standardised == False:
    X_train_std = X_train
    X_test_std = X_test

# We add max_iter=1000 becaue the default is max_iter=200 and
# it is not enough for full convergence
mlp = MLPClassifier(random_state=1, max_iter=1000)
mlp.fit(X_train_std, y_train)

y_pred = mlp.predict(X_test_std)
print("Misclassified samples: %d" % (y_test != y_pred).sum())

print("Accuracy: %.2f" % accuracy_score(y_test, y_pred))


def plot_decision_regions(data, labels, classifier, resolution=0.01):
    markers = ("s", "*", "^")
    colors = ("blue", "green", "red")
    cmap = ListedColormap(colors)
    # plot the decision surface
    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

    x, y = np.meshgrid(
        np.arange(x_min, x_max, resolution), np.arange(y_min, y_max, resolution)
    )

    Z = classifier.predict(np.array([x.ravel(), y.ravel()]).T)
    Z = Z.reshape(x.shape)

    plt.pcolormesh(x, y, Z, cmap=cmap)
    plt.xlim(x.min(), x.max())
    plt.ylim(y.min(), y.max())

    colors = ("yellow", "white", "black")
    # cmap = ListedColormap(colors)
    # plot the data
    classes = ["setosa", "versicolor", "verginica"]
    for index, cl in enumerate(np.unique(labels)):
        plt.scatter(
            data[labels == cl, 0],
            data[labels == cl, 1],
            c=cmap(index),
            marker=markers[index],
            edgecolor="black",
            alpha=1.0,
            s=50,
            label=classes[index],
        )


X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X_combined_std, y_combined, classifier=mlp)

if standardised == False:
    xString = M[x] + " [not standardized]"
    yString = M[y] + " [not standardized]"
else:
    xString = M[x] + " [standardized]"
    yString = M[y] + " [standardized]"

plt.xlabel(xString)
plt.ylabel(yString)
plt.legend(loc="upper left")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 建立模型
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

"""
# 使用Adam 每次計算移動0.001
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])
"""
# SGD 優化器 optimizer
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01, clipnorm=1.0),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

history = model.fit(x_train, y_train2, epochs=200, batch_size=128)

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_show.py

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 建立模型
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))

# Adam 優化器 optimizer
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

history = model.fit(x_train, y_train2, epochs=200, batch_size=128)

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

plt.plot(history.history["accuracy"])
plt.plot(history.history["loss"])
plt.title("model accuracy")
plt.ylabel("acc & loss")
plt.xlabel("epoch")
plt.legend(["acc", "loss"], loc="upper left")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_Tensorboard.py

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 建立模型
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))

# Adam 優化器 optimizer
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")
"""
# NG
history=model.fit(x_train, y_train2,
    epochs=200,batch_size=128,
    callbacks=[tensorboard],
    verbose=1)

#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:",y_pred)
print("y_test",y_test[:])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_Save.py

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 建立模型
model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim))

model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))

model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))

# Adam 優化器 optimizer
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")

"""
# NG
history=model.fit(x_train, y_train2,
    epochs=200,batch_size=128,
    callbacks=[tensorboard],
    verbose=1)

#保存模型架構
with open("tmp_model_mlp.json", "w") as json_file:
   json_file.write(model.to_json())
#保存模型權重
model.save_weights("tmp_model_mlp.h5")


#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:",y_pred)
print("y_test",y_test[:])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_Load.py

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 讀取模型架構
json_file = open("data/model_mlp_old.json", "r")
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

# 讀取模型權重
model.load_weights("data/model_mlp_old.h5")

# Adam 優化器 optimizer
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])


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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
