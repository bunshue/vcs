"""
pip install scikit-learn

"""

import sklearn

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

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

from sklearn import datasets, svm, metrics
print(sklearn.__version__)
print(dir(datasets))
print(sklearn)

print("------------------------------------------------------------")  # 60個

# 1. Rescale Data
# 將資料比例縮放到0與1之間# Rescale data (between 0 and 1)

import scipy
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 2. Standardize Data
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import StandardScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 3. Normalize Data
# 最大值變為1，最小值變為0

from sklearn.preprocessing import Normalizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(normalizedX[0:5, :])

print("------------------------------------------------------------")  # 60個

# 4. Binarize Data (Make Binary)
# 資料二元化(0或者1)

from sklearn.preprocessing import Binarizer

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(url, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
# summarize transformed data
np.set_printoptions(precision=3)
print(binaryX[0:5, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer


def similarity_tfidf(s1, s2):
    def add_space(s):
        return " ".join(list(s))

    s1, s2 = add_space(s1), add_space(s2)

    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()

    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


string1 = "漢堡蛋"
string2 = "我要一份漢堡蛋"
# string2 = '請給我來一份漢堡蛋'
# string2 = '你是一個漢堡蛋嗎?'

result = similarity_tfidf(string1, string2)

print("相似度 : ", result)
if result > 0.2:
    print("OK, 一個漢堡蛋")
else:
    print("Sorry, 無法接受訂餐")

print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
iris.head()

sns.set()
sns.pairplot(iris, hue="species", height=3)

print(iris)
print("cccc")

print("------------------------------------------------------------")  # 60個

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"

tips = sns.load_dataset("tips")
print(tips)

print("------------------------------------------------------------")  # 60個

# 怎麼選最好參數、model？
# 製造像真的一様的數據

# from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=500, centers=3, n_features=2, random_state=0)
plt.scatter(x[:, 0], x[:, 1], c=y)

#plt.show()

print("------------------------------------------------------------")  # 60個

# Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

clf = SVC()
# clf = SVC(gamma = 'scale')

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

# 試用 Decision Tree
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

# 試用 Random Forest

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)

# 看一下五次的成績
scores = cross_val_score(clf, x, y, cv=5)
print(scores)

# 很快的算一下平均
print(scores.mean())

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

x, y = datasets.make_regression(n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
plt.legend()

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習")

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="*", color="red")
plt.title("無監督學習")

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=5)
d_sta = StandardScaler().fit_transform(data)  # 標準化

# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=0)
print(data)
print(label)
print(f"分類 : {label}")

plt.scatter(data[:, 0], data[:, 1], c=label, cmap="bwr")
plt.grid(True)

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

data, label = make_blobs(n_samples=10, n_features=2, centers=2, random_state=0)

print(data)
print(label)
print(f"分類 : {label}")

plt.subplot(121)
plt.scatter(data[:, 0], data[:, 1], c=label, cmap="bwr")

d_sta = StandardScaler().fit_transform(data)  # 標準化
print(d_sta)

plt.subplot(122)
plt.scatter(d_sta[:, 0], d_sta[:, 1], c=label, cmap="bwr")
plt.grid(True)

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)

print(f"特徵數據外形 : {d_sta.shape}")
print(f"訓練數據外形 : {dx_train.shape}")
print(f"測試數據外形 : {dx_test.shape}")
print(f"標籤數據外形 : {label.shape}")
print(f"訓練數據外形 : {label_train.shape}")
print(f"測試數據外形 : {label_test.shape}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
k_model = KNeighborsClassifier(n_neighbors=5)  # k = 5
# 建立訓練數據模型
k_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = k_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {k_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {k_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
lo_model = LogisticRegression()
# 建立訓練數據模型
lo_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = lo_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=0)
d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 建立分類模型
svm_model = LinearSVC()
# 建立訓練數據模型
svm_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = svm_model.predict(dx_test)
# 輸出測試數據的 label
print(label_test)
# 輸出預測數據的 label
print(pred)
# 輸出準確性
print(f"訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {svm_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

data, label = make_moons(n_samples=200, noise=0.2, random_state=0)

d_sta = StandardScaler().fit_transform(data)  # 標準化
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=0
)
# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm_model = LinearSVC()
svm_model.fit(dx_train, label_train)
pred = svm_model.predict(dx_test)
# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print("=" * 50)
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)
# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

data, label = datasets.load_iris(return_X_y=True)
print("鳶尾花花萼和花瓣數據")
print(data[0:5])
print(f"分類 : {label[0:5]}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=0
)
# 建立分類模型
tree_model = DecisionTreeClassifier()
# 建立訓練數據模型
tree_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = tree_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {tree_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {tree_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data, label = datasets.load_iris(return_X_y=True)
# 分割數據為訓練數據和測試數據
dx_train, dx_test, label_train, label_test = train_test_split(
    data, label, test_size=0.2, random_state=0
)
# 建立分類模型
forest_model = RandomForestClassifier()
# 建立訓練數據模型
forest_model.fit(dx_train, label_train)
# 對測試數據做預測
pred = forest_model.predict(dx_test)
# 輸出準確性
print(f"訓練資料的準確性 = {forest_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {forest_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習", fontsize=16)

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

# 建立 300 個點, n_features = 2, centers = 3
data, label = datasets.make_blobs(
    n_samples=300, n_features=2, centers=3, random_state=10
)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色,
plt.scatter(data[:, 0], data[:, 1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:, 0], e.cluster_centers_[:, 1], marker="*", color="red")
plt.title("無監督學習", fontsize=16)

#plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

df = pd.read_csv("data/iris.csv")

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:4].astype(float)
Y = to_categorical(dataset[:, 4])

X = StandardScaler().fit_transform(X)  # 標準化

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

print(model.summary())

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=100, batch_size=5)

loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

# Y_pred = model.predict_classes(X_test)
Y_pred = model.predict_step(X_test)
print(Y_pred)

Y_target = dataset[:, 4][120:].astype(int)
print(Y_target)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("迴歸效果評估")

print("MSE均方誤差")

from sklearn.metrics import mean_squared_error

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_squared_error(y_true, y_pred))

print("MAE平均絕對誤差")
from sklearn.metrics import mean_absolute_error

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_absolute_error(y_true, y_pred))

print("R-Squared擬合度")
from sklearn.metrics import r2_score

y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(r2_score(y_true, y_pred))

print("------------------------------------------------------------")  # 60個

print("分類效果評估")
print("FP/FN/TP/TN")

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)

print("準確率")
from sklearn.metrics import accuracy_score

print(accuracy_score(y_real, y_pred))

print("召回率")
from sklearn.metrics import recall_score

print(recall_score(y_real, y_pred))

print("精度")
from sklearn.metrics import precision_score

print(precision_score(y_real, y_pred))

print("F值")

from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2))  # 計算fn

print("Logloss")
from sklearn.metrics import log_loss

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real, y_score))

print("ROC曲線和AUC")
from sklearn.metrics import roc_auc_score, roc_curve

print(roc_auc_score(y_real, y_score))  # AUC值

fpr, tpr, thresholds = roc_curve(y_real, y_score)
plt.plot(fpr, tpr)  # 繪圖

#plt.show()

# P-R曲線
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_real, y_score)
plt.plot(recall, precision)

#plt.show()

print("------------------------------------------------------------")  # 60個

print("多指標評分")

from sklearn.metrics import classification_report

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print("------------------------------------------------------------")  # 60個

print("聚類算法")

from sklearn.datasets import make_blobs  # 數據支持
from sklearn.cluster import KMeans  # 聚類方法

X, y = make_blobs(n_samples=100, random_state=150)
y_pred = KMeans(n_clusters=3, random_state=5).fit_predict(X)  # 訓練
plt.scatter(X[:, 0], X[:, 1], c=y_pred)

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())

print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())

df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

#plt.show()

print("------------------------------")  # 30個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())

print("------------------------------")  # 30個

scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std, columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_std.head())

df_std.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

f_tracking = [
    110,
    1018,
    1130,
    417,
    626,
    957,
    90,
    951,
    946,
    797,
    981,
    125,
    456,
    731,
    1640,
    486,
    1309,
    472,
    1133,
    1773,
    906,
    532,
    742,
    621,
    855,
]
happiness = [
    0.3,
    0.8,
    0.5,
    0.4,
    0.6,
    0.4,
    0.7,
    0.5,
    0.4,
    0.3,
    0.3,
    0.6,
    0.2,
    0.8,
    1,
    0.6,
    0.2,
    0.7,
    0.5,
    0.7,
    0.1,
    0.4,
    0.3,
    0.6,
    0.3,
]

df = pd.DataFrame({"FB追蹤數": f_tracking, "快樂程度": happiness})
print(df.head())
print("------------------------------")  # 30個

df_scaled = pd.DataFrame(preprocessing.scale(df), columns=["標準化FB追蹤數", "標準化快樂程度"])
print(df_scaled.head())
df_scaled.plot(kind="scatter", x="標準化FB追蹤數", y="標準化快樂程度")

print("------------------------------")  # 30個

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax, columns=["最小最大值縮放FB追蹤數", "最小最大值縮放快樂程度"])
print(df_minmax.head())

df_minmax.plot(kind="scatter", x="最小最大值縮放FB追蹤數", y="最小最大值縮放快樂程度")

#plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

df = pd.read_csv("data/test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)

print("------------------------------------------------------------")  # 60個

# How do I use pandas with scikit-learn to create Kaggle submissions? (video)

# 讀取[Kaggle's Titanic competition]資料集至df
# train = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
train = pd.read_csv(filename)

print("檢視前幾行")
cc = train.head()
print(cc)

# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ["Pclass", "Parch"]
X = train.loc[:, feature_cols]

print("X之大小")
cc = X.shape
print(cc)

# create a response vector 'y' by selecting a Series
y = train.Survived
print("y之大小")
cc = y.shape
print(cc)

# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, y)

# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv("http://bit.ly/kaggletest")
print("檢視前幾行")
cc = test.head()
print(cc)

# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
print("X_new之大小")
cc = X_new.shape
print(cc)

# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)

# create a DataFrame of passenger IDs and testing set predictions
print("檢視前幾行")
cc = pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).head()
print(cc)

# ensure that PassengerID is the first column by setting it as the index
print("檢視前幾行")
cc = (
    pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class})
    .set_index("PassengerId")
    .head()
)
print(cc)

print("df轉csv")
pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).set_index(
    "PassengerId"
).to_csv("tmp_sub.csv")

print("df轉pickle")
train.to_pickle("tmp_train.pkl")

print("pickle轉df")
print("檢視前幾行")
cc = pd.read_pickle("tmp_train.pkl").head()
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data[:, :2], iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

# Standardize the features using StandardScaler
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Create a K-Nearest Neighbors classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Predict the target values on the test data
y_pred = knn.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)

#Accuracy: 0.631578947368421

print("------------------------------------------------------------")  # 60個

#Loading The Data

from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data, iris.target

# Print the lengths of X and y
print("Size of X:", X.shape) #  (150, 4)
print("Size of y:", y.shape) #  (150, )

print("------------------------------------------------------------")  # 60個

#Training And Test Data

# Import train_test_split from sklearn
from sklearn.model_selection import train_test_split

# Split the data into training and test sets with test_size=0.2 (20% for test set)
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Print the sizes of the arrays
print("Size of X_train:", X_train.shape)
print("Size of X_test: ", X_test.shape)
print("Size of y_train:", y_train.shape)
print("Size of y_test: ", y_test.shape)

print("------------------------------------------------------------")  # 60個

#Create instances of the models

# Import necessary classes from sklearn libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Create instances of supervised learning models
# Logistic Regression classifier (max_iter=1000)
lr = LogisticRegression(max_iter=1000)

# k-Nearest Neighbors classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)

# Support Vector Machine classifier
svc = SVC()

# Create instances of unsupervised learning models
# k-Means clustering with 3 clusters and 10 initialization attempts
k_means = KMeans(n_clusters=3, n_init=10)

# Principal Component Analysis with 2 components
pca = PCA(n_components=2)

print("------------------------------------------------------------")  # 60個

#Model Fitting

# Fit models to the data
lr.fit(X_train, y_train)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
k_means.fit(X_train)
pca.fit_transform(X_train)

# Print the instances and models
print("lr:", lr)
print("knn:", knn)
print("svc:", svc)
print("k_means:", k_means)
print("pca:", pca)

print("------------------------------------------------------------")  # 60個

#Prediction

# Predict using different supervised estimators
y_pred_svc = svc.predict(X_test)
y_pred_lr = lr.predict(X_test)
y_pred_knn_proba = knn.predict_proba(X_test)

# Predict labels using KMeans in clustering algorithms
y_pred_kmeans = k_means.predict(X_test)

# Print the results
print("Supervised Estimators:")
print("SVC predictions:", y_pred_svc)
print("Logistic Regression predictions:", y_pred_lr)
print("KNeighborsClassifier probabilities:\n", y_pred_knn_proba[:5],"\n     ...")

print("\nUnsupervised Estimators:")
print("KMeans predictions:", y_pred_kmeans)

print("------------------------------------------------------------")  # 60個

#Preprocessing The Data
#Standardization

from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler and fit it to training data
scaler = StandardScaler().fit(X_train)

# Transform the training and test data using the scaler
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

# Print the variables
print("\nStandardized X_train:\n", standardized_X[:5],"\n     ...")
print("\nStandardized X_test:\n", standardized_X_test[:5],"\n     ...")

#Normalization

from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

# Print the variables
print("\nNormalized X_train:\n", normalized_X[:5],"\n     ...")
print("\nNormalized X_test:\n", normalized_X_test[:5],"\n     ...")

#Binarization

import numpy as np
from sklearn.preprocessing import Binarizer

# Create a sample data array
data = np.array([[1.5, 2.7, 0.8],
                 [0.2, 3.9, 1.2],
                 [4.1, 1.0, 2.5]])

# Create a Binarizer instance with a threshold of 2.0
binarizer = Binarizer(threshold=2.0)

# Apply binarization to the data
binarized_data = binarizer.transform(data)

print("Original data:")
print(data)
print("\nBinarized data:")
print(binarized_data)

#Encoding Categorical Features

from sklearn.preprocessing import LabelEncoder

# Sample data: categorical labels
labels = ['cat', 'dog', 'dog', 'fish', 'cat', 'dog', 'fish']

# Create a LabelEncoder instance
label_encoder = LabelEncoder()

# Fit and transform the labels
encoded_labels = label_encoder.fit_transform(labels)

# Print the original labels and their encoded versions
print("Original labels:", labels)
print("Encoded labels:", encoded_labels)

# Decode the encoded labels back to the original labels
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("Decoded labels:", decoded_labels)

print("------------------------------------------------------------")  # 60個

#Imputing Missing Values

import numpy as np
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = np.array([[1.0, 2.0, np.nan],
                 [4.0, np.nan, 6.0],
                 [7.0, 8.0, 9.0]])

# Create a SimpleImputer instance with strategy='mean'
imputer = SimpleImputer(strategy='mean')

# Fit and transform the imputer on the data
imputed_data = imputer.fit_transform(data)

print("Original data:")
print(data)
print("\nImputed data:")
print(imputed_data)

print("------------------------------------------------------------")  # 60個

#Generating Polynomial Features

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Sample data
data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

# Create a PolynomialFeatures instance of degree 2
poly = PolynomialFeatures(degree=2)

# Transform the data to include polynomial features
poly_data = poly.fit_transform(data)

print("Original data:")
print(data)
print("\nPolynomial features:")
print(poly_data)

print("------------------------------------------------------------")  # 60個

#Classification Metrics

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Accuracy Score
accuracy_knn = knn.score(X_test, y_test)
print("Accuracy Score (knn):", knn.score(X_test, y_test))

accuracy_y_pred = accuracy_score(y_test, y_pred_lr)
print("Accuracy Score (y_pred):", accuracy_y_pred)

# Classification Report
classification_rep_y_pred = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred):\n", classification_rep_y_pred)

classification_rep_y_pred_lr = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred_lr):\n", classification_rep_y_pred_lr)

# Confusion Matrix
conf_matrix_y_pred_lr = confusion_matrix(y_test, y_pred_lr)
print("Confusion Matrix (y_pred_lr):\n", conf_matrix_y_pred_lr)

print("------------------------------------------------------------")  # 60個

#Regression Metrics

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# True values (ground truth)
y_true = [3, -0.5, 2]

# Predicted values
y_pred = [2.8, -0.3, 1.8]

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)

# Calculate Mean Squared Error
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)

# Calculate R² Score
r2 = r2_score(y_true, y_pred)
print("R² Score:", r2)

print("------------------------------------------------------------")  # 60個

#Clustering Metrics

from sklearn.metrics import adjusted_rand_score, homogeneity_score, v_measure_score

# Adjusted Rand Index
adjusted_rand_index = adjusted_rand_score(y_test, y_pred_kmeans)
print("Adjusted Rand Index:", adjusted_rand_index)

# Homogeneity Score
homogeneity = homogeneity_score(y_test, y_pred_kmeans)
print("Homogeneity Score:", homogeneity)

# V-Measure Score
v_measure = v_measure_score(y_test, y_pred_kmeans)
print("V-Measure Score:", v_measure)

print("------------------------------------------------------------")  # 60個

#Cross-Validation

# Import necessary library
from sklearn.model_selection import cross_val_score

# Cross-validation with KNN estimator
knn_scores = cross_val_score(knn, X_train, y_train, cv=4)
print(knn_scores)

# Cross-validation with Linear Regression estimator
lr_scores = cross_val_score(lr, X, y, cv=2)
print(lr_scores)

#Grid Search

# Import necessary library
from sklearn.model_selection import GridSearchCV

# Define parameter grid
params = {
    'n_neighbors': np.arange(1, 3),
    'weights': ['uniform', 'distance']
}

# Create GridSearchCV object
grid = GridSearchCV(estimator=knn, param_grid=params)

# Fit the grid to the data
grid.fit(X_train, y_train)

# Print the best parameters found
print("Best parameters:", grid.best_params_)

# Print the best cross-validation score
print("Best cross-validation score:", grid.best_score_)

# Print the accuracy on the test set using the best parameters
best_knn = grid.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)
print("Test set accuracy:", test_accuracy)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

