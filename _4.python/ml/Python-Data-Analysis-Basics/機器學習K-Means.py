"""
機器學習 K-Means

K-Means 自動分類

"""

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

plt.figure(
    num="K-Means",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# K-Means 會自動分類!
# 我們介紹一個很好用的 unsupervised learning, 叫 K-Means。
# 我們可以指定把我們資料分成幾類, 然後它就會快速分好!

# 生成任意 N 點
N = 100
x = np.random.rand(N, 2)  # N X 2 亂數陣列

print(x.shape)
print(x)
plt.subplot(131)
# plt.scatter(x[:, 0], x[:, 1], s = 50)
plt.scatter(x[:, 0], x[:, 1], cmap="Paired")
plt.title("原始資料")

# step 1: 製做一個 K-Means 分類器
# 和 SVM 很像。

from sklearn.cluster import KMeans

# 記得要告訴 K-Means 要分成幾類 (我們這裡是 3 類)
clf = KMeans(n_clusters=3)

# step 2: fit 學習、訓練 注意這時沒有「正確答案」
clf.fit(x)

# step 3: 預測
# 訓練好的結果, 在神秘的 labels_ 之下。
Z = clf.labels_
print("訓練好的結果1 :")
print(Z)

# 當然我們還是有 predict, 所以也可以用 predict 預測,
# 但這電腦自己分的, 答案自然 100% 相同!
print(clf.predict(x))

y_prd = clf.predict(x)

# 我們可以檢查一下, 確認答案是不是真的一樣!
print(np.array_equal(clf.labels_, clf.predict(x)))

plt.subplot(132)
plt.scatter(x[:, 0], x[:, 1], s=50, c=Z)
plt.title("訓練好的結果1")

# 預測函數 predict

x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.subplot(133)
plt.contourf(xm, ym, Z, alpha=0.3)
# plt.scatter(x[:, 0], x[:, 1], c = clf.labels_)
plt.scatter(x[:, 0], x[:, 1], s=50, c=clf.labels_, cmap="Paired")
plt.title("訓練好的結果2")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="Means Shift",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# Mean Shift
# Mean Shift 也會自動分類
# 有時我們甚至不想告訴電腦, 你自動分類應該分成幾類。這時 Mean Shift 可以幫我們。

from sklearn.cluster import MeanShift

# step 1: 打開 MeanShift 函數學習機, 這裡的 bandwidth 是控制分類要寬鬆一點, 還是嚴一點
clf = MeanShift(bandwidth=0.2)

# step 2: fit 學習、訓練
clf.fit(x)

# step 3: predict
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)

plt.subplot(231)
plt.scatter(x[:, 0], x[:, 1], c=clf.labels_, cmap="Paired")
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
plt.title("使用Mean Shift")

print("------------------------------------------------------------")  # 60個


# 觀察 bandwidth 對分類的影響。
def my_mean_shift(b=0.2):
    clf = MeanShift(bandwidth=b)
    clf.fit(x)

    x0 = y0 = np.arange(-0.2, 1.2, 0.02)
    xm, ym = np.meshgrid(x0, y0)

    P = np.c_[xm.ravel(), ym.ravel()]
    z = clf.predict(P)
    Z = z.reshape(xm.shape)

    plt.scatter(x[:, 0], x[:, 1], c=clf.labels_, cmap="Paired")
    plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")


plt.subplot(232)
my_mean_shift(0.2)  # (0.1, 0.3, 0.02)

# 畫完整分類
# 和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])
gdc = clf.predict(gd)

plt.subplot(233)
plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.coolwarm, c=gdc)
plt.title("訓練好的結果2")

plt.subplot(234)
plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.prism, c=gdc)
plt.title("訓練好的結果3")

plt.subplot(235)
plt.scatter(gd[:, 0], gd[:, 1], s=50, cmap=plt.cm.Set1, c=gdc)
plt.title("訓練好的結果4")


# 畫完整分類
# 和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

x1, x2 = np.meshgrid(np.arange(-0.2, 1.2, 0.02), np.arange(-0.2, 1.2, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
z = Z.reshape(x1.shape)
plt.subplot(236)
plt.contourf(x1, x2, z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=100, c=clf.labels_)
plt.title("畫完整分類")

plt.show()

print("------------------------------------------------------------")  # 60個

import pickle

f = open("clf.pkl", "wb")
pickle.dump(clf, f)
f.close()

f = open("clf.pkl", "rb")
clf2 = pickle.load(f)
print(clf2.predict([[3, 4]]))

f.close()

print("------------------------------------------------------------")  # 60個

"""
4. K-Means 是神奇的自動分類機

我們來學一個「非監督式」的學習, 也就是我們沒有「標準答案」, 但要讓機器做出來。
比如說我們有一堆資料, 不知怎麼分類, 現在我們想叫電腦去分, 只告訴他要分幾類...
然後 1, 2, 3! 就神奇的分好了!
"""

# 生成任意 N 點
N = 100
x = np.random.randn(N, 2)  # N X 2 常態亂數陣列

# 看一下我們的資料。
plt.scatter(x[:, 0], x[:, 1], s=50)
plt.title("原始資料")
plt.show()

# 到現在我們有點熟了, 就是要把 KMeans 函數學習機找來。

from sklearn.cluster import KMeans

# 然後打開一台「KMeans 函數學習機」。這次我們第一次設參數! 那是因為我們至少要讓 KMeans 學習機知道要分幾類。

clf = KMeans(n_clusters=3)

# 接著一樣是訓練。注意現在我們沒有標準答案, 所以只有 x 的資料。

clf.fit(x)

# 分類好的結果 KMeans 會神秘的放在 clf.labels_
print(clf.labels_)

# 畫出分類結果
plt.scatter(x[:, 0], x[:, 1], c=clf.labels_)
plt.title("分類結果")
plt.show()


# 看來還不錯! 我們仿之前 SVC 中介紹的畫法, 看 KMeans 到底怎麼分的。
x1, y1 = np.meshgrid(np.arange(-3, 3, 0.02), np.arange(-4, 4, 0.02))
Z = clf.predict(np.c_[x1.ravel(), y1.ravel()])
Z = Z.reshape(x1.shape)
plt.scatter(x[:, 0], x[:, 1], s=70, c=clf.labels_)
plt.contourf(x1, y1, Z, alpha=0.3)
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
