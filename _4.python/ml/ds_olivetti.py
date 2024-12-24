"""
Olivetti 資料集

Olivetti Faces 人臉圖片數據集

40人 每人10張
400張圖 每張 64X64

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report

from numpy.random import RandomState
from sklearn import decomposition


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

n_row, n_col = 2, 5
n_components = n_row * n_col
image_shape = (64, 64)
rng = RandomState(0)

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

print("Olivetti 資料集 基本數據 fetch_olivetti_faces()")

olivetti_faces = datasets.fetch_olivetti_faces()

X = olivetti_faces.data
y = olivetti_faces.target

print("X.shape :")
print(X.shape)
# (400, 4096)

# 標籤 y
print("y.shape :")
print(y.shape)
# (400,)

# 圖像 olivetti_faces.images
print("olivetti_faces.images.shape :")
print(olivetti_faces.images.shape)
# (400, 64, 64)

print("------------------------------")  # 30個

plt.figure(figsize=(12, 8))
for i in range(80):
    plt.subplot(8, 10, i + 1)
    plt.imshow(X[(i // 2) * 10 + 1].reshape(64, 64), cmap=plt.cm.gray)
    plt.axis("off")

plt.suptitle("原圖 80張, 一人兩張")
show()

print("------------------------------")  # 30個

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca = decomposition.PCA()

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

# pip install scikit-image
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
print("target_names :", target_names)

n_targets = target_names.shape[0]
n_samples, h, w = olivetti_faces.images.shape

print("Sample count: {}".format(n_samples))
print("Target count: {}".format(n_targets))
print("Image size: {}x{}".format(w, h))
print("Dataset shape: {}\n".format(X.shape))

print("------------------------------")  # 30個


def plot_gallery(images, titles, h, w, n_row=2, n_col=5):
    print("R = ", n_row, ", C = ", n_col)
    plt.figure(figsize=(12, 8))
    # plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.01)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.axis("off")


n_row = 4
n_col = 5

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
plot_gallery(sample_images, sample_titles, h, w, n_row, n_col)
show()

print("------------------------------")  # 30個

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

start = time.time()
print("Fitting train datasets ...")
clf = SVC(class_weight="balanced")
clf.fit(X_train, y_train)
print("量測時間 Done in {0:.2f}s".format(time.time() - start))

start = time.time()
print("Predicting test dataset ...")
y_pred = clf.predict(X_test)
print("量測時間 Done in {0:.2f}s".format(time.time() - start))

cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("confusion matrix:\n")

np.set_printoptions(threshold=sys.maxsize)
print(cm)

""" not match
print(classification_report(y_test, y_pred, target_names=target_names))
"""

print("------------------------------")  # 30個

from sklearn.decomposition import PCA

print("Exploring explained variance ratio for dataset ...")
candidate_components = range(10, 300, 30)
explained_ratios = []
start = time.time()
for c in candidate_components:
    pca = PCA(n_components=c)
    X_pca = pca.fit_transform(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))
print("量測時間 Done in {0:.2f}s".format(time.time() - start))

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


n_row = 1
n_col = 5

sample_images = sample_images[0:5]
sample_titles = sample_titles[0:5]

plotting_images = sample_images
plotting_titles = [title_prefix("orig", t) for t in sample_titles]
candidate_components = [140, 75, 37, 19, 8]
for c in candidate_components:
    print("Fitting and projecting on PCA(n_components={}) ...".format(c))
    start = time.time()
    pca = PCA(n_components=c)
    pca.fit(X)
    X_sample_pca = pca.transform(sample_images)
    X_sample_inv = pca.inverse_transform(X_sample_pca)
    plotting_images = np.concatenate((plotting_images, X_sample_inv), axis=0)
    sample_title_pca = [title_prefix("{}".format(c), t) for t in sample_titles]
    plotting_titles = np.concatenate((plotting_titles, sample_title_pca), axis=0)
    print("量測時間 Done in {0:.2f}s".format(time.time() - start))

print("Plotting sample image with different number of PCA conpoments ...")
print("plot_gallery 2")
plot_gallery(
    plotting_images,
    plotting_titles,
    h,
    w,
    n_row * (len(candidate_components) + 1),
    n_col,
)

show()

print("------------------------------")  # 30個

n_components = 140

print("Fitting PCA by using training data ...")
start = time.time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
print("量測時間 Done in {0:.2f}s".format(time.time() - start))

print("Projecting input data for PCA ...")
start = time.time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("量測時間 Done in {0:.2f}s".format(time.time() - start))

from sklearn.model_selection import GridSearchCV

print("Searching the best parameters for SVC ...")
param_grid = {"C": [1, 5, 10, 50, 100], "gamma": [0.0001, 0.0005, 0.001, 0.005, 0.01]}
clf = GridSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, verbose=2, n_jobs=4
)
clf = clf.fit(X_train_pca, y_train)
print("Best parameters found by grid search:")
print(clf.best_params_)

start = time.time()
print("Predict test dataset ...")
y_pred = clf.best_estimator_.predict(X_test_pca)
cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("量測時間 Done in {0:.2f}.\n".format(time.time() - start))
print("confusion matrix:")
np.set_printoptions(threshold=sys.maxsize)
print(cm)

print(classification_report(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# decision_tree_multioutput_face_completion

# 使用Scikit-learn各種迴歸演算法預測人臉下半部

from sklearn.utils.validation import check_random_state
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

X, y = datasets.fetch_olivetti_faces(return_X_y=True)

# X : 400 張圖 每張4096=64X64點
# y : 編號 0~39 號

# 資料分割
train = X[y < 30]  # 前30張臉為訓練資料, 300張
test = X[y >= 30]  # 後10張臉為測試資料, 100張

print(train.shape)
print(test.shape)

# 模型訓練
n_pixels = X.shape[1]
print(n_pixels)

# 人臉上半部為 X，人臉下半部為 Y
X_train = train[:, : (n_pixels + 1) // 2]
y_train = train[:, n_pixels // 2 :]

# 使用各種迴歸演算法
ESTIMATORS = {
    "迴歸樹": DecisionTreeRegressor(),
    "KNN": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

# 訓練
for name, estimator in ESTIMATORS.items():
    print(name, estimator)
    estimator.fit(X_train, y_train)

# 測試 5 筆資料

n_faces = 5
rng = check_random_state(4)
face_ids = rng.randint(test.shape[0], size=(n_faces,))
test = test[face_ids, :]

X_test = test[:, : (n_pixels + 1) // 2]
y_test = test[:, n_pixels // 2 :]

# 預測
y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    y_test_predict[name] = estimator.predict(X_test)

# 依照各種迴歸演算法測試結果繪製人臉

# 設定圖片寬/高
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2.0 * n_cols, 2.26 * n_faces))
plt.suptitle("預測人臉下半部", size=16)

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
