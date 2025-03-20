"""
Synth_Time_series

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

# Synthesizing time series data

# Functions


# cylinder bell funnel based on "Learning comprehensible descriptions of multivariate time series"
def generate_bell(length, amplitude, default_variance):
    bell = (
        np.random.normal(0, default_variance, length)
        + amplitude * np.arange(length) / length
    )
    return bell


def generate_funnel(length, amplitude, default_variance):
    funnel = (
        np.random.normal(0, default_variance, length)
        + amplitude * np.arange(length)[::-1] / length
    )
    return funnel


def generate_cylinder(length, amplitude, default_variance):
    cylinder = np.random.normal(0, default_variance, length) + amplitude
    return cylinder


std_generators = [generate_bell, generate_funnel, generate_cylinder]


def generate_pattern_data(
    length=100,
    avg_pattern_length=5,
    avg_amplitude=1,
    default_variance=1,
    variance_pattern_length=10,
    variance_amplitude=2,
    generators=std_generators,
    include_negatives=True,
):
    data = np.random.normal(0, default_variance, length)
    current_start = random.randint(0, avg_pattern_length)
    current_length = current_length = max(
        1, math.ceil(random.gauss(avg_pattern_length, variance_pattern_length))
    )

    while current_start + current_length < length:
        generator = random.choice(generators)
        current_amplitude = random.gauss(avg_amplitude, variance_amplitude)

        while current_length <= 0:
            current_length = -(current_length - 1)
        pattern = generator(current_length, current_amplitude, default_variance)

        if include_negatives and random.random() > 0.5:
            pattern = -1 * pattern

        data[current_start : current_start + current_length] = pattern

        current_start = (
            current_start + current_length + random.randint(0, avg_pattern_length)
        )
        current_length = max(
            1, math.ceil(random.gauss(avg_pattern_length, variance_pattern_length))
        )

    return np.array(data)


# Generate time series and plot

n_data = [50, 150, 500]
n_pattern_length = [5, 10, 20]

from itertools import product

config_ = list(product(n_data, n_pattern_length))

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 9))
ax = axes.ravel()
i = 0
for n1, n2 in config_:
    data = generate_pattern_data(length=n1, avg_pattern_length=n2)
    ax[i].plot(data, color="k")
    ax[i].grid(True)
    i += 1
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
