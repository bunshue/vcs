"""


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

# Time-profiling

# Time-profiling Data Science code using cProfile

import cProfile

SIZE = 10_000_000
a = np.arange(SIZE)
b = np.random.normal(size=SIZE)

cProfile.run('a+b')

print("------------------------------")  # 60個

code = """SIZE = 10_000_000
a = np.arange(SIZE)
b = np.random.normal(size=SIZE)
a+b"""

print(code)

cProfile.run(code)

print("------------------------------")  # 60個

def add():
    SIZE = 10_000_000
    a = np.arange(SIZE)
    b = np.random.normal(size=SIZE)
    c=a+b

cProfile.run('add()')

print("------------------------------")  # 60個

def add(size):
    a = np.arange(size)
    b = np.random.normal(size=size)
    c=a+b

SIZE = 10_000_000
cProfile.run('add(SIZE)')

print("------------------------------")  # 60個

SIZE = 20_000_000
cProfile.run('add(SIZE)')

print("------------------------------")  # 60個

def ops(a,b):
    x1 = a+b
    x2 = a-b
    x3 = a*b
    x4 = a/b

cProfile.run('ops(a,b)')

print("------------------------------")  # 60個

import cProfile
import pstats

profiler = cProfile.Profile()
# Enable profiler
profiler.enable()
# Function execution
add(SIZE)
# Disable profiler
profiler.disable()
# pstats
stats = pstats.Stats(profiler)
# Print the total time and function calls
print("Total function calls:", stats.total_calls)
print("Total time (seconds):", stats.total_tt)

#Total function calls: 48
#Total time (seconds): 1.1839559

stats = pstats.Stats(profiler)
stats.print_stats()

type(stats)

#pstats.Stats

stats.total_tt

#1.1839559

stats.fcn_list

size = [int(i*1e6) for i in range(5,26,5)]
total_tt = []
for s in size:
    profiler = cProfile.Profile()
    profiler.enable()
    add(s)
    profiler.disable()
    stats = pstats.Stats(profiler)
    total_tt.append(round(stats.total_tt,3))       

total_tt

[0.274, 0.464, 0.706, 0.94, 1.187]

plt.figure(figsize=(6,3),dpi=120)
plt.bar(x=[str(i)+'-million' for i in range(5,26,5)],
        height=total_tt, 
        edgecolor='k',
        color="#2c75b0")
plt.xlabel("Array size", fontsize=16)
plt.ylabel("Time taken (seconds)",fontsize=16)

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
