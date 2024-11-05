"""

鳶尾花

鳶尾花 (Iris) 數據庫是很有名的資料, 就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。

標準的分類問題: 這是哪種鳶尾花

鳶尾花 (Iris)  數據庫是很有名的資料,
就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。

我們現在來看看, 可不可以讓電腦辨識, 這是哪個亞種的鳶尾花?

在 sklearn.datasets 有幾個數據庫可以提供給大家玩玩。

以Iris dataset為例，鳶尾花資料集是非常著名的生物資訊資料集之一，
取自美國加州大學歐文分校的機器學習資料庫http://archive.ics.uci.edu/ml/datasets/Iris
資料的筆數為150筆，共有五個欄位：
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。

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

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Iris 鳶尾花數據庫 150筆資料 4個欄位 3種品種 每種50筆資料
iris = load_iris()

"""
print("另存新檔");
filename = 'aaaa.csv'
np.savetxt(filename, iris.data, delimiter=',')
print("寫入完成")
"""

print("看鳶尾花數據庫的說明")
print(iris.DESCR)

print("看鳶尾花數據庫的features")
print(iris.feature_names)

# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# 有四個 features: 花萼長度、花萼寬度 和 花瓣長度、花瓣寬度
# sepal 花萼
# petal  花瓣

print(iris.data)
print(type(iris.data))
print(len(iris.data))
print(iris.data.shape)
print(iris.data[5])  # 第5筆資料
print(iris.data[:5])  # 前5筆資料
print("答案")
print(iris.target)

"""
#debug 10筆資料
iris.data = iris.data[45:55]
iris.target = iris.target[45:55]
"""
"""
#debug 10筆資料
irisdata = [[5.1, 3.5, 1.4, 0.2],
            [4.9, 3.0, 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            [7.0, 3.2, 4.7, 1.4],
            [6.4, 3.2, 4.5, 1.5],
            [6.9, 3.1, 4.9, 1.5],
            [6.3, 2.5, 5.0, 1.9],
            [6.5, 3.0, 5.2, 2.0],
            [6.2, 3.4, 5.4, 2.3],
            [5.9, 3.0, 5.1, 1.8]]
iris.data = np.array(irisdata)
iristarget = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]
iris.target = np.array(iristarget)
"""

"""
print('data')
print(iris.data)
print('target')
print(iris.target)
"""

print("共有 :", len(iris.data), "筆資料")

# 資料內容
# 這些數據中, data 就是我們的 x (輸入), target 是 y (輸出)。
# 輸入的數據四個 features 是: 花萼長度、花萼寬度、花瓣長度、花瓣寬度。
# print(iris.data)   many

# 輸出就是某筆數據是哪種 (事實上是哪個亞屬) 的鳶尾花, 共分為 0, 1, 2 三種。
# print(iris.target)

# 只用部份 features
# 我們只選用花萼長度、花萼寬度 (當然只是例子, 事實上四個參數很少, 全部一起來也可以) 當輸入資料。
# 準備輸入及輸出數據, 注意 4 個特徵我們只用了兩個。

# :2 是 前兩個 => 花萼
# 2: 是 第2個(含)以後 => 花瓣

# 準備 inputs 和 outputs
x = iris.data
y = iris.target

# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 只選兩個 features 原因之一是好畫 :)

plt.scatter(X[:, 0], X[:, 1], c="pink", s=150)
plt.scatter(X[:, 0], X[:, 1], s=50, c=Y, alpha=0.6)
plt.title("花瓣 原始資料")
plt.show()

# 試著用我們學過的方式, 看能不能做出一個分類器函數, 來把鳶尾花正確分類!

# 準備 inputs 和 outputs
x = iris.data
y = iris.target

# 為了表示我們很神 (事實上只是好畫圖), 我們只用兩個 features (花瓣長度、寬度)。
# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 切分訓練及測試資料。
# 用 80% 當訓練資料, 留 20% 看我們做得如何?
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=87
)

# 看一下整筆數據的分佈。
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("花瓣 原始資料")
plt.show()

# 看訓練結果
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.title("花瓣 訓練資料")
plt.show()

# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 開個分類機、訓練
# 再一次, 三部曲打造函數學習機。
# 第一部曲：打開一台函數學習機

from sklearn.svm import SVC

clf = SVC()

# 第二部曲：訓練
clf.fit(x_train, y_train)

# 第三部曲：預測
y_predict = clf.predict(x_test)

print("看看我們模型預測和真實狀況差多少?")
print(y_predict - y_test)

# 看看有沒有不準的?
y_predict = clf.predict(x_test)

# 這時因為如果答對了, 我們和正確答案相減就是 0。學得不錯就會大部份是 0, 錯的不是 0 畫出來就會不同色。我們來試試看。
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)
plt.title("看差值")
plt.show()

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)
plt.title("看最後預測結果")
plt.show()


# 現在我們做的是讓平面上密密麻麻的點都去看它會是哪種鳶尾花的數據。

x1, y1 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))

# 記得 x1, y1 是什麼樣子的, 我們要拉平之後 (x1_ravel(), y1_ravel()), 再用 np.c_ 合成一點一點的, 才可以送進去預測。

Z = clf.predict(np.c_[x1.ravel(), y1.ravel()])

# 好奇的話可以看看我們到底送了多少點進去?

print(len(x1.ravel()))

# 52500

# 等一下我們要用 contourf 做填充型的等高線, 每一點的「高度」就是我們的 SVC 學習機判斷鳶尾花的亞種。但用 contourf 輸入的格點是前面 meshgrid 後的 x1, y1, 而高度 Z 也是要用同樣的型式。

Z = Z.reshape(x1.shape)

# 於是我們終於可以畫圖了...

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
plt.contourf(x1, y1, Z, alpha=0.3)
plt.show()


# 這是測試資料, 之前我們已經知道我們全對!
# 不如就來看看所有鳶尾花資料我們 SVC 的表現。

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.contourf(x1, y1, Z, alpha=0.3)
plt.show()

# 在測試資料中是全對!! 我們畫圖來看看整體表現如何?
# 畫出結果
x0 = np.linspace(0, 7.5, 500)
y0 = np.linspace(0, 2.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:, 0], X[:, 1], c=Y)

plt.show()

x0 = np.linspace(3, 8, 500)
y0 = np.linspace(1.5, 4.5, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()

# 畫出結果
x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()

x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
np.c_[xx, yy]
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.title("更炫的畫圖法")
plt.show()


"""
X, Y = np.meshgrid(np.arange(4, 8, 0.02), np.arange(2, 4.5, 0.02))

x_data = np.c_[X.ravel(), Y.ravel()]

data_pred = clf.predict(x_data)

Z = data_pred.reshape(X.shape)

plt.contourf(X, Y, Z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], c = y)

plt.show()
"""

# 畫出結果

x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.show()

print("------------------------------------------------------------")  # 60個

# 全部訓練 SVM
from sklearn.datasets import load_iris

iris = load_iris()
# 資料內容 iris.data
# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 答案 iris.target

x = iris.data[:, :2]
y = iris.target

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("原圖")
plt.show()

from sklearn.svm import SVC

clf = SVC()
clf.fit(x, y)
clf.predict(x)
clf.predict(x) - y
gd = np.array([[i, j] for i in np.arange(4, 8, 0.2) for j in np.arange(1.8, 4.5, 0.2)])
gdc = clf.predict(gd)
plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
plt.title("SVM結果")
plt.show()

# 呈現學習成果
# 學出來的用比較透明的顏色, 真實資料用 100% 不透明。

gd = np.array([[i, j] for i in np.arange(4, 8, 0.1) for j in np.arange(1.8, 4.5, 0.1)])
gdc = clf.predict(gd)
plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc, alpha=0.4)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.title("SVM結果2")
plt.show()

print("------------------------------------------------------------")  # 60個

# PCA 可以救鳶尾花嗎？
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)
# 我們來看原來的樣子, 是一個 4 維的向量。
print(x.shape)
print(len(x))
print(x)
print(x[7])

# 經 PCA 之後, 濃縮成 2 維向量。
print(X.shape)
print(len(X))
print(X)
print(X[7])

# 看看 PCA 後, 來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
plt.show()

# 看來好像真的會比較容易切開, 我們來試試是否真的這樣。先來分訓練和測試資料。

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# 再來進入標準程序。
# step 1: 打造函數學習機

clf = SVC()

# step 2: 訓練

clf.fit(x_train, y_train)

SVC()

# step 3: 預測

# 這次我們直接畫出來。

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")

plt.show()


print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


