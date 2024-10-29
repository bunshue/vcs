"""
Iris 的

"""

# import keras

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
"""
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

plt.subplot(1, 2, 1)
plt.subplots_adjust(hspace = .5)
plt.scatter(df["sepal_length"], df["sepal_width"], color=colmap[Y])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.subplot(1, 2, 2)
plt.scatter(df["petal_length"], df["petal_width"], color=colmap[Y])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.show()
"""
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
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
