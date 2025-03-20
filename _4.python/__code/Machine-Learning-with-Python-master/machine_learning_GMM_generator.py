"""
GMM_generator

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

# Synthesizing a Gaussian Mixture Model (GMM) dataset

# The generating function


def gen_GMM(N=1000, n_comp=3, mu=[-1, 0, 1], sigma=[1, 1, 1], mult=[1, 1, 1]):
    """
    Generates a Gaussian mixture model data, from a given list of Gaussian components
    N: Number of total samples (data points)
    n_comp: Number of Gaussian components
    mu: List of mean values of the Gaussian components
    sigma: List of sigma (std. dev) values of the Gaussian components
    mult: (Optional) list of multiplier for the Gaussian components
    """
    assert n_comp == len(
        mu
    ), "The length of the list of mean values does not match number of Gaussian components"
    assert n_comp == len(
        sigma
    ), "The length of the list of sigma values does not match number of Gaussian components"
    assert n_comp == len(
        mult
    ), "The length of the list of multiplier values does not match number of Gaussian components"
    rand_samples = []
    for i in range(N):
        pivot = random.uniform(0, n_comp)
        j = int(pivot)
        rand_samples.append(mult[j] * random.gauss(mu[j], sigma[j]))

    return np.array(rand_samples)


# Testing the function including AssertionError

cc = gen_GMM(10)
print(cc)

""" NG
cc = gen_GMM(N=10,n_comp=4,mu=[1,2,0],sigma=[1,1,1,2])
print(cc)

gen_GMM(N=10,n_comp=4,mu=[1,2,0,-1],sigma=[1,1,2])
"""

# Data and plot examples

data = gen_GMM(N=100, mu=[-6, 0, 6])

plt.scatter(x=np.arange(100), y=data, color="k")
plt.grid(True)
show()

data = gen_GMM(N=10000, mu=[-6, 0, 6])

sns.distplot(
    data,
    bins=50,
    hist_kws={"color": "blue", "edgecolor": "k"},
    kde_kws={"lw": 3, "color": "k"},
)
show()

data = gen_GMM(N=10000, mu=[-3, 0, 3])

sns.distplot(
    data,
    bins=50,
    hist_kws={"color": "blue", "edgecolor": "k"},
    kde_kws={"lw": 3, "color": "k"},
)
show()

data = gen_GMM(N=10000, mu=[-5, 0, 5], sigma=[1, 2, 1.5])

sns.distplot(
    data,
    bins=50,
    hist_kws={"color": "blue", "edgecolor": "k"},
    kde_kws={"lw": 3, "color": "k"},
)
show()

data = gen_GMM(N=10000, mu=[-5, 0, 5], sigma=[1.8, 0.3, 1.1], mult=[0.7, 1.8, 1.1])

sns.distplot(
    data,
    bins=50,
    hist_kws={"color": "blue", "edgecolor": "k"},
    kde_kws={"lw": 3, "color": "k"},
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


print("------------------------------------------------------------")  # 60個
