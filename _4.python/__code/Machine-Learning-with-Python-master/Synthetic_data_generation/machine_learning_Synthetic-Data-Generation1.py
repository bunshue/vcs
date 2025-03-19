"""
machine_learning_Synthetic-Data-Generation1

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

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Synthetic Data Generation

# Regression problem generation

from sklearn.datasets import make_regression

data1 = make_regression(
    n_samples=20,
    n_features=4,
    n_informative=2,
    n_targets=1,
    bias=0.0,
    effective_rank=None,
    tail_strength=0.5,
    noise=0.0,
    shuffle=True,
    coef=False,
    random_state=None,
)
df1 = pd.DataFrame(data1[0], columns=["x" + str(i) for i in range(1, 5)])
df1["y"] = data1[1]

df1.head()

plt.figure(figsize=(15, 10))
for i in range(1, 5):
    fit = np.polyfit(df1[df1.columns[i - 1]], df1["y"], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2, 2, i)
    plt.scatter(df1[df1.columns[i - 1]], df1["y"], s=200, c="orange", edgecolor="k")
    plt.plot(df1[df1.columns[i - 1]], fit_fn(df1[df1.columns[i - 1]]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Data with Gaussian noise

data2 = make_regression(
    n_samples=20,
    n_features=4,
    n_informative=2,
    n_targets=1,
    bias=0.0,
    effective_rank=None,
    tail_strength=0.5,
    noise=2.0,
    shuffle=True,
    coef=False,
    random_state=None,
)
df2 = pd.DataFrame(data2[0], columns=["x" + str(i) for i in range(1, 5)])
df2["y"] = data2[1]

plt.figure(figsize=(15, 10))
for i in range(1, 5):
    fit = np.polyfit(df2[df2.columns[i - 1]], df2["y"], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2, 2, i)
    plt.scatter(df2[df2.columns[i - 1]], df2["y"], s=200, c="orange", edgecolor="k")
    plt.plot(df2[df2.columns[i - 1]], fit_fn(df2[df2.columns[i - 1]]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Plot datasets with varying degree of noise

plt.figure(figsize=(15, 6))
df2 = pd.DataFrame(data=np.zeros((20, 1)))
for i in range(3):
    data2 = make_regression(
        n_samples=20,
        n_features=1,
        n_informative=1,
        n_targets=1,
        bias=0.0,
        effective_rank=None,
        tail_strength=0.5,
        noise=i * 10,
        shuffle=True,
        coef=False,
        random_state=None,
    )
    df2["x" + str(i + 1)] = data2[0]
    df2["y" + str(i + 1)] = data2[1]

for i in range(3):
    fit = np.polyfit(df2["x" + str(i + 1)], df2["y" + str(i + 1)], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(1, 3, i + 1)
    plt.scatter(
        df2["x" + str(i + 1)], df2["y" + str(i + 1)], s=200, c="orange", edgecolor="k"
    )
    plt.plot(df2["x" + str(i + 1)], fit_fn(df2["x" + str(i + 1)]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Classification problem generation

from sklearn.datasets import make_classification

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=1.0,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

df3.head()

from itertools import combinations
from math import ceil

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making class separation easy by tweaking class_sep

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=3.0,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

from itertools import combinations
from math import ceil

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making class separation hard by tweaking class_sep

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=0.5,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

from itertools import combinations
from math import ceil

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making data noisy by increasing flip_y

plt.figure(figsize=(18, 10))
for i in range(6):
    data3 = make_classification(
        n_samples=20,
        n_features=4,
        n_informative=4,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=1,
        weights=None,
        flip_y=0.1 * i,
        class_sep=1.0,
        hypercube=True,
        shift=0.0,
        scale=1.0,
        shuffle=False,
        random_state=101,
    )
    df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
    df3["y"] = data3[1]
    plt.subplot(2, 3, i + 1)
    plt.title(f"Plot for flip_y={round(0.1*i,2)}")
    plt.scatter(df3["x1"], df3["x2"], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel("x1", fontsize=14)
    plt.ylabel("x2", fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Plot datasets with varying degree of class separation

plt.figure(figsize=(18, 5))
df2 = pd.DataFrame(data=np.zeros((20, 1)))
for i in range(3):
    data2 = make_classification(
        n_samples=20,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=1,
        weights=None,
        flip_y=0,
        class_sep=i + 0.5,
        hypercube=True,
        shift=0.0,
        scale=1.0,
        shuffle=False,
        random_state=101,
    )
    df2["x" + str(i + 1) + "1"] = data2[0][:, 0]
    df2["x" + str(i + 1) + "2"] = data2[0][:, 1]
    df2["y" + str(i + 1)] = data2[1]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(
        df2["x" + str(i + 1) + "1"],
        df2["x" + str(i + 1) + "2"],
        s=200,
        c=df2["y" + str(i + 1)],
        edgecolor="k",
    )
    plt.grid(True)

show()

print("------------------------------------------------------------")  # 60個

# Clustering problem generation

from sklearn.datasets import make_blobs

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=1.0,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations
from math import ceil

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making clusters compact and easily separable by tweaking cluster_std

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=0.3,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations
from math import ceil

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making clusters spread out and difficult to separate by tweaking cluster_std

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=2.5,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations
from math import ceil

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    plt.subplot(2, ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1, fontsize=14)
    plt.ylabel(var2, fontsize=14)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making anisotropically distributed clustering problem

data5 = make_blobs(n_samples=50, n_features=2, centers=3, cluster_std=1.5)

transformation = [[0.5, -0.5], [-0.4, 0.8]]

data5_0 = np.dot(data5[0], transformation)
df5 = pd.DataFrame(data5_0, columns=["x" + str(i) for i in range(1, 3)])
df5["y"] = data5[1]

plt.figure(figsize=(8, 5))
plt.scatter(df5["x1"], df5["x2"], c=df5["y"], s=200, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making concentric circle clusters

from sklearn.datasets import make_circles

data6 = make_circles(
    n_samples=50, shuffle=True, noise=None, random_state=None, factor=0.6
)
df6 = pd.DataFrame(data6[0], columns=["x" + str(i) for i in range(1, 3)])
df6["y"] = data6[1]

plt.figure(figsize=(8, 5))
plt.scatter(df6["x1"], df6["x2"], c=df6["y"], s=200, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Introdue noise in the circle clusters

data6 = make_circles(
    n_samples=50, shuffle=True, noise=0.15, random_state=None, factor=0.6
)
df6 = pd.DataFrame(data6[0], columns=["x" + str(i) for i in range(1, 3)])
df6["y"] = data6[1]

plt.figure(figsize=(8, 5))
plt.scatter(df6["x1"], df6["x2"], c=df6["y"], s=200, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Make moon shape clusters

from sklearn.datasets import make_moons

data7 = make_moons(n_samples=50, shuffle=True, noise=None, random_state=None)
df7 = pd.DataFrame(data7[0], columns=["x" + str(i) for i in range(1, 3)])
df7["y"] = data7[1]

plt.figure(figsize=(8, 5))
plt.scatter(df7["x1"], df7["x2"], c=df7["y"], s=200, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Introduce noise in the moon-shaped clusters

data7 = make_moons(n_samples=50, shuffle=True, noise=0.1, random_state=None)
df7 = pd.DataFrame(data7[0], columns=["x" + str(i) for i in range(1, 3)])
df7["y"] = data7[1]

plt.figure(figsize=(8, 5))
plt.scatter(df7["x1"], df7["x2"], c=df7["y"], s=200, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Random regression/classification problem generation using symbolic function

from Symbolic_regression_classification_generator import gen_regression_symbolic

# Generate regression data with a symbolic expression of:

data8 = gen_regression_symbolic(
    m="((x1^2)/2-3*x2)+20*sin(x3)", n_samples=50, noise=0.01
)
df8 = pd.DataFrame(data8, columns=["x" + str(i) for i in range(1, 4)] + ["y"])

df8.head()

plt.figure(figsize=(18, 5))
for i in range(1, 4):
    plt.subplot(1, 3, i)
    plt.scatter(df8[df8.columns[i - 1]], df8["y"], s=200, c="orange", edgecolor="k")
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

from Symbolic_regression_classification_generator import gen_regression_symbolic

# Generate regression data with a symbolic expression of:

data8 = 0.1 * gen_regression_symbolic(m="x1^2*sin(x1)", n_samples=200, noise=0.05)
df8 = pd.DataFrame(data8, columns=["x" + str(i) for i in range(1, 2)] + ["y"])

plt.figure(figsize=(8, 5))
plt.scatter(df8["x1"], df8["y"], s=100, c="orange", edgecolor="k")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

from Symbolic_regression_classification_generator import gen_classification_symbolic

# Generate classification data with a symbolic expression of:

data9 = gen_classification_symbolic(
    m="((x1^2)/3-(x2^2)/15)", n_samples=500, flip_y=0.01
)
df9 = pd.DataFrame(data9, columns=["x" + str(i) for i in range(1, 3)] + ["y"])

df9.head()

plt.figure(figsize=(8, 5))
plt.scatter(df9["x1"], df9["x2"], c=df9["y"], s=100, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

from Symbolic_regression_classification_generator import gen_classification_symbolic

# Generate classification data with a symbolic expression of:

data9 = gen_classification_symbolic(m="x1-3*sin(x2/2)", n_samples=500, flip_y=0.01)
df9 = pd.DataFrame(data9, columns=["x" + str(i) for i in range(1, 3)] + ["y"])

plt.figure(figsize=(8, 5))
plt.scatter(df9["x1"], df9["x2"], c=df9["y"], s=100, edgecolors="k")
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Generate name, address, phone number, email etc. using pydbgen package

from pydbgen import pydbgen

generator = pydbgen.pydb()

# Generate a license-plate (US style)
cc = generator.license_plate()
print(cc)
# 'OKY-2318'

""" NG
# Generate few random names
cc = generator.gen_data_series(num=10,data_type='name')
print(cc)
"""

# Generate random phone numbers
cc = generator.simple_ph_num()
print(cc)

# '389-066-8154'
""" NG
cc = generator.gen_data_series(num=10,data_type='phone_number_full')
print(cc)
"""
# Generate a full data frame with random name, street address, SSN, email, date
""" NG
df10 = generator.gen_dataframe(fields=['name','street_address','ssn','email','date'])
print(df10)
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
