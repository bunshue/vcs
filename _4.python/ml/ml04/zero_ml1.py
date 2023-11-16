import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_iris

data = load_iris()
X = pd.DataFrame(data.data, columns = data.feature_names)
y = pd.DataFrame(data.target, columns = ["Species"])
df = pd.concat([X, y], axis = 1)

print(df.head())

print('------------------------------------------------------------')	#60個

#學習分類
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()

X = data.data
y = data.target

X = X[:, :10]

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X, y)

y_pred = model.predict(X)

from sklearn.metrics import accuracy_score
accuracy_score(y, y_pred)

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_wine

data = load_wine()

X = data.data[:, [0, 9]]

from sklearn.cluster import KMeans
n_clusters = 3
model = KMeans(n_clusters = n_clusters)

pred = model.fit_predict(X)

fig, ax = plt.subplots()
ax.scatter(X[pred == 0, 0], X[pred == 0, 1], color = 'red', marker = 's', label = 'Label1')
ax.scatter(X[pred == 1, 0], X[pred == 1, 1], color = 'blue', marker = 's', label = 'Label2')
ax.scatter(X[pred == 2, 0], X[pred == 2, 1], color = 'green', marker = 's', label = 'Label3')
ax.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s = 200, color = 'yellow', marker = "*", label = "center")
ax.legend()
plt.title('wine')

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_wine

data = load_wine()

x3 = data.data[:, [0]]
y3 = data.data[:, [9]]

plt.subplot(121)
plt.scatter(x3, y3)
plt.title('wine')

plt.subplot(122)
plt.hist(y3, bins = 5)
plt.title('wine')

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_wine

data = load_wine()
df_X = pd.DataFrame(data.data, columns = data.feature_names)
print(df_X.head())

df_y = pd.DataFrame(data.target, columns = ["kind(target)"])
print(df_y.head())

df = pd.concat([df_X, df_y], axis = 1)
print(df.head())

plt.subplot(121)
plt.hist(df.loc[:, "alcohol"])

plt.subplot(122)
plt.boxplot(df.loc[:, "alcohol"])

plt.show()

print(df.corr())
print(df.describe())

print('------------------------------------------------------------')	#60個

print('使用 scatter_matrix')
from pandas.plotting import scatter_matrix

_ = scatter_matrix(df, figsize = (15, 15))
plt.show()

_ = scatter_matrix(df.iloc[:, [0, 9, -1]])
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.linear_model import LinearRegression

X = [[10.0], [8.0], [13.0], [9.0], [11.0], [14.0], [6.0], [4.0], [12.0], [7.0], [5.0]]
y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
model = LinearRegression()
model.fit(X, y) 
print(model.intercept_) # 切片 
print(model.coef_) # 傾き

y_pred = model.predict([[0], [1]]) 
print(y_pred) # x=0, x=1に対する予測結果

print('------------------------------------------------------------')	#60個

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

train_size = 20
test_size = 12
train_X = np.random.uniform(low=0, high=1.2, size=train_size)
test_X = np.random.uniform(low=0.1, high=1.3, size=test_size)
train_y = np.sin(train_X * 2 * np.pi) + np.random.normal(0, 0.2, train_size)
test_y = np.sin(test_X * 2 * np.pi) + np.random.normal(0, 0.2, test_size)
poly = PolynomialFeatures(6) # 次数は6
train_poly_X = poly.fit_transform(train_X.reshape(train_size, 1))
test_poly_X = poly.fit_transform(test_X.reshape(test_size, 1))
model = Ridge(alpha=1.0)
model.fit(train_poly_X, train_y)
train_pred_y = model.predict(train_poly_X)
test_pred_y = model.predict(test_poly_X)
print(mean_squared_error(train_pred_y, train_y))
print(mean_squared_error(test_pred_y, test_y))

print('------------------------------------------------------------')	#60個

from sklearn.linear_model import LogisticRegression

X_train = np.r_[np.random.normal(3, 1, size=50), np.random.normal(-1, 1, size=50)].reshape((100, -1))
y_train = np.r_[np.ones(50), np.zeros(50)]
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.predict_proba([[0], [1], [2]])[:, 1])

print('------------------------------------------------------------')	#60個

from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
centers = [(-1, -0.125), (0.5, 0.5)]
X, y = make_blobs(n_samples=50, n_features=2, centers=centers, cluster_std=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = LinearSVC() 
model.fit(X_train, y_train) # 学習
y_pred = model.predict(X_test) 
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個

from sklearn.svm import SVC
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_gaussian_quantiles(n_features=2, n_classes=2, n_samples=300)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))

print('------------------------------------------------------------')	#60個

from sklearn.naive_bayes import MultinomialNB

# データ生成
X_train = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]]
y_train = [1, 1, 1, 0, 0, 0]
model = MultinomialNB()
model.fit(X_train, y_train) # 学習
print(model.predict([[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]])) # 評価

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ読み込み
data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)
model = RandomForestClassifier() 
model.fit(X_train, y_train) # 学習
y_pred = model.predict(X_test) 
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ読み込み
data = load_digits()
X = data.images.reshape(len(data.images), -1)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = model = MLPClassifier(hidden_layer_sizes=(16, )) 
model.fit(X_train, y_train) # 学習
y_pred = model.predict(X_test) 
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train, y_train) # 学習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



