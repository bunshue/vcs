"""
PythonMachineLearning-master 01

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
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# K-nearest neighbor Classification

df = pd.read_csv("data/Classified Data", index_col=0)
cc = df.head()
print(cc)

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# Check the spread of the features

l = list(df.columns)
l[0 : len(l) - 2]

for i in range(len(l) - 1):
    sns.boxplot(x="TARGET CLASS", y=l[i], data=df)
    plt.figure()

plt.show()

# Scale the features using sklearn.preprocessing package

# Instantiate a scaler standardizing estimator

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(df.drop("TARGET CLASS", axis=1))
scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

# Train/Test split, model fit and prediction

from sklearn.model_selection import train_test_split

X = df_feat
y = df["TARGET CLASS"]
X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, df["TARGET CLASS"], test_size=0.50, random_state=101
)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

pred = knn.predict(X_test)

# Evaluation of classification quality

from sklearn.metrics import classification_report, confusion_matrix

conf_mat = confusion_matrix(y_test, pred)
print(conf_mat)

print(classification_report(y_test, pred))

print("Misclassification error rate:", round(np.mean(pred != y_test), 3))

# Misclassification error rate: 0.082

# Choosing 'k' by elbow method

error_rate = []

# Will take some time
for i in range(1, 60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10, 6))
plt.plot(
    range(1, 60),
    error_rate,
    color="blue",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=8,
)
plt.title("Error Rate vs. K Value", fontsize=20)
plt.xlabel("K", fontsize=15)
plt.ylabel("Error (misclassification) Rate", fontsize=15)

plt.show()


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
