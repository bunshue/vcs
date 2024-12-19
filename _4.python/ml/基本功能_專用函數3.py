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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多指標評分")

from sklearn.metrics import classification_report

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("分類效果評估")
print("FP/FN/TP/TN")

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)

print("準確率")
from sklearn.metrics import accuracy_score

print(accuracy_score(y_real, y_pred))

print("召回率")
from sklearn.metrics import recall_score

print(recall_score(y_real, y_pred))

print("精度")
from sklearn.metrics import precision_score

print(precision_score(y_real, y_pred))

print("F值")

from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2))  # 計算fn

print("Logloss")
from sklearn.metrics import log_loss

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real, y_score))

print("ROC曲線和AUC")
from sklearn.metrics import roc_auc_score, roc_curve

print(roc_auc_score(y_real, y_score))  # AUC值

fpr, tpr, thresholds = roc_curve(y_real, y_score)
plt.plot(fpr, tpr)  # 繪圖

show()

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

# 08_04_confusion_matrix

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
ax.set_xticks(range(cm.shape[0]), labels=["真", "偽"], fontsize=14)
ax.set_yticks(range(cm.shape[1]), labels=["真", "偽"], fontsize=14)

# 設定標籤
plt.xlabel("Predicted label", fontsize=16)
plt.ylabel("True label", fontsize=16)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 08_05_confusion_matrix_multiple-categories

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
# ax.set_xticks(range(cm.shape[0]), fontsize=14)
# ax.set_yticks(range(cm.shape[1]), fontsize=14)

# 設定標籤
plt.xlabel("Predicted label", fontsize=16)
plt.ylabel("True label", fontsize=16)
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

print("比較字串的距離")

from sklearn.feature_extraction.text import CountVectorizer

corpus = ["I am a good student", "I am a good teacher", "This is a pencil"]  # 文集

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(corpus).todense()  # 得到文集corpus的特征向量，並將其轉為密集矩陣
print(counts)

""" kilo OK, 但是 sugar不OK
for x,y in [[0,1],[0,2],[1,2]]:
    dist = euclidean_distances(counts[x],counts[y])
    print('文檔{}與文檔{}的距離{}'.format(x,y,dist))
"""

print("比較幾個向量的距離")

# 每個人的特徵向量
vector1 = [1.0, 1.0, 1.0]  # 嫌犯 1 的特徵
vector2 = [0.2, 0.7, 0.2]  # 嫌犯 2 的特徵
vector3 = [0.4, 0.8, 0.9]  # 嫌犯 3 的特徵
vector4 = [0.8, 0.8, 0.3]  # 嫌犯 4 的特徵

# 把特徵向量集合成一個串列，好讓 sklearn 方便直接計算任兩個向量間的相似度
feature_vectors = [vector1, vector2, vector3, vector4]
print("Feature vectors:")
print(feature_vectors)
print()

# 計算任兩個向量間的歐幾里德距離
print("Euclidean distances:")
distances_similarity_metrix = euclidean_distances(feature_vectors)
print(distances_similarity_metrix)
print()

# 計算任兩個向量間的餘弦相似度
print("Cosine similarity:")
cosine_similarity_metrix = cosine_similarity(feature_vectors)
print(cosine_similarity_metrix)
print()

print("------------------------------------------------------------")  # 60個
"""
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

text = ["小貝來到北京清華大學",
        "小花來到了網易杭研大廈",
        "小明碩士畢業于中國科學院",
        "小明愛北京小明愛北京天安門"
        ]
               
corpus = ["小貝 來到 北京 清華大學",
          "小花 來到 了 網易 杭研 大廈",
          "小明 碩士 畢業 于 中國 科學院",
          "小明 愛 北京 小明 愛 北京 天安門"
          ]

print('二值化、詞頻')
vectorizer = CountVectorizer(min_df = 1, binary = True) #Transformer
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)
print(len(features))

print(data.todense())

doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)

print(doc_df)
print(doc_df.columns)

print('------------------------------')	#30個

from sklearn.metrics.pairwise import cosine_similarity

cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index = text, columns = text)
print(sims_df)

print('------------------------------')	#30個

#tf-idf

vectorizer = TfidfVectorizer(min_df = 1)
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)

print('------------------------------')	#30個

pd.set_option('display.precision', 2)
doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)
print(doc_df)

"""

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


print("------------------------------------------------------------")  # 60個

np.random.seed(42)

a = np.random.randn(10)
b = np.random.randn(10)

np.dot(a, b)

print("------------------------------------------------------------")  # 60個

import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pystatsml.plot_utils
import seaborn as sns  # nice color

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
    pystatsml.plot_utils.plot_cov_ellipse(
        Cov[i], pos=mean[i], facecolor="none", linewidth=2, edgecolor=colors[i]
    )

plt.axis("equal")
_ = plt.legend(loc="upper left")

show()

print("------------------------------------------------------------")  # 60個

# Correlation matrix

import matplotlib.pyplot as plt
import seaborn as sns

url = "https://python-graph-gallery.com/wp-content/uploads/mtcars.csv"
df = pd.read_csv(url)

# Compute the correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
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

print("------------------------------------------------------------")  # 60個

# Re-order correlation matrix using AgglomerativeClustering

# convert correlation to distances
d = 2 * (1 - np.abs(corr))

from sklearn.cluster import AgglomerativeClustering

clustering = AgglomerativeClustering(
    n_clusters=3, linkage="single", affinity="precomputed"
).fit(d)
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

import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pystatsml.plot_utils

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
pystatsml.plot_utils.plot_cov_ellipse(
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

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D


def multivariate_normal_pdf(X, mean, sigma):
    """Multivariate normal probability density function over X (n_samples x n_features)"""
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
assert np.allclose(norm, norm_scpy)

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


print("------------------------------------------------------------")  # 60個
