"""
其他

# 下載資料集, 讀取數據集
from sklearn.datasets import fetch_20newsgroups
#news = fetch_20newsgroups(data_home=download_directory, subset="all")
news = fetch_20newsgroups(subset="all")

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

"""
#Ames房價 愛俄華州的一個城市
from sklearn.datasets import fetch_openml
housing = fetch_openml(name="house_prices", as_frame=True)

"""
from sklearn.datasets import fetch_openml

housing = fetch_openml(name="house_prices", as_frame=True)
print(housing)

sns.set(rc={"figure.figsize": (11.7, 8.27)})
sns.histplot(housing.MedHouseVal, bins=30)

plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用PCA及KernelPCA進行影像去躁
# KernelPCA_image_denoising

from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler

# 載入資料

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
cc = X.shape
print(cc)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

# 加躁
rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise

# 繪製原圖及加入雜訊的影像


# 繪圖函數
def plot_digits(X, title):
    """Small helper function to plot 100 digits."""
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)


# 繪製原圖
plot_digits(X_test, "原圖")
plot_digits(X_test_noisy, f"加躁\nMSE: {np.mean((X_test - X_test_noisy) ** 2):.2f}")
plt.show()

# PCA及Kernel PCA 轉換

from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

pca = PCA(n_components=32)
kernel_pca = KernelPCA(
    n_components=400, kernel="rbf", gamma=1e-3, fit_inverse_transform=True, alpha=5e-3
)

pca.fit(X_train_noisy)  # 學習訓練.fit

_ = kernel_pca.fit(X_train_noisy)  # 學習訓練.fit

# 使用 inverse_transform 重建影像

X_reconstructed_kernel_pca = kernel_pca.inverse_transform(
    kernel_pca.transform(X_test_noisy)
)
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test_noisy))

# PCA 重建影像繪圖

plot_digits(
    X_reconstructed_pca,
    f"PCA reconstruction\nMSE: {np.mean((X_test - X_reconstructed_pca) ** 2):.2f}",
)
plt.show()

# Kernel PCA 重建影像繪圖

plot_digits(
    X_reconstructed_kernel_pca,
    "Kernel PCA reconstruction\n"
    f"MSE: {np.mean((X_test - X_reconstructed_kernel_pca) ** 2):.2f}",
)
plt.show()

# 結論：PCA雖然比 Kernel PCA 的MSE小，但 Kernel PCA 去躁效果比較好

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
