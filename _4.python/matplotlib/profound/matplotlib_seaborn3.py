"""

一般畫圖 vs 海生畫圖

"""

import seaborn as sns  # 海生, 自動把圖畫得比較好看

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數


print("另外用海生畫出來")

import seaborn as sns  # 海生, 自動把圖畫得比較好看

mu, sigma = 100, 15 # 平均值, 標準差
x = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)
plt.title("用海生畫常態分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

import seaborn as sns  # 海生, 自動把圖畫得比較好看

x = np.random.uniform(size=N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)
plt.title("用海生畫均勻分佈")

plt.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
