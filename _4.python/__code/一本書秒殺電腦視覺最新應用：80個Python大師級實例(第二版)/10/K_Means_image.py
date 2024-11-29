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

from sklearn.cluster import KMeans  # 导入kmeans
from sklearn.utils import shuffle
from skimage import io

import warnings

warnings.filterwarnings("ignore")

print("------------------------------------------------------------")  # 60個

# original = mpl.image.imread('frog.jpg')
original = plt.imread("frog.jpg")
width, height, depth = original.shape
temp = original.reshape(width * height, depth)
temp = np.array(temp, dtype=np.float64) / 255

original_sample = shuffle(temp, random_state=0)[:1000]  # 随机取1000个RGB值作为训练集


def cluster(k):
    estimator = KMeans(n_clusters=k, random_state=9487)  # K-平均演算法, 分成k群
    kmeans = estimator.fit(original_sample)  # 聚类
    return kmeans


def recreate_image(codebook, labels, w, h):
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


kmeans = cluster(32)
labels = kmeans.predict(temp)
kmeans_32 = recreate_image(kmeans.cluster_centers_, labels, width, height)

kmeans = cluster(64)
labels = kmeans.predict(temp)
kmeans_64 = recreate_image(kmeans.cluster_centers_, labels, width, height)

kmeans = cluster(128)
labels = kmeans.predict(temp)
kmeans_128 = recreate_image(kmeans.cluster_centers_, labels, width, height)

plt.figure(figsize=(15, 10))

plt.subplot(221)
plt.imshow(original.reshape(width, height, depth))
plt.title("原始图像")
plt.axis("off")

plt.subplot(222)
plt.imshow(kmeans_128)
# NG io.imsave('kmeans_128.png',kmeans_128)
plt.title("量化的图像(128颜色, K-Means)")
plt.axis("off")

plt.subplot(223)
plt.imshow(kmeans_64)
# NG io.imsave('kmeans_64.png',kmeans_64)
plt.title("量化的图像(64颜色, K-Means)")
plt.axis("off")

plt.subplot(224)
plt.imshow(kmeans_32)
# NG io.imsave('kmeans_32.png',kmeans_32)
plt.title("量化的图像(32颜色, K-Means)")
plt.axis("off")

plt.show()
