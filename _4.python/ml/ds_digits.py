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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

digits = load_digits()
print(digits.data.shape)
plt.gray()
plt.matshow(digits.images[0])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

data = load_digits()
print(type(data))
print(len(data))

print("TSNE")
n_components = 2  # 削減後の次元を2に設定
model = TSNE(n_components=n_components)
print(model.fit_transform(data.data))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 変換後のベクトルデータを入力として機械学習モデルを適用する

from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

model = RandomForestClassifier(n_estimators=10)

model.fit(data[: n_samples // 2], digits.target[: n_samples // 2])  # 學習訓練.fit

expected = digits.target[n_samples // 2 :]
predicted = model.predict(data[n_samples // 2 :])  # 預測.predict

print(metrics.classification_report(expected, predicted))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

digits = datasets.load_digits(n_class=10)

X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30

print(X.shape)
print(y.shape)

for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.imshow(digits.data[i].reshape(8, 8), cmap=plt.cm.gray)
    plt.axis("off")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

digits = datasets.load_digits()

# 把数据所代表的图片显示出来
images_and_labels = list(zip(digits.images, digits.target))
plt.figure(figsize=(8, 6))
for index, (image, label) in enumerate(images_and_labels[:8]):
    plt.subplot(2, 4, index + 1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Digit: %i" % label, fontsize=20)

plt.show()

print("shape of raw image data: {0}".format(digits.images.shape))
print("shape of data: {0}".format(digits.data.shape))

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
Xtrain, Xtest, Ytrain, Ytest = train_test_split(
    digits.data, digits.target, test_size=0.2
)
# 訓練組8成, 測試組2成

# 使用支持向量机来训练模型
from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.0, probability=True)

clf.fit(Xtrain, Ytrain)  # 學習訓練.fit

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


from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

data = load_digits()

X = data.images.reshape(len(data.images), -1)
y = data.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

model = MLPClassifier(hidden_layer_sizes=(16,))

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import svm

# 识别手写体数字
svc = svm.SVC(gamma=0.001, C=100.0)

digits = datasets.load_digits()
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
    svc.fit(digits.data[:1791], digits.target[:1791])  # 學習訓練.fit
    res = svc.predict(digits.data[1791:1797])  # 识别
    return list(res)


result = svms()

duibi = digits.target[1791:1797]
print("识别的数字: {}\n实际的结果: {}".format(result, list(duibi)))
plts()

print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# some NG
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC

digits = load_digits()
X = digits.data
y = digits.target
train_sizes, train_loss, test_loss = learning_curve(
    SVC(gamma=0.01),
    X,
    y,
    cv=10,
    scoring="mean_squared_error",
    train_sizes=[0.1, 0.25, 0.5, 0.75, 1],
)
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(train_sizes, train_loss_mean, "o-", color="r", label="Training")
plt.plot(train_sizes, test_loss_mean, "o-", color="g", label="Cross-validation")

plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# some NG
from sklearn.learning_curve import validation_curve
from sklearn.svm import SVC

digits = load_digits()
X = digits.data
y = digits.target
param_range = np.logspace(-6, -2.3, 5)
train_loss, test_loss = validation_curve(
    SVC(),
    X,
    y,
    param_name="gamma",
    param_range=param_range,
    cv=10,
    scoring="mean_squared_error",
)
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(param_range, train_loss_mean, "o-", color="r", label="Training")
plt.plot(param_range, test_loss_mean, "o-", color="g", label="Cross-validation")

plt.xlabel("gamma")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_05_scikit-learn_adaBoost

# Bagging演算法測試

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import learning_curve

from sklearn.datasets import load_digits

# 載入資料集

dataset = load_digits()
X = dataset["data"]
y = dataset["target"]

plt.imshow(X[4].reshape(8, 8))
plt.show()

# 個別模型評估

clf = DecisionTreeClassifier()
scores_ada = cross_val_score(clf, X, y, cv=6)
cc = scores_ada.mean()
print(cc)

# 0.7952173913043478

# AdaBoost模型評估

clf = AdaBoostClassifier(DecisionTreeClassifier())
scores_ada = cross_val_score(clf, X, y, cv=6)
cc = scores_ada.mean()
print(cc)
# 0.8019435154217764

clf.fit(X, y)  # 學習訓練.fit

cc = clf.estimator_errors_
print(cc)

cc = clf.estimator_weights_
print(cc)

score = []
for depth in [1, 2, 10]:
    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=depth))
    scores_ada = cross_val_score(clf, X, y, cv=6)
    score.append(scores_ada.mean())
print(score)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_04_label_propagation_digits_active_learning

# Label Propagation digits active learning

from scipy import stats
from sklearn.semi_supervised import LabelSpreading
from sklearn.metrics import classification_report, confusion_matrix

# 載入資料集

digits = datasets.load_digits()
rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

# 取前 330 筆資料
X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

# 參數設定
n_total_samples = len(y)
n_labeled_points = 40  # 初始取40筆標註資料
max_iterations = 5  # 5 個執行週期

unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
cc = len(unlabeled_indices)
print(cc)

# Label propagation 模型訓練與評估

f = plt.figure()
for i in range(max_iterations):
    y_train = np.copy(y)
    y_train[unlabeled_indices] = -1

    # LabelSpreading 模型訓練
    lp_model = LabelSpreading(gamma=0.25, max_iter=20)

    lp_model.fit(X, y_train)  # 學習訓練.fit

    # 預測
    predicted_labels = lp_model.transduction_[unlabeled_indices]
    true_labels = y[unlabeled_indices]

    print(f"Iteration {i} {70 * '_'}")
    print(
        f"Label Spreading model: {n_labeled_points} labeled & "
        + f"{n_total_samples - n_labeled_points} unlabeled ({n_total_samples} total)"
    )

    if i == 0 or i == max_iterations - 1:
        print(classification_report(true_labels, predicted_labels))

    print("Confusion matrix")
    cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_)
    print(cm)

    # 計算熵，以找出最不確定的五筆資料
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[
        np.in1d(uncertainty_index, unlabeled_indices)
    ][:5]

    # 記錄最不確定的五筆資料
    delete_indices = np.array([], dtype=int)
    f.text(
        0.05,
        (1 - (i + 1) * 0.183),
        f"model {i + 1}\n\nfit with\n{n_labeled_points} labels",
        size=10,
    )
    for index, image_index in enumerate(uncertainty_index):
        image = images[image_index]

        sub = f.add_subplot(5, 5, index + 1 + (5 * i))
        sub.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
        sub.set_title(
            f"predict: {lp_model.transduction_[image_index]}\ntrue: {y[image_index]}",
            size=10,
        )
        sub.axis("off")

        # 將最不確定的五筆資料加入待刪除的陣列
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))

    # 將最不確定的五筆資料加入標註資料
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)

print("\n最不確定的五筆資料：")
plt.subplots_adjust(left=0.2, bottom=0.03, right=0.9, top=0.9, wspace=0.2, hspace=0.85)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# load data
digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


def add_layer(
    inputs,
    in_size,
    out_size,
    layer_name,
    activation_function=None,
):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(
        tf.zeros([1, out_size]) + 0.1,
    )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    # here to dropout
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(
            Wx_plus_b,
        )
    tf.summary.histogram(layer_name + "/outputs", outputs)
    return outputs


# define placeholder for inputs to network
keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32, [None, 64])  # 8x8
ys = tf.placeholder(tf.float32, [None, 10])

# add output layer
l1 = add_layer(xs, 64, 50, "l1", activation_function=tf.nn.tanh)
prediction = add_layer(l1, 50, 10, "l2", activation_function=tf.nn.softmax)

# the loss between prediction and real data
cross_entropy = tf.reduce_mean(
    -tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1])
)  # loss
tf.summary.scalar("loss", cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
merged = tf.summary.merge_all()
# summary writer goes in here
train_writer = tf.summary.FileWriter("logs/train", sess.graph)
test_writer = tf.summary.FileWriter("logs/test", sess.graph)

# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split(".")[1]) < 12 and int((tf.__version__).split(".")[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
sess.run(init)

for i in range(500):
    # here to determine the keeping probability
    sess.run(train_step, feed_dict={xs: X_train, ys: y_train, keep_prob: 0.5})
    if i % 50 == 0:
        # record loss
        train_result = sess.run(
            merged, feed_dict={xs: X_train, ys: y_train, keep_prob: 1}
        )
        test_result = sess.run(merged, feed_dict={xs: X_test, ys: y_test, keep_prob: 1})
        train_writer.add_summary(train_result, i)
        test_writer.add_summary(test_result, i)


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
