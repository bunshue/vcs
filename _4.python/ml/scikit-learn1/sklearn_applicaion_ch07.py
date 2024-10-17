"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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
print("------------------------------------------------------------")  # 60個

# 07_01_svm_from_scratch
# 自行開發支援向量機分類器，並進行鳶尾花(Iris)品種的辨識

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# SVM 演算法


class SVM:
    def __init__(self, learning_rate=1e-3, lambda_param=1e-2, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    # 初始化權重、偏差
    def _init_weights_bias(self, X):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0

    # 類別代碼：-1, 1
    def _get_cls_map(self, y):
        return np.where(y <= 0, -1, 1)

    # 限制條件：y(wx + b) >= 1
    def _satisfy_constraint(self, x, idx):
        linear_model = np.dot(x, self.w) + self.b
        return self.cls_map[idx] * linear_model >= 1

    # 反向傳導
    def _get_gradients(self, constrain, x, idx):
        if constrain:
            dw = self.lambda_param * self.w
            db = 0
            return dw, db

        dw = self.lambda_param * self.w - np.dot(self.cls_map[idx], x)
        db = -self.cls_map[idx]
        return dw, db

    # 更新權重、偏差
    def _update_weights_bias(self, dw, db):
        self.w -= self.lr * dw
        self.b -= self.lr * db

    # 訓練
    def fit(self, X, y):
        self._init_weights_bias(X)
        self.cls_map = self._get_cls_map(y)

        for _ in range(self.n_iters):
            for idx, x in enumerate(X):
                constrain = self._satisfy_constraint(x, idx)
                dw, db = self._get_gradients(constrain, x, idx)
                self._update_weights_bias(dw, db)

    # 預測
    def predict(self, X):
        estimate = np.dot(X, self.w) + self.b
        prediction = np.sign(estimate)
        return np.where(prediction == -1, 0, 1)


# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 選擇演算法

clf = SVM(learning_rate=1e-2, lambda_param=1e-3, n_iters=5000)

# 模型訓練

clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 73.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以Scikit-learn SVM進行鳶尾花(Iris)品種的辨識

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.svm import SVC

clf = SVC(probability=True)
clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

cc = clf.support_vectors_
print(cc)

cc = clf.support_
print(cc)

cc = clf.predict_proba(X_test)
print(cc)

cc = clf.predict_log_proba(X_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
SVM優點：

    切出來的線很漂亮，擁有最大margin的特性
    可以很容易透過更換Kernel，做出非線性的線（非線性的決策邊界）

SVM缺點：

    效能較不佳，由於時間複雜度為O(n²)當有超過一萬筆資料時，運算速度會慢上許多

"""

from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 載入Iris資料集
iris = datasets.load_iris()

x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
print("target_names: " + str(iris["target_names"]))
y = pd.DataFrame(iris["target"], columns=["target"])
iris_data = pd.concat([x, y], axis=1)
iris_data = iris_data[["sepal length (cm)", "petal length (cm)", "target"]]
iris_data = iris_data[iris_data["target"].isin([0, 1])]
cc = iris_data.head(3)
print(cc)

# 將資料分為Train以及Test並將特徵標準化

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    iris_data[["sepal length (cm)", "petal length (cm)"]],
    iris_data[["target"]],
    test_size=0.3,
    random_state=0,
)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 載入SVM中的SVC，並將kernel設為線性（SVM的Kernel可以換成非線性），並將Probability設為True

from sklearn.svm import SVC

svm = SVC(kernel="linear", probability=True)

svm.fit(X_train_std, y_train["target"].values)

""" Out
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=True, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

SVC是SVM用C++語言實作的版本，背後是libsvm

"""

cc = svm.predict(X_test_std)
print(cc)

cc = y_test["target"].values
print(cc)

error = 0
for i, v in enumerate(svm.predict(X_test_std)):
    if v != y_test["target"].values[i]:
        error += 1
print(error)

cc = svm.predict_proba(X_test_std)
print(cc)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            c=cmap(idx),
            edgecolor="black",
            marker=markers[idx],
            label=cl,
        )

    # highlight test samples
    if test_idx:
        # plot all samples
        if not versiontuple(np.__version__) >= versiontuple("1.9.0"):
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            warnings.warn("Please update to NumPy 1.9.0 or newer")
        else:
            X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c="",
            alpha=1.0,
            edgecolor="black",
            linewidths=1,
            marker="o",
            s=55,
            label="test set",
        )


plot_decision_regions(X_train_std, y_train["target"].values, classifier=svm)
plt.xlabel("sepal length [standardized]")
plt.ylabel("petal width [standardized]")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_03_svm _sample_weight

# 不平衡的資料集利用sample_weight矯正

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 生成隨機資料

np.random.seed(0)
# 20筆資料，前10筆+1
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
# y 前10筆為1，後10筆為-1
y = [1] * 10 + [-1] * 10
print(X)
print(y)

# 指定不同權重

# 初始權重為隨機亂數
modified_weight = abs(np.random.randn(len(X)))

# 後5筆權重乘以 5
modified_weight[15:] *= 5
# 第10筆權重乘以 15
modified_weight[9] *= 15
print(modified_weight)

# 無加權的模型訓練

clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

"""
SVC(gamma=1)
"""

# 加權的模型訓練

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=modified_weight)

"""
SVC(gamma=1)
"""

# 決策邊界函數


def plot_decision_function(classifier, sample_weight, axis, title):
    # plot the decision function
    xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))

    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plot the line, the points, and the nearest vectors to the plane
    axis.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
    axis.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        s=100 * sample_weight,
        alpha=0.9,
        cmap=plt.cm.bone,
        edgecolors="black",
    )

    axis.axis("off")
    axis.set_title(title)


# 繪圖比較兩個模型

# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 權重全部為 1
constant_weight = np.ones(len(X))
plot_decision_function(clf_no_weights, constant_weight, axes[0], "無加權的模型")

# 權重全部為 1
plot_decision_function(clf_weights, modified_weight, axes[1], "加權的模型")
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_04_svm_kernels

# 非線性分割SVM測試

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# 生成隨機資料

# 16筆資料，分兩類
X = np.c_[
    (0.4, -0.7),
    (-1.5, -1),
    (-1.4, -0.9),
    (-1.3, -1.2),
    (-1.1, -0.2),
    (-1.2, -0.4),
    (-0.5, 1.2),
    (-1.5, 2.1),
    (1, 1),
    (1.3, 0.8),
    (1.2, 0.5),
    (0.2, -2),
    (0.5, -2.4),
    (0.2, -2.3),
    (0, -2.7),
    (1.3, 2.1),
].T
Y = [0] * 8 + [1] * 8

print(X)
print(Y)

# 繪圖比較三種 kernels 模型

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
for fignum, kernel in enumerate(["linear", "poly", "rbf"]):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)

    plt.subplot(1, 3, fignum + 1)
    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="r",
    )
    colors = np.array(["yellow", "lightgreen"])
    plt.scatter(X[:, 0], X[:, 1], c=colors[Y], zorder=10, cmap=plt.cm.Paired)

    x_min, x_max, y_min, y_max = -3, 3, -3, 3
    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_05_svr_kernels

# 房價預測

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 載入 Boston 房價資料集

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 觀察資料集彙總資訊
cc = df.info()
print(cc)

# 描述統計量
cc = df.describe()
print(cc)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 繪圖

# 直方圖
import seaborn as sns

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
plt.show()

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.svm import SVR

model = SVR(kernel="linear")

# 6. 模型訓練

model.fit(X_train_std, y_train)

"""
SVR(kernel='linear')
"""

# 7. 模型評分

# R2、MSE、MAE
y_pred = model.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

"""
R2 = 69.56
MSE = 19.12608965301932
MAE = 3.198509245210469
"""

# 取得偏差項及權重
cc = model.intercept_, model.coef_
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition

# SVM人臉辨識

from time import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.decomposition import PCA

# 載入資料集

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print(f"n_samples: {n_samples}")
print(f"n_features: {n_features}")
print(f"n_classes: {n_classes}")

"""
Total dataset size:
n_samples: 1288
n_features: 1850
n_classes: 7
"""

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 使用 PCA 萃取 150 個特徵

n_components = 150

t0 = time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print(f"轉換耗時: {(time() - t0):.3f}s")

# 轉換耗時: 0.183s

# 模型訓練

from sklearn.svm import SVC

clf = SVC(kernel="rbf", class_weight="balanced")
clf.fit(X_train_pca, y_train)

"""
SVC(class_weight='balanced')
"""

# 模型評分

# 計算準確率
from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 分類報告

y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))

# 混淆矩陣圖

ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation=30
)
plt.show()

# 結合圖像與預測結果驗證


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    return f"predicted: {pred_name}\ntrue:         {true_name}"


prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w, n_row=6, n_col=4)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition_org

# Faces recognition example using eigenfaces and SVMs

# The dataset used in this example is a preprocessed excerpt of the "Labeled Faces in the Wild", aka LFW_:

# http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

from time import time
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from scipy.stats import loguniform

# Download the data, if not already on disk and load it as numpy arrays

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

# Split into a training set and a test and keep 25% of the data for testing.

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled dataset): unsupervised feature extraction / dimensionality reduction

n_components = 150

print(
    "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
)
t0 = time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))

# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}
clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)

# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
plt.tight_layout()
plt.show()

# Predicting people's names on the test set

# Qualitative evaluation of the predictions using matplotlib


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


# plot the result of the prediction on a portion of the test set


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    return "predicted: %s\ntrue:      %s" % (pred_name, true_name)


prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_07_decision_tree_from_scratch

# 自行開發決策樹

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 計算熵(entropy)


# 熵公式
def entropy_func(c, n):
    return -(c * 1.0 / n) * math.log(c * 1.0 / n, 2)
    # gini
    # return 1-(c*1.0/n)**2


"""
# 熵公式
def entropy_func(c, n):
    # return -(c*1.0/n)*math.log(c*1.0/n, 2)
    # gini
    return 1 - (c * 1.0 / n) ** 2
"""


# 依特徵值切割成兩類，分別計算熵，再加總
# 計算同一節點內的熵，只有兩個類別
def entropy_cal(c1, c2):
    if c1 == 0 or c2 == 0:
        return 0
    return entropy_func(c1, c1 + c2) + entropy_func(c2, c1 + c2)


# 視每個特徵都是類別變數，依每個類別切割，分別計算熵
# 計算同一節點內的熵，多個類別
def entropy_of_one_division(division):
    s = 0
    n = len(division)
    classes = set(division)
    # 計算每一類別的熵，再加總
    for c in classes:
        n_c = sum(division == c)
        e = n_c * 1.0 / n * entropy_cal(sum(division == c), sum(division != c))
        s += e
    return s, n


# 依分割條件計算熵
def get_entropy(y_predict, y_real):
    if len(y_predict) != len(y_real):
        print("They have to be the same length")
        return None
    n = len(y_real)
    # 左節點
    s_true, n_true = entropy_of_one_division(y_real[y_predict])
    # 右節點
    s_false, n_false = entropy_of_one_division(y_real[~y_predict])
    # 左、右節點加權總和
    s = n_true * 1.0 / n * s_true + n_false * 1.0 / n * s_false
    return s


# 決策樹演算法類別


class DecisionTreeClassifier(object):
    def __init__(self, max_depth=3):
        self.depth = 0
        self.max_depth = max_depth

    # 訓練
    def fit(self, x, y, par_node={}, depth=0):
        if par_node is None:
            return None
        elif len(y) == 0:
            return None
        elif self.all_same(y):
            return {"val": float(y[0])}
        elif depth >= self.max_depth:
            return None
        else:
            # 計算資訊增益
            col, cutoff, entropy = self.find_best_split_of_all(x, y)
            if cutoff is not None:
                y_left = y[x[:, col] < cutoff]
                y_right = y[x[:, col] >= cutoff]
                par_node = {
                    "col": feature_names[col],
                    "index_col": int(col),
                    "cutoff": float(cutoff),
                    "val": float(np.round(np.mean(y))),
                }
                par_node["left"] = self.fit(
                    x[x[:, col] < cutoff], y_left, {}, depth + 1
                )
                par_node["right"] = self.fit(
                    x[x[:, col] >= cutoff], y_right, {}, depth + 1
                )
                self.depth += 1
            self.trees = par_node
            return par_node

    # 比較所有特徵找到最佳切割條件
    def find_best_split_of_all(self, x, y):
        col = None
        min_entropy = 1
        cutoff = None
        for i, c in enumerate(x.T):
            entropy, cur_cutoff = self.find_best_split(c, y)
            if entropy == 0:  # 找到最佳切割條件
                return i, cur_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                col = i
                cutoff = cur_cutoff
        return col, cutoff, min_entropy

    # 根據一個特徵找到最佳切割條件
    def find_best_split(self, col, y):
        min_entropy = 10
        n = len(y)
        for value in set(col):
            y_predict = col < value
            my_entropy = get_entropy(y_predict, y)
            if my_entropy <= min_entropy:
                min_entropy = my_entropy
                cutoff = value
        return min_entropy, cutoff

    # 檢查是否節點中所有樣本均屬同一類
    def all_same(self, items):
        return all(x == items[0] for x in items)

    # 預測
    def predict(self, x):
        tree = self.trees
        results = np.array([0] * len(x))
        for i, c in enumerate(x):
            try:
                results[i] = self._get_prediction(c)
            except:
                pass
        return results

    # 預測一筆
    def _get_prediction(self, row):
        cur_layer = self.trees
        while cur_layer is not None and cur_layer.get("cutoff"):
            if row[cur_layer["index_col"]] < cur_layer["cutoff"]:
                cur_layer = cur_layer["left"]
            else:
                cur_layer = cur_layer["right"]
        else:
            return cur_layer.get("val") if cur_layer is not None else None


# 載入資料集

# ds = datasets.load_iris()

ds = datasets.load_wine()

feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 選擇演算法

# 模型訓練

import json

clf = DecisionTreeClassifier()
output = clf.fit(X_train, y_train)
# output
print(json.dumps(output, indent=4))

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 30.56%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_08_scikit-learn_decision_tree

# Scikit-learn決策樹演算法

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 載入資料集

ds = datasets.load_wine()
feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()  # criterion='entropy')
clf.fit(X_train, y_train)

# DecisionTreeClassifier()

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 繪製樹狀圖

import matplotlib.pyplot as plt

from sklearn.tree import plot_tree

plt.figure(figsize=(14, 10))
plot_tree(clf, feature_names=feature_names)
plt.show()


# 使用 graphviz 繪製圖形
"""
安裝
    安裝 graphviz (https://graphviz.org/download/)
    將安裝路徑的bin加入環境變數Path中(C:\Program Files (x86)\Graphviz2.XX\bin)
    pip install graphviz pydotplus
"""
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=ds.target_names,
    feature_names=ds.feature_names,
    out_file=None,
)
graph = graph_from_dot_data(dot_data)
# graph.write_png('tmp_wine_tree.png')  NG

# dot 格式存檔

dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=ds.target_names,
    feature_names=ds.feature_names,
    out_file="tmp_wine_tree.dot",
)

# 取得樹狀圖的相關資訊

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, -1)]  # seed is the root node id and its parent depth
while len(stack) > 0:
    node_id, parent_depth = stack.pop()
    node_depth[node_id] = parent_depth + 1

    # If we have a test node
    if children_left[node_id] != children_right[node_id]:
        stack.append((children_left[node_id], parent_depth + 1))
        stack.append((children_right[node_id], parent_depth + 1))
    else:
        is_leaves[node_id] = True

print(f"樹狀圖共有{n_nodes}個節點:")
for i in range(n_nodes):
    depth = node_depth[i] * "\t"
    if is_leaves[i]:
        print(f"{depth}node={i} leaf node.")
    else:
        print(
            f"{depth}node={i} child node: go to node {children_left[i]} if X[:, "
            + f"{feature[i]}] <= {threshold[i]} else to node {children_right[i]}."
        )
print()

node_indicator = clf.decision_path(X)
leave_id = clf.apply(X)
sample_id = 0
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print(f"Rules used to predict sample {sample_id}: ")
for node_id in node_index:
    if leave_id[sample_id] == node_id:
        continue

    if X[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "decision id node {} : (X[{}, {}] (= {}) {} {})".format(
            node_id,
            sample_id,
            feature[node_id],
            X[sample_id, feature[node_id]],
            threshold_sign,
            threshold[node_id],
        )
    )

# For a group of samples, we have the following common node.
sample_ids = [0, 1]
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)

common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nThe following samples %s share the node %s in the tree"
    % (sample_ids, common_node_id)
)
print("It is %s %% of all nodes." % (100 * len(common_node_id) / n_nodes,))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_09_scikit-learn_decision_tree_regression

# Scikit-learn迴歸樹測試

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# 生成隨機資料

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# 訓練兩個模型

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_1.fit(X, y)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_2.fit(X, y)

# DecisionTreeRegressor(max_depth=5)

# 預測

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# 模型繪圖

plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_10_decision_tree_regression_boston

# 房價預測

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 載入 Boston 房價資料集

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 繪圖

# 直方圖
import seaborn as sns

X, y = df.drop("MEDV", axis=1).values, df.MEDV.values
sns.histplot(x=y)
plt.show()

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()

# 6. 模型訓練

model.fit(X_train_std, y_train)

# DecisionTreeRegressor()

# 7. 模型評分

# R2、MSE、MAE
y_pred = model.predict(X_test_std)
print(f"R2 = {r2_score(y_test, y_pred)*100:.2f}")
print(f"MSE = {mean_squared_error(y_test, y_pred)}")
print(f"MAE = {mean_absolute_error(y_test, y_pred)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_11_decision_tree_multioutput_face_completion

# 使用Scikit-learn各種迴歸演算法預測人臉下半部

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.utils.validation import check_random_state
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

# 載入資料集

data, targets = fetch_olivetti_faces(return_X_y=True)

# 資料分割

train = data[targets < 30]
test = data[targets >= 30]

# 模型訓練

n_pixels = data.shape[1]
# 人臉上半部為 X，人臉下半部為 Y
X_train = train[:, : (n_pixels + 1) // 2]
y_train = train[:, n_pixels // 2 :]

# 使用各種迴歸演算法
ESTIMATORS = {
    "迴歸樹": DecisionTreeRegressor(),
    "KNN": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

# 訓練
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)

# 測試 5 筆資料

n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]

# 預測
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    y_test_predict[name] = estimator.predict(X_test)

# 依照各種迴歸演算法測試結果繪製人臉

# 設定圖片寬/高
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("預測人臉下半部", size=16)

# 繪圖
for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i > 0:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1, title="true faces")

    sub.axis("off")
    sub.imshow(
        true_face.reshape(image_shape), cmap=plt.cm.gray, interpolation="nearest"
    )

    # 依照各種迴歸演算法繪製人臉
    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j, title=est)

        sub.axis("off")
        sub.imshow(
            completed_face.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation="nearest",
        )
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_12_scikit-learn_random_forest
# Scikit-learn決策樹演算法

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math

# 載入資料集

ds = datasets.load_wine()
feature_names = ds.feature_names
X, y = ds.data, ds.target

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, y_train)

# RandomForestClassifier(n_estimators=50)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 97.22%

# 特徵重要性

cc = clf.feature_importances_
print(cc)

print(feature_names)

# 繪圖

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.figure(figsize=(10, 6))
df = pd.DataFrame(
    {"feature_names": feature_names, "feature_importance": clf.feature_importances_}
)
df.sort_values(by=["feature_importance"], ascending=False, inplace=True)
sns.barplot(x=df["feature_importance"], y=df["feature_names"])
plt.show()

# 使用Permutation importance評估特徵重要性

from sklearn.inspection import permutation_importance

result = permutation_importance(
    clf, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)

sorted_importances_idx = result.importances_mean.argsort()
importances = pd.DataFrame(
    result.importances[sorted_importances_idx].T,
    columns=np.array(feature_names)[sorted_importances_idx],
)

ax = importances.plot.box(vert=False, whis=10, figsize=(10, 6))
ax.set_title("Permutation Importances (test set)")
ax.axvline(x=0, color="k", linestyle="--")
ax.set_xlabel("Decrease in accuracy score")
ax.figure.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_13_chaid_three_cat

from seaborn import load_dataset

df = load_dataset("titanic")
cc = df.head()
print(cc)

df.embarked = df.embarked.fillna(method="ffill")
cc = df.head()
print(cc)

from CHAID import Tree

independent_variable_columns = ["sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

from CHAID import Tree

independent_variable_columns = ["fare", "sex", "embarked"]
dep_variable = "survived"
tree = Tree.from_pandas_df(
    df,
    dict(zip(independent_variable_columns, ["ordinal"] + ["nominal"] * 3)),
    dep_variable,
    dep_variable_type="categorical",
    max_depth=5,
    min_parent_node_size=2,
    alpha_merge=0.1,
)
tree.print_tree()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
