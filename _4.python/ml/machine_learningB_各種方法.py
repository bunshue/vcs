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


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup markers generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )

    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot all samples
    X_test, y_test = X[test_idx, :], y[test_idx]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.8,
            c=cmap(idx),
            marker=markers[idx],
            label=cl,
        )

    # hightlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            # c='',
            alpha=1.0,
            linewidth=1,
            marker="o",
            s=55,
            label="test set",
        )


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap


def do_svm():
    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target
    X = np.array([m for m, n in zip(X, y) if n != 2])
    boolarr = y != 2
    y = y[boolarr]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=9487
    )

    sc = StandardScaler()
    sc.fit(X_train)  # 學習訓練.fit
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    svm = SVC(kernel="linear", C=1.0, random_state=9487)  # SVM 函數學習機
    svm.fit(X_train_std, y_train)  # 學習訓練.fit
    y_pred = svm.predict(X_test_std)  # 預測.predict

    print("Misclassified smaples: %d" % (y_test != y_pred).sum())
    print("Accuracy: %0.2f" % accuracy_score(y_test, y_pred))

    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined_std = np.hstack((y_train, y_test))
    plot_decision_regions(
        X=X_combined_std, y=y_combined_std, classifier=svm, test_idx=range(50, 100)
    )
    plt.xlabel("sepal length [standarlized]")
    plt.ylabel("petal length [standarlized]")
    plt.legend(loc="upper left")
    plt.show()


print("SVM")
do_svm()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap


def do_svm_kernel():
    X_xor = np.random.randn(200, 2)
    y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
    y_xor = np.where(y_xor, 1, -1)

    plt.scatter(
        X_xor[y_xor == 1, 0], X_xor[y_xor == 1, 1], c="b", marker="x", label="1"
    )
    plt.scatter(
        X_xor[y_xor == -1, 0], X_xor[y_xor == -1, 1], c="r", marker="s", label="-1"
    )
    plt.ylim(-3.0)
    plt.legend()
    plt.show()

    svm = SVC(kernel="rbf", random_state=9487, gamma=0.6, C=10.0)  # SVM 函數學習機
    svm.fit(X_xor, y_xor)  # 學習訓練.fit
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc="upper left")
    plt.show()


print("SVN Kernel")
do_svm_kernel()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets, metrics
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap


def do_decision_tree():
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data[:, [2, 3]], iris.target, test_size=0.25, random_state=4
    )
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    X_combined = np.vstack((x_train, x_test))
    y_combined = np.hstack((y_train, y_test))

    plot_decision_regions(X_combined, y_combined, classifier=clf)
    plt.xlabel("petal length [cm]")
    plt.ylabel("petal width [cm]")
    plt.legend(loc="upper left")
    plt.show()


print("決策樹")
do_decision_tree()

print("------------------------------------------------------------")  # 60個

from matplotlib.colors import ListedColormap
from sklearn import datasets, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def do_random_forest():
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data[:, [2, 3]], iris.target, test_size=0.25, random_state=4
    )
    clf = RandomForestClassifier(n_estimators=20, max_depth=4)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)

    X_combined = np.vstack((x_train, x_test))
    y_combined = np.hstack((y_train, y_test))

    plot_decision_regions(
        X_combined, y_combined, classifier=clf, test_idx=range(105, 150)
    )
    plt.xlabel("petal length [cm]")
    plt.ylabel("petal width [cm]")
    plt.legend(loc="upper left")
    plt.show()


print("隨機森林")
do_random_forest()

print("------------------------------------------------------------")  # 60個


class Perceptron:
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.errors = []

        for _ in range(self.n_iter):
            error = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w[1:] += update * xi
                self.w[0] += update
                error += int(update != 0.0)
            self.errors.append(error)
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def do_perceptrons():
    df = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
        header=None,
    )
    X = df.iloc[0:100, [0, 2]].values
    y = df.iloc[0:100, 4].values
    y = np.where(y == "Iris-setosa", -1, 1)

    plt.scatter(X[:50, 0], X[:50, 1], color="red", marker="o", label="setosa")
    plt.scatter(
        X[50:100, 0], X[50:100, 1], color="blue", marker="x", label="versicolor"
    )
    plt.xlabel("petal length")
    plt.ylabel("sepal length")
    plt.legend(loc="upper left")
    plt.show()


print("perceptrons 感知器 前饋神經網路")
do_perceptrons()

print("------------------------------------------------------------")  # 60個

import tensorflow as tf


def _height(x, y):
    # z = np.sqrt(x**2 + y**2)
    z = 0.5 * (x**2) + 0.8 * (y**2)
    return z


def do_adative_learning_rate():
    x = tf.Variable(-8.00000)
    y = tf.Variable(4.00000)
    a = tf.constant(0.1000)
    b = tf.constant(1.0000)
    mul1 = tf.multiply(a, tf.square(x))
    mul2 = tf.multiply(b, tf.square(y))
    output = tf.add(mul1, mul2)

    gradient_op = tf.train.GradientDescentOptimizer(learning_rate=0.4).minimize(output)

    momentum_op = tf.train.MomentumOptimizer(
        learning_rate=0.035, momentum=0.9
    ).minimize(output)

    adagrad_op = tf.train.AdagradOptimizer(learning_rate=2).minimize(output)

    rms_op = tf.train.RMSPropOptimizer(learning_rate=0.5).minimize(output)

    adam_op = tf.train.AdamOptimizer(learning_rate=0.35).minimize(output)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        epochs = 30
        start_x = [-8.0]
        start_y = [4.0]

        for epoch in range(epochs):
            print("epoch of triaining", epoch)
            sess.run(rms_op)
            array_x = sess.run(x)
            array_y = sess.run(y)
            start_x.append(array_x)
            start_y.append(array_y)

        print(epoch)
        print(start_x)
        print(start_y)

        x = np.arange(-10.0, 10.0, 2)
        y = np.arange(-10.0, 10.0, 2)
        X, Y = np.meshgrid(x, y)
        Z = _height(X, Y)

        plt.figure(figsize=(8, 4))
        cs = plt.contourf(X, Y, Z, 15, alpha=0.75, cmap="rainbow")
        # cs = plt.contour(X, Y, Z, 15, cmap='rainbow')
        plt.plot(start_x, start_y, c="b")
        plt.title("rms")
        for xt, yt in zip(start_x, start_y):
            plt.scatter(xt, yt, c="b")
        plt.show()


print("adative_learning_rate")
do_adative_learning_rate()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
