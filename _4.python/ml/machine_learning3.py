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
poly = PolynomialFeatures(6) # 次數は6
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
model.fit(X_train, y_train) # 學習
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
model.fit(X_train, y_train) # 學習
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
model.fit(X_train, y_train) # 學習
y_pred = model.predict(X_test) 
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個
"""


print("------------------------------------------------------------")  # 60個

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train, y_train)  # 學習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import TruncatedSVD

data = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]
n_components = 2  # 潜在変数の数
model = TruncatedSVD(n_components=n_components)
model.fit(data)
print(model.transform(data))  # 変換したデータ
print(model.explained_variance_ratio_)  # 寄与率
print(sum(model.explained_variance_ratio_))  # 累積寄与率

print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import NMF

# from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

centers = [[5, 10, 5], [10, 4, 10], [6, 8, 8]]
X, _ = make_blobs(centers=centers)  # centersを中心としたデータを生成
n_components = 2  # 潜在変数の数
model = NMF(n_components=n_components)
model.fit(X)
W = model.transform(X)  # 分解後の行列
H = model.components_
print(W)
print(H)

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# removeで本文以外の情報を取り除く
data = fetch_20newsgroups(remove=("headers", "footers", "quotes"))
max_features = 1000
# 文書 データをベクトルに変換
tf_vectorizer = CountVectorizer(max_features=max_features, stop_words="english")
tf = tf_vectorizer.fit_transform(data.data)
n_topics = 20
model = LatentDirichletAllocation(n_components=n_topics)
model.fit(tf)
print(model.components_)  # 各トピックが持つ単語分布
print(model.transform(tf))  # トピックで表現された文書

print("------------------------------------------------------------")  # 60個

""" import fail
from sklearn.datasets import samples_generator
from sklearn.manifold import LocallyLinearEmbedding

data, color = samples_generator.make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍点の数 
n_components = 2 # 削減後の次元数
model = LocallyLinearEmbedding(n_neighbors=n_neighbors,
n_components=n_components)
model.fit(data)
print(model.transform(data)) # 変換したデータ
"""

print("------------------------------------------------------------")  # 60個

from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

data = load_digits()
n_components = 2  # 削減後の次元を2に設定
model = TSNE(n_components=n_components)
print(model.fit_transform(data.data))

print("------------------------------------------------------------")  # 60個

# 分類問題における評価方法
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data
y = 1 - data.target
# ラベルの0と1を反転

X = X[:, :10]
from sklearn.linear_model import LogisticRegression

model_lor = LogisticRegression()
model_lor.fit(X, y)
y_pred = model_lor.predict(X)

print("------------------------------------------------------------")  # 60個

print("混同行列")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y, y_pred)
print(cm)

print("------------------------------------------------------------")  # 60個

print("正解率")
from sklearn.metrics import accuracy_score

accuracy_score(y, y_pred)

print("------------------------------------------------------------")  # 60個

print("適合率")
from sklearn.metrics import precision_score

precision_score(y, y_pred)

print("------------------------------------------------------------")  # 60個

print("再現率")
from sklearn.metrics import recall_score

recall_score(y, y_pred)

print("------------------------------------------------------------")  # 60個

print("F値")
from sklearn.metrics import f1_score

f1_score(y, y_pred)

print("------------------------------------------------------------")  # 60個

print("予測確率")
model_lor.predict_proba(X)

print("------------------------------------------------------------")  # 60個

y_pred2 = (model_lor.predict_proba(X)[:, 1] > 0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print("------------------------------------------------------------")  # 60個

print("ROC曲線・AUC")
from sklearn.metrics import roc_curve

probas = model_lor.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print("------------------------------------------------------------")  # 60個

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, "gray")
ax.fill_between(fpr, tpr, 0, color="skyblue", alpha=0.8)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_facecolor("xkcd:white")
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import roc_auc_score

roc_auc_score(y, probas[:, 1])

print("------------------------------------------------------------")  # 60個

print("平均二乗誤差")

from sklearn.metrics import mean_squared_error

mean_squared_error(y, y_pred)

print("------------------------------------------------------------")  # 60個
print("決定係数")

from sklearn.metrics import r2_score

print(r2_score(y, y_pred))

print("------------------------------------------------------------")  # 60個

print("異なるアルゴリズムを利用した場合との比較")

from sklearn.svm import SVR

model_svr_linear = SVR(C=0.01, kernel="linear")
model_svr_linear.fit(X, y)
y_svr_pred = model_svr_linear.predict(X)
print(y_svr_pred)

"""
fig, ax = plt.subplots()
ax.scatter(X, y, color='pink', marker='s', label='data set')
ax.plot(X, y_pred, color='blue', label='regression curve')
ax.plot(X, y_svr_pred, color='red', label='SVR')
ax.legend()
plt.show()
"""

print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数
print(model_svr_linear.coef_)  # 傾き
print(model_svr_linear.intercept_)  # 切片

print("------------------------------------------------------------")  # 60個

print("ハイパーパラメータの設定")

model_svr_rbf = SVR(C=1.0, kernel="rbf")
model_svr_rbf.fit(X, y)
y_svr_pred = model_svr_rbf.predict(X)
print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]
model_svr_rbf_1 = SVR(C=1.0, kernel="rbf")
model_svr_rbf_1.fit(train_X, train_y)
test_y_pred = model_svr_rbf_1.predict(test_X)
print(mean_squared_error(test_y, test_y_pred))  # 平均二乗誤差
print(r2_score(test_y, test_y_pred))  # 決定係数

print("------------------------------------------------------------")  # 60個

print("学習データと検証データに分割")

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data
y = data.target
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.svm import SVC

model_svc = SVC()
model_svc.fit(X_train, y_train)
y_train_pred = model_svc.predict(X_train)
y_test_pred = model_svc.predict(X_test)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

from sklearn.ensemble import RandomForestClassifier

model_rfc = RandomForestClassifier()
model_rfc.fit(X_train, y_train)
y_train_pred = model_rfc.predict(X_train)
y_test_pred = model_rfc.predict(X_test)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

print("------------------------------------------------------------")  # 60個

print("交差検証（クロスバリデーション）")

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True)
model_rfc_1 = RandomForestClassifier()
cross_val_score(model_rfc_1, X, y, cv=cv, scoring="accuracy")

cross_val_score(model_rfc_1, X, y, cv=cv, scoring="f1")

print("------------------------------------------------------------")  # 60個

print("ハイパーパラメータの探索")

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data
y = 1 - data.target  # ラベルの0と1を反転
X = X[:, :10]

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True)
param_grid = {"max_depth": [5, 10, 15], "n_estimators": [10, 20, 30]}
model_rfc_2 = RandomForestClassifier()
grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring="accuracy")
grid_search.fit(X, y)

print(grid_search.best_score_)
print(grid_search.best_params_)

grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring="f1")

print("------------------------------------------------------------")  # 60個

print("機械学習モデルへの適用")

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups

categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]
remove = ("headers", "footers", "quotes")
twenty_train = fetch_20newsgroups(
    subset="train", remove=remove, categories=categories
)  # 学習データ
twenty_test = fetch_20newsgroups(
    subset="test", remove=remove, categories=categories
)  # 検証データ

count_vect = CountVectorizer()  # 単語カウント
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_test_count = count_vect.transform(twenty_test.data)

model = LinearSVC()
model.fit(X_train_counts, twenty_train.target)
predicted = model.predict(X_test_count)
np.mean(predicted == twenty_test.target)

tf_vec = TfidfVectorizer()  # tf-idf
X_train_tfidf = tf_vec.fit_transform(twenty_train.data)
X_test_tfidf = tf_vec.transform(twenty_test.data)

model = LinearSVC()
model.fit(X_train_tfidf, twenty_train.target)
predicted = model.predict(X_test_tfidf)
np.mean(predicted == twenty_test.target)

print("------------------------------------------------------------")  # 60個

# 変換後のベクトルデータを入力として機械学習モデルを適用する

from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

model = RandomForestClassifier(n_estimators=10)

model.fit(data[: n_samples // 2], digits.target[: n_samples // 2])

expected = digits.target[n_samples // 2 :]
predicted = model.predict(data[n_samples // 2 :])

print(metrics.classification_report(expected, predicted))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("產生測試資料 並畫出")

from sklearn.datasets import make_blobs

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

print(dx.shape)
print(dy.shape)
# print(dx)
# print(dy)

plt.scatter(dx.T[0], dx.T[1], c=dy, cmap="Dark2")
plt.title("dx的分佈狀況, dy是用顏色表示")
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個

# StandardScaler
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

dx_std = StandardScaler().fit_transform(dx)

plt.scatter(dx_std.T[0], dx_std.T[1], c=dy, cmap="Dark2")
plt.grid(True)

plt.show()

# 分割訓練資料集和測試資料集
from sklearn.model_selection import train_test_split

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

print(dx.shape)
print(dx_train.shape)
print(dx_test.shape)

print(dy.shape)
print(dy_train.shape)
print(dy_test.shape)

# k 最近鄰演算法 (KNN)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(dx_train, dy_train)
predictions = knn.predict(dx_test)

print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

sys.exit()

print("------------------------------------------------------------")  # 60個

# 邏輯斯迴歸 (logistic regression)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print("產生500筆資料 2維 2群")
dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

log_reg = LogisticRegression()
log_reg.fit(dx_train, dy_train)
predictions = log_reg.predict(dx_test)

print(log_reg.score(dx_train, dy_train))
print(log_reg.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個

# 線性支援向量機 (Linear SVM)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

print("產生500筆資料 2維 2群")
dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

linear_svm = LinearSVC()
linear_svm.fit(dx_train, dy_train)
predictions = linear_svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))
print(linear_svm.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個

# 非線性 SVM

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

dx, dy = make_moons(n_samples=500, noise=0.15, random_state=0)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    StandardScaler().fit_transform(dx), dy, test_size=0.2, random_state=0
)

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

print("------------------------------------------------------------")  # 60個

# k-fold 交叉驗證法

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_wine(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

val_score = cross_val_score(forest, dx_train, dy_train, cv=5)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(val_score.mean().round(3))

print(forest.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個

# 產生預測結果報告

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

dx, dy = load_wine(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(forest.score(dx_test, dy_test).round(3))

print(classification_report(dy_test, predictions))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 13-1-1 最近 k 鄰數量：n_neighbors

from sklearn.datasets import load_breast_cancer  # 匯入資料集
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt  # 匯入 matplotlib

# 取得特徵與標籤資料

dx, dy = load_breast_cancer(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

cv_scores = []  # 用來收集交叉驗證準確率的 list

test_scores = []  # 用來收集測試集準確率的 list

x = np.arange(10) + 1  # 圖表 X 軸 (KNN 模型的 k 值)

for k in x:
    knn = KNeighborsClassifier(n_neighbors=k).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(knn, dx_train, dy_train, cv=5).mean())
    test_scores.append(knn.score(dx_test, dy_test))

plt.title("KNN hyperparameter")
plt.plot(x, cv_scores, label="CV score")  # 繪製交叉驗證折線圖
plt.plot(x, test_scores, label="Test score")  # 繪製測試集預測折線圖
plt.xlabel("k neighbors")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

# 13-1-2 用 GridSearchCV 自動搜尋最佳 k 值

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

param_grid = {"n_neighbors": np.arange(10) + 1}  # 要網格搜尋的參數
model = GridSearchCV(KNeighborsClassifier(), param_grid)
model.fit(dx_train, dy_train)  # 用最佳模型來做訓練

print("Best params:", model.best_params_)  # 傳回最佳參數
print("CV score:", model.best_score_.round(3))
print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個

# 13-2-1 邏輯斯迴歸的 C：常規化強度

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)  # 資料標準化
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

cv_scores = []
test_scores = []

x = [10**n for n in range(-4, 5)]

x_str = [str(n) for n in x]  # X 軸各數值『名稱』

for c in x:
    log_reg = LogisticRegression(C=c, max_iter=1000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(log_reg, dx_train, dy_train, cv=5).mean())
    test_scores.append(log_reg.score(dx_test, dy_test))

plt.title("Logistic Regression hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("C")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個

# 13-2-2 線性 SVC 的 C：常規化強度

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

cv_scores = []
test_scores = []

x = [10**n for n in range(-4, 5)]
x_str = [str(n) for n in x]

for c in x:
    linear_svc = LinearSVC(C=c, max_iter=10000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(linear_svc, dx_train, dy_train, cv=5).mean())
    test_scores.append(linear_svc.score(dx_test, dy_test))

plt.title("Linear SVM hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("C")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

# 13-3-1 C, gamma 與 kernel 參數

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

x = [10**n for n in range(-2, 3)]

param_grid = {"C": x, "gamma": x, "kernel": ["linear", "rbf", "poly", "sigmoid"]}

model = GridSearchCV(SVC(), param_grid)
model.fit(dx_train, dy_train)

print("Best params: ", model.best_params_)
print("CV score:", model.best_score_.round(3))
print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個

# 13-3-2 使用 RandomizedSearchCV 更快速尋找較適當的參數

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

param_grid = {
    "C": np.linspace(1, 100, 100),
    "gamma": np.linspace(0.01, 1, 100),
    "kernel": ["linear", "rbf", "poly", "sigmoid"],
}

model = RandomizedSearchCV(SVC(), param_grid, n_iter=100)
model.fit(dx_train, dy_train)

print("Best params:", model.best_params_)
print("CV score:", model.best_score_.round(3))
print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個

# 13-4-1 決策樹的最大深度：max_depth

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

cv_scores = []

test_scores = []

x = np.arange(12) + 1

x_str = [str(n) for n in x]

for d in x:
    tree = DecisionTreeClassifier(max_depth=d).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(tree, dx_train, dy_train, cv=5).mean())
    test_scores.append(tree.score(dx_test, dy_test))

plt.title("Decision Tree hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("Max depth")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

dx, dy = load_breast_cancer(return_X_y=True)
feature_names = list(load_breast_cancer().feature_names)

dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

model = DecisionTreeClassifier(max_depth=3).fit(dx_train, dy_train)

print(export_text(model, feature_names=feature_names))

print("------------------------------------------------------------")  # 60個

# 13-4-2 隨機森林的規模 n_estimators 與亂數種子 random_state

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

cv_scores = []
test_scores = []

x = (np.arange(10) + 1) * 50
x_str = [str(n) for n in x]

for t in x:
    tree = RandomForestClassifier(n_estimators=t, max_depth=3, random_state=0)
    tree.fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(tree, dx_train, dy_train, cv=5).mean())
    test_scores.append(tree.score(dx_test, dy_test))

plt.title("Random Forest hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("Number of trees")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
