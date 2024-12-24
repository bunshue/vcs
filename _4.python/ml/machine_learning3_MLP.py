"""
MLPClassifier（多層感知器分類器）




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

X = [[0.0, 0.0], [1.0, 1.0]]
y = [0, 1]

mlp = MLPClassifier(
    solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 5), random_state=1
)  # 函數學習機

mlp.fit(X, y)  # 學習訓練.fit

print(mlp.n_layers_)
print(mlp.n_iter_)
print(mlp.loss_)
print(mlp.out_activation_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

digits = datasets.load_digits()

X = digits.images.reshape(len(digits.images), -1)
y = digits.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

model = MLPClassifier(hidden_layer_sizes=(16,))

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iris 資料 全部")

iris = datasets.load_iris()
data = iris.data
labels = iris.target

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 函數學習機

mlp.fit(data, labels)  # 學習訓練.fit

pred = mlp.predict(data)  # 預測.predict

print("Accuracy: %.2f" % accuracy_score(labels, pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iris 資料 分割+標準化")

iris = datasets.load_iris()
data = iris.data
labels = iris.target

data_train, data_test, labels_train, labels_test = train_test_split(
    data, labels, test_size=0.5
)

scaler = StandardScaler()
scaler.fit(data)
data_train_std = scaler.transform(data_train)
data_test_std = scaler.transform(data_test)

data_train = data_train_std
data_test = data_test_std

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 函數學習機

mlp.fit(data, labels)  # 學習訓練.fit

mlp.fit(data_train, labels_train)  # 學習訓練.fit

pred = mlp.predict(data_test)  # 預測.predict

print("Misclassified samples: %d" % (labels_test != pred).sum())
print("Accuracy: %.2f" % accuracy_score(labels_test, pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap

# 0萼長 1萼寬 2瓣長 3瓣寬
M = {
    0: "sepal length 萼長",
    1: "sepal width 萼寬",
    2: "petal length 瓣長",
    3: "petal width 瓣寬",
}

# Choose two features
x = 1  # 1 corresponds to the sepal width 萼寬
y = 3  # 3 corresponds to the petal width 瓣寬

iris = datasets.load_iris()
data = iris.data[:, [x, y]]

labels = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.5)

reg = StandardScaler()
reg.fit(data)
X_train_std = reg.transform(X_train)
X_test_std = reg.transform(X_test)

mlp = MLPClassifier(random_state=1, max_iter=1000)  # 函數學習機

mlp.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = mlp.predict(X_test_std)  # 預測.predict

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

    Z = classifier.predict(np.array([x.ravel(), y.ravel()]).T)  # 預測.predict
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

plt.xlabel(M[x] + " (標準化)")
plt.ylabel(M[y] + " (標準化)")
plt.legend()
show()

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


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
