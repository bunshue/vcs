"""
Iris 鳶尾花
Iris 鳶尾花數據庫 150筆資料 4個欄位 3種品種 每種50筆資料

以Iris dataset為例，鳶尾花資料集是非常著名的生物資訊資料集之一，
取自美國加州大學歐文分校的機器學習資料庫http://archive.ics.uci.edu/ml/datasets/Iris
資料的筆數為150筆，共有五個欄位：

        萼長SL        萼寬SW       瓣長PL        瓣寬PW       品種
4個欄位 sepal_length, sepal_width, petal_length, petal_width, species
萼長 花萼長度(Sepal.Length)(cm)
萼寬 花萼寬度(Sepal.Width)(cm)
瓣長 花瓣長度(Petal.Length)(cm)
瓣寬 花瓣寬度(Petal.Width)(cm)

# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 有四個 features: 花萼長度、花萼寬度 和 花瓣長度、花瓣寬度

3種品種 類別(Class/Species)
['setosa' 'versicolor' 'virginica']
# 山鳶尾   變色鳶尾    維吉尼亞鳶尾

#鳶尾花(Iris)品種的辨識
標準的分類問題: 這是哪種鳶尾花

鳶尾花 (Iris)  數據庫是很有名的資料,
就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。
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

import joblib
import sklearn.linear_model
import tensorflow as tf
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# 不要顯示一些警告
import warnings

# warnings.filterwarnings("ignore")

print("------------------------------------------------------------")  # 60個


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("鳶尾花數據庫 基本數據 load_iris()")

X, y = datasets.load_iris(return_X_y=True)  # 分別回傳兩種資料

iris = datasets.load_iris()  # 回傳iris包含data和target兩欄位資料
X = iris.data
y = iris.target  # 資料集目標

print("dir(iris)", dir(iris))
print("iris.feature_names=", iris.feature_names)

"""
#只取出一些資料來測試
iris.data = iris.data[45:55]
iris.target = iris.target[45:55]
"""
"""
#自己建立10筆資料來測試
irisdata = [[5.1, 3.5, 1.4, 0.2],
            [4.9, 3.0, 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            [7.0, 3.2, 4.7, 1.4],
            [6.4, 3.2, 4.5, 1.5],
            [6.9, 3.1, 4.9, 1.5],
            [6.3, 2.5, 5.0, 1.9],
            [6.5, 3.0, 5.2, 2.0],
            [6.2, 3.4, 5.4, 2.3],
            [5.9, 3.0, 5.1, 1.8]]
iris.data = np.array(irisdata)
iristarget = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
iris.target = np.array(iristarget)
"""

print("所有資料 :")
# many print(iris)
print("資料集資料 :")
# many print(iris.data)
print("資料集目標/答案/target/y")
print(iris.target)

print("共有 :", len(X), "筆資料")

print("資料集目標名稱：")
print(iris.target_names)

print("鳶尾花資料集描述")
# many print(iris.DESCR)

print("特徵名稱(資料集欄位)：")
print(iris.feature_names)

print("filename :", iris.filename)
print("data_module :", iris.data_module)

print("keys")
print(iris.keys())

print("iris.data.shape :", X.shape)
print("iris.target.shape :", y.shape)

print("前幾筆資料內容：")
print(X[3:6])  # 第3~6筆資料
print(X[5])  # 第5筆資料
print(X[:5])  # 前5筆資料

print("------------------------------------------------------------")  # 60個

print("鳶尾花數據庫 基本數據 load_iris()轉df, 再看iris資料")

print("load_iris()轉df")
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=iris.feature_names)

print("觀察資料集彙總資訊")  # 了解行資料的標題與資料型別(整數、浮點數、字串等)
# many df.info()  # 這樣就已經把資料集彙總資訊印出來

print("描述統計量")
cc = df.describe()
# many print(cc)

M, N = df.shape
print("df之大小", M, "X", N)

print("iris 資料集欄名columns")
cc = df.columns
print(cc)

"""
# 印出一些資料
print("花萼長度")
print(df["sepal length (cm)"].head())
print("花萼寬度")
print(df["sepal width (cm)"].head())
print("花瓣長度")
print(df["petal length (cm)"].head())
print("花瓣寬度")
print(df["petal width (cm)"].head())
"""

print("------------------------------------------------------------")  # 60個

print("鳶尾花數據庫 基本數據 csv檔轉df, 再看iris資料")

print("讀取csv檔案成df 1")
filename = "data/iris_sample.csv"
df = pd.read_csv(filename)

print("資料")
# many print(df)

print("資料.shape :", df.shape)
print("資料.長度 :", len(df))
print("資料.head()")
print(df.head())

print("花萼長度資料 :")
print(df["花萼長度"])
print()
print("花萼長度資料長度 :", len(df["花萼長度"]))
print("花萼長度資料之第 0 筆資料 :", df["花萼長度"][0])

print("花萼長度 不同的數字 size :", np.unique(df["花萼長度"].values).size)
print("花萼寬度 不同的數字 size :", np.unique(df["花萼寬度"].values).size)
print("花瓣長度 不同的數字 size :", np.unique(df["花瓣長度"].values).size)
print("花瓣寬度 不同的數字 size :", np.unique(df["花瓣寬度"].values).size)

print("花萼長度 :", df["花萼長度"].values)
print("花萼寬度 :", df["花萼寬度"].values)
print("花瓣長度 :", df["花瓣長度"].values)
print("花瓣寬度 :", df["花瓣寬度"].values)

class1 = np.where(df["類別"] == "setosa", 1, 0)
print("抓出versicolor :", class1)
class2 = np.where(df["類別"] == "versicolor", 1, 0)
print("抓出versicolor :", class2)
class3 = np.where(df["類別"] == "virginica", 1, 0)
print("抓出versicolor :", class3)

color = ["r", "y", "b"]
species = ["Setosa", "Versicolour", "Virginica"]
Setosa = []
Versicolour = []
Virginica = []

print(df["花萼長度"])
print(len(df["花萼長度"]))

print(df["花萼長度"][0])

# 不同種類保存為不同的列表
for i in range(len(df)):
    if df["類別"][i] == "setosa":
        Setosa.append(1)
        Versicolour.append(0)
        Virginica.append(0)
    elif df["類別"][i] == "versicolor":
        Setosa.append(0)
        Versicolour.append(1)
        Virginica.append(0)
    elif df["類別"][i] == "virginica":
        Setosa.append(0)
        Versicolour.append(0)
        Virginica.append(1)

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

print("------------------------------")  # 30個

Setosa = []
Versicolour = []
Virginica = []

# 不同種類保存為不同的列表
for i in range(len(df)):
    if df["類別"][i] == "setosa":
        Setosa.append((df["花萼長度"][i], df["花萼寬度"][i], df["花瓣長度"][i], df["花瓣寬度"][i]))
    elif df["類別"][i] == "versicolor":
        Versicolour.append((df["花萼長度"][i], df["花萼寬度"][i], df["花瓣長度"][i], df["花瓣寬度"][i]))
    elif df["類別"][i] == "virginica":
        Virginica.append((df["花萼長度"][i], df["花萼寬度"][i], df["花瓣長度"][i], df["花瓣寬度"][i]))

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

plt.scatter(
    x=np.array(Setosa)[:, 0],  # Setosa種類的花瓣的長度
    y=np.array(Setosa)[:, 1],  # Setosa種類的花瓣的寬度
    s=80,
    c="red",
    label="Setosa",
)

plt.scatter(
    x=np.array(Versicolour)[:, 0],  # Versicolour種類的花瓣的長度
    y=np.array(Versicolour)[:, 1],  # Versicolour種類的花瓣的寬度
    s=50,
    c="green",
    label="Versicolour",
)

plt.scatter(
    x=np.array(Virginica)[:, 0],  # Virginica種類的花瓣的長度
    y=np.array(Virginica)[:, 1],  # Virginica種類的花瓣的寬度
    s=20,
    c="blue",
    label="Virginica",
)

# 添加軸標籤和標題
plt.title("花瓣長度 vs 花瓣寬度")
plt.xlabel("花瓣長度")
plt.ylabel("花瓣寬度")
plt.legend(loc="best")  # 添加圖例

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取csv檔案成df 2")
filename = "data/iris.csv"
df = pd.read_csv(filename)

# many print(df)

plt.scatter(x=df.petal_width, y=df.petal_length, color="r")
plt.xlabel("花瓣寬度")
plt.ylabel("花瓣長度")
plt.title("鳶尾花的花瓣寬度與長度關係")

show()

# pd畫散點圖Virginica
df.plot(x="petal_width", y="petal_length", kind="scatter", title="鳶尾花的花瓣寬度與長度關係")
plt.xlabel("花瓣寬度")
plt.ylabel("花瓣長度")

show()

# seaborn模塊繪制分組散點圖
sns.lmplot(
    x="petal_width",  # 指定x軸變量
    y="petal_length",  # 指定y軸變量
    hue="target",  # 指定分組變量
    data=df,  # 指定繪圖數據集
    legend_out=False,  # 將圖例呈現在圖框內
    truncate=True,  # 根據實際的數據範圍，對擬合線作截斷操作
)
plt.xlabel("花瓣寬度")
plt.ylabel("花瓣長度")
plt.title("鳶尾花的花瓣寬度與長度關係")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("load_iris()轉df")
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=iris.feature_names)
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

target = pd.DataFrame(y, columns=["target"])
y = target["target"]

colmap = np.array(["r", "g", "y"])

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.subplots_adjust(hspace=0.5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[y])
plt.xlabel("花萼長度(Sepal Length)")
plt.ylabel("花萼寬度(Sepal Width)")

plt.subplot(122)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

print("load_iris()轉df")
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=iris.feature_names)

target = pd.DataFrame(y, columns=["target"])
y = target["target"]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
XTrain, XTest, yTrain, yTest = train_test_split(df, y, test_size=0.2)
# 訓練組8成, 測試組2成

dtree = tree.DecisionTreeClassifier(max_depth=8)  # 決策樹函數學習機

dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print(dtree.predict(XTest))
print(yTest.values)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

print("load_iris()轉df")
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=iris.feature_names)

target = pd.DataFrame(y, columns=["target"])
y = target["target"]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
XTrain, XTest, yTrain, yTest = train_test_split(df, y, test_size=0.2)
# 訓練組8成, 測試組2成

dtree = tree.DecisionTreeClassifier(max_depth=8)  # 決策樹函數學習機

dtree.fit(XTrain, yTrain)

with open("tmp_tree2.dot", "w") as f:
    f = tree.export_graphviz(dtree, feature_names=iris.feature_names, out_file=f)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取csv檔案成df 3")
filename = "data/iris.csv"
df = pd.read_csv(filename)

# many print(df)

target_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])

plt.figure(figsize=(10, 5))

plt.subplot(121)
plt.subplots_adjust(hspace=0.5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length 花萼長")
plt.ylabel("Sepal Width 花萼寬")

plt.subplot(122)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length 花瓣長")
plt.ylabel("Petal Width 花瓣寬")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("load_iris()轉df")
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=iris.feature_names)

y = pd.DataFrame(y, columns=["Species"])
df = pd.concat([df, y], axis=1)

print(df.head())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

n_components = 2  # 削減後の次元を2に設定

clf = PCA(n_components=n_components)

clf = clf.fit(X)

X2 = clf.transform(X)
print(X2)  # 変換したデータ

print(X.shape)
print(X2.shape)

plt.subplot(121)
plt.plot(X[:, 0], c='r')
plt.plot(X[:, 1], c='g')
plt.plot(X[:, 2], c='b')
plt.plot(X[:, 3], c='c')

plt.subplot(122)
plt.plot(X2[:, 0], c='r')
plt.plot(X2[:, 1], c='g')
#plt.plot(X2[:, 2], c='b')
#plt.plot(X2[:, 3], c='c')

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

n_components = 3  # ガウス分布の數
clf = GaussianMixture(n_components=n_components)
clf.fit(X)
print(clf.predict(X))  # クラスを予測
print(clf.means_)  # 各ガウス分布の平均
print(clf.covariances_)  # 各ガウス分布の分散

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹 (decision tree)")

from sklearn.tree import DecisionTreeClassifier  # 決策樹函數學習機

X, y = datasets.load_iris(return_X_y=True)

print("鳶尾花花萼和花瓣數據")
print(X[0:5])
print(f"分類 : {y[0:5]}")

print(X[0])
print(y[0])

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

tree = DecisionTreeClassifier()  # 決策樹函數學習機

tree.fit(dx_train, dy_train)

predictions = tree.predict(dx_test)

print(tree.score(dx_train, dy_train))

print(tree.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("隨機森林 (random forest)")

from sklearn.ensemble import RandomForestClassifier

X, y = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train))

print(forest.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取csv檔案成df 4")
filename = "data/iris.csv"
df = pd.read_csv(filename)

# many print(df)

target_mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace=0.5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.subplot(1, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

show()

print("------------------------------------------------------------")  # 60個

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

print("讀取csv檔案成df 5")
filename = "data/iris.csv"
df = pd.read_csv(filename)

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:4].astype(float)
Y = to_categorical(dataset[:, 4])

scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

cc = model.summary()
print(cc)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=100, batch_size=5)

loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

Y_pred = np.argmax(model.predict(X_test), axis=-1)
print(Y_pred)

Y_target = dataset[:, 4][120:].astype(int)
print(Y_target)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("模型篩選特徵")

from sklearn import tree

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

clf = tree.DecisionTreeClassifier()  # 決策樹函數學習機

clf = clf.fit(X, y)

print(clf.feature_importances_)

print("------------------------------------------------------------")  # 60個

print("數學方法降維")

from sklearn.decomposition import PCA

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

df = pd.DataFrame(X, columns=["萼長", "萼寬", "瓣長", "瓣寬"])

mat = df.corr()
print(mat)

sns.heatmap(
    mat,
    annot=True,
    vmax=1,
    vmin=-1,
    xticklabels=True,
    yticklabels=True,
    square=True,
    cmap="gray",
)

show()

print("------------------------------")  # 30個

clf = PCA(n_components=2)

X2 = clf.fit_transform(df)

print(X2.shape)
plt.scatter(X2[:, 0], X2[:, 1], c=np.array(y), cmap=plt.cm.copper)

show()

print(clf.explained_variance_ratio_)
print(clf.explained_variance_ratio_.sum())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹")

from sklearn import tree  # 決策樹工具
import pydotplus  # 做圖工具
import io

iris = datasets.load_iris()
X = iris.data  # 獲取自變量??
y = iris.target  # 獲取因變量??  # 資料集目標

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = tree.DecisionTreeClassifier(max_depth=5)  # 決策樹函數學習機

clf.fit(X_train, y_train)  # 訓練模型

print("score:", clf.score(X_test, y_test))  # 模型打分

# 生成決策樹圖片
dot_data = io.StringIO()
tree.export_graphviz(
    clf,
    out_file=dot_data,
    feature_names=iris.feature_names,
    filled=True,
    rounded=True,
    impurity=False,
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

# fail
# open('a.jpg','wb').write(graph.create_jpg()) # 保存圖片

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("切分數據集與交叉驗證")

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# ????
X_train, X_test = train_test_split(X, test_size=0.2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取csv檔案成df 6")
filename = "data/Iris2.csv"
df = pd.read_csv(filename)

# print(df)

df = df.drop("Id", axis=1)
print(df.head())

# 資料清理
# 缺失值的補值或刪除
# 刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True)  # 將列索引重新編號

# 資料轉換

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
print(df.head())

# 探索性資料分析
# 觀察資料的分佈(統計)
print(df.head())

c = {0: "r", 1: "g", 2: "b"}
df["colors"] = df["Species"].map(c)
print(df)

df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (圖)-不同欄位和「類別(Species)」所繪製的散佈圖
# (a)花萼長度
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (b)花萼寬度
df.plot(kind="scatter", x="SepalWidthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (c)花瓣長度
df.plot(kind="scatter", x="PetalLengthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (d)花瓣寬度
df.plot(kind="scatter", x="PetalWidthCm", y="Species", c=df["colors"])
show()

print("------------------------------")  # 30個

# (圖)-2個欄位組合所繪製的散佈圖
# (a)花萼長度 vs. 花萼寬度
df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (b)花瓣長度 vs. 花瓣寬度
df.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (c)花萼長度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (d)花瓣長度 vs. 花萼寬度
df.plot(kind="scatter", x="PetalLengthCm", y="SepalWidthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (e)花萼長度 vs. 花瓣長度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalLengthCm", c=df["colors"])
show()

print("------------------------------")  # 30個

# (f)花萼寬度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalWidthCm", y="PetalWidthCm", c=df["colors"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


""" no clf
# 圖形化我們的成果

# 上次的成果拿回來使用

# 記得上次我們做了個鳶尾花分類器。
# 找回我們的分類器

from sklearn.externals import joblib

clf = joblib.load("iris_clf_01.pkl")

# 真的可以用了嗎?

print(clf.predict([[2, 3]]))

# 看看我們分類的全貌

# 我們用一下之前的方式, 畫出我們想要看到我們可愛的 SVM 是怎麼以花萼長度、花萼寬度來分類的。
# 上次我們用了 Python 所謂 "list comprehension" 的作法 (本質上是 for 迴圈), 現在我們換個方式看來比較「高級」的方式。

xt, yt = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-1, 1, 0.5))

print(xt)
print(yt)

# 看得出來 meshgrid 做了什麼呢? 基本上它就是說我們在 x, y 兩個指定範圍的長方型當中, 依我們指定的間隔找出格點。
# 這些格點的座標分成 x 座標一個 array, y 座標一個。x 或 y 座標的 array, 的座標是一列一列標記的。
# 要是你覺得這樣的表示法很討厭, 我們也可以讓它變一長串的向量。

print(xt.ravel())

# 注意這其實原來的 xt 並沒有變哦。

print(xt)

# 我們可以把 (x,y) 一點一點的座標收集起來嗎?

print(np.c_[xt.ravel(), yt.ravel()])


# 把資料的型式這樣變來變去會是數據分析非常非常常做的事情。
# 我們經這麼多廢話後終於可以來做正事。

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.2), np.arange(1.5, 5.0, 0.2))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z)
show()

# 快速換個配色

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.coolwarm, alpha=0.8)
show()


plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.prism, alpha=0.8)
show()

# 取回鳶尾花訓練資料
iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

x = X[:, :2]
y = iris.target  # 資料集目標

plt.subplot(121)

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.subplot(122)

plt.scatter(x[:, 0], x[:, 1], s=50, c=clf.predict(x))

show()

# 左邊的是訓練資料, 右邊是用我們 SVM 分類器分出來的。你有看出差異嗎?
# 是不是很難看出? 我們來用用另一個方式。

# 畫圖的另一個方式

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.02), np.arange(1.5, 5.0, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
show()

Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap=plt.cm.coolwarm)
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# knn_from_scratch_iris

# 自行開發KNN

# 公用函數


# 依筆數找出最大類別
def most_common(lst):
    return max(set(lst), key=lst.count)


# 歐幾里得距離(Euclidean distance)
def euclidean(point, data):
    return np.sqrt(np.sum((point - data) ** 2, axis=1))


# KNN 演算法


class KNN:
    def __init__(self, k=5, dist_metric=euclidean):
        self.k = k
        self.dist_metric = dist_metric

    # 指定訓練資料
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # 預測
    def predict(self, X_test):
        neighbors = []
        for x in X_test:
            # 計算距離
            distances = self.dist_metric(x, self.X_train)
            # 距離排序
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            # K個最近鄰
            neighbors.append(y_sorted[: self.k])

        # 找出最大類別
        return list(map(most_common, neighbors))

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = sum(y_pred == y_test) / len(y_test)
        return accuracy


X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = KNN()

clf.fit(X_train_std, y_train)

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# naive_bayes_from_scratch

# 自行開發高斯單純貝氏分類器

# NaiveBayes 演算法


# 貝氏定理 P(y|X) = P(X|y) * P(y) / P(X)
class NaiveBayesClassifier:
    # 計算常態分配的機率(pdf)：P(X)
    def gaussian_density(self, class_idx, x):
        """
        常態分配 pdf 公式:
        (1/√2pi*σ) * exp((-1/2)*((x-μ)^2)/(2*σ²))
        """
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp((-1 / 2) * ((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        prob = numerator / denominator
        return prob

    # 計算後驗機率 P(y|X)
    def calc_posterior(self, x):
        posteriors = []

        # 計算每一類的後驗機率 P(y|X)
        for i in range(self.count):
            # 使用 log 比較穩定
            prior = np.log(self.prior[i])
            conditional = np.sum(np.log(self.gaussian_density(i, x)))
            posterior = prior + conditional
            posteriors.append(posterior)

        # 傳回最大機率的類別
        return self.classes[np.argmax(posteriors)]

    # 訓練
    def fit(self, features, target):
        self.classes = np.unique(target)
        self.count = len(self.classes)
        self.feature_nums = features.shape[1]
        self.rows = features.shape[0]

        # 計算每個特徵的平均數、變異數
        data = np.concatenate((target.reshape(-1, 1), features), axis=1)
        self.mean = np.array(
            [np.mean(data[data[:, 0] == i, 1:], axis=0) for i in self.classes]
        )
        self.var = np.array(
            [np.var(data[data[:, 0] == i, 1:], axis=0) for i in self.classes]
        )
        # 計算先驗機率 P(y)
        self.prior = (
            np.array([target[target == i].shape[0] for i in self.classes]) / self.rows
        )

    # 預測
    def predict(self, features):
        preds = [self.calc_posterior(f) for f in features]
        return preds


X, y = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = NaiveBayesClassifier()

clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn_naive_bayes

# 以單純貝氏分類器進行鳶尾花(Iris)品種的辨識

X, y = datasets.load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 93.33%

# 使用伯努利單純貝氏分類器

from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 20.00%

# 使用多項單純貝氏分類器

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 80.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn AgglomerativeClustering
from sklearn.cluster import AgglomerativeClustering

# 繪製樹狀圖(dendrogram)
from scipy.cluster.hierarchy import dendrogram

# 使用鳶尾花資料集測試


# 繪製樹狀圖
def plot_dendrogram(model, **kwargs):
    # 計算每個集群的筆數
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # 繪製樹狀圖
    dendrogram(linkage_matrix, **kwargs)


X, y = datasets.load_iris(return_X_y=True)

# distance_threshold=0 表示會建立完整的樹狀圖(dendrogram)
clf = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

clf = clf.fit(X)  # 學習訓練.fit

plt.title("Hierarchical Clustering Dendrogram")
plot_dendrogram(clf, truncate_mode="level", p=3)  # 限制 3 層
plt.ylabel("歐幾里德距離")
plt.xlabel("每個集群的筆數")
show()

# 各種距離衡量方式的比較

from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

# Generate sample data
n_samples = 1500
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)

X = np.concatenate((x, y))
X += 0.7 * np.random.randn(2, n_samples)
X = X.T

# Create a graph capturing local connectivity. Larger number of neighbors
# will give more homogeneous clusters to the cost of computation
# time. A very large number of neighbors gives more evenly distributed
# cluster sizes, but may not impose the local manifold structure of
# the data
knn_graph = kneighbors_graph(X, 30, include_self=False)

for connectivity in (None, knn_graph):
    for n_clusters in (30, 3):
        plt.figure(figsize=(10, 4))
        for index, linkage in enumerate(("average", "complete", "ward", "single")):
            plt.subplot(1, 4, index + 1)
            clf = AgglomerativeClustering(
                linkage=linkage, connectivity=connectivity, n_clusters=n_clusters
            )
            t0 = time.time()
            clf.fit(X)  # 學習訓練.fit
            elapsed_time = time.time() - t0
            plt.scatter(X[:, 0], X[:, 1], c=clf.labels_, cmap=plt.cm.nipy_spectral)
            plt.title(
                "linkage=%s\n(time %.2fs)" % (linkage, elapsed_time),
                fontdict=dict(verticalalignment="top"),
            )
            plt.axis("equal")
            plt.axis("off")

            plt.subplots_adjust(bottom=0, top=0.89, wspace=0, left=0, right=1)
            plt.suptitle(
                "n_cluster=%i, connectivity=%r"
                % (n_clusters, connectivity is not None),
                size=17,
            )
            plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import scipy
from sklearn import cluster

iris = datasets.load_iris()
X = iris.data[:, :2]  # use only 'sepal length and sepal width'
y = iris.target  # 資料集目標

kmr = cluster.KMeans(n_clusters=3, random_state=42).fit(X)
labels_r = kmr.predict(X)

nboot = 500
orig_all = np.arange(X.shape[0])
scores_boot = np.zeros(nboot)
for boot_i in range(nboot):
    # boot_i = 43
    np.random.seed(boot_i)
    boot_idx = np.random.choice(orig_all, size=len(orig_all), replace=True)
    # boot_idx = orig_all
    kmb = cluster.KMeans(n_clusters=3, random_state=42).fit(X[boot_idx, :])
    dist = scipy.spatial.distance.cdist(kmb.cluster_centers_, kmr.cluster_centers_)
    reorder = np.argmin(dist, axis=1)
    # print(reorder)
    # kmb.cluster_centers_ = kmb.cluster_centers_[reorder]
    labels_b = kmb.predict(X)
    labels_b = np.array([reorder[lab] for lab in labels_b])
    scores_boot[boot_i] = np.sum(labels_b == labels_r) / len(labels_b)

sns.distplot(scores_boot)
show()

print(np.min(scores_boot), np.argmin(scores_boot))

pd.Series(scores_boot).describe(percentiles=[0.975, 0.5, 0.025])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 海生畫圖 畫 iris

"""
sns.pairplot()
pairplot:pair是成對的意思，即是說這個用來展現變量兩兩之間的關係，線性、非線性、相關等等
"""

# sns.set_style('white',{'font.sans-serif':['simhei','Arial']})  #解決中文不能顯示問題

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

iris_data = pd.DataFrame(X, columns=iris.feature_names)
iris_data["species"] = iris.target_names[y]

# NG iris_data.head(3).append(iris_data.tail(3))   #前面三條+后面三條
iris_data.rename(
    columns={
        "sepal length (cm)": "萼片長",
        "sepal width (cm)": "萼片寬",
        "petal length (cm)": "花瓣長",
        "petal width (cm)": "花瓣寬",
        "species": "種類",
    },
    inplace=True,
)
kind_dict = {"setosa": "山鳶尾", "versicolor": "雜色鳶尾", "virginica": "維吉尼亞鳶尾"}
iris_data["種類"] = iris_data["種類"].map(kind_dict)

# 畫變量之間關係的圖

# 全部變量都放進去
sns.pairplot(iris_data)
show()


"""
可以看到對角線上是各個屬性的直方圖（分布圖），而非對角線上是兩個不同屬性之間的相關圖，
從圖中我們發現，花瓣的長度和寬度之間以及萼片的長短和花瓣的長、寬之間具有比較明顯的相關關係
"""

# kind:用于控制非對角線上圖的類型，可選'scatter'與'reg'
# diag_kind:用于控制對角線上的圖分類型，可選'hist'與'kde'

sns.pairplot(iris_data, kind="reg", diag_kind="ked")
show()

sns.pairplot(iris_data, kind="reg", diag_kind="hist")
show()

# hue：針對某一字段進行分類
sns.pairplot(iris_data, hue="種類")
show()

"""
經過hue分類后的pairplot中發現，不論是從對角線上的分布圖還是從分類后的散點圖，
都可以看出對于不同種類的花，其萼片長、花瓣長、花瓣寬的分布差異較大，換句話說，
這些屬性是可以幫助我們去識別不同種類的花的。
比如，對于萼片、花瓣長度較短，花瓣寬度較窄的花，那么它大概率是山鳶尾
"""

# vars：研究某2個或者多個變量之間的關係vars,
# x_vars,y_vars：選擇數據中的特定字段，以list形式傳入需要注意的是，x_vars和y_vars要同時指定

sns.pairplot(iris_data, vars=["萼片長", "花瓣長"])
show()

sns.pairplot(iris_data, x_vars=["萼片長", "花瓣寬"], y_vars=["萼片寬", "花瓣長"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以下很久

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

category = 3
dim = 4

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

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

history = model.fit(x_train, y_train2, epochs=200, batch_size=128)  # 學習訓練.fit

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)  # 預測.predict
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)  # 預測.predict
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_show.py

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

category = 3
dim = 4

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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

history = model.fit(x_train, y_train2, epochs=200, batch_size=128)  # 學習訓練.fit

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:", score)

predict = model.predict(x_test)  # 預測.predict
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)  # 預測.predict
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
X = iris.data
y = iris.target  # 資料集目標

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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
    verbose=1)  # 學習訓練.fit

#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)  # 預測.predict
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)  # 預測.predict
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:",y_pred)
print("y_test",y_test[:])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_Save.py

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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
    verbose=1)  # 學習訓練.fit

#保存模型架構
with open("tmp_model_mlp.json", "w") as json_file:
   json_file.write(model.to_json())
#保存模型權重
model.save_weights("tmp_model_mlp.h5")


#測試
score = model.evaluate(x_test, y_test2, batch_size=128)
print("score:",score)

predict = model.predict(x_test)  # 預測.predict
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)  # 預測.predict
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:",y_pred)
print("y_test",y_test[:])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris-MLP_Load.py

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
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

predict = model.predict(x_test)  # 預測.predict
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)  # 預測.predict
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
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


""" 測試 df
df.to_csv("tmp_iris1.csv")
df.to_csv("tmp_iris2.csv", encoding="utf8")
df.to_csv("tmp_iris3.csv", encoding="utf-8-sig")
df.to_csv("tmp_iris4.csv", sep="\t")

print("讀取csv檔案成df 7")

df1 = pd.read_csv("tmp_iris1.csv")
print(df1)

df2 = pd.read_csv("tmp_iris2.csv")
print(df2)

df3 = pd.read_csv("tmp_iris3.csv")
print(df3)

print("比較df是否相同")
cc = df.equals(df1)
print(cc)
cc = df.equals(df2)
print(cc)
cc = df.equals(df3)
print(cc)
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
