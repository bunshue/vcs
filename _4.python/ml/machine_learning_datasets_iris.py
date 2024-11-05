"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

花萼長度(Sepal.Length)
花萼寬度(Sepal.Width)
花瓣長度(Petal.Length)
花瓣寬度(Petal.Width)。
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
['setosa' 'versicolor' 'virginica']

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
print("------------------------------------------------------------")  # 60個
'''
from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
print("---------------------------")
print(iris.data.shape)
print("---------------------------")
print(iris.feature_names)
print("---------------------------")
print(iris.DESCR)

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#鳶尾花(Iris)品種的辨識
ds = datasets.load_iris()

"""
print("資料集說明")
print(ds.DESCR)

print("資料集欄位")
print(ds.feature_names)

print("資料集資料")
print(ds.data)

print("資料集目標名稱")
print(ds.target_names)

print("資料集目標")
print(ds.target)
"""

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(ds.data, columns=ds.feature_names)
# print(df)

""" 測試 df
df.to_csv("tmp_iris1.csv")
df.to_csv("tmp_iris2.csv", encoding="utf8")
df.to_csv("tmp_iris3.csv", encoding="utf-8-sig")


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

# 資料集目標
y = ds.target
# print(y)
# 資料集目標名稱
# print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

print("描述統計量")
cc = df.describe()
print(cc)

print("df之大小")
M, N = df.shape
print(df.shape)
print("df之大小", M, "X", N)

print("iris 資料集欄名columns")
cc = df.columns
print(cc)

print("花萼長度")
print(df["sepal length (cm)"].head())
print("花萼寬度")
print(df["sepal width (cm)"].head())
print("花瓣長度")
print(df["petal length (cm)"].head())
print("花瓣寬度")
print(df["petal width (cm)"].head())

# 箱型圖

sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
plt.show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
sns.countplot(x=y)
plt.title('y 各類別資料筆數統計')
plt.show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
# print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型評估

y_pred = clf.predict(X_test_std)
print("預測目標")
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
plt.show()

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_model.joblib")
joblib.dump(scaler, "tmp_scaler.joblib")

print("------------------------------------------------------------")  # 60個

import joblib

# 10.模型預測

# 載入模型與標準化轉換模型
clf = joblib.load("tmp_model.joblib")
scaler = joblib.load("tmp_scaler.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]
# 山鳶尾 變色鳶尾 維吉尼亞鳶尾

print("### 預測品種是：", labels[clf.predict(X_new)[0]])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#鳶尾花(Iris)品種的辨識
ds = datasets.load_iris()

"""
print("資料集說明")
print(ds.DESCR)

print("資料集欄位")
print(ds.feature_names)

print("資料集資料")
print(ds.data)

print("資料集目標名稱")
print(ds.target_names)

print("資料集目標")
print(ds.target)
"""

# 2. 資料清理、資料探索與分析

df = pd.DataFrame(ds.data, columns=ds.feature_names)
# print(df)

# 資料集目標
y = ds.target
# print(y)
# 資料集目標名稱
# print(ds.target_names)

print("觀察資料集彙總資訊")
cc = df.info()
print(cc)

print("描述統計量")
cc = df.describe()
print(cc)

# 集中
cc = (
    df["sepal length (cm)"].mean(),
    df["sepal length (cm)"].median(),
    df["sepal length (cm)"].mode(),
)
print(cc)

# 計算變異數(variance)、標準差(standard deviation)、IQR
cc = (
    df["sepal length (cm)"].var(),
    df["sepal length (cm)"].std(),
    df["sepal length (cm)"].quantile(0.75) - df["sepal length (cm)"].quantile(0.25),
)

print(cc)

# (0.6856935123042505, 0.8280661279778629, 1.3000000000000007)

# 計算偏態(skewness)及峰度(kurtosis)
cc = df["sepal length (cm)"].skew(), df["sepal length (cm)"].kurt()
print(cc)

# 自行計算偏態
mean1 = df["sepal length (cm)"].mean()
std1 = df["sepal length (cm)"].std()
n = len(df["sepal length (cm)"])
skew1 = (
    (((df["sepal length (cm)"] - mean1) / std1) ** 3).sum() * n / ((n - 1) * (n - 2))
)
print(skew1)

# 0.31491095663697277

# 自行計算峰度
M2 = (((df["sepal length (cm)"] - mean1) / std1) ** 2).mean()
M4 = (((df["sepal length (cm)"] - mean1) / std1) ** 4).mean()
K = M4 / (M2**2)
print(K - 3)

# -0.5735679489249756

from scipy.stats import kurtosis

print(kurtosis(df["sepal length (cm)"], axis=0, bias=True))

# -0.5735679489249765

# 直方圖
sns.histplot(x="sepal length (cm)", data=df)
plt.show()

# 直方圖平滑化
sns.kdeplot(x="sepal length (cm)", data=df)
plt.show()

# 右偏

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(5, 1, 100)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

# 右偏

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 500)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
plt.show()

# 關聯度

df["y"] = y
cc = df.corr()
print(cc)

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
plt.show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")

sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
plt.show()

print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
# 訓練資料, 測試資料, 訓練目標, 測試目標
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 8成訓練 2成測試

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("訓練目標")
# print(y_train)

print("測試目標")
print(y_test)

print("特徵縮放")

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型評估

y_pred = clf.predict(X_test_std)
print("預測目標")
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
plt.show()

# 8. 模型評估，暫不進行

# 9. 模型佈署

# 模型存檔
import joblib

joblib.dump(clf, "tmp_model.joblib")
joblib.dump(scaler, "tmp_scaler.joblib")

print("------------------------------------------------------------")  # 60個

import joblib

# 10.模型預測

# 載入模型與標準化轉換模型
clf = joblib.load("tmp_model.joblib")
scaler = joblib.load("tmp_scaler.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
""" NG
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]

print("### 預測品種是：", labels[clf.predict(X_new)[0]])
"""

""" 使用 streamlit 與人互動

import streamlit as st

# 設定 st 標題
st.title('鳶尾花（Iris）預測')

# 製作4個 st slider
sepal_length = st.slider('花萼長度:', min_value=3.0, max_value=8.0, value=5.8)
sepal_width = st.slider('花萼寬度:', min_value=2.0, max_value=5.0, value=3.5)
petal_length = st.slider('花瓣長度:', min_value=1.0, max_value=7.0, value=4.4)
petal_width = st.slider('花瓣寬度:', min_value=0.1, max_value=2.5, value=1.3)

if st.button('預測'):  # 當按下 預測 按鈕
    X_new = [[sepal_length,sepal_width,petal_length,petal_width]]
    X_new = scaler.transform(X_new)
    st.write('### 預測品種是：', labels[clf.predict(X_new)[0]])
"""

'''
print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["sepal_length"], X["sepal_width"], color=colmap[y])
plt.xlabel("花萼長度(Sepal Length)")
plt.ylabel("花萼寬度(Sepal Width)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)
k = 3

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

print("準確率:", knn.score(XTest, yTest))
print("---------------------------")
print(knn.predict(XTest))
print("---------------------------")
print(yTest.values)

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

Ks = np.arange(1, round(0.2*len(XTrain) + 1))
accuracies=[]
for k in Ks:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    accuracy = knn.score(XTest, yTest)
    accuracies.append(accuracy)
    
plt.plot(Ks, accuracies)

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import neighbors 
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

Ks = np.arange(1, round(0.2*len(X) + 1))
accuracies=[]
for k in Ks:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, scoring="accuracy",
                            cv=10)
    accuracies.append(scores.mean())

plt.plot(Ks, accuracies)

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print(kmeans.labels_)
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("真實分類(Real Classification)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[kmeans.labels_])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("K-means分類(K-means Classification)")

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
print("K-means分類(K-means Classification):")
print(kmeans.labels_)
# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [2,0,1]).astype(np.int64)
print("K-means修正分類(K-means Fix Classification):")
print(pred_y) 
print("真實分類(Real Classification):")
print(y)

colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(X["petal_length"], X["petal_width"],
            color=colmap[y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("真實分類(Real Classification)")
plt.subplot(1, 2, 2)
plt.scatter(X["petal_length"], X["petal_width"], 
            color=colmap[pred_y])
plt.xlabel("花瓣長度(Petal Length)")
plt.ylabel("花瓣寬度(Petal Width)")
plt.title("K-means分類(K-means Classification)")

plt.show()

print("------------------------------------------------------------")  # 60個

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import cluster
import sklearn.metrics as sm

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length","sepal_width","petal_length","petal_width"]
y = iris.target
k = 3

kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
# 修正標籤錯誤
pred_y = np.choose(kmeans.labels_, [2,0,1]).astype(np.int64)
# 績效矩陣
print(sm.accuracy_score(y, pred_y))
print("---------------------------")
# 混淆矩陣
print(sm.confusion_matrix(y, pred_y))


print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier(max_depth = 8)
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
print(dtree.predict(XTest))
print("---------------------------")
print(yTest.values)

print("------------------------------------------------------------")  # 60個

import pandas as pd
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier(max_depth = 8)
dtree.fit(XTrain, yTrain)

with open("tmp_tree2.dot", "w") as f:
    f = tree.export_graphviz(dtree,
                             feature_names=iris.feature_names,
                             out_file=f)

print("------------------------------------------------------------")  # 60個


df = pd.read_csv('data/iris.csv')

print(df.shape)

print(df.head(5))

print(df.describe())

target_mapping = {"setosa": 0,
          "versicolor": 1,
          "virginica": 2}
Y = df["target"].map(target_mapping)
colmap = np.array(["r", "g", "y"])
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.subplots_adjust(hspace = .5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length 花萼長")
plt.ylabel("Sepal Width 花萼寬")

plt.subplot(122)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length 花瓣長")
plt.ylabel("Petal Width 花瓣寬")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris

data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=["Species"])
df = pd.concat([X, y], axis=1)

print(df.head())

print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
n_components = 2  # 削減後の次元を2に設定
model = PCA(n_components=n_components)
model = model.fit(data.data)
print(model.transform(data.data))  # 変換したデータ

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

data = load_iris()
n_clusters = 3  # クラスタ数を3に設定
model = KMeans(n_clusters=n_clusters)
model.fit(data.data)
print(model.labels_)  # 各データ点が所属するクラスタ
print(model.cluster_centers_)  # fit()によって計算された重心

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

data = load_iris()
n_components = 3  # ガウス分布の数
model = GaussianMixture(n_components=n_components)
model.fit(data.data)
print(model.predict(data.data))  # クラスを予測
print(model.means_)  # 各ガウス分布の平均
print(model.covariances_)  # 各ガウス分布の分散

print("------------------------------------------------------------")  # 60個

# 決策樹 (decision tree)

from sklearn.datasets import load_iris

dx, dy = load_iris(return_X_y=True)

print(dx[0])
print(dy[0])

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

dx, dy = load_iris(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

tree = DecisionTreeClassifier()

tree.fit(dx_train, dy_train)

predictions = tree.predict(dx_test)

print(tree.score(dx_train, dy_train))

print(tree.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個

# 隨機森林 (random forest)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_iris(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train))

print(forest.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
