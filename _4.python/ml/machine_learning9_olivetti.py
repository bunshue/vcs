"""

Olivetti 資料集

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

print("Olivetti 資料集 ST")

from numpy.random import RandomState
import matplotlib.image as mpimg
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 5
n_components = n_row * n_col
image_shape = (64, 64)
rng = RandomState(0)

print("------------------------------------------------------------")  # 60個

# 讀取數據集

"""
#指定下載位置
data_home='data\\'
olivetti_faces = fetch_olivetti_faces(data_home=data_home,shuffle=True, random_state=rng)
olivetti_faces = fetch_olivetti_faces(data_home=data_home)
"""

# 未指定下載位置, 下載至 C:/Users/070601/scikit_learn_data/olivetti_py3.pkz
olivetti_faces = fetch_olivetti_faces()

print("olivetti_faces 資料型態")
print(olivetti_faces.data.shape)
# (400, 4096)

# 標籤 olivetti_faces.target
print(olivetti_faces.target.shape)
# (400,)

# 圖像 olivetti_faces.images
print(olivetti_faces.images.shape)
# (400, 64, 64)

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))
for i in range(15):
    ax = plt.subplot2grid((3, 5), (i // 5, i % 5))
    ax.imshow(olivetti_faces.data[i * 10].reshape(64, 64), cmap=plt.cm.gray)
    # ax.set_title('Original')
    ax.axis("off")

plt.suptitle("Original")
plt.show()

print("------------------------------------------------------------")  # 60個

# 主成分分析 (Principal Component Analysis, PCA), 降低數據維度
pca = decomposition.PCA()
pca.fit(olivetti_faces.data)

print(pca.components_.shape)

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))

for i in range(15):
    ax = plt.subplot2grid((3, 5), (i // 5, i % 5))
    ax.imshow(pca.components_[i].reshape(64, 64), cmap=plt.cm.gray)
    # ax.set_title('PCA')
    ax.axis("off")

plt.suptitle("PCA")
plt.show()

print("------------------------------------------------------------")  # 60個

# pip install scikit-image
from skimage.io import imsave

face = olivetti_faces.data[0]

""" 看一下 Olivetti 臉的樣子
print('face.shape = ', face.shape)
fig = plt.figure(figsize=(12, 8))
plt.imshow(face.reshape(64, 64))
plt.show()
"""

trans = pca.transform(face.reshape(1, -1))
print(trans.shape)
for k in range(400):
    rank_k_approx = trans[:, :k].dot(pca.components_[:k]) + pca.mean_
    if k % 10 == 0:
        print("{:>03}".format(str(k)) + ".jpg", end="\t")
        # 存圖fail
        # imsave('{:>03}'.format(str(k)) + '.jpg', rank_k_approx.reshape(64, 64))
        # imsave('cccc.jpg', rank_k_approx.reshape(64, 64))

print()


print("Olivetti 資料集 SP")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("Olivetti 資料集 ST")

from sklearn.datasets import fetch_olivetti_faces

data_home = "datasets/"
olivetti_faces = fetch_olivetti_faces(data_home=data_home)

print("------------------------------")  # 30個

X = olivetti_faces.data
y = olivetti_faces.target

targets = np.unique(olivetti_faces.target)
target_names = np.array(["c%d" % t for t in targets])
n_targets = target_names.shape[0]
n_samples, h, w = olivetti_faces.images.shape
print("Sample count: {}\nTarget count: {}".format(n_samples, n_targets))
print("Image size: {}x{}\nDataset shape: {}\n".format(w, h, X.shape))

print("------------------------------")  # 30個


def plot_gallery(images, titles, h, w, n_row=2, n_col=5):
    plt.figure(figsize=(12, 8))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.01)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i])
        plt.axis("off")


n_row = 2
n_col = 6

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

plot_gallery(sample_images, sample_titles, h, w, n_row, n_col)
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)


from sklearn.svm import SVC

start = time.time()
print("Fitting train datasets ...")
clf = SVC(class_weight="balanced")
clf.fit(X_train, y_train)
print("Done in {0:.2f}s".format(time.time() - start))

start = time.time()
print("Predicting test dataset ...")
y_pred = clf.predict(X_test)
print("Done in {0:.2f}s".format(time.time() - start))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred, labels=range(n_targets))
print("confusion matrix:\n")

np.set_printoptions(threshold=sys.maxsize)
print(cm)

""" not match
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred, target_names=target_names))
"""
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import PCA

print("Exploring explained variance ratio for dataset ...")
candidate_components = range(10, 300, 30)
explained_ratios = []
start = time.time()
for c in candidate_components:
    pca = PCA(n_components=c)
    X_pca = pca.fit_transform(X)
    explained_ratios.append(np.sum(pca.explained_variance_ratio_))
print("Done in {0:.2f}s".format(time.time() - start))

print("------------------------------")  # 30個

plt.figure(figsize=(12, 8))
plt.grid()
plt.plot(candidate_components, explained_ratios)
plt.xlabel("Number of PCA Components")
plt.ylabel("Explained Variance Ratio")
plt.title("Explained variance ratio for PCA")
plt.yticks(np.arange(0.5, 1.05, 0.05))
plt.xticks(np.arange(0, 300, 20))

plt.show()

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
    print("Done in {0:.2f}s".format(time.time() - start))

print("Plotting sample image with different number of PCA conpoments ...")
plot_gallery(
    plotting_images,
    plotting_titles,
    h,
    w,
    n_row * (len(candidate_components) + 1),
    n_col,
)

plt.show()

print("------------------------------------------------------------")  # 60個

n_components = 140

print("Fitting PCA by using training data ...")
start = time.time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
print("Done in {0:.2f}s".format(time.time() - start))

print("Projecting input data for PCA ...")
start = time.time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("Done in {0:.2f}s".format(time.time() - start))


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
print("Done in {0:.2f}.\n".format(time.time() - start))
print("confusion matrix:")
np.set_printoptions(threshold=sys.maxsize)
print(cm)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))


print("Olivetti 資料集 SP")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
