"""
數字 資料集

1797個數字圖
每張圖 8X8 數值範圍0~15

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
from sklearn import svm
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score  # 計算分類模型的準確率
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

print("------------------------------------------------------------")  # 60個


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("數字 基本數據 load_digits()")

digits = datasets.load_digits()
# digits = datasets.load_digits(n_class=6)  # 多了 n_class 參數，只要數字 0 ~ n_class-1

print(type(digits))

X = digits.data
y = digits.target

# X = digits["data"] same
# y = digits["target"] same

print("digits.keys() :", digits.keys())
# 資料keys包含'data', 'target', 'target_names', 'images', 'DESCR'
print("data形狀 :", X.shape)
print("data影像形狀 :", digits.images.shape)
print("影像個數 :", len(digits.images))
# print(digits.DESCR)  # 查看数据集的说明信息

index = 3
print("看第", index, "張圖")
print("圖的內容 :\n", digits.images[index], sep="")
print("圖的形狀 :", digits.images[index].shape)
plt.imshow(digits.images[index], cmap=plt.cm.gray)
# plt.imshow(X[index].reshape(8, 8), cmap=plt.cm.gray)
show()

print("------------------------------")  # 30個

print("畫出前100張圖")

plt.figure(figsize=(8, 8))

for i in range(100):
    plt.subplot(10, 10, i + 1)
    plt.imshow(X[i].reshape(8, 8), cmap=plt.cm.gray)
    plt.axis("off")
plt.suptitle("畫出前100張圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RandomForestClassifier
# 以sklearn中的手寫數字集合來舉例：

digits = datasets.load_digits()
X = digits.data
y = digits.target

# 將手寫的資料視覺化呈現，可以看到每個數字(images)的左下角會記錄該數字的正確值(target)

# set up the figure
fig = plt.figure(figsize=(8, 8))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

print("畫64張圖")
for i in range(64):
    tx = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    tx.imshow(digits.images[i], cmap=plt.cm.binary, interpolation="nearest")
    tx.text(0, 7, str(digits.target[i]))
show()

# 用 隨機森林分類函數學習機 將手寫資料進行分類

Xtrain, Xtest, ytrain, ytest = train_test_split(X, digits.target)
model = RandomForestClassifier(n_estimators=1000)  # 隨機森林分類函數學習機

model.fit(Xtrain, ytrain)

y_pred = model.predict(Xtest)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

print(classification_report(y_pred, ytest))

# 可以看到上圖，最左邊為數字0~9的類別，主要回傳精確值以及support，看這些數字很難懂，先看下圖

mat = confusion_matrix(ytest, y_pred)
sns.heatmap(mat.T, square=True, annot=True, fmt="d", cbar=False)
plt.xlabel("true label")
plt.ylabel("predicted label")
show()

"""
可以看到上圖，X軸為真實手寫數字的值，Y軸會預測手寫的數字的值，
其斜對角0對0、1對1、2對2...，代表預測的準確次數(對照前一輸出結果的support)，
將該類別準確次數/全部筆數=精確值(對照前一輸出結果的precision)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RandomForestClassifier

digits = datasets.load_digits()
X = digits.data
y = digits.target

N = len(digits.images)
data = digits.images.reshape((N, -1))

model = RandomForestClassifier(n_estimators=10)

model.fit(data[: N // 2], digits.target[: N // 2])  # 學習訓練.fit

expected = digits.target[N // 2 :]

y_pred = model.predict(data[N // 2 :])  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

print(classification_report(expected, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MLPClassifier

from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機

digits = datasets.load_digits()
X = digits.data
y = digits.target

N = len(digits.images)
X = digits.images.reshape(N, -1)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

mlp = MLPClassifier(hidden_layer_sizes=(16,))  # 多層感知器分類器 函數學習機

mlp.fit(X_train, y_train)  # 學習訓練.fit

y_pred = mlp.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SVC
digits = datasets.load_digits()
X = digits.data
y = digits.target

# 資料分割
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.2)

# 使用支持向量机来训练模型

clf = svm.SVC(gamma=0.001, C=100.0, probability=True)

clf.fit(Xtrain, Ytrain)  # 學習訓練.fit

y_pred = clf.predict(Xtest)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

cc = accuracy_score(Ytest, y_pred)
print("計算分類模型的準確率 accuracy_score :", cc)

cc = clf.score(Xtest, Ytest)
print("score :", cc)

N = 30
print("測試資料前N筆 :", Ytest[:N])
print("預測結果前N筆 :", y_pred[:N])

print("------------------------------")  # 30個

print("Xtest[4] 的各种可能性")
print(clf.predict_proba(Xtest[4].reshape(1, -1)))

""" no joblib
print('保存模型参数')
from sklearn.externals import joblib

joblib.dump(clf, 'digits_svm.pkl')

print('导入模型参数，直接进行预测')
clf = joblib.load('digits_svm.pkl')
y_pred = clf.predict(Xtest)  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

print(clf.score(Xtest, Ytest))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SVC

digits = datasets.load_digits()
X = digits.data
y = digits.target

clf = svm.SVC(gamma=0.001, C=100.0)

clf.fit(X[:1791], y[:1791])  # 學習訓練.fit

y_pred = clf.predict(X[1791:1797])  # 預測.predict
print("預測結果 :\n", y_pred, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SVC 學習曲線

digits = datasets.load_digits()
X = digits.data
y = digits.target
print(X.shape)
print(y.shape)
print("------------------------------")  # 30個

train_sizes, train_loss, test_loss = learning_curve(
    svm.SVC(gamma=0.01),
    X,
    y,
    cv=10,
    scoring="neg_mean_squared_error",
    train_sizes=[0.1, 0.25, 0.5, 0.75, 1],
)

# 全部樣本(1797個)9成拿來訓練 照比例做訓練
print("訓練大小(5比例) :", train_sizes)
print("訓練損失(10輪 X 5比例) :\n", train_loss, sep="")
print("測試損失(10輪 X 5比例) :\n", test_loss, sep="")

train_loss_mean = -np.mean(train_loss, axis=1)  # 取平均, 取相反數
test_loss_mean = -np.mean(test_loss, axis=1)  # 取平均, 取相反數

print("訓練損失 10輪平均 :", train_loss_mean)
print("測試損失 10輪平均 :", test_loss_mean)

plt.plot(train_sizes, train_loss_mean, "o-", color="r", label="Training")
plt.plot(train_sizes, test_loss_mean, "o-", color="g", label="Cross-validation")

plt.xlabel("訓練樣本數")
plt.ylabel("損失")
plt.legend()
show()

print("------------------------------")  # 30個

train_size_abs, train_loss, test_loss = learning_curve(
    svm.SVC(),
    X,
    y,
    # train_sizes=np.array([0.1, 0.33, 0.55, 0.78, 1. ]),
    cv=10,
    # cv='warn',
    scoring="neg_mean_squared_error",
)

print(A * 0.9 * 0.1)  # ok
print(A * 0.9 * 0.32)
print(A * 0.9 * 0.55)  # ok
print(A * 0.9 * 0.77)
print(A * 0.9 * 1)  # ok
print(A * 0.9 * 0.1)
print(A * 0.9 * 0.33)
print(A * 0.9 * 0.55)
print(A * 0.9 * 0.78)
print(A * 0.9 * 1)

print("訓練大小(5比例) abs:", train_size_abs)
print("訓練損失(10輪 X 5比例) :\n", train_loss, sep="")
print("測試損失(10輪 X 5比例) :\n", test_loss, sep="")

train_loss_mean = -np.mean(train_loss, axis=1)  # 取平均, 取相反數
test_loss_mean = -np.mean(test_loss, axis=1)  # 取平均, 取相反數
print("訓練損失 10輪平均 :", train_loss_mean)
print("測試損失 10輪平均 :", test_loss_mean)

param_range = np.logspace(-6, -2.3, 5)
print("x軸範圍 :", param_range)

plt.plot(param_range, train_loss_mean, "o-", color="r", label="Training")
plt.plot(param_range, test_loss_mean, "o-", color="g", label="Cross-validation")

plt.xlabel("gamma")
plt.ylabel("損失")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DecisionTreeClassifier AdaBoostClassifier

# scikit-learn_adaBoost

# Bagging演算法測試

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

digits = datasets.load_digits()
# X = digits.data
# y = digits.target

X = digits["data"]
y = digits["target"]

# 決策樹分類器 模型評估

clf = DecisionTreeClassifier()
scores_ada = cross_val_score(clf, X, y, cv=6)
print("決策樹分類器 6次成績 :", scores_ada)
print("決策樹分類器 6次成績平均 :", scores_ada.mean())

# AdaBoost分類器 模型評估

clf = AdaBoostClassifier(DecisionTreeClassifier())
scores_ada = cross_val_score(clf, X, y, cv=6)

print("AdaBoost分類器 6次成績 :", scores_ada)
print("AdaBoost分類器 6次成績平均 :", scores_ada.mean())

clf.fit(X, y)  # 學習訓練.fit

cc = clf.estimator_errors_
print("errors :\n", cc, sep="")

cc = clf.estimator_weights_
print("weights :\n", cc, sep="")

print("不同深度AdaBoostClassifier(DecisionTreeClassifier())")

score = []
for depth in [1, 2, 10]:
    print("深度 :", depth)
    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=depth))
    scores_ada = cross_val_score(clf, X, y, cv=6)
    score.append(scores_ada.mean())

print("深度 :", [1, 2, 10])
print("成績 :", score)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_04_label_propagation_digits_active_learning

# Label Propagation digits active learning

from scipy import stats
from sklearn.semi_supervised import LabelSpreading

digits = datasets.load_digits()
X = digits.data
y = digits.target

rng = np.random.RandomState(0)

indices = np.arange(len(X))
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer

digits = datasets.load_digits()
X = digits.data
y = digits.target

y = LabelBinarizer().fit_transform(y)  # .fit + .transform一起做

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


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


import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

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


def plot_digits(data):
    # 顯示前 100 筆手寫阿拉伯數字
    fig, ax = plt.subplots(
        10, 10, figsize=(8, 8), subplot_kw=dict(xticks=[], yticks=[])
    )
    fig.subplots_adjust(hspace=0.05, wspace=0.05)
    for i, axi in enumerate(ax.flat):
        im = axi.imshow(data[i].reshape(8, 8), cmap="binary")
        im.set_clim(0, 16)


digits = datasets.load_digits()
X = digits.data
y = digits.target

plot_digits(X)
plt.suptitle("顯示前 100 筆手寫阿拉伯數字")
show()

# 降維

from sklearn.decomposition import PCA

pca = PCA(0.99, whiten=True)
data = pca.fit_transform(X)  # .fit + .transform一起做

print("PCA前 :", X.shape)  ## (1797, 64)
print("PCA後 :", data.shape)  # (1797, 41)

# 以AIC決定最佳集群數量

# GMM

from sklearn.mixture import GaussianMixture

n_components = np.arange(50, 210, 10)

aics = []
for n in n_components:
    print("GaussianMixture, n =", n)
    gmm = GaussianMixture(n, covariance_type="full")
    aic = gmm.fit(data).aic(data)
    aics.append(aic)
    print("n = ", n, "\taic = ", aic)

plt.plot(n_components, aics)

# 畫直線
plt.plot([110, 110], [110, min(aics)], linewidth=5, color="0.3")
# plt.plot([110, 110], [110, -250000], linewidth=5, color="0.8")

show()

# 以AIC決定最佳集群數量=110
# 設定集群數量=110

gmm = GaussianMixture(110, covariance_type="full", random_state=9487)

gmm.fit(data)  # 學習訓練.fit
print(gmm.converged_)
# True

# Now we can draw samples of 100 new points within this 41-dimensional projected space,
# using the GMM as a generative model
# 生成100個樣本

data_new, _ = gmm.sample(100)

print("data_new.shape :", data_new.shape)  # (100, 41)

digits_new = pca.inverse_transform(data_new)

plot_digits(digits_new)
plt.suptitle("顯示前 100 筆手寫阿拉伯數字")
show()

print("digits_new.shape :", digits_new.shape)  # (100, 64)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectPercentile 單變數特徵選取(Univariate feature selection)

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2

print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# SelectPercentile 特徵選取

logistic_regression = SelectPercentile(chi2, percentile=10)
X_new = logistic_regression.fit_transform(X, y)  # .fit + .transform一起做
print(X_new.shape)

print("顯示特徵分數")
cc = logistic_regression.scores_
print(cc)

print("顯示 p value")
cc = logistic_regression.pvalues_
print(cc)

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放  # .fit + .transform一起做
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict
print("y_pred :\n", y_pred, sep="")

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print("y_pred_prob :\n", y_pred_prob, sep="")

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放  # .fit + .transform一起做
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# GenericUnivariateSelect 單變數特徵選取(Univariate feature selection)

from sklearn.feature_selection import GenericUnivariateSelect
from sklearn.feature_selection import chi2

print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# GenericUnivariateSelect 特徵選取

# 使用 SelectKBest, 20 個特徵
clf = GenericUnivariateSelect(chi2, mode="k_best", param=20)

X_new = clf.fit_transform(X, y)  # .fit + .transform一起做
print(X_new.shape)

print("顯示特徵分數")
cc = clf.scores_
print(cc)

print("顯示 p value")
cc = clf.pvalues_
print(cc)

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放  # .fit + .transform一起做
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred), sep="")

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放  # .fit + .transform一起做
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

x = np.arange(10)
y = np.arange(10)
print(x)
print(y)

z = list(zip(x, y))
print(z)


plt.style.use("ggplot")

import matplotlib as mpl

plt.cmap = mpl.colors.ListedColormap(colors)
# plt.rcParams['savefig.dpi'] = 300
# plt.rcParams['figure.dpi'] = 300


plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
ax.imshow(X[i].reshape(8, 8), cmap=plt.cm.gray_r, interpolation="nearest")


plt.imshow(digits.images[1791], cmap=plt.cm.gray_r, interpolation="nearest")
plt.imshow(digits.images[1792], cmap=plt.cm.gray_r, interpolation="nearest")
plt.imshow(digits.images[1793], cmap=plt.cm.gray_r, interpolation="nearest")
plt.imshow(digits.images[1794], cmap=plt.cm.gray_r, interpolation="nearest")
plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation="nearest")
plt.imshow(digits.images[1796], cmap=plt.cm.gray_r, interpolation="nearest")
