"""
MDS


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

# MDS

# 使用美国各大城市距离数据CITY_DISTANCE

df = pd.read_csv("data/CITY_DISTANCE.csv", skipinitialspace=True)
print(df)

df_filled = df.fillna(0)
distance_array = np.array(df_filled.iloc[:, 1:])
cities = distance_array + distance_array.T
# pd.DataFrame(cities)

# 建模

from sklearn.manifold import MDS

mds = MDS(n_components=2, dissimilarity="precomputed", random_state=123)
mds.fit_transform(cities)
mds.stress_

# 350.0770309073701

mds.embedding_


# 绘制感知图

x = mds.embedding_[:, 0]
y = mds.embedding_[:, 1]
plt.scatter(x, y)
for a, b, s in zip(x, y, df["City"]):
    plt.text(a, b, s, fontsize=12)
show()

print("------------------------------------------------------------")  # 60個
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
