"""
Naive_Bayes_Practice

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

df = pd.read_csv("data/wine.data.csv")
df.head(10)

# df.iloc[:,1:].describe()

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4), fontsize=14)
    plt.title("{}\n".format(c), fontsize=16)
    plt.xlabel("Wine Class", fontsize=16)
    plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["OD280/OD315 of diluted wines"],
    df["Flavanoids"],
    c=df["Class"],
    edgecolors="k",
    alpha=0.8,
    s=100,
)
plt.grid(True)
plt.title(
    "Scatter plot of two features showing the \ncorrelation and class seperation",
    fontsize=15,
)
plt.xlabel("OD280/OD315 of diluted wines", fontsize=15)
plt.ylabel("Flavanoids", fontsize=15)
plt.show()


def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation\n", fontsize=15)
    labels = df.columns
    ax1.set_xticklabels(labels, fontsize=9)
    ax1.set_yticklabels(labels, fontsize=9)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    plt.show()


cc = correlation_matrix(df)
print(cc)

# Naive Bayes Classification

from sklearn.model_selection import train_test_split

test_size = 0.3  # Test-set fraction

X = df.drop("Class", axis=1)
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

X_train.shape

(124, 13)

X_train.head()

# Classification using GaussianNB

from sklearn.naive_bayes import GaussianNB

nbc = GaussianNB()

nbc.fit(X_train, y_train)

GaussianNB(priors=None)

# Prediction, classification report, and confusion matrix

y_pred = nbc.predict(X_test)
mislabel = np.sum((y_test != y_pred))
print(
    "Total number of mislabelled data points from {} test samples is {}".format(
        len(y_test), mislabel
    )
)

# Total number of mislabelled data points from 54 test samples is 2

from sklearn.metrics import classification_report

print("The classification report is as follows...\n")
print(classification_report(y_pred, y_test))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
cmdf = pd.DataFrame(
    cm,
    index=["Class 1", "Class 2", " Class 3"],
    columns=["Class 1", "Class 2", " Class 3"],
)
print("The confusion matrix looks like following...\n")
cmdf

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
