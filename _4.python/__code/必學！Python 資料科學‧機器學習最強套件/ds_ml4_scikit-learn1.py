"""

必學！Python 資料科學‧機器學習最強套件 scikit-learn 1

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

#12-2-1 產生測試資料

from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples=10, n_features=2, centers=2, random_state=0)

print(x)
print(y)

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2,random_state=0)

plt.scatter(dx.T[0], dx.T[1], c=dy, cmap='Dark2')

plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import make_blobs

from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2,random_state=0)

dx_std = StandardScaler().fit_transform(dx)

plt.scatter(dx_std.T[0], dx_std.T[1], c=dy, cmap='Dark2')

plt.grid(True)

plt.show()

print('------------------------------------------------------------')	#60個

#12-2-2 分割訓練資料集和測試資料集

from sklearn.datasets import make_blobs

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2,random_state=0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy, test_size=0.2, random_state=0)

print(dx.shape)

print(dx_train.shape)

print(dx_test.shape)

print(dy.shape)

print(dy_train.shape)

print(dy_test.shape)

print('------------------------------------------------------------')	#60個

#12-3-1 k 最近鄰演算法 (KNN)

from sklearn.datasets import make_blobs

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2, random_state=0)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(dx_train, dy_train)

predictions = knn.predict(dx_test)

print(dy_test)

print(predictions)

print(knn.score(dx_train, dy_train))

print(knn.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-3-2 邏輯斯迴歸 (logistic regression)

from sklearn.datasets import make_blobs

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2,random_state=0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2, random_state=0)

log_reg = LogisticRegression()

log_reg.fit(dx_train, dy_train)

predictions = log_reg.predict(dx_test)

print(log_reg.score(dx_train, dy_train))

print(log_reg.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-3-3 線性支援向量機 (Linear SVM)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

dx, dy = make_blobs(n_samples=500, n_features=2, centers=2,random_state=0)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2, random_state=0)

linear_svm = LinearSVC()

linear_svm.fit(dx_train, dy_train)

predictions = linear_svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))

print(linear_svm.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-3-4 非線性 SVM

from sklearn.datasets import make_moons

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

from sklearn.svm import LinearSVC, SVC

dx, dy = make_moons(n_samples=500, noise=0.15, random_state=0)

dx_train, dx_test, dy_train, dy_test = \
      train_test_split(StandardScaler().fit_transform(dx),dy, test_size=0.2, random_state=0)

linear_svm = LinearSVC()

linear_svm.fit(dx_train, dy_train)

predictions = linear_svm.predict(dx_test)

svm = SVC()

svm.fit(dx_train, dy_train)

predictions = svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))

print(linear_svm.score(dx_test, dy_test))

print(svm.score(dx_train, dy_train))

print(svm.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-3-5 決策樹 (decision tree)

from sklearn.datasets import load_iris

dx, dy = load_iris(return_X_y=True)

print(dx[0])
print(dy[0])

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

dx, dy = load_iris(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy, test_size=0.2, random_state=0)

tree = DecisionTreeClassifier()

tree.fit(dx_train, dy_train)

predictions = tree.predict(dx_test)

print(tree.score(dx_train, dy_train))

print(tree.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-3-6 隨機森林 (random forest)

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

dx, dy = load_iris(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size=0.2, random_state=0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train))

print(forest.score(dx_test, dy_test))

print('------------------------------------------------------------')	#60個

#12-4-1 k-fold 交叉驗證法

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_wine(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2, random_state=0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

val_score = cross_val_score(forest, dx_train, dy_train, cv=5)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(val_score.mean().round(3))

print(forest.score(dx_test, dy_test) .round(3))

print('------------------------------------------------------------')	#60個

#12-4-2 產生預測結果報告

from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report

dx, dy = load_wine(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy,test_size=0.2, random_state=0)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(forest.score(dx_test, dy_test).round(3))

print(classification_report(dy_test, predictions))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


