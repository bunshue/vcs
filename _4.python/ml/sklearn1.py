"""
pip install scikit-learn

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
'''
import sklearn as skl

print(skl.__version__)

from sklearn import datasets, svm, metrics

print(dir(datasets))

import sklearn

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

print("線性回歸的範例 1")

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [88, 72, 90, 76, 92]
lm.fit(X, y)
print("第6次考試分數：", lm.predict([[6]]))

print("線性回歸的範例 2")

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [1, 4, 9, 16, 25]
lm.fit(X, y)

xx = np.linspace(0, 10, 11)
yy = np.linspace(0, 10, 11)
for i in range(11):
    print(i)
    print("第", i, "項", lm.predict([[i]]))
    xx[i] = i
    yy[i] = lm.predict([[i]])

plt.plot(X, y, "ro-")
plt.plot(xx, yy, "go:")


plt.show()

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

import seaborn as sns  # 海生, 自動把圖畫得比較好看

iris = sns.load_dataset("iris")
iris.head()

sns.set()
sns.pairplot(iris, hue="species", height=3)

print(iris)
print("cccc")

print("------------------------------------------------------------")  # 60個

# seaborn

import seaborn as sns  # 海生, 自動把圖畫得比較好看

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
plt.show()

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

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()  # 建立線性模組物件
regression.fit(x_train, y_train)
print(f"斜率  = {regression.coef_[0].round(2)}")
print(f"截距  = {regression.intercept_.round(2)}")

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()  # 建立線性模組物件
regression.fit(x_train, y_train)
print(f"斜率  = {regression.coef_[0].round(2)}")
print(f"截距  = {regression.intercept_.round(2)}")

y_pred = regression.predict(x_test)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color="red")

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)
print(f"決定係數 = {r2.round(2)}")

plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

np.random.seed(3)  # 設定隨機數種子值

# np.random.seed(5)                                       # 設定隨機數種子值

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

# 繪圓點, 圓點用黑色外框
plt.scatter(data[:, 0], data[:, 1], marker="o", edgecolor="black")

plt.title("無監督學習")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)  # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)

e = cluster.KMeans(n_clusters=3)  # k-mean方法建立 3 個群集中心物件
e.fit(data)  # 將數據帶入物件, 做群集分析
print(e.labels_)  # 列印群集類別標籤
print(e.cluster_centers_)  # 列印群集中心

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)  # 設定隨機數種子值
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
plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

print("------------------------------------------------------------")  # 60個

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

np.random.seed(7)  # 固定亂數種子

df = pd.read_csv("iris.csv")

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

# 線性回歸

print("------------------------------------------------------------")  # 60個

from sklearn import linear_model

# x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
# y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量
# x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
# y = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
xs = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]], dtype=float)
ys = np.array([[0.0], [1.0], [2.0], [5.0], [4.0], [5.0]], dtype=float)

regression = linear_model.LinearRegression()  # 建立線性模組物件
regression.fit(xs, ys)
a = regression.coef_[0][0]  # 取出斜率
b = regression.intercept_[0]  # 取出截距
print(f"斜率  = {a.round(2)}")
print(f"截距  = {b.round(2)}")

# 畫 理論值 y = x
plt.plot([-1, 12], [-1, 12], "lime", lw=3, label="理論值 y = x")

y2 = a * xs + b
plt.plot(xs, ys, "b-o", lw=1, ms=10, label="實驗值")
plt.plot(xs, y2, "r", lw=2, label="迴歸直線")  # 繪製迴歸直線

xx = 10
predicted = a * xx + b
print(f"x = 10 的 預測值 = {predicted}")
plt.plot(xx, predicted, "ro", lw=1, ms=12, label="預測值")

xmin, xmax, ymin, ymax = -1, 12, -1, 12
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100, n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)  # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100, n_features=1, noise=20)
# 數據分割為x_train,y_train訓練數據, x_test,y_test測試數據
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label="訓練數據")
plt.scatter(x_test, y_test, label="測試數據")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)  # 設計隨機數種子
print("製作原始資料 x, y")
x, y = datasets.make_regression(n_samples=10, n_features=1, noise=20)

# 數據分割為x_train,y_train訓練數據80%, x_test,y_test測試數據20%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()  # 建立線性模組物件
regression.fit(x_train, y_train)
print(f"斜率  = {regression.coef_[0].round(2)}")
print(f"截距  = {regression.intercept_.round(2)}")

print("預測")
y_pred = regression.predict(x_test)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y, c="blue", marker="o", lw=8, label="原始資料")
plt.scatter(x_train, y_train, c="red", marker="o", lw=4, label="訓練數據")
plt.scatter(x_test, y_test, c="green", marker="o", lw=4, label="測試數據")

# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color="red", label="迴歸直線")

print("x_test")
print(x_test)
print("y_pred")
print(y_pred)

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)

print(f"決定係數 = {r2.round(2)}")

"""
print('原始資料')
print(x)
print()
print(y)
print('train')
print(x_train)
print()
print(y_train)
print('test')
print(x_test)
print()
print(y_test)
"""

plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

'''

print('迴歸效果評估')


print('MSE均方誤差')

from sklearn.metrics import mean_squared_error
y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_squared_error(y_true, y_pred))

print('MAE平均絕對誤差')
from sklearn.metrics import mean_absolute_error
y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(mean_absolute_error(y_true, y_pred))

print('R-Squared擬合度')
from sklearn.metrics import r2_score
y_true = [1, 1.25, 2.37]
y_pred = [1, 1, 2]
print(r2_score(y_true,y_pred))

print('------------------------------------------------------------')	#60個

print('分類效果評估')
print('FP/FN/TP/TN')

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)

print('準確率')
from sklearn.metrics import accuracy_score
print(accuracy_score(y_real, y_pred))

print('召回率')
from sklearn.metrics import recall_score
print(recall_score(y_real, y_pred))

print('精度')
from sklearn.metrics import precision_score
print(precision_score(y_real, y_pred))

print('F值')

from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2)) # 計算fn

print('Logloss')
from sklearn.metrics import log_loss
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score=[0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real,y_score))

print('ROC曲線和AUC')
from sklearn.metrics import roc_auc_score, roc_curve

print(roc_auc_score(y_real, y_score)) # AUC值

fpr, tpr, thresholds = roc_curve(y_real, y_score) 
plt.plot(fpr, tpr) # 繪圖
plt.show()

# P-R曲線
from sklearn.metrics import precision_recall_curve
precision, recall, _ = precision_recall_curve(y_real, y_score)
plt.plot(recall,precision)

plt.show()

print('------------------------------------------------------------')	#60個

print('多指標評分')

from sklearn.metrics import classification_report

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score=[0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print('------------------------------------------------------------')	#60個

print('K近鄰算法')

from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split

data = datasets.load_breast_cancer()
X = data.data # 自變量
y = data.target # 因變量
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=0)
clf = neighbors.KNeighborsClassifier(5) # 設鄰居數爲5個
clf.fit(x_train, y_train) # 訓練模型
print(clf.score(x_test, y_test)) # 給模型打分
print(clf.predict([x_test[0]]), y_test[0], clf.predict_proba([x_test[0]]))

print('------------------------------------------------------------')	#60個

from sklearn.metrics import accuracy_score
from scipy.spatial import distance
import operator

def classify(inX, dataSet, labels, k):
    #S=np.cov(dataSet.T)   #協方差矩陣，爲計算馬氏距離
    #SI = np.linalg.inv(S)  #協方差矩陣的逆矩陣
    #distances = np.array(distance.cdist(dataSet, [inX], 'mahalanobis', VI=SI)).reshape(-1)
    distances = np.array(distance.cdist(dataSet, [inX], 'euclidean').reshape(-1))
    sortedDistIndicies = distances.argsort() # 取排序的索引，用於label排序
    classCount={}
    for i in range(k): # 訪問距離最近的五個實例
        voteILabel = labels[sortedDistIndicies[i]]
        classCount[voteILabel]=classCount.get(voteILabel,0)+1
    sortedClassCount = sorted(classCount.items(), 
             key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0] # 取最多的分類

ret = [classify(x_test[i], x_train, y_train, 5) for i in range(len(x_test))]
print(accuracy_score(y_test, ret))

print('------------------------------------------------------------')	#60個

print('聚類算法')

from sklearn.datasets import make_blobs  # 數據支持
from sklearn.cluster import KMeans  # 聚類方法

X,y = make_blobs(n_samples=100, random_state=150) 
y_pred = KMeans(n_clusters=3, random_state=5).fit_predict(X)  # 訓練
plt.scatter(X[:,0],X[:,1],c=y_pred)
plt.show()

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

