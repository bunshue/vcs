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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#把鳶尾花的資料集讀進來

iris = load_iris()

#確認一下資料集的描述

print(iris.DESCR) 

#分好 features 跟 target
X = iris.data
Y = iris.target

#照著題目的說明，只拿花萼的 features 來用
#分好訓練跟測試資料，再把「正確答案」的分佈畫一下做個確認

X = X[:, :2]
x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size = 0.2,
                                                    random_state = 87)

plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.show()


#設定一個 SVM 的函數學習機，把訓練資料放進去 train

from sklearn.svm import SVC
clf = SVC()
clf.fit(x_train, y_train)

"""
SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,    decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,    max_iter=-1, probability=False, random_state=None, shrinking=True,
,    tol=0.001, verbose=False)
"""

#稍微瞄一下預測結果跟正確答案的差距，發現大致上做得還不錯！
#而且好像比原本用花瓣的 features 還要好！
#選擇 features 真的很重要！

y_predict = clf.predict(x_test)
print(y_predict - y_test)
y_predict-y_test

"""
array([ 0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,
,        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1])
"""

#當然要畫個圖看一下，這樣還可以確認哪些特殊的情況下模型會分不好
plt.scatter(x_test[:, 0], x_test[:, 1], c = y_predict - y_test)
plt.show()

#也可以畫這種的

y_predict = clf.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c = y_predict)
plt.show()

#照著題目的說明，換另一種 SVM 來試試看

from sklearn.svm import NuSVC
clf1 = NuSVC()
clf1.fit(x_train, y_train)

"""
NuSVC(break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,      decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,      max_iter=-1, nu=0.5, probability=False, random_state=None, shrinking=True,
,      tol=0.001, verbose=False)
"""

"""
嗚，好像變差了
但這件事告訴我們，不同的模型在不同的參數情況下，
也會學出不同的結果跟好壞，
因此適時的做實驗調整模型跟參數也是很重要的！
"""

y_predict = clf1.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c = y_predict - y_test)

plt.show()

print("------------------------------------------------------------")  # 60個

# 下面幾個操作都跟之前一樣，只是我們把所有的特徵都拿來用了

from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target

# 只是這次的函數學習機是 k-Means！
# 叫它自己想辦法分三類

from sklearn.cluster import KMeans

clf = KMeans(n_clusters=3)
clf.fit(X)

"""
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
,       n_clusters=3, n_init=10, n_jobs=None, precompute_distances='auto',
,       random_state=None, tol=0.0001, verbose=0)
"""
# 花瓣長和花瓣寬對結果的影響分布
plt.scatter(X[:, 2], X[:, 3], c=clf.labels_)
plt.show()

# 花萼長和花萼寬對結果的影響分布
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
plt.show()

# 跟前面 SVM 的結果好像還真的有點像
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X_SVM = X[:, :2]
x_train, x_test, y_train, y_test = train_test_split(
    X_SVM, Y, test_size=0.2, random_state=87
)
clf = SVC()
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)

plt.show()

# 來做一份模擬的資料

X = np.random.rand(50, 2)

# 當然要畫出來看一下

plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()

# 雖然還是叫 K-Means 當函數學習機，
# 讓它分四類，但這次真的沒有答案了
from sklearn.cluster import KMeans

clf = KMeans(n_clusters=4)
clf.fit(X)
"""
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
,       n_clusters=4, n_init=10, n_jobs=None, precompute_distances='auto',
,       random_state=None, tol=0.0001, verbose=0)
"""
# 畫出來看一下結果，好像還真得有模有樣的
plt.scatter(X[:, 0], X[:, 1], c=clf.labels_)
plt.show()

# 放一些新的資料進去看看，點變多了！
a = np.random.rand(20, 2)
X_add = np.row_stack((X, a))
plt.scatter(X_add[:, 0], X_add[:, 1])
plt.show()

# 看一看我們的 k-Means 分的怎麼樣
predict_label = clf.predict(X_add)
plt.scatter(X_add[:, 0], X_add[:, 1], c=predict_label)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# -------------------------------------------------------------------------------

# 鳶尾花 Iris 數據集

from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

X = x[:, :2]
Y = y

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("原始資料")
plt.show()

from sklearn.svm import SVC

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

Ypred = clf.predict(x_test)

print(Ypred - y_test)

x0 = np.linspace(3.8, 8.2, 500)
y0 = np.linspace(1.8, 4.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()


# PCA 可以救鳶尾花嗎？

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)

# 我們稍稍的「欣賞一下」 PCA 對我們的資料集做了什麼，來看看某朵鳶尾花的資料。
# pca.transform([[6.3, 2.3, 4.4, 1.3]])
# 真的變成平面上一個點！來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
plt.show()

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


print(x[87])

print(y[87])

print(pca.transform([[6.3, 2.3, 4.4, 1.3]]))

print(clf.predict([[0.81509524, -0.37203706]]))

print(X.shape)

# print(Z.reshape(X.shape))


# 畫完整分類
# 和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
plt.show()

x1, x2 = np.meshgrid(np.arange(-0.2, 1.2, 0.02), np.arange(-0.2, 1.2, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=100, c=clf.labels_)
plt.show()

# 呈現出來
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], c=clf.labels_)
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


