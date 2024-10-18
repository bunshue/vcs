"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

"""

from sklearn import datasets

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
import nltk
nltk.download('wordnet')
"""
print("------------------------------------------------------------")  # 60個

# SelectFromModel

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import SVC

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print("X.shape")
print(cc)

# SelectFromModel特徵選取

svc = SVC(kernel="linear", C=1)
clf = SelectFromModel(estimator=svc, threshold="mean")
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print("X_new.shape")
print(cc)

print("特徵是否被選取")
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

print("選擇2個特徵")
X = X_new

print("資料分割")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
# ((120, 2), (30, 2), (120,), (30,))

print("特徵縮放")
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

print("計算準確率")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.67%

from sklearn.metrics import confusion_matrix

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import ConfusionMatrixDisplay
print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

print("使用全部特徵")

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# (120, 4) (30, 4) (120,) (30,)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

print("模型計分")
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 順序特徵選取(Sequential Feature Selection)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.svm import SVC

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)
cc = X.shape
print(cc)

# SFS 特徵選取
svc = SVC(kernel="linear", C=1)
clf = SequentialFeatureSelector(estimator=svc, n_features_to_select=2)
X_new = clf.fit_transform(X, y)
cc = X_new.shape
print(cc)

# 特徵是否被選取
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 86.67%

from sklearn.metrics import confusion_matrix

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import ConfusionMatrixDisplay
print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

print("使用全部特徵")

# 載入資料集
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 實現PCA演算法

# 建立測試資料

# 固定隨機種子
np.random.seed(2342347)

# 第一個類別
mu_vec1 = np.array([0, 0, 0])  # 平均數
cov_mat1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

# 第二個類別
mu_vec2 = np.array([1, 1, 1])  # 平均數
cov_mat2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 共變異矩陣
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T

cc = class1_sample.shape, class2_sample.shape
print(cc)

# 繪圖

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot(
    class1_sample[0, :],
    class1_sample[1, :],
    class1_sample[2, :],
    "o",
    markersize=8,
    color="blue",
    alpha=0.5,
    label="類別1",
)
ax.plot(
    class2_sample[0, :],
    class2_sample[1, :],
    class2_sample[2, :],
    "^",
    markersize=8,
    alpha=0.5,
    color="red",
    label="類別2",
)

plt.title("測試資料")
ax.legend(loc="upper right")

plt.show()

# 合併資料

all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
cc = all_samples.shape
print(cc)

# 計算共變異數矩陣(covariance matrix)

cov_mat = np.cov([all_samples[0, :], all_samples[1, :], all_samples[2, :]])
print("共變異數矩陣:\n", cov_mat)

# 計算特徵向量(eigenvector)及對應的特徵值(eigenvalue, λ)

# 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
eig_val_sc, eig_vec_sc = np.linalg.eig(cov_mat)
print("特徵向量:\n", eig_vec_sc)
print("特徵值:\n", eig_val_sc)

# 繪製特徵向量

from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch


# 繪製箭頭
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


# 設定 3D 繪圖
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# 繪製特徵向量
ax.plot(
    all_samples[0, :],
    all_samples[1, :],
    all_samples[2, :],
    "o",
    markersize=8,
    color="green",
    alpha=0.2,
)
[mean_x, mean_y, mean_z] = np.mean(all_samples, axis=1)
ax.plot([mean_x], [mean_y], [mean_z], "o", markersize=10, color="red", alpha=0.5)
for v in eig_vec_sc.T:
    a = Arrow3D(
        [mean_x, v[0]],
        [mean_y, v[1]],
        [mean_z, v[2]],
        mutation_scale=20,
        lw=3,
        arrowstyle="-|>",
        color="r",
    )
    ax.add_artist(a)
ax.set_xlabel("x_values")
ax.set_ylabel("y_values")
ax.set_zlabel("z_values")

plt.show()

# 合併特徵向量及特徵值，針對特徵值降冪排序，挑出前2名。

# 合併特徵向量及特徵值
eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:, i]) for i in range(len(eig_val_sc))]

# 針對特徵值降冪排序
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# 挑出前2名
for i in eig_pairs[:2]:
    print(i[1])

# 座標轉換矩陣

matrix_w = np.hstack((eig_pairs[0][1].reshape(3, 1), eig_pairs[1][1].reshape(3, 1)))
print("Matrix W:\n", matrix_w)

# 原始資料乘以轉換矩陣，得到主成分

transformed = matrix_w.T.dot(all_samples)
cc = transformed.shape
print(cc)

# 繪製轉換後的資料

plt.plot(
    transformed[0, 0:20],
    transformed[1, 0:20],
    "o",
    markersize=7,
    color="blue",
    alpha=0.5,
    label="class1",
)
plt.plot(
    transformed[0, 20:40],
    transformed[1, 20:40],
    "^",
    markersize=7,
    color="red",
    alpha=0.5,
    label="class2",
)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel("x_values")
plt.ylabel("y_values")
plt.legend()
plt.title("Transformed samples with class labels")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PCA 個案實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 3. 資料分割

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 進行特徵萃取(PCA)


# PCA 函數實作
def PCA_numpy(X, X_test, no):
    cov_mat = np.cov(X.T)
    # 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
    eigen_val, eigen_vecs = np.linalg.eig(cov_mat)
    # 合併特徵向量及特徵值
    eigen_pairs = [
        (np.abs(eigen_val[i]), eigen_vecs[:, i]) for i in range(len(eigen_vecs))
    ]

    # 針對特徵值降冪排序
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)

    w = eigen_pairs[0][1][:, np.newaxis]
    for i in range(1, no):
        w = np.hstack((w, eigen_pairs[i][1][:, np.newaxis]))

    # 轉換：矩陣相乘 (n, m) x (m, 2) = (n, 2)
    return X.dot(w), X_test.dot(w)


X_train_pca, X_test_pca = PCA_numpy(X_train_std, X_test_std, 2)  # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_pca, y_train)

# 7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

# 繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn PCA 實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 3. 資料分割

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 特徵萃取(PCA)

from sklearn.decomposition import PCA

pca1 = PCA(n_components=2)
X_train_pca = pca1.fit_transform(X_train_std)
X_test_pca = pca1.transform(X_test_std)
cc = X_train_pca.shape, X_test_pca.shape, pca1.explained_variance_ratio_
print(cc)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_pca, y_train)

# 7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 97.22%

# 繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 94.44%

# 測試Scikit-learn 的PCA函數其他用法

# 不設定參數
pca1 = PCA()
X_train_pca = pca1.fit_transform(X_train_std)
pca1.explained_variance_ratio_

# 加總可解釋變異
np.sum(pca1.explained_variance_ratio_)

# 1.0

# 對可解釋變異繪製柏拉圖(Pareto)
plt.bar(range(1, 14), pca1.explained_variance_ratio_, alpha=0.5, align="center")
plt.step(range(1, 14), np.cumsum(pca1.explained_variance_ratio_), where="mid")
plt.ylabel("Explained variance ratio")
plt.xlabel("Principal components")
plt.axhline(0.8, color="r", linestyle="--")
plt.show()

# 設定可解釋變異下限
pca2 = PCA(0.8)
X_train_pca = pca2.fit_transform(X_train_std)
cc = X_train_pca.shape
print(cc)

print("------------------------------------------------------------")  # 60個

# LDA 個案實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 3. 資料分割

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 進行特徵萃取


# 計算 S_W, S_B 散佈矩陣
def calculate_SW_SB(X, y, label_count):
    mean_vecs = []
    for label in range(label_count):
        mean_vecs.append(np.mean(X[y == label], axis=0))
        print(f"Class {label} Mean = {mean_vecs[label]}")

    d = X.shape[1]  # number of features
    S_W = np.zeros((d, d))
    for label, mv in zip(range(label_count), mean_vecs):
        class_scatter = np.cov(X[y == label].T)
        S_W += class_scatter
    print(f"Sw shape:{S_W.shape}")

    mean_overall = np.mean(X, axis=0)
    S_B = np.zeros((d, d))
    for i, mean_vec in enumerate(mean_vecs):
        n = X[y == i + 1, :].shape[0]
        mean_vec = mean_vec.reshape(d, 1)  # make column vector
        mean_overall = mean_overall.reshape(d, 1)  # make column vector
        S_B += n * (mean_vec - mean_overall).dot((mean_vec - mean_overall).T)
    print(f"Sb shape:{S_B.shape}")
    return S_W, S_B


# LDA 函數實作
def LDA_numpy(X, X_test, y, label_count, no):
    S_W, S_B = calculate_SW_SB(X, y, label_count)
    # 計算特徵值(eigenvalue)及對應的特徵向量(eigenvector)
    eigen_val, eigen_vecs = np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
    # 合併特徵向量及特徵值
    eigen_pairs = [
        (np.abs(eigen_val[i]), eigen_vecs[:, i]) for i in range(len(eigen_vecs))
    ]
    print("Eigenvalues in descending order:\n")
    for eigen_val in eigen_pairs:
        print(eigen_val[0])

    # 針對特徵值降冪排序
    eigen_pairs.sort(key=lambda x: x[0], reverse=True)

    w = eigen_pairs[0][1][:, np.newaxis].real
    for i in range(1, no):
        w = np.hstack((w, eigen_pairs[i][1][:, np.newaxis].real))

    # 轉換：矩陣相乘 (n, m) x (m, 2) = (n, 2)
    return X.dot(w), X_test.dot(w)


X_train_pca, X_test_pca = LDA_numpy(
    X_train_std, X_test_std, y_train, len(ds.target_names), 2
)  # 取 2 個特徵
cc = X_train_pca.shape, X_test_pca.shape
print(cc)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_pca, y_train)

# 7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_pca, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn LDA實作

# 1. 載入資料
ds = datasets.load_wine()
df = pd.DataFrame(ds.data, columns=ds.feature_names)
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 資料集說明
# print(ds.DESCR)

# 3. 資料分割

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 指定X、Y
X = df.values
y = ds.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 4. 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 特徵萃取(LDA)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std, y_train)
X_test_lda = lda.transform(X_test_std)
cc = X_train_lda.shape, X_test_lda.shape, lda.explained_variance_ratio_
print(cc)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_lda, y_train)

# 7. 模型計分

# 計算準確率
y_pred = clf.predict(X_test_lda)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

# 繪製決策邊界(Decision regions)

from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
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

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            color=cmap(idx),
            marker=markers[idx],
            label=cl,
        )


plot_decision_regions(X_test_lda, y_test, classifier=clf)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.legend(loc="lower left")
plt.tight_layout()
# plt.savefig('decision_regions.png', dpi=300)
plt.show()

# 使用全部特徵

# 載入資料集
X, y = datasets.load_wine(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train_std, y_train)

# 模型計分
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (142, 13) (36, 13) (142,) (36,)
# 100.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn LDA實作

# 載入資料

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)

# 資料切割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# 繪製訓練及測試資料
_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
plt.show()

# PCA 萃取特徵

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=2)
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = pca.fit(X_train).transform(X_test)

# 繪製原始測試資料及經PCA轉換後的新資料

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
plt.show()

# KernelPCA 萃取特徵

from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")
plt.show()

# 載入上/下弦月資料

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# X, y = make_moons(n_samples=1_000, noise=0.05, random_state=0)
X, y = make_moons(n_samples=1000, random_state=123)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
plt.show()

# PCA 萃取特徵

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=2)
kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = pca.fit(X_train).transform(X_test)

fig, (orig_data_ax, pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

# Text(0.5, 1.0, 'Projection of testing data\n using PCA')
plt.show()

# KernelPCA 萃取特徵

from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(n_components=None, kernel="rbf", gamma=15)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)

fig, (orig_data_ax, kernel_pca_proj_ax) = plt.subplots(ncols=2, figsize=(10, 4))

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用PCA及KernelPCA進行影像去躁
# KernelPCA_image_denoising

from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 載入資料

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
cc = X.shape
print(cc)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

# 加躁
rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise

# 繪製原圖及加入雜訊的影像

# 繪圖函數
def plot_digits(X, title):
    """Small helper function to plot 100 digits."""
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)


# 繪製原圖
plot_digits(X_test, "原圖")
plot_digits(X_test_noisy, f"加躁\nMSE: {np.mean((X_test - X_test_noisy) ** 2):.2f}")
plt.show()

# PCA及Kernel PCA 轉換

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=32)
kernel_pca = KernelPCA(
    n_components=400, kernel="rbf", gamma=1e-3, fit_inverse_transform=True, alpha=5e-3
)

pca.fit(X_train_noisy)
_ = kernel_pca.fit(X_train_noisy)

# 使用 inverse_transform 重建影像

X_reconstructed_kernel_pca = kernel_pca.inverse_transform(
    kernel_pca.transform(X_test_noisy)
)
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test_noisy))

# PCA 重建影像繪圖

plot_digits(
    X_reconstructed_pca,
    f"PCA reconstruction\nMSE: {np.mean((X_test - X_reconstructed_pca) ** 2):.2f}",
)
plt.show()

# Kernel PCA 重建影像繪圖

plot_digits(
    X_reconstructed_kernel_pca,
    "Kernel PCA reconstruction\n"
    f"MSE: {np.mean((X_test - X_reconstructed_kernel_pca) ** 2):.2f}",
)
plt.show()

# 結論：PCA雖然比 Kernel PCA 的MSE小，但 Kernel PCA 去躁效果比較好

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# t-SNE測試

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# 生成3個集群資料

np.random.seed(10)
num_points_per_class = 50

# Class 1
mean1 = [0, 0]
cov = [[0.1, 0], [0, 0.1]]
X1 = np.random.multivariate_normal(mean1, cov, num_points_per_class)

# Class 2
mean2 = [10, 0]
X2 = np.random.multivariate_normal(mean2, cov, num_points_per_class)

# Class 3
mean3 = [5, 6]
X3 = np.random.multivariate_normal(mean3, cov, num_points_per_class)

X = np.concatenate([X1, X2, X3], axis=0)
cc = X.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# 繪圖

colors = ["red", "green", "blue"]
for i in range(3):
    plt.scatter(X[i * 50 : (i + 1) * 50, 0], X[i * 50 : (i + 1) * 50, 1], c=colors[i])

plt.show()

# t-SNE

perplexity = 25
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()

# PCA

X_pca = PCA(n_components=1).fit_transform(X)
for i in range(3):
    plt.scatter(X_pca[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


# 困惑度(perplexity)測試

perplexity = 2
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


perplexity = 130
X_embedded = TSNE(
    n_components=1, perplexity=perplexity, learning_rate="auto", init="random"
).fit_transform(X)
for i in range(3):
    plt.scatter(X_embedded[i * 50 : (i + 1) * 50], np.zeros(50), c=colors[i])
plt.show()


# 非線性分離
# 生成S曲線資料

from matplotlib import ticker
from sklearn import manifold, datasets

n_samples = 1500
S_points, S_color = datasets.make_s_curve(n_samples, random_state=0)
cc = S_points.shape, S_color.shape
print(cc)

# ((1500, 3), (1500,))

# 定義繪圖函數


def plot_2d(points, points_color, title):
    fig, ax = plt.subplots(figsize=(3, 3), facecolor="white", constrained_layout=True)
    fig.suptitle(title, size=16)
    add_2d_scatter(ax, points, points_color)
    plt.show()


def add_2d_scatter(ax, points, points_color, title=None):
    x, y = points.T
    ax.scatter(x, y, c=points_color, s=50, alpha=0.8)
    ax.set_title(title)
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.yaxis.set_major_formatter(ticker.NullFormatter())


def plot_3d(points, points_color, title):
    x, y, z = points.T

    fig, ax = plt.subplots(
        figsize=(6, 6),
        facecolor="white",
        tight_layout=True,
        subplot_kw={"projection": "3d"},
    )
    fig.suptitle(title, size=16)
    col = ax.scatter(x, y, z, c=points_color, s=50, alpha=0.8)
    ax.view_init(azim=-60, elev=9)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.zaxis.set_major_locator(ticker.MultipleLocator(1))

    fig.colorbar(col, ax=ax, orientation="horizontal", shrink=0.6, aspect=60, pad=0.01)
    plt.show()


# 繪製原始資料

plot_3d(S_points, S_color, "Original S-curve samples")

# 繪製降維後資料

t_sne = manifold.TSNE(
    n_components=2,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)

plot_2d(S_t_sne, S_color, "T-distributed Stochastic  \n Neighbor Embedding")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04_19_BOW

# 使用BOW猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 載入資料

with open("./data/news.txt", "r+", encoding="UTF-8") as f:
    text = f.read()
# print(text)

# BOW 轉換
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([text])
# 生字表
cc = vectorizer.get_feature_names_out()
print(cc)


print("單字對應的出現次數")
cc = X.toarray()
print(cc)


print("找出較常出現的單字")

import collections

MAX_FEATURES = 20
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")


print("考慮停用詞(Stop words)")

MAX_FEATURES = 20

# 轉換為 BOW
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")


print("詞形還原(Lemmatization)")

text = text.lower().replace("korean", "korea").replace("stores", "store")

MAX_FEATURES = 20

# 轉換為 BOW
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform([text])

# 找出較常出現的單字
word_freqs = collections.Counter()
for word, freq in zip(vectorizer.get_feature_names_out(), X.toarray()[0]):
    word_freqs[word] = freq

print(f"前{MAX_FEATURES}名單字:{word_freqs.most_common(MAX_FEATURES)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用BOW猜測文章大意

from sklearn.feature_extraction.text import CountVectorizer

# 測試資料

corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# BOW 轉換
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
# 生字表
cc = vectorizer.get_feature_names_out()
print(cc)

print("使用表格呈現單字及對應出現的次數")

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(df)

print("相似性比較")

from sklearn.metrics.pairwise import cosine_similarity

cc = cosine_similarity(df.iloc[-1:].values, df.iloc[:-1].values)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# spam_classification_with_tfidf
# 垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
from wordcloud import WordCloud
from math import log, sqrt
import re

# 讀取資料集

mails = pd.read_csv("./data/spam.csv", encoding="latin-1")
cc = mails.head()
print(cc)

# 資料整理
mails.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
cc = mails.head()
print(cc)

mails.rename(columns={"v1": "label", "v2": "message"}, inplace=True)
cc = mails.head()
print(cc)

cc = mails["label"].value_counts()
print(cc)

mails["label"] = mails["label"].map({"ham": 0, "spam": 1})
cc = mails.head()
print(cc)

# 設定停用詞
import string

stopword_list = set(stopwords.words("english") + list(string.punctuation))
# 詞形還原(Lemmatization)
lem = WordNetLemmatizer()


# 前置處理(Preprocessing)
def preprocess(text, is_lower_case=True):
    if is_lower_case:
        text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens if len(token) > 1 and token != "..."]
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_tokens = [lem.lemmatize(token) for token in filtered_tokens]
    filtered_text = " ".join(filtered_tokens)
    return filtered_text


mails["message"] = mails["message"].map(preprocess)
cc = mails.head()
print(cc)

# 文字雲

# 凸顯垃圾信的常用單字
spam_words = " ".join(list(mails[mails["label"] == 1]["message"]))
spam_wc = WordCloud(width=512, height=512).generate(spam_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(spam_wc)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# 找出正常信件的常用單字
ham_words = " ".join(list(mails[mails["label"] == 0]["message"]))
ham_wc = WordCloud(width=512, height=512).generate(ham_words)
plt.figure(figsize=(10, 8), facecolor="k")
plt.imshow(ham_wc)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# 使用 SciKit-learn TF-IDF

mails_message, labels = mails["message"].values, mails["label"].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

# (5572, 8111)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no = 0
for i in tfidf_matrix.toarray()[0]:
    if i > 0.0:
        no += 1
print(no)

# 資料分割

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    tfidf_matrix.toarray(), labels, test_size=0.2
)

# 模型訓練

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)

# 模型評分

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
cc = accuracy_score(y_pred, y_test)
print(cc)

# 0.9668161434977578

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, y_pred))

print("混淆矩陣")
cc = confusion_matrix(y_test, y_pred)
print(cc)

# 測試

message_processed_list = (
    "I cant pick the phone right now. Pls send a message",
    "Congratulations ur awarded $500",
    "Thanks for your subscription to Ringtone UK your mobile will be charged",
    "Oops, I'll let you know when my roommate's done",
    "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, 憯1.50 to rcv",
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
)
X_new = tfidf_vectorizer.transform(message_processed_list)
cc = clf.predict(X_new.toarray())
print(cc)

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

