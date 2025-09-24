"""
Olivetti Faces 人臉圖片數據集 fetch_olivetti_faces 

40人, 每人10張, 共 400張灰度圖像
每張 64X64

data: 形狀 (400, 4096=64X64)
每一列對應於原始大小為 64 x 64 像素的展開人臉圖像。

#指定下載位置
download_directory='download_directory/'

olivetti_faces = datasets.fetch_olivetti_faces(data_home=download_directory,shuffle=True, random_state=rng)
olivetti_faces = datasets.fetch_olivetti_faces(data_home=download_directory)

# 未指定下載位置, 下載至 C:/Users/070601/scikit_learn_data/olivetti_py3.pkz
olivetti_faces = datasets.fetch_olivetti_faces()
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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import matplotlib.image as mpimg
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn import decomposition
from sklearn.utils.validation import check_random_state
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import classification_report  # 分類報告
from sklearn.metrics import ConfusionMatrixDisplay


def show():
    plt.show()
    pass


R, C = 2, 5
n_components = R * C
image_shape = (64, 64)  # 設定圖片寬/高

rng = np.random.RandomState(0)  # 皆可
rng = check_random_state(4)  # 皆可

print("------------------------------------------------------------")  # 60個

olivetti_faces = datasets.fetch_olivetti_faces()

X = olivetti_faces.data  # 64X64之影像檔, 共400個
y = olivetti_faces.target  # 第幾人 0~39 號, 共400個

cc = olivetti_faces.DESCR
# print("資料集說明 :\n", cc, sep="")

print("資料 olivetti_faces.data")
print("olivetti_faces.data.shape :")
print(olivetti_faces.data.shape)  # (400, 4096)

print("資料 影像 olivetti_faces.images")
print("olivetti_faces.images.shape :")
print(olivetti_faces.images.shape)  # (400, 64, 64)

print("目標 olivetti_faces.target")
print("olivetti_faces.target.shape :")
print(olivetti_faces.target.shape)  # (400,)

print("------------------------------------------------------------")  # 60個

import cv2

# 圖片切分範例
filename = "data/OlivettiFaces.jpg"
image = cv2.imread(filename)

# 轉為灰度圖像
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

w, h = 47, 57
# 將人臉圖片提取為 (label:list) 形式
olivetti_faces = []

# 左排
for row in range(20):
    for column in range(10):
        # print("("+str(row) + ", " + str(column)+") ", end="")
        img = image[row * h : (row + 1) * h, column * w : (column + 1) * w]
        olivetti_faces.append(img)
        """ many
        #存圖
        filename = "tmp_{:>02}".format(str(row+1)) + "_{:>02}".format(str(column+1))+".jpg"
        cv2.imwrite(img=img, filename=filename)
        #print('存檔檔名 :', filename)
        """


# 右排
for row in range(20):
    for column in range(10):
        column += 10
        # print("("+str(row) + ", " + str(column)+") ", end="")
        img = image[row * h : (row + 1) * h, column * w : (column + 1) * w]
        olivetti_faces.append(img)
        """ many
        #存圖
        filename = "tmp_{:>02}".format(str(row+21)) + "_{:>02}".format(str(column+1-10))+".jpg"
        cv2.imwrite(img=img, filename=filename)
        #print('存檔檔名 :', filename)
        """

print("共有 :", len(olivetti_faces), "張圖")

plt.figure(figsize=(12, 8))
for i in range(80):
    plt.subplot(8, 10, i + 1)
    plt.imshow(olivetti_faces[(i // 2) * 10 + 1], cmap=plt.cm.gray)
    plt.axis("off")

plt.suptitle("原圖 80張, 一人兩張")
show()

"""
print("存圖 全部 40人 每人10張, 共400張")
for row in range(20):  # 40人 每列2人 共20列
    for column in range(20):  # 每人10張 1列20張
        img = image[row * h : (row + 1) * h, column * w : (column + 1) * w]
        filename = "tmp_{:>02}".format(str(row+1)) + "_{:>02}".format(str(column+1))+".jpg"
        cv2.imwrite(img=img, filename=filename)
        #print('存檔檔名 :', filename)
"""
print("------------------------------------------------------------")  # 60個

olivetti_faces = datasets.fetch_olivetti_faces()

X = olivetti_faces.data  # 64X64之影像檔, 共400個
y = olivetti_faces.target  # 第幾人 0~39 號, 共400個

plt.figure(figsize=(12, 8))
for i in range(80):
    plt.subplot(8, 10, i + 1)
    plt.imshow(X[(i // 2) * 10 + 1].reshape(64, 64), cmap=plt.cm.gray)
    plt.axis("off")

plt.suptitle("原圖 80張, 一人兩張")
show()

print("------------------------------")  # 30個

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca = PCA()

pca.fit(X)

print("pca.components_.shape :")
print(pca.components_.shape)

print("------------------------------")  # 30個

plt.figure(figsize=(12, 8))

for i in range(60):
    plt.subplot(6, 10, i + 1)
    plt.imshow(pca.components_[i].reshape(64, 64), cmap=plt.cm.gray)
    plt.axis("off")

plt.suptitle("PCA 前60張")
show()

print("------------------------------")  # 30個

from skimage.io import imsave

index = 70  # 第幾張圖
face = X[index]

# 看一下 Olivetti 臉的樣子, 就是  64 X 64
print("face.shape :")
print(face.shape)

fig = plt.figure(figsize=(6, 4))
plt.imshow(face.reshape(64, 64), cmap=plt.cm.gray)
plt.title("第" + str(index) + "張圖")
show()

trans = pca.transform(face.reshape(1, -1))
print("trans.shape :")
print(trans.shape)

for k in range(400):
    # 每張圖的某種計算
    rank_k_approx = trans[:, :k].dot(pca.components_[:k]) + pca.mean_
    img = rank_k_approx.reshape(64, 64)
    img = img.astype(np.uint8)
    """
    # 存圖
    filename = "{:>03}".format(str(k)) + ".jpg"
    imsave(filename, img)
    #print('存檔檔名 :', filename)
    """

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

olivetti_faces = datasets.fetch_olivetti_faces()

X = olivetti_faces.data  # 64X64之影像檔, 共400個
y = olivetti_faces.target  # 第幾人 0~39 號, 共400個

# print("原目標 :", y)
targets = np.unique(y)
print("單一化目標 :", targets)

target_names = np.array(["c%d" % t for t in targets])
print("目標名稱 :\n", target_names, sep="")

n_targets = target_names.shape[0]
print("目標個數 :", n_targets)

n_samples, h, w = olivetti_faces.images.shape  # (400, 64, 64)

print("------------------------------")  # 30個


def plot_gallery1(images, titles, h, w, n_row=2, n_col=5):
    print("R = ", n_row, ", C = ", n_col)
    plt.figure(figsize=(2.0 * n_col, 2.26 * n_row))

    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.axis("off")
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.01)


R, C = 4, 5
sample_images = None
sample_titles = []
for i in range(n_targets):
    people_images = X[y == i]
    people_sample_index = np.random.randint(0, people_images.shape[0], 1)
    people_sample_image = people_images[people_sample_index, :]
    if sample_images is not None:
        sample_images = np.concatenate((sample_images, people_sample_image), axis=0)
    else:
        sample_images = people_sample_image
    sample_titles.append(target_names[i])

print("plot_gallery 1")
plot_gallery1(sample_images, sample_titles, h, w, R, C)
show()

print("------------------------------")  # 30個

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Fitting train datasets ...")
clf = SVC(class_weight="balanced")

clf.fit(X_train, y_train)

print("Predicting test dataset ...")
y_pred = clf.predict(X_test)

np.set_printoptions(threshold=sys.maxsize)

# 混淆矩陣
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("混淆矩陣 :\n", cm, sep="")

""" not match
# 分類報告
print(classification_report(y_test, y_pred, target_names=target_names))
"""

print("------------------------------")  # 30個

print("Exploring explained variance ratio for dataset ...")
candidate_components = range(10, 300, 30)
explained_ratios = []

for c in candidate_components:
    pca = PCA(n_components=c)
    X_pca = pca.fit_transform(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))

print("------------------------------")  # 30個

plt.figure(figsize=(12, 8))

plt.grid()
plt.plot(candidate_components, explained_ratios)
plt.xlabel("Number of PCA Components")
plt.ylabel("Explained Variance Ratio")
plt.title("Explained variance ratio for PCA")
plt.yticks(np.arange(0.5, 1.05, 0.05))
plt.xticks(np.arange(0, 300, 20))

show()

print("------------------------------")  # 30個


def title_prefix(prefix, title):
    return "{}: {}".format(prefix, title)


R, C = 1, 5

sample_images = sample_images[0:5]
sample_titles = sample_titles[0:5]

plotting_images = sample_images
plotting_titles = [title_prefix("orig", t) for t in sample_titles]
candidate_components = [140, 75, 37, 19, 8]
for c in candidate_components:
    print("Fitting and projecting on PCA(n_components={}) ...".format(c))
    # 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
    pca = PCA(n_components=c)
    pca.fit(X)
    X_sample_pca = pca.transform(sample_images)
    X_sample_inv = pca.inverse_transform(X_sample_pca)
    plotting_images = np.concatenate((plotting_images, X_sample_inv), axis=0)
    sample_title_pca = [title_prefix("{}".format(c), t) for t in sample_titles]
    plotting_titles = np.concatenate((plotting_titles, sample_title_pca), axis=0)

print("Plotting sample image with different number of PCA conpoments ...")
print("plot_gallery 2")
plot_gallery1(
    plotting_images,
    plotting_titles,
    h,
    w,
    R * (len(candidate_components) + 1),
    C,
)

show()

print("------------------------------")  # 30個

n_components = 140

print("Fitting PCA by using training data ...")

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)

print("Projecting input data for PCA ...")
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

from sklearn.model_selection import GridSearchCV  # 網格搜索

print("Searching the best parameters for SVC ...")
param_grid = {"C": [1, 5, 10, 50, 100], "gamma": [0.0001, 0.0005, 0.001, 0.005, 0.01]}
clf = GridSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, verbose=2, n_jobs=4
)
clf = clf.fit(X_train_pca, y_train)
print("Best parameters found by grid search:")
print(clf.best_params_)

print("Predict test dataset ...")
y_pred = clf.best_estimator_.predict(X_test_pca)

np.set_printoptions(threshold=sys.maxsize)

# 混淆矩陣
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("混淆矩陣 :\n", cm, sep="")

# 分類報告
print(classification_report(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# decision_tree_multioutput_face_completion

# 使用Scikit-learn各種迴歸演算法預測人臉下半部

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

X, y = datasets.fetch_olivetti_faces(return_X_y=True, random_state=rng)
# X : 400 張圖 每張4096=64X64點
# y : 編號 0~39 號

# 資料分割
train = X[y < 30]  # 前30張臉為訓練資料, 300張
test = X[y >= 30]  # 後10張臉為測試資料, 100張

print("訓練資料大小 :", train.shape)
print("測試資料大小 :", test.shape)

# 模型訓練
n_pixels = X.shape[1]
print("X長度 :", n_pixels)

# 人臉上半部為 X，人臉下半部為 Y
X_train = train[:, : (n_pixels + 1) // 2]
y_train = train[:, n_pixels // 2 :]

# 使用各種迴歸演算法
ESTIMATORS = {
    "迴歸樹": DecisionTreeRegressor(),
    "KNN": KNeighborsRegressor(),
    "線性迴歸": LinearRegression(),
    "Ridge": RidgeCV(),
}

# 訓練
for name, estimator in ESTIMATORS.items():
    print("演算法名稱 :", name, "\t演算法 :", estimator)
    estimator.fit(X_train, y_train)

# 測試 5 筆資料

n_faces = 5
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]

# 預測
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    y_test_predict[name] = estimator.predict(X_test)

# 依照各種迴歸演算法測試結果繪製人臉

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("預測人臉下半部")

# 繪圖
for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i > 0:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1, title="真實圖片")

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

R, C = 2, 5
N = R * C

olivetti_faces = datasets.fetch_olivetti_faces()

X, y = datasets.fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
# X : 400 張圖 每張4096=64X64點
# y : 編號 0~39 號

n_samples, n_features = X.shape  # (400, 4096)


def plot_gallery2(title, images, n_col=C, n_row=R, cmap=plt.cm.gray):
    print("R = ", n_row, ", C = ", n_col)
    plt.figure(figsize=(2.0 * n_col, 2.26 * n_row))
    plt.suptitle(title)
    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)
        vmax = max(comp.max(), -comp.min())
        plt.imshow(
            comp.reshape(image_shape),
            cmap=cmap,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )
        plt.axis("off")
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.01)


# Preprocessing
# global centering
faces_centered = X - X.mean(axis=0)
# local centering
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

title = "Original Olivetti faces"
plot_gallery2(title, X[:N])
show()

# First centered Olivetti faces
title = "First centered Olivetti faces"
plot_gallery2(title, faces_centered[:N])
show()

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca = PCA(n_components=N)
pca.fit(faces_centered)
title = "PCA first %i loadings" % N
plot_gallery2(title, pca.components_[:N])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
人臉資料集分解 ST
https://scikit-learn.dev.org.tw/1.6/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-auto-examples-decomposition-plot-faces-decomposition-py
"""
print("------------------------------------------------------------")  # 60個

# 資料集準備
# 載入並預處理 Olivetti 人臉資料集。

from sklearn import cluster

X, y = datasets.fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
# X : 400 張圖 每張4096=64X64點
# y : 編號 0~39 號

n_samples, n_features = X.shape  # 400, 4096

# Global centering (focus on one feature, centering all samples)
faces_centered = X - X.mean(axis=0)

# Local centering (focus on one sample, centering all features)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

# 定義一個基本函數來繪製人臉的圖庫。

n_row, n_col = 2, 3
n_components = n_row * n_col


def plot_gallery3(title, images, n_col=n_col, n_row=n_row, cmap=plt.cm.gray):
    print("R = ", n_row, ", C = ", n_col)
    # plt.figure(figsize=(2.0 * n_col, 2.26 * n_row))
    fig, axs = plt.subplots(
        nrows=n_row,
        ncols=n_col,
        figsize=(2.0 * n_col, 2.3 * n_row),
        facecolor="white",
        constrained_layout=True,
    )
    fig.set_constrained_layout_pads(w_pad=0.01, h_pad=0.02, hspace=0, wspace=0)
    fig.set_edgecolor("black")
    fig.suptitle(title)
    for ax, vec in zip(axs.flat, images):
        vmax = max(vec.max(), -vec.min())
        im = ax.imshow(
            vec.reshape(image_shape),
            cmap=cmap,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )
        ax.axis("off")
    # plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.01)

    fig.colorbar(im, ax=axs, orientation="horizontal", shrink=0.99, aspect=40, pad=0.01)
    show()


# 看一下資料
title = "Faces from dataset 灰色表示負值, 白色表示正值"
plot_gallery3(title, faces_centered[:n_components])

print("------------------------------")  # 30個

# 分解 Decomposition

# 特徵臉 - 使用隨機 SVD 的 PCA
# 使用資料的奇異值分解 (SVD) 進行線性降維，將其投影到較低的維度空間。

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca_estimator = PCA(n_components=n_components, svd_solver="randomized", whiten=True)

pca_estimator.fit(faces_centered)

title = "Eigenfaces - PCA using randomized SVD 經過 PCA"
plot_gallery3(title, pca_estimator.components_[:n_components])

print("------------------------------")  # 30個

# 非負組件 - NMF Non-negative components - NMF
# 估計非負原始資料作為兩個非負矩陣的乘積。

nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(X)  # original non- negative dataset

title = "Non-negative components - NMF"
plot_gallery3(title, nmf_estimator.components_[:n_components])

print("------------------------------")  # 30個

# 獨立組件 - FastICA Independent components - FastICA
# 獨立成分分析將多變量向量分解為彼此最大獨立的加性子成分。

ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
title = "Independent components - FastICA"
plot_gallery3(title, ica_estimator.components_[:n_components])

print("------------------------------")  # 30個

# 稀疏組件 - MiniBatchSparsePCA Sparse components - MiniBatchSparsePCA
# 小批量稀疏 PCA (MiniBatchSparsePCA) 提取最能重建資料的一組稀疏組件。
# 此變體比類似的 SparsePCA更快，但準確度較低。

batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
title = "Sparse components - MiniBatchSparsePCA"
plot_gallery3(title, batch_pca_estimator.components_[:n_components])

print("------------------------------")  # 30個

# 字典學習
# 預設情況下，MiniBatchDictionaryLearning 將資料分成小批量，
# 並透過在指定次數的迭代中循環小批量，以線上方式進行最佳化。

batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
title = "Dictionary learning"
plot_gallery3(title, batch_dict_estimator.components_[:n_components])

print("------------------------------")  # 30個

# 叢集中心 - MiniBatchKMeans   # Cluster centers - MiniBatchKMeans
# sklearn.cluster.MiniBatchKMeans 在計算上是有效率的，並使用 partial_fit 方法實作線上學習。這就是為什麼用 MiniBatchKMeans 來增強一些耗時的演算法可能是有益的。

kmeans_estimator = cluster.MiniBatchKMeans(
    n_clusters=n_components,
    tol=1e-3,
    batch_size=20,
    max_iter=50,
    random_state=rng,
)
kmeans_estimator.fit(faces_centered)
title = "Cluster centers - MiniBatchKMeans"
plot_gallery3(title, kmeans_estimator.cluster_centers_[:n_components])

print("------------------------------")  # 30個

# 因子分析組件 - FA
# Factor Analysis components - FA
# FactorAnalysis 與 PCA 相似，
# 但具有獨立地對輸入空間每個方向的變異數進行建模的優點（異質雜訊）。
# 在使用者指南中閱讀更多資訊。

fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
title = "Factor Analysis (FA)"
plot_gallery3(title, fa_estimator.components_[:n_components])

# --- Pixelwise variance
plt.figure(figsize=(3.2, 3.6), facecolor="white", tight_layout=True)
vec = fa_estimator.noise_variance_
vmax = max(vec.max(), -vec.min())
plt.imshow(
    vec.reshape(image_shape),
    cmap=plt.cm.gray,
    interpolation="nearest",
    vmin=-vmax,
    vmax=vmax,
)
plt.axis("off")
plt.title("Pixelwise variance from \n Factor Analysis (FA)", wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
show()

print("------------------------------")  # 30個

# 分解：字典學習
# Decomposition: Dictionary learning
# 使用另一個顏色圖繪製我們資料集中相同的樣本。紅色表示負值，藍色表示正值，白色表示零。

title = "Faces from dataset"
plot_gallery3(title, faces_centered[:n_components], cmap=plt.cm.RdBu)

print("------------------------------")  # 30個

# 字典學習 - 正向字典  # Dictionary learning - positive dictionary
# 在以下章節中，我們在尋找字典時強制執行正向性。

dict_pos_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=0.1,
    max_iter=50,
    batch_size=3,
    random_state=rng,
    positive_dict=True,
)
dict_pos_dict_estimator.fit(faces_centered)

title = "Dictionary learning - positive dictionary"
plot_gallery3(
    title, dict_pos_dict_estimator.components_[:n_components], cmap=plt.cm.RdBu
)

print("------------------------------")  # 30個

# 字典學習 - 正向編碼 # Dictionary learning - positive code
# 以下我們將編碼係數限制為正矩陣。

dict_pos_code_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=0.1,
    max_iter=50,
    batch_size=3,
    fit_algorithm="cd",
    random_state=rng,
    positive_code=True,
)
dict_pos_code_estimator.fit(faces_centered)
title = "Dictionary learning - positive code"
plot_gallery3(
    title, dict_pos_code_estimator.components_[:n_components], cmap=plt.cm.RdBu
)

print("------------------------------")  # 30個

# 字典學習 - 正向字典和編碼 # Dictionary learning - positive dictionary & code
# 以下是字典值和編碼係數受到正向約束時的結果。

dict_pos_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=0.1,
    max_iter=50,
    batch_size=3,
    fit_algorithm="cd",
    random_state=rng,
    positive_dict=True,
    positive_code=True,
)
dict_pos_estimator.fit(faces_centered)

title = "Dictionary learning - positive dictionary & code"
plot_gallery3(title, dict_pos_estimator.components_[:n_components], cmap=plt.cm.RdBu)

print("------------------------------------------------------------")  # 60個
"""
人臉資料集分解 SP
https://scikit-learn.dev.org.tw/1.6/auto_examples/decomposition/plot_faces_decomposition.html#sphx-glr-auto-examples-decomposition-plot-faces-decomposition-py
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)

olivetti_faces = datasets.fetch_olivetti_faces(
    shuffle=True, random_state=np.random.RandomState(0)
)  # 創建隨機種子

# olivetti_faces = datasets.fetch_olivetti_faces(data_home=None,shuffle=False,random_state=0,download_if_missing=True)

faces = olivetti_faces.data  # 加载工打开数据


def plot_gallery4(title, images, n_col=n_col, n_row=n_row):
    print("R = ", n_row, ", C = ", n_col)
    plt.figure(figsize=(2.0 * n_col, 2.26 * n_row))  # 创建图片，并指定图片大小
    plt.suptitle(title)

    for i, comp in enumerate(images):
        plt.subplot(n_row, n_col, i + 1)  # 选择绘制的子图
        vmax = max(comp.max(), -comp.min())

        plt.imshow(
            comp.reshape(image_shape),
            cmap=plt.cm.gray,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )  # 对数值归一化，并以灰度图形式显示
        plt.xticks(())
        plt.yticks(())  # 去除子图的坐标轴标签
    plt.subplots_adjust(0.01, 0.05, 0.99, 0.94, 0.04, 0.0)  # 对子图位置及间隔调整


plot_gallery4("First centered Olivetti faces", faces[:n_components])
estimators = [
    ("Eigenfaces-PCA using randomized SVD", PCA(n_components=6, whiten=True)),
    ("Non-negative components - NMF", NMF(n_components=6, init="nndsvda", tol=5e-3)),
]  # NMF和PCA实例化

for name, estimator in estimators:  # 分别调用PCA和NMF
    estimator.fit(faces)  # 调用PCA或NMF提取特征
    components_ = estimator.components_  # 获取提取的特征
    plot_gallery4(name, components_[:n_components])  # 按照固定格式进行排列
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# same
# plt.xticks(())
# plt.yticks(())
# plt.axis("off")
