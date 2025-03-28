"""
非負矩陣分解 Non-negative Matrix Factorization(NMF)


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

import tensorflow as tf
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.models import model_from_json
from sklearn.metrics import accuracy_score

from sklearn.decomposition import NMF


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

centers = [[5, 10, 5], [10, 4, 10], [6, 8, 8]]
X, _ = datasets.make_blobs(centers=centers)  # centersを中心としたデータを生成
n_components = 2  # 潜在変数の数

model = NMF(n_components=n_components)

model.fit(X)  # 學習訓練.fit

W = model.transform(X)  # 分解後の行列
H = model.components_
print(W)
print(H)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()
iris_X = iris.data  # x有4个属性，共有150个样本点
iris_y = iris.target  # y的取值有3个，分别是0,1,2

NMF = NMF(n_components=2)
NMF.fit(iris_X)

X_new = NMF.transform(iris_X)

# NG plt.scatter(X_new[:], X_new[:], marker='o',c=iris_y)
plt.scatter(X_new[:, 0], X_new[:, 1], marker="o", c=iris_y)
plt.show()

"""
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X_new[:, 0], X_new[:, 1], X_new[:, 2], marker='o',c=iris_y)
plt.show()
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
