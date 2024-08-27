"""
海生, 自動把圖畫得比較好看

sns.set() 繪圖風格設置

"""

print("------------------------------------------------------------")  # 60個

import sys
import numpy as np
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個
'''
print('無海生')

plt.plot(x, y)
plt.title("no seaborn")
plt.show()
'''
print("------------------------------------------------------------")  # 60個

print('前面加兩行變海生, 引用與設定')

import seaborn as sns  # 海生, 自動把圖畫得比較好看
#sns.set()
#sns.set(color_codes=True)
sns.set(rc={"figure.figsize": (12, 8)})

plt.plot(x, y)
plt.title("seaborn")
plt.show()

sys.exit()

print("------------------------------------------------------------")  # 60個

print('用海生的函數畫圖')

N = 1000
x = np.random.randn(N)
#print(np.mean(x))

print('海生函數 lineplot')
sns.lineplot(data=y)

#print('海生函數 histplot')
#sns.histplot(x, kde=False)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
# 平均值 μ, 標準差 σ

μ = 87
σ = 2.5

eggs = np.random.randn(100) * σ + μ

# 我們來檢查這樣生出的平均值、標準差是不是我們想的那樣。

print("平均值 :", eggs.mean())
# 87.3032349761459

print("標準差 :", eggs.std())
# 2.411544933383249

import seaborn as sns

sns.distplot(eggs)
plt.show()
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 一般畫圖 vs 海生畫圖

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
x = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)
plt.title("用海生畫常態分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.random.uniform(size=N)  # 隨機數

n, bins, patches = plt.hist(
    x, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(x)

plt.title("用海生畫均勻分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 10000 # 樣本數
mu = 0  # 平均值
sigma = 1  # 標準差

x1 = np.random.randn(N)  # 隨機數
x2 = np.random.uniform(size=N)  # 隨機數

left = -2
peak = 8  # mode尖峰值
right = 10
x3 = np.random.triangular(left, peak, right, N)

bins = 50 # 束

plt.figure(figsize=(12, 6))

plt.subplot(131)

count, bins, ignored = plt.hist(x1, bins, density=True)  # 直方圖
sns.kdeplot(x1)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(132)

plt.hist(x2, bins, density=True)  # 直方圖
sns.kdeplot(x2)  # 核密度估計圖, 多了外圍那圈
plt.title("均勻分布 + kdeplot")

plt.subplot(133)

plt.hist(x3, bins, density=True)
#sns.kdeplot(x3)  # 核密度估計圖, 多了外圍那圈
plt.title("np.random.triangular")

#用density
#plt.hist(x3, bins, density=True)

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import seaborn as sns  # 海生, 自動把圖畫得比較好看

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

font_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_font/TaipeiSansTCBeta-Regular.ttf"
)

import matplotlib as mpl
import matplotlib.font_manager as fm

fm.fontManager.addfont(font_filename)
mpl.rc("font", family="Taipei Sans TC Beta")

x = np.linspace(-5, 5, 200)
y = np.sinc(x)

plt.plot(x, y)
plt.title("原圖, 無海生")
plt.show()

# 把預設狀態存起來
saved_state = mpl.rcParams.copy()

# plt.xkcd()  #加此行變成搞笑風格

# 多此三行 變成海生風格
import seaborn as sns

sns.set()
plt.rcParams[
    "font.sans-serif"
] = "Microsoft JhengHei"  # 海生設定中文字型 將字體換成 Microsoft JhengHei

plt.plot(x, y)
plt.title("使用海生")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.plot(x, y)
plt.title("再畫一新圖, 還是海生風格")
plt.show()

print("------------------------------------------------------------")  # 60個

mpl.rcParams.update(saved_state)

plt.plot(x, y)
plt.title("恢復成原風格, 無海生")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.xlabel("銷售張數")
plt.ylabel("成功次數")
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)
#sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.title("二項式分布 Binomial")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#sns折線圖的繪製範例
#sns.set(style="whitegrid", font="meiryo")



# 繪製折線圖
#sns.set(style="white", font="meiryo")



# 調整資料的格式
#sns.set(style="white", font="meiryo") 
#sns.set(style="white", font="meiryo") 

ax.legend(loc="lower left", bbox_to_anchor=(1, 0))


