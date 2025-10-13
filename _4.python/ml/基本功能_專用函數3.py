"""
基本功能_專用函數3

少量的


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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_recall_fscore_support

y_pred = [0, 1, 0, 0]
y_true = [0, 1, 0, 1]

accuracy_score(y_true, y_pred)

# The overall precision an recall
precision_score(y_true, y_pred)
recall_score(y_true, y_pred)

# Recalls on individual classes: SEN & SPC
recalls = recall_score(y_true, y_pred, average=None)
recalls[0]  # is the recall of class 0: specificity
recalls[1]  # is the recall of class 1: sensitivity

# Balanced accuracy
b_acc = recalls.mean()

# The overall precision an recall on each individual class
p, r, f, s = precision_recall_fscore_support(y_true, y_pred)

print("------------------------------------------------------------")  # 60個
from sklearn.metrics import classification_report

print("------------------------------------------------------------")  # 60個

"""
机器学习classification_report方法及precision精确率和recall召回率

classification_report简介
classification_report函数主要用于显示主要分类指标的文本报告
sklearn中的classification_report函数用于显示主要分类指标的文本报告．在报告中显示每个类的精确度，召回率，F1值等信息。 
主要参数: 
y_true：1维数组，或标签指示器数组/稀疏矩阵，目标值。 
y_pred：1维数组，或标签指示器数组/稀疏矩阵，分类器返回的估计值。 
labels：array，shape = [n_labels]，报表中包含的标签索引的可选列表。 
target_names：字符串列表，与标签匹配的可选显示名称（相同顺序）。 
sample_weight：类似于shape = [n_samples]的数组，可选项，样本权重。
digits：int，输出浮点值的位数．
"""

print("多指標評分 classification_report")

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print("------------------------------")  # 30個

y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
target_names = ["class 0", "class 1", "class 2"]
print(classification_report(y_true, y_pred, target_names=target_names))

"""
其中列表左边的一列为分类的标签名，右边support列为每个标签的出现次数．avg / total行为各列的均值（support列为总和）． 
precision recall f1-score三列分别为各个类别的精确度/召回率及 F1 F1值．
"""

print("------------------------------")  # 30個

y_true = [0, 1, 2, 2, 2]
y_pred = [0, 0, 2, 2, 1]
print(classification_report(y_true, y_pred))

print("------------------------------------------------------------")  # 60個
from sklearn.metrics import recall_score

print("------------------------------------------------------------")  # 60個

print("測試 召回率 recall_score")

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
cc = recall_score(y_true, y_pred, average="macro")  # doctest: +ELLIPSIS
print("recall_score :", cc)

cc = recall_score(y_true, y_pred, average="micro")
print("recall_score :", cc)

cc = recall_score(y_true, y_pred, average="weighted")
print("recall_score :", cc)

cc = recall_score(y_true, y_pred, average=None)
print("recall_score :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("分類效果評估")
print("FP/FN/TP/TN")

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值
print("------------------------------")  # 30個
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)
print("------------------------------")  # 30個
print("準確率")
from sklearn.metrics import accuracy_score

print(accuracy_score(y_real, y_pred))
print("------------------------------")  # 30個
print("召回率")
from sklearn.metrics import recall_score

print(recall_score(y_real, y_pred))
print("------------------------------")  # 30個
print("精度")
from sklearn.metrics import precision_score

print(precision_score(y_real, y_pred))
print("------------------------------")  # 30個
print("F值")
from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2))  # 計算fn
print("------------------------------")  # 30個
print("Logloss")
from sklearn.metrics import log_loss

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real, y_score))
print("------------------------------")  # 30個
print("ROC曲線和AUC")
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

print(roc_auc_score(y_real, y_score))  # AUC值
fpr, tpr, thresholds = roc_curve(y_real, y_score)
plt.plot(fpr, tpr)  # 繪圖
show()
print("------------------------------")  # 30個
# P-R曲線
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_real, y_score)
plt.plot(recall, precision)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Binarization
from sklearn.preprocessing import Binarizer

# Create a sample data array
data = np.array([[1.5, 2.7, 0.8], [0.2, 3.9, 1.2], [4.1, 1.0, 2.5]])

# Create a Binarizer instance with a threshold of 2.0
binarizer = Binarizer(threshold=2.0)

# Apply binarization to the data
binarized_data = binarizer.transform(data)

print("Original data:")
print(data)
print("\nBinarized data:")
print(binarized_data)

# Encoding Categorical Features

from sklearn.preprocessing import LabelEncoder

# Sample data: categorical labels
labels = ["cat", "dog", "dog", "fish", "cat", "dog", "fish"]

# Create a LabelEncoder instance
label_encoder = LabelEncoder()

# Fit and transform the labels
encoded_labels = label_encoder.fit_transform(labels)

# Print the original labels and their encoded versions
print("Original labels:", labels)
print("Encoded labels:", encoded_labels)

# Decode the encoded labels back to the original labels
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("Decoded labels:", decoded_labels)

print("------------------------------------------------------------")  # 60個

# Imputing Missing Values
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0], [7.0, 8.0, 9.0]])

# Create a SimpleImputer instance with strategy='mean'
imputer = SimpleImputer(strategy="mean")

# Fit and transform the imputer on the data
imputed_data = imputer.fit_transform(data)

print("Original data:")
print(data)
print("\nImputed data:")
print(imputed_data)

print("------------------------------------------------------------")  # 60個

# Generating Polynomial Features
from sklearn.preprocessing import PolynomialFeatures

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6]])

# Create a PolynomialFeatures instance of degree 2
poly = PolynomialFeatures(degree=2)

# Transform the data to include polynomial features
poly_data = poly.fit_transform(data)

print("Original data:")
print(data)
print("\nPolynomial features:")
print(poly_data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# confusion_matrix

# 計算及繪製混淆矩陣

# 載入資料
y_true = [0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 0, 1, 0, 1, 0, 1]

y_true = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
y_pred = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 真實的資料
y_true = np.random.randint(2, size=100)

# 預測的資料
y_pred = np.random.randint(2, size=100)

# 計算混淆矩陣
cc = confusion_matrix(y_true, y_pred)
print(cc)

cc = confusion_matrix(y_true, y_pred, labels=[1, 0])
print(cc)

# 取得混淆矩陣的4個格子
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
cc = tn, fp, fn, tp
print(cc)

# 繪製混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(
    y_true, y_pred, labels=[1, 0], display_labels=["真", "偽"]
)

show()

# 方法 2
cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["真", "偽"])
disp.plot()
show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0] - 1, -1, -1):
    for j in range(cm.shape[1] - 1, -1, -1):
        ax.text(x=j, y=i, s=cm[i, j], va="center", ha="center")

# 置換刻度
ax.set_xticks(range(cm.shape[0]), labels=["真", "偽"])
ax.set_yticks(range(cm.shape[1]), labels=["真", "偽"])

# 設定標籤
plt.xlabel("Predicted label")
plt.ylabel("True label")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# confusion_matrix_multiple-categories

# 計算及繪製多分類混淆矩陣

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]

# 計算混淆矩陣
cc = confusion_matrix(y_true, y_pred)
print(cc)

# 繪製混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_predictions(y_true, y_pred)
show()

# 方法 2
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
show()

# 方法 3
fig, ax = plt.subplots(figsize=(5, 5))

# 顯示矩陣
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.3)

# 按 [1, 0] 順序
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(x=j, y=i, s=cm[i, j], va="center", ha="center")

# 置換刻度 NG
# ax.set_xticks(range(cm.shape[0]))
# ax.set_yticks(range(cm.shape[1]))

# 設定標籤
plt.xlabel("Predicted label")
plt.ylabel("True label")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sklearn.utils

# sklearn.utils.shuffle 把array打亂
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
print(X)

X = sklearn.utils.shuffle(X, random_state=9487)
print(X)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("相似性比較")
from sklearn.metrics.pairwise import cosine_similarity

print("測試 cosine_similarity")

X = np.array(
    [
        [3, 0],  # r1
        [0, 3],  # r2
    ]
)

sim = cosine_similarity(X)
print(sim)


"""
計算相似度
#sklearn sklearn向量距離計算

通過 euclidean_distances 計算多個向量間的歐氏距離。

歐幾里得距離 (Euclidean distance)
    0, r1*r2, r1*r3, r1*r4
-----,     0, r2*r3, r2*r4
-----, -----,     0, r3*r4
-----, -----, -----,     0
"""

from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity

print("測試 euclidean_distances 歐幾里得距離 (Euclidean distance)")

X = np.array(
    [
        [4, 3, 0, 0, 5, 0],  # r1
        [5, 0, 4, 0, 4, 0],  # r2
        [4, 0, 5, 3, 4, 0],  # r3
        [0, 3, 0, 0, 0, 5],  # r4
    ]
)

"""
X = np.array(
    [
        [4, 3, 0, 0, 5, 0, 4, 3, 0, 0, 5, 0],  # r1
        [5, 0, 4, 0, 4, 0, 5, 0, 4, 0, 4, 0],  # r2
    ]
)
"""

dist = euclidean_distances(X)
print(dist)

print("測試 cosine_similarity")
sim = cosine_similarity(X)
print(sim)

print("兩列之間的距離")
X = [[0, 1], [1, 1]]
cc = euclidean_distances(X, X)
print(cc)

print("與原點之間的距離")
cc = euclidean_distances(X, [[0, 0]])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import scipy
import plot_utils

np.random.seed(42)
colors = sns.color_palette()

n_samples, n_features = 100, 2

mean, Cov, X = [None] * 4, [None] * 4, [None] * 4
mean[0] = np.array([-2.5, 2.5])
Cov[0] = np.array([[1, 0], [0, 1]])

mean[1] = np.array([2.5, 2.5])
Cov[1] = np.array([[1, 0.5], [0.5, 1]])

mean[2] = np.array([-2.5, -2.5])
Cov[2] = np.array([[1, 0.9], [0.9, 1]])

mean[3] = np.array([2.5, -2.5])
Cov[3] = np.array([[1, -0.9], [-0.9, 1]])

# Generate dataset
for i in range(len(mean)):
    X[i] = np.random.multivariate_normal(mean[i], Cov[i], n_samples)

# Plot
for i in range(len(mean)):
    # Points
    plt.scatter(X[i][:, 0], X[i][:, 1], color=colors[i], label="class %i" % i)
    # Means
    plt.scatter(
        mean[i][0],
        mean[i][1],
        marker="o",
        s=200,
        facecolors="w",
        edgecolors=colors[i],
        linewidth=2,
    )
    # Ellipses representing the covariance matrices
    plot_utils.plot_cov_ellipse(
        Cov[i], pos=mean[i], facecolor="none", linewidth=2, edgecolor=colors[i]
    )

plt.axis("equal")
_ = plt.legend(loc="upper left")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Correlation matrix

# 使用mtcars数据集，通过一些数字变量提供几辆汽车的性能参数。
url = "data/mtcars.csv"

df = pd.read_csv(url)

df = df.set_index("model")

# 横轴为汽车性能参数，纵轴为汽车型号
cc = df.head()
print(cc)

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool_)
mask[np.triu_indices_from(mask)] = True

f, ax = plt.subplots(figsize=(5.5, 4.5))
cmap = sns.color_palette("RdBu_r", 11)
# Draw the heatmap with the mask and correct aspect ratio
_ = sns.heatmap(
    corr,
    mask=None,
    cmap=cmap,
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
)

show()

print("------------------------------")  # 30個

# Re-order correlation matrix using AgglomerativeClustering

# convert correlation to distances
d = 2 * (1 - np.abs(corr))

from sklearn.cluster import AgglomerativeClustering

clustering = AgglomerativeClustering(n_clusters=3, linkage="single").fit(d)

lab = 0

clusters = [
    list(corr.columns[clustering.labels_ == lab]) for lab in set(clustering.labels_)
]
print(clusters)

reordered = np.concatenate(clusters)

R = corr.loc[reordered, reordered]

f, ax = plt.subplots(figsize=(5.5, 4.5))
# Draw the heatmap with the mask and correct aspect ratio
_ = sns.heatmap(
    R,
    mask=None,
    cmap=cmap,
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Precision matrix

Cov = np.array(
    [
        [1.0, 0.9, 0.9, 0.0, 0.0, 0.0],
        [0.9, 1.0, 0.9, 0.0, 0.0, 0.0],
        [0.9, 0.9, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.9, 0.0],
        [0.0, 0.0, 0.0, 0.9, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    ]
)

print("# Precision matrix:")
Prec = np.linalg.inv(Cov)
print(Prec.round(2))

print("# Partial correlations:")
Pcor = np.zeros(Prec.shape)
Pcor[::] = np.NaN

for i, j in zip(*np.triu_indices_from(Prec, 1)):
    Pcor[i, j] = -Prec[i, j] / np.sqrt(Prec[i, i] * Prec[j, j])

print(Pcor.round(2))

print("------------------------------------------------------------")  # 60個

ones = np.ones(Cov.shape[0])
d_euc = np.sqrt(np.dot(ones, ones))
d_mah = np.sqrt(np.dot(np.dot(ones, Prec), ones))

print("Euclidean norm of ones=%.2f. Mahalanobis norm of ones=%.2f" % (d_euc, d_mah))

print(np.dot(ones, Prec))

print("------------------------------------------------------------")  # 60個

import scipy
import plot_utils

np.random.seed(40)
colors = sns.color_palette()

mean = np.array([0, 0])
Cov = np.array([[1, 0.8], [0.8, 1]])
samples = np.random.multivariate_normal(mean, Cov, 100)
x1 = np.array([0, 2])
x2 = np.array([2, 2])

plt.scatter(samples[:, 0], samples[:, 1], color=colors[0])
plt.scatter(mean[0], mean[1], color=colors[0], s=200, label="mean")
plt.scatter(x1[0], x1[1], color=colors[1], s=200, label="x1")
plt.scatter(x2[0], x2[1], color=colors[2], s=200, label="x2")

# plot covariance ellipsis
plot_utils.plot_cov_ellipse(
    Cov, pos=mean, facecolor="none", linewidth=2, edgecolor=colors[0]
)
# Compute distances
d2_m_x1 = scipy.spatial.distance.euclidean(mean, x1)
d2_m_x2 = scipy.spatial.distance.euclidean(mean, x2)

Covi = scipy.linalg.inv(Cov)
dm_m_x1 = scipy.spatial.distance.mahalanobis(mean, x1, Covi)
dm_m_x2 = scipy.spatial.distance.mahalanobis(mean, x2, Covi)

# Plot distances
vm_x1 = (x1 - mean) / d2_m_x1
vm_x2 = (x2 - mean) / d2_m_x2
jitter = 0.1
plt.plot(
    [mean[0] - jitter, d2_m_x1 * vm_x1[0] - jitter],
    [mean[1], d2_m_x1 * vm_x1[1]],
    color="k",
)
plt.plot(
    [mean[0] - jitter, d2_m_x2 * vm_x2[0] - jitter],
    [mean[1], d2_m_x2 * vm_x2[1]],
    color="k",
)

plt.plot(
    [mean[0] + jitter, dm_m_x1 * vm_x1[0] + jitter],
    [mean[1], dm_m_x1 * vm_x1[1]],
    color="r",
)
plt.plot(
    [mean[0] + jitter, dm_m_x2 * vm_x2[0] + jitter],
    [mean[1], dm_m_x2 * vm_x2[1]],
    color="r",
)

plt.legend(loc="lower right")
plt.text(
    -6.1,
    3,
    "Euclidian:   d(m, x1) = %.1f<d(m, x2) = %.1f" % (d2_m_x1, d2_m_x2),
    color="k",
)
plt.text(
    -6.1,
    3.5,
    "Mahalanobis: d(m, x1) = %.1f>d(m, x2) = %.1f" % (dm_m_x1, dm_m_x2),
    color="r",
)

plt.axis("equal")
print("Euclidian   d(m, x1) = %.2f < d(m, x2) = %.2f" % (d2_m_x1, d2_m_x2))
print("Mahalanobis d(m, x1) = %.2f > d(m, x2) = %.2f" % (dm_m_x1, dm_m_x2))

show()

print("------------------------------------------------------------")  # 60個

# Multivariate normal distribution

import scipy.stats
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D


def multivariate_normal_pdf(X, mean, sigma):
    # Multivariate normal probability density function over X (n_samples x n_features)
    P = X.shape[1]
    det = np.linalg.det(sigma)
    norm_const = 1.0 / (((2 * np.pi) ** (P / 2)) * np.sqrt(det))
    X_mu = X - mu
    inv = np.linalg.inv(sigma)
    d2 = np.sum(np.dot(X_mu, inv) * X_mu, axis=1)
    return norm_const * np.exp(-0.5 * d2)


# mean and covariance
mu = np.array([0, 0])
sigma = np.array([[1, -0.5], [-0.5, 1]])

# x, y grid
x, y = np.mgrid[-3:3:0.1, -3:3:0.1]
X = np.stack((x.ravel(), y.ravel())).T
norm = multivariate_normal_pdf(X, mean, sigma).reshape(x.shape)

# Do it with scipy
norm_scpy = multivariate_normal(mu, sigma).pdf(np.stack((x, y), axis=2))
# np.allclose():檢查兩個數組是否每個元素都相似, 預設誤差在1e-05內
assert np.allclose(norm, norm_scpy)
"""
# Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection="3d")
surf = ax.plot_surface(
    x,
    y,
    norm,
    rstride=3,
    cstride=3,
    cmap=plt.cm.coolwarm,
    linewidth=1,
    antialiased=False,
)

ax.set_zlim(0, 0.2)
ax.zaxis.set_major_locator(plt.LinearLocator(10))
ax.zaxis.set_major_formatter(plt.FormatStrFormatter("%.02f"))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("p(x)")

plt.title("Bivariate Normal/Gaussian distribution")
fig.colorbar(surf, shrink=0.5, aspect=7, cmap=plt.cm.coolwarm)
show()
"""
print("------------------------------------------------------------")  # 60個

# 歐幾里得距離(Euclidean distance)

print("自己計算歐氏距離")

print("計算兩個向量間的歐氏距離")
# Compute Euclidean distance between 2 vectors
vec1 = np.random.randn(10)
vec2 = np.random.randn(10)
dist = np.sqrt(np.sum((vec1 - vec2) ** 2))
print(dist)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 核密度估计 Kernel Density Estimation.

from sklearn.neighbors import KernelDensity

rng = np.random.RandomState(42)
X = rng.random_sample((100, 3))

kde = KernelDensity(kernel="gaussian", bandwidth=0.5).fit(X)
log_density = kde.score_samples(X[:3])
print(log_density)
# array([-1.52955942, -1.51462041, -1.60244657])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 这个例子使用KernelDensity类来演示一维核密度估计的原理。

# ----------------------------------------------------------------------
# Plot a 1D density example
# ---------------------------------------------------------------------------
from scipy.stats import norm

"""
用随机种子生成100个数据，其中30个是符合高斯分布（0,1）的数据，70个是符合高斯分布(5,1)的数据，
（0,1）表示以x轴上的0为中心点，宽度为1的高斯分布。
（5,1）表示以x轴上5为中心店，宽度为1的高斯分布
"""
# ---------------------------------------------------------------------------
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
# ---------------------------------------------------------------------------
# 创建一个[-5,10]范围内包含1000个数据的等差数列
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
# 使用简单的高斯模型norm得到两个高斯分布的概率密度作为真实值（我不觉得这是最佳的办法）
true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])
fig, ax = plt.subplots()
# 填充出用简单高斯模型得出的密度真实值
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="input distribution")
colors = ["navy", "cornflowerblue", "darkorange"]
# 使用不同的内核进行拟合，我也不推荐这样做，我们首先应该是观察数据的分布，然后选择模型，而不是
# 一个个尝试，应该做的是调整我们的带宽。
kernels = ["gaussian", "tophat", "epanechnikov"]
# 划线的粗细
lw = 2
for color, kernel in zip(colors, kernels):
    # 用X数据进行训练模型
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    # 在X_plot数据上测试
    log_dens = kde.score_samples(X_plot)
    # 画图
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="kernel = '{0}'".format(kernel),
    )
ax.text(6, 0.38, "N={0} points".format(N))
ax.legend(loc="upper left")
# 用'+'代表真实的数据并且画出，用于观察数据分布集中情况
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import sklearn
from sklearn.neighbors import KernelDensity
from scipy.stats import norm
from collections import defaultdict

# 1、数据预处理
# Step1、Data pretreatment
Q1_data = pd.read_csv("data/Question_1.csv")
X = np.array(Q1_data["X"].tolist())[:, np.newaxis]
N = len(X)
print("max_value_in_X:{}".format(max(X)))
print("min_value_inX:{}".format(min(X)))
print(X.shape)

# 2、得到最佳带宽作为真实值（我认为比较合理的方式去选取真实值）
# from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV  # 網格搜索
from sklearn.model_selection import LeaveOneOut

bandwidths = 10 ** np.linspace(-1, 1, 100)
grid = GridSearchCV(
    KernelDensity(kernel="gaussian"), {"bandwidth": bandwidths}, cv=LeaveOneOut()
)
grid.fit(X)
# The best estimated bandwidth density is used as the truth value
best_KDEbandwidth = grid.best_params_["bandwidth"]
kernel = "gaussian"
lw = 2
kde = KernelDensity(kernel=kernel, bandwidth=best_KDEbandwidth).fit(X)
truth_density = np.exp(kde.score_samples(X))
print(grid.best_params_)


# 3、开始使用KDE
# Step2、Kernel Density Estimation.
MSE_MAP = defaultdict(list)
fig, ax = plt.subplots()
ax.fill(X[:, 0], truth_density, fc="black", alpha=1, label="truth density")
bandwidths = [0.15, 0.5, 1]
colors = ["navy", "cornflowerblue", "darkorange"]
for bandwidth, color in zip(bandwidths, colors):
    kde = KernelDensity(kernel=kernel, bandwidth=bandwidth).fit(X)
    log_dens = kde.score_samples(X)
    if bandwidth == best_KDEbandwidth:
        bandwidth = "ground truth"
    ax.plot(
        X[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="bandwidth = '{0}'".format(bandwidth),
    )
    MSE_MAP[bandwidth] = log_dens

ax.text(6, 0.32, "N={0} points".format(N))
ax.legend(loc="upper right")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.50)
show()


# （预测效果）
# 4，计算估计密度与地面真实密度之间的MSE
def cal_mse(a, b):
    if len(a) == len(b):
        n = len(a)
    else:
        return "len(a) != len(b)"
    res = 0
    for i in range(n):
        res += (a[i] - b[i]) ** 2
    return res / n


for bandwidth in MSE_MAP:
    estimate_density = MSE_MAP[bandwidth]
    MSE = cal_mse(estimate_density, truth_density)
    print(
        "When bandwidth is {:.2f} ----> MSE(estimate, truth): {:.3f}".format(
            bandwidth, MSE
        )
    )

"""
When bandwidth is 0.15 ----> MSE(estimate, truth): 2.603
When bandwidth is 0.50 ----> MSE(estimate, truth): 2.803
When bandwidth is 1.00 ----> MSE(estimate, truth): 3.059
        可以看出MSE表示与3.中的图表示出的信息是一致的。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import roc_curve
from sklearn.metrics import recall_score  # 召回率

print("測試 accuracy_score")

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))

print("測試 混淆矩陣")

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]

# 混淆矩陣
cm = confusion_matrix(y_true, y_pred)
print("混淆矩陣 :\n", cm, sep="")

print("混淆矩陣")
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]

# 混淆矩陣
cm = confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
print("混淆矩陣 :\n", cm, sep="")

print("測試 roc_curve")

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=2)
print(fpr)
print(tpr)
print(thresholds)

plt.plot(fpr, tpr)

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


print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
