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


"""
Machine Learning 練習篇-Multiple Regression多元回歸糖尿病案例

diabetes dataset 資料集是一個糖尿病的資料集
主要包括442筆資料,10個屬性值,分別是:
Age(年齡)、Sex(性別)、Body mass index(體質指數)、
Average Blood Pressure(平均血壓)、S1-S6一年後疾病級數指標,
Target為一年後患疾病的定量指標。

題目1
建立線性多元回歸的預測模型,繪製散佈圖來比較一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。

題目2
建立線性多元回歸的預測模型,只取Age(年齡)、Sex(性別)、Body mass index(體質指數)、Average Blood Pressure(平均血壓)作為解釋變數,產生模型,並匯出散佈圖來比較預測一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。
"""

# 題目1
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# 載入資料集
diabetes = datasets.load_diabetes()

# print(diabetes.DESCR)
print("keys")
print(diabetes.keys())
print("feature_names")
print(diabetes.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=["Target"])

print("Target為一年後患疾病的定量指標")
y = target["Target"]  # Series
print()
print(y)
print()

lm = LinearRegression()
lm.fit(X, y)

print(
    "迴歸係數:", lm.coef_
)  # 迴歸係數: [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163 476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]
print("截距:", lm.intercept_)  # 截距: 152.1334841628965

predicted_diabetes = lm.predict(X)
plt.scatter(y, predicted_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")

plt.show()

"""

#題目2
###################### 4 items ##############################
X1 = diabetes.data[:,:4]
X1 = pd.DataFrame(X1, columns=["age","sex","bmi", "bp"])
#print(X1)

target = pd.DataFrame(diabetes.target ,columns=["Target"])
y1 = target["Target"]
lm_4items = LinearRegression()
lm_4items.fit(X1,y1)
print("迴歸係數:", lm_4items.coef_)
print("截距:", lm_4items.intercept_)
predicted_4items_diabetes = lm_4items.predict(X1)
plt.scatter(y1 ,predicted_4items_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")
plt.show()


最後編輯： 
 
Gina·追蹤
<< 娜式coding style >> 想為自己的學習結果,留下一點點的痕跡~ 於是開始了程式小白的筆記人生!!
0
965
閱讀更多
Object 物件導向 & 繼承
==Object Oriented Programming== ==物件導向Object== 現實生活中,每件事物都是物件 -實質性(眼睛看的到) -概念性(關係,師生,同儕,隨時可以轉換) 物件 -屬性Property -方法Method

2023年5月12日
Machine Learning 基礎篇train_test_split(訓練和測試資料集)
在機器學習中，我們通常將原始數據按照比例分割為==測試集==和==訓練集==，從 sklearn套件使用train_test_split 函數來將數據分成兩個類別 資料比例 train dataset test dataset 4:1 80% 20%

2023年5月8日
Machine Learning 基礎篇-Linear Rregression,Multiple Regression
機器學習演算法是一種從資料中學習，不需要人類干預，就可以自從資料中取得經驗，並且從經驗提升能力的演算法。 機器學習理論主要是設計和分析一些讓電腦可以自動「學習」的演算法。 機器學習演算法是一類從資料中自動分析獲得規律，並利用規律對未知資料進行預測的演算法。 機器學習已廣泛應用於資料探勘、電腦視覺、自然語言處理、生物特徵辨識、搜尋引擎、醫學診斷、檢測信用卡欺詐、證券市場分析、DNA序列定序、語音和手寫辨識、戰略遊戲和機器人等領域。 監督式學習(給予答案): 回歸問題:預測連續的回應資料，例如:預測商店的營業額、學生的身高和體重. 常用的演算法有線性回歸(Rregression)、SVR。 分類問題: 預測可分類的回應資料，這是一些有限集合，例如:分類男生與女生、是或否、癌症分類1到4期、喜愛程度(1到5級別)等。 常用的演算法:Logistic回歸、決策樹、K鄰近演算法、CART、樸素被葉斯等。

2023年5月8日
OpenCV 專題實作篇part 1-擴增實境AR (ho~ho~ho~)
&#x64F4;&#x589E;&#x5BE6;&#x5883; (AR) &#x2013; &#x65E8;&#x5728;&#x900F;&#x904E;&#x6709;&#x9650;&#x4E92;&#x52D5;&#x5728;&#x771F;&#x5BE6;&#x4E16;&#x754C;&#x6AA2;&#x8996;&#x4E0A;&#x65B0;&#x589E;&#x6578;&#x4F4D;&#x5143;&#x7D20;&#x3002; &#x64F4;&#x589E;&#x5BE6;&#x5883;&#x985E;&#x578B; &#x6709;&#x5169;&#x7A2E;&#x985E;&#x578B;&#x7684;&#x64F4;&#x589E;&#x5BE6;&#x5883;&#xFF1A;&#x6A19;&#x8A18;&#x5F0F;&#x548C;&#x7121;&#x6A19;&#x8A18;&#x5F0F;&#x3002; &#x6A19;&#x8A18;&#x5F0F; AR &#x662F;&#x4F7F;&#x7528;&#x5F71;&#x50CF;&#x8FA8;&#x8B58;&#x5EFA;&#x7ACB;&#x7684;&#xFF0C;&#x4EE5;&#x8B58;&#x5225;&#x7DE8;&#x78BC;&#x5230; AR &#x88DD;&#x7F6E;&#x6216;&#x61C9;&#x7528;&#x7A0B;&#x5F0F;&#x4E2D;&#x7684;&#x7269;&#x4EF6;&#x3002;&#x5C07;&#x7269;&#x4EF6;&#x505A;&#x70BA;&#x53C3;&#x8003;&#x9EDE;&#x653E;&#x7F6E;&#x5728;&#x8996;&#x91CE;&#x7BC4;&#x570D;&#x5167;&#x6642;&#xFF0C;&#x5B83;&#x5011;&#x53EF;&#x4EE5;&#x5E6B;&#x52A9;&#x60A8;&#x7684; AR &#x88DD;&#x7F6E;&#x78BA;&#x5B9A;&#x651D;&#x5F71;&#x6A5F;&#x7684;&#x4F4D;&#x7F6E;&#x548C;&#x65B9;&#x5411;&#x3002;&#x5BE6;&#x73FE;&#x65B9;&#x5F0F;&#x901A;&#x5E38;&#x662F;&#x900F;&#x904E;&#x5C07;&#x651D;&#x5F71;&#x6A5F;&#x5207;&#x63DB;&#x5230;&#x7070;&#x968E;&#xFF0C;&#x4E26;&#x5075;&#x6E2C;&#x6A19;&#x8A18;&#xFF0C;&#x4EE5;&#x5C07;&#x8A72;&#x6A19;&#x8A18;&#x8207;&#x8CC7;&#x8A0A;&#x5EAB;&#x4E2D;&#x7684;&#x6240;&#x6709;&#x5176;&#x4ED6;&#x6A19;&#x8A18;&#x9032;&#x884C;&#x6BD4;&#x8F03;&#x3002;&#x4E00;&#x65E6;&#x88DD;&#x7F6E;&#x627E;&#x5230;&#x76F8;&#x7B26;&#x9805;&#x76EE;&#xFF0C;&#x5B83;&#x5C31;&#x6703;&#x4F7F;&#x7528;&#x8A72;&#x8CC7;&#x6599;&#x4EE5;&#x6578;&#x5B78;&#x65B9;&#x5F0F;&#x78BA;&#x5B9A;&#x59FF;&#x52E2;&#xFF0C;&#x4E26;&#x5C07; AR &#x5F71;&#x50CF;&#x653E;&#x7F6E;&#x5728;&#x6B63;&#x78BA;&#x7684;&#x4F4D;&#x7F6E;&#x3002; &#x7121;&#x6A19;&#x8A18;&#x5F0F; AR &#x66F4;&#x8907;&#x96DC;&#xFF0C;&#x56E0;&#x70BA;&#x88DD;&#x7F6E;&#x6C92;&#x6709;&#x805A;&#x7126;&#x9EDE;&#x3002;&#x56E0;&#x6B64;&#xFF0C;&#x88DD;&#x7F6E;&#x5FC5;&#x9808;&#x8FA8;&#x8B58;&#x51FA;&#x73FE;&#x5728;&#x8996;&#x91CE;&#x7BC4;&#x570D;&#x5167;&#x7684;&#x9805;&#x76EE;&#x3002;&#x4F7F;&#x7528;&#x8FA8;&#x8B58;&#x6F14;&#x7B97;&#x6CD5;&#xFF0C;&#x8A72;&#x88DD;&#x7F6E;&#x5C07;&#x5C0B;&#x627E;&#x8272;&#x5F69;&#x3001;&#x5716;&#x6A23;&#x548C;&#x985E;&#x4F3C;&#x7279;&#x5FB5;&#x4F86;&#x78BA;&#x5B9A;&#x8A72;&#x7269;&#x4EF6;&#x662F;&#x4EC0;&#x9EBC;&#xFF0C;&#x7136;&#x5F8C;&#x4F7F;&#x7528;&#x6642;&#x9593;&#x3001;&#x52A0;&#x901F;&#x8A08;&#x3001;GPS &#x548C;&#x6307;&#x5357;&#x91DD;&#x8CC7;&#x8A0A;&#xFF0C;&#x88DD;&#x7F6E;&#x6703;&#x81EA;&#x6211;&#x5B9A;&#x4F4D;&#xFF0C;&#x4E26;&#x4F7F;&#x7528;&#x651D;&#x5F71;&#x6A5F;&#x5C07;&#x60A8;&#x60F3;&#x8981;&#x7684;&#x4EFB;&#x4F55;&#x6771;&#x897F;&#x5F71;&#x50CF;&#x758A;&#x52A0;&#x5728;&#x771F;&#x5BE6;&#x4E16;&#x754C;&#x74B0;&#x5883;&#x4E2D;&#x3002; &#x64F4;&#x589E;&#x5BE6;&#x5883;&#x904B;&#x4F5C;&#x65B9;&#x5F0F;,AR&#x6709;&#x4E94;&#x500B;&#x91CD;&#x8981;&#x5143;&#x4EF6;&#xFF1A;

2022年9月22日
閱讀更多 Gina 的文章
發表於  HackMD

"""


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

"""
糖尿病数据（适用于回归任务）

这是一个糖尿病的数据集，主要包括442行数据，10个属性值，分别是：
Age(年龄)、性别(Sex)、Body mass index(体质指数)、Average Blood Pressure(平均血压)、
S1~S6一年后疾病级数指标。

Target为一年后患疾病的定量指标，因此适合与回归任务

"""

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score


def do_linear_regression():
    diabetes = datasets.load_diabetes()

    X = diabetes.data[:, np.newaxis, 2]
    print("Data shape: ", X.shape)

    x_train, x_test, y_train, y_test = train_test_split(
        X, diabetes.target, test_size=0.1, random_state=4
    )

    regr = linear_model.LinearRegression()

    regr.fit(x_train, y_train)

    y_pred = regr.predict(x_test)

    plt.scatter(x_test, y_test, color="black")
    plt.plot(x_test, y_pred, color="blue", linewidth=3)
    plt.show()


print("線性迴歸")
do_linear_regression()

print("------------------------------------------------------------")  # 60個

cl_num = 3
data_num = 20
thr = [0.00001, 0.00001, 0.00001]


def dist(x, y, mu_x, mu_y):
    return (mu_x - x) ** 2 + (mu_y - y) ** 2


def cluster(x, y, mu_x, mu_y):
    cls_ = dict()
    for i in range(data_num):
        dists = []
        for j in range(cl_num):
            distant = dist(x[i], y[i], mu_x[j], mu_y[j])
            dists.append(distant)
        cl = dists.index(min(dists))
        if cl not in cls_:
            cls_[cl] = [(x[i], y[i])]
        elif cl in cls_:
            cls_[cl].append((x[i], y[i]))

    return cls_


def re_mu(cls_, mu_x, mu_y):
    new_muX = []
    new_muY = []

    for key, values in cls_.items():
        if len(values) == 0:
            values.append([mu_x[key], mu_y[key]])

        sum_x = 0
        sum_y = 0
        for v in values:
            sum_x += v[0]
            sum_y += v[1]

        new_mu_x = sum_x / len(values)
        new_mu_y = sum_y / len(values)

        new_muX.append(round(new_mu_x, 2))
        new_muY.append(round(new_mu_y, 2))
    return new_muX, new_muY


def do_k_means():
    x = np.random.randint(0, 500, data_num)
    y = np.random.randint(0, 500, data_num)

    mu_x = np.random.randint(0, 500, cl_num)
    mu_y = np.random.randint(0, 500, cl_num)

    cls_ = cluster(x, y, mu_x, mu_y)

    new_muX, new_muY = re_mu(cls_, mu_x, mu_y)

    while (
        any((abs(np.array(new_muX) - np.array(mu_x)) > thr)) != False
        or any((abs(np.array(new_muY) - np.array(mu_y)) > thr)) != False
    ):
        mu_x = new_muX
        mu_y = new_muY
        cls_ = cluster(x, y, mu_x, mu_y)
        new_muX, new_muY = re_mu(cls_, mu_x, mu_y)

    print("Done")

    plt.scatter(x, y)
    plt.scatter(new_muX, new_muY)
    plt.show()

    colors = ["r", "b", "g"]
    for key, values in cls_.items():
        cx = []
        cy = []
        for v in values:
            cx.append(v[0])
            cy.append(v[1])
        plt.scatter(cx, cy, color=colors[key])

    plt.show()


print("K-Means")
do_k_means()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
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
        X, y, test_size=0.3, random_state=0
    )

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    svm = SVC(kernel="linear", C=1.0, random_state=0)
    svm.fit(X_train_std, y_train)
    y_pred = svm.predict(X_test_std)

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

from sklearn.svm import SVC
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

    svm = SVC(kernel="rbf", random_state=0, gamma=0.6, C=10.0)
    svm.fit(X_xor, y_xor)
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc="upper left")
    plt.show()


print("SVN Kernel")
do_svm_kernel()

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
