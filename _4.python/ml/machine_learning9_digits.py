"""

數字 資料集

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print("數字 資料集 ST")

import matplotlib as mpl
from IPython.core.pylabtools import figsize

figsize(8, 6)
plt.style.use("ggplot")
colors = [
    "#348ABD",
    "#A60628",
    "#7A68A6",
    "#467821",
    "#D55E00",
    "#CC79A7",
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#0072B2",
]
plt.cmap = mpl.colors.ListedColormap(colors)
# plt.rcParams['savefig.dpi'] = 300
# plt.rcParams['figure.dpi'] = 300

from sklearn import datasets

digits = datasets.load_digits(n_class=10)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30

print(X.shape)

fig = plt.figure()
for i in range(10):
    ax = plt.subplot2grid((1, 10), (0, i))
    ax.imshow(digits.data[i * 100].reshape(8, 8), cmap=plt.cm.gray)
    ax.set_title("")
    ax.axis("off")

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_embedding(ax, X):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    for i in range(X.shape[0]):
        ax.text(
            X[i, 0],
            X[i, 1],
            str(digits.target[i]),
            color=colors[int(y[i] % 10)],
            fontdict={"size": 12},
        )


def format_plot(ax, x_label, y_label, title):
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())

    ax.set_title(title)


# PCA降維
from sklearn import decomposition, manifold

X_pca = decomposition.TruncatedSVD(n_components=2).fit_transform(X)

fig, ax = plt.subplots()
plot_embedding(ax, X_pca)
format_plot(ax, "", "", "PCA")

plt.show()

print("------------------------------------------------------------")  # 60個

embedder = manifold.SpectralEmbedding(
    n_components=2, random_state=0, eigen_solver="arpack"
)
X_se = embedder.fit_transform(X)

tsne = manifold.TSNE(n_components=2, init="pca", random_state=0)

X_tsne = tsne.fit_transform(X)

mds = manifold.MDS(n_components=2, n_init=1, max_iter=100)
X_mds = mds.fit_transform(X)

fig, ax = plt.subplots(2, 2)
figsize(20, 16)
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

plot_embedding(ax[0, 0], X_pca)
format_plot(ax[0, 0], "", "", "PCA")

plot_embedding(ax[0, 1], X_mds)
format_plot(ax[0, 1], "", "", "MDS")

plot_embedding(ax[1, 0], X_se)
format_plot(ax[1, 0], "", "", "Spectral")

plot_embedding(ax[1, 1], X_tsne)
format_plot(ax[1, 1], "", "", "tSNE")

plt.show()

print("數字 資料集 SP")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from sklearn import datasets

digits = datasets.load_digits()  # 加载数据

# 把数据所代表的图片显示出来
images_and_labels = list(zip(digits.images, digits.target))
plt.figure(figsize=(8, 6))
for index, (image, label) in enumerate(images_and_labels[:8]):
    plt.subplot(2, 4, index + 1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Digit: %i" % label, fontsize=20)

plt.show()

print("------------------------------")  # 30個

print("shape of raw image data: {0}".format(digits.images.shape))
print("shape of data: {0}".format(digits.data.shape))

# 把数据分成训练数据集和测试数据集
from sklearn.model_selection import train_test_split

Xtrain, Xtest, Ytrain, Ytest = train_test_split(
    digits.data, digits.target, test_size=0.20, random_state=2
)

# 使用支持向量机来训练模型
from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.0, probability=True)
clf.fit(Xtrain, Ytrain)

# 评估模型的准确度
from sklearn.metrics import accuracy_score

Ypred = clf.predict(Xtest)
print(accuracy_score(Ytest, Ypred))

print(clf.score(Xtest, Ytest))

# 查看预测的情况
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

for i, ax in enumerate(axes.flat):
    ax.imshow(Xtest[i].reshape(8, 8), cmap=plt.cm.gray_r, interpolation="nearest")
    ax.text(
        0.05,
        0.05,
        str(Ypred[i]),
        fontsize=32,
        transform=ax.transAxes,
        color="green" if Ypred[i] == Ytest[i] else "red",
    )
    ax.text(
        0.8, 0.05, str(Ytest[i]), fontsize=32, transform=ax.transAxes, color="black"
    )
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()

print("------------------------------")  # 30個

print("Xtest[4] 的各种可能性")
print(clf.predict_proba(Xtest[4].reshape(1, -1)))

""" no joblib
print('保存模型参数')
from sklearn.externals import joblib
joblib.dump(clf, 'digits_svm.pkl')

print('导入模型参数，直接进行预测')
clf = joblib.load('digits_svm.pkl')
Ypred = clf.predict(Xtest)
print(clf.score(Xtest, Ytest))
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ読み込み
data = load_digits()
X = data.images.reshape(len(data.images), -1)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = model = MLPClassifier(hidden_layer_sizes=(16,))
model.fit(X_train, y_train)  # 學習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from sklearn import datasets, svm
import matplotlib.pyplot as plt

# 识别手写体数字
svc = svm.SVC(gamma=0.001, C=100.0)
digits = datasets.load_digits()  # 导入Digits数据集
# print(digits.DESCR) # 查看数据集的说明信息


def plts():
    """显示要识别的数字图片"""
    plt.subplot(321)
    plt.imshow(digits.images[1791], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.subplot(322)
    plt.imshow(digits.images[1792], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.subplot(323)
    plt.imshow(digits.images[1793], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.subplot(324)
    plt.imshow(digits.images[1794], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.subplot(325)
    plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.subplot(326)
    plt.imshow(digits.images[1796], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()


def svms():
    # 学习并返回识别结果
    svc.fit(digits.data[:1791], digits.target[:1791])  # 训练
    res = svc.predict(digits.data[1791:1797])  # 识别
    return list(res)


result = svms()

duibi = digits.target[1791:1797]
print("识别的数字: {}\n实际的结果: {}".format(result, list(duibi)))
plts()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
