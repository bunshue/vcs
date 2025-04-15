"""
Face-Detection

fetch_lfw_people

人臉辨識資料集(Labeled Faces in the Wild, LFW)


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

import sklearn.linear_model

from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

ds = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# 資料集說明
print(ds.DESCR)

# 資料維度
n_samples, h, w = ds.images.shape

X = ds.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = ds.target
target_names = ds.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

print(ds.target_names)

# 是否有含遺失值(Missing value)

cc = np.isnan(X).sum()
print(cc)

print("# y 各類別資料筆數統計")

df_y = pd.DataFrame({"code": y})
df_y["name"] = df_y["code"].map(dict(enumerate(ds.target_names)))

sns.countplot(x="name", data=df_y)
plt.xticks(rotation=30)

show()

print("以Pandas函數統計各類別資料筆數")
pd.Series(y).value_counts()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的import seaborn as sns  # 海生, 自動把圖畫得比較好看 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression(max_iter=500)  # 邏輯迴歸函數學習機

# 6. 模型訓練
logistic_regression.fit(X_train_std, y_train)

# 7. 模型計分
y_pred = logistic_regression.predict(X_test_std)
print(y_pred)

print("計算準確率 測試目標 與 預測目標 接近程度")
from sklearn.metrics import accuracy_score

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
plt.xticks(rotation=30)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from skimage import data, color, transform, feature

print("讀資料")
faces = fetch_lfw_people()
print("讀資料 OK")

positive_patches = faces.images
print(positive_patches.shape)

# (3185, 62, 47)

from skimage import data, transform

imgs_to_use = [
    "camera",
    "text",
    "coins",
    "moon",
    "page",
    "clock",
    "immunohistochemistry",
    "chelsea",
    "coffee",
    "hubble_deep_field",
]

images = [color.rgb2gray(getattr(data, name)()) for name in imgs_to_use]

from sklearn.feature_extraction.image import PatchExtractor


def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
    extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(
        patch_size=extracted_patch_size, max_patches=N, random_state=0
    )
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size) for patch in patches])
    return patches


negative_patches = np.vstack(
    [extract_patches(im, 1000, scale) for im in images for scale in [0.5, 1.0, 2.0]]
)

print(negative_patches.shape)

# (30000, 62, 47)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(6, 10)
for i, axi in enumerate(ax.flat):
    axi.imshow(negative_patches[500 * i], cmap="gray")
    axi.axis("off")
show()


from itertools import chain

X_train = np.array(
    [feature.hog(im) for im in chain(positive_patches, negative_patches)]
)
y_train = np.zeros(X_train.shape[0])
y_train[: positive_patches.shape[0]] = 1
print(X_train.shape)

# (33185, 1215)


from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

cross_val_score(GaussianNB(), X_train, y_train)

# array([0.96112702, 0.986741  , 0.98900105, 0.99261715, 0.98885038])

from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV  # 網格搜索

grid = GridSearchCV(LinearSVC(), {"C": [1.0, 2.0, 4.0, 8.0]})
grid.fit(X_train, y_train)
print(grid.best_score_)

# 0.9934910351062227

print(grid.best_params_)

# {'C': 1.0}

model = grid.best_estimator_
model.fit(X_train, y_train)

LinearSVC(
    C=1.0,
    class_weight=None,
    dual=True,
    fit_intercept=True,
    intercept_scaling=1,
    loss="squared_hinge",
    max_iter=1000,
    multi_class="ovr",
    penalty="l2",
    random_state=None,
    tol=0.0001,
    verbose=0,
)

import skimage

test_image = skimage.data.astronaut()
test_image = skimage.color.rgb2gray(test_image)
test_image = skimage.transform.rescale(test_image, 0.5)
test_image = test_image[:160, 40:180]
plt.imshow(test_image, cmap="gray")
plt.axis("off")
show()


def sliding_window(
    img, patch_size=positive_patches[0].shape, istep=2, jstep=2, scale=1.0
):
    Ni, Nj = (int(scale * s) for s in patch_size)
    for i in range(0, img.shape[0] - Ni, istep):
        for j in range(0, img.shape[1] - Ni, jstep):
            patch = img[i : i + Ni, j : j + Nj]
            if scale != 1:
                patch = transform.resize(patch, patch_size)
            yield (i, j), patch


print(patches_hog.shape)

# (1911, 1215)


indices, patches = zip(*sliding_window(test_image))
patches_hog = np.array([feature.hog(patch) for patch in patches])
print(patches_hog.shape)

# (1911, 1215)


labels = model.predict(patches_hog)
print(labels.sum())

# 36.0

fig, ax = plt.subplots()
ax.imshow(test_image, cmap="gray")
ax.axis("off")
Ni, Nj = positive_patches[0].shape
indices = np.array(indices)
for i, j in indices[labels == 1]:
    ax.add_patch(
        plt.Rectangle(
            (j, i), Nj, Ni, edgecolor="yellow", alpha=0.4, lw=3, facecolor="none"
        )
    )
show()

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
