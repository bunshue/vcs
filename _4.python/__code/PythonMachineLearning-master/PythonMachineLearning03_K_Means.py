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
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# K Means Clustering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get the Data

df = pd.read_csv("data/College_Data", index_col=0)

# Check the head of the data

cc = df.head()
print(cc)

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# Exploratory Analysis

sns.set_style("whitegrid")
sns.lmplot(
    x="Room.Board",
    y="Grad.Rate",
    data=df,
    hue="Private",
    palette="coolwarm",
    aspect=1,
    fit_reg=True,
)
plt.show()


sns.set_style("whitegrid")
sns.lmplot(
    x="Outstate",
    y="F.Undergrad",
    data=df,
    hue="Private",
    palette="coolwarm",
    aspect=1,
    fit_reg=False,
)

plt.show()

sns.boxplot(x="Private", y="S.F.Ratio", data=df)
plt.show()

sns.boxplot(x="Private", y="perc.alumni", data=df)
plt.show()

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Outstate", bins=20, alpha=0.7)

plt.show()

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=0.7)
plt.show()

cc = df[df["Grad.Rate"] > 100]
print(cc)


cc = df["Grad.Rate"]["Cazenovia College"] = 100
print(cc)

cc = df[df["Grad.Rate"] > 100]
print(cc)

sns.set_style("darkgrid")
g = sns.FacetGrid(df, hue="Private", palette="coolwarm", aspect=2)
g = g.map(plt.hist, "Grad.Rate", bins=20, alpha=0.7)
plt.show()

# K Means Cluster Creation

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, verbose=0, tol=1e-3, max_iter=300, n_init=20)

kmeans.fit(df.drop("Private", axis=1))

clus_cent = kmeans.cluster_centers_
print(clus_cent)

cc = df[df["Private"] == "Yes"].describe()  # Statistics for private colleges only
print(cc)

cc = df[df["Private"] == "No"].describe()  # Statistics for public colleges only
print(cc)

df_desc = pd.DataFrame(df.describe())
feat = list(df_desc.columns)
kmclus = pd.DataFrame(clus_cent, columns=feat)
print(kmclus)

# What are the cluster labels?

print(kmeans.labels_)

# Evaluation


def converter(cluster):
    if cluster == "Yes":
        return 1
    else:
        return 0


df1 = df  # Create a copy of data frame so that original data frame does not get 'corrupted' with the cluster index
df1["Cluster"] = df["Private"].apply(converter)

cc = df1.head()
print(cc)

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(df1["Cluster"], kmeans.labels_))
print(classification_report(df1["Cluster"], kmeans.labels_))

# Clustering performance (e.g. distance between centroids)

df_pvt = df[df["Private"] == "Yes"]
df_pub = df[df["Private"] == "No"]

kmeans = KMeans(n_clusters=2, verbose=0, tol=1e-3, max_iter=50, n_init=10)
kmeans.fit(df.drop("Private", axis=1))
clus_cent = kmeans.cluster_centers_
df_desc = pd.DataFrame(df.describe())
feat = list(df_desc.columns)
kmclus = pd.DataFrame(clus_cent, columns=feat)
a = np.array(kmclus.diff().iloc[1])

centroid_diff = pd.DataFrame(
    a, columns=["K-means cluster centroid-distance"], index=df_desc.columns
)

""" NG
centroid_diff['Mean of corresponding entity (private)']=np.array(df_pvt.mean())
centroid_diff['Mean of corresponding entity (public)']=np.array(df_pub.mean())
print(centroid_diff)
"""


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
