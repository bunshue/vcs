"""
機器學習概要

這種學函數的方法, 又可以分為:

    supervised learning
    unsupervised learning

其中的 supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。而 unsupervised learning 就神了, 我們不知道答案, 卻要電腦自己去學!

今天我們就來介紹最最基本的方式, 一個是 SVM, 一個是 K-Means。

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

#SVM 支援向量機
#簡單的分類
#假設我們有四個點, 有兩個類別。

p = np.array([[1, 2], [2, 1], [1, 1], [2, 2]])
c = np.array([1, 2, 1, 2])
plt.scatter(p[:, 0], p[:, 1], c = c, s = 100, cmap = "Paired")
plt.show()


from sklearn.svm import SVC
#step 1: 打開一台 SVM 函數學習機

clf = SVC()

#step 2: 訓練

clf.fit(p, c)

SVC()

#step 3: 預測

y_pred = clf.predict(p)

print(y_pred)


x = y = np.arange(0.5, 2.5, 0.02)
X, Y = np.meshgrid(x, y)
P = np.c_[X.ravel(), Y.ravel()]
z = clf.predict(P)
Z = z.reshape(X.shape)
plt.contourf(X, Y, Z, alpha=0.3, cmap='Paired')
plt.scatter(p[:,0], p[:,1], c=c, cmap='Paired')

plt.show()


print('------------------------------------------------------------')	#60個


#1. 用 SVM 來做分類

x = np.array([[-3, 2], [-6, 5], [3, -4], [2, -8]])
y = np.array([1, 1, 2, 2])

print('x全部')
print(x)
print('x全部')
print(x[:])
print('x之x座標')
print(x[:, 0])
print('x之y座標')
print(x[:, 1])

plt.scatter(x[:, 0], x[:, 1], s = 50, c = y)#c=y 就是指定顏色, 不同類別不同色

plt.show()

print('------------------------------------------------------------')	#60個

#SVM 支持向量機

#支持向量機, 大家都用英文縮寫 SVM 稱呼。是一個用曲線把資料分隔的辦法。在高維度的時候自然就是曲面 (超曲面) 分隔資料的方法。

from sklearn.svm import SVC

clf = SVC() #打開一台機器 (這以後我們常常會做類似的動作)。

clf.fit(x, y)   #學習


print('------------------------------------------------------------')	#60個

print('預測結果')
print(clf.predict([[-0.8, -1]]))

#再來視覺化一下我們的成果
gd = np.array([[i,j] for i in np.arange(-8, 4, 0.6) 
 for j in np.arange(-10, 6, 0.8)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s = 50, c = gdc)

plt.show()


#視覺化成果之一
x1, x2 = np.meshgrid(np.arange(-8, 4, 0.6), np.arange(-10, 6, 0.8))
X = np.c_[x1.ravel(), x2.ravel()]
c = clf.predict(X)
plt.scatter(X[:, 0], X[:, 1], s = 50, c = c)
plt.show()

#視覺化成果之二

x1, x2 = np.meshgrid(np.arange(-7, 4, 0.02), np.arange(-10, 6, 0.02))
X = np.c_[x1.ravel(),x2.ravel()]
Z = clf.predict(X)

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = y)

plt.show()

print('------------------------------------------------------------')	#60個

#2. 生個「像樣點」的假數據
#用 sklearn 生一些「像真的一樣」的數據。
#用 make_classification 製造分類數據

from sklearn.datasets import make_classification

#n_features 是指 x 的參數要幾個, n_classes 是你要分成幾類。
x, y = make_classification(n_features = 2, n_redundant = 0,
                           n_informative = 2,
                           n_clusters_per_class = 1, n_classes = 3)

plt.scatter(x[:, 0], x[:, 1], s = 50, c = y)

plt.show()

#訓練

clf = SVC()

clf.fit(x, y)

plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.predict(x))
plt.show()


#如果沒錯的會用一個顏色, 錯了就用其他顏色表示

plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.predict(x) - y)
plt.show()



gd = np.array([[i,j] for i in np.arange(-4, 4, 0.4) 
 for j in np.arange(-3, 4, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:,0], gd[:, 1], s = 50, c = gdc)
plt.show()


x1, x2 = np.meshgrid(np.arange(-4, 4, 0.02), np.arange(-3, 4, 0.02))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = y)

plt.show()

print('------------------------------------------------------------')	#60個

#3. K-Means 會自動分類!
#我們介紹一個很好用的 unsupervised learning, 叫 K-Means。
#我們可以指定把我們資料分成幾類, 然後它就會快速分好!

x = np.random.rand(200, 2)
plt.scatter(x[:, 0], x[:, 1], s = 50)
#plt.scatter(x[:, 0], x[:, 1], cmap = 'Paired')
plt.show()

#再次進入標準程序。
#step 1. 製做一個 K-Means 分類器
#和前面 SVM 很像。

from sklearn.cluster import KMeans

#告訴 K-Means 要分成幾類 (我們這裡是 3 類)。

clf = KMeans(n_clusters = 3)

#step 2. fit 學習、訓練
#注意這時沒有「正確答案」。

clf.fit(x)

#step 3. predict
#訓練好的結果, 在神秘的 labels_ 之下。

print(clf.labels_)

#當然我們還是有 predict, 所以也可以用 predict 預測, 但這電腦自己分的, 答案自然 100% 相同!
print(clf.predict(x))

#我們可以檢查一下, 確認答案是不是真的一樣!
print(np.array_equal(clf.labels_, clf.predict(x)))

#畫圖來看看分得怎麼樣。
plt.scatter(x[:, 0], x[:, 1], c = clf.labels_, cmap='Paired')
#plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.labels_)
plt.show()

#畫完整分類
#和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i,j] for i in np.arange(-4, 4, 0.4) 
 for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:,0], gd[:,1], s=50, c=gdc)
plt.show()


x1, x2 = np.meshgrid(np.arange(-0.2,1.2,0.02), np.arange(-0.2,1.2,0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha=0.3)
plt.scatter(x[:,0], x[:,1], s=100, c=clf.labels_)
plt.show()

#呈現出來
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(x[:,0], x[:,1], c=clf.labels_)

print('------------------------------------------------------------')	#60個

#6. Mean Shift 也會自動分類！

#有時我們甚至不想告訴電腦, 你自動分類應該分成幾類。這時 Mean Shift 可以幫我們。

from sklearn.cluster import MeanShift

#再來又是我們三部曲標準程序!
#step 1: 打開 MeanShift 函數學習機

clf = MeanShift(bandwidth = 0.2)

#這裡的 bandwidth 是控制分類要寬鬆一點, 還是嚴一點。
#step 2: fit 學習、訓練

clf.fit(x)

#MeanShift(bandwidth=0.2)

#step 3: predict

#這次我們直接畫圖!

x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)

plt.scatter(x[:, 0], x[:, 1], c = clf.labels_, cmap = 'Paired')
plt.contourf(xm, ym, Z, alpha = 0.3, cmap = 'Paired')

plt.show()


print('------------------------------------------------------------')	#60個

#觀察 bandwidth 對分類的影響

def my_mean_shift(b = 0.2):
    clf = MeanShift(bandwidth = b)
    clf.fit(x)

    x0 = y0 = np.arange(-0.2, 1.2, 0.02)
    xm, ym = np.meshgrid(x0, y0)

    P = np.c_[xm.ravel(), ym.ravel()]
    z = clf.predict(P)
    Z = z.reshape(xm.shape)
    
    plt.scatter(x[:, 0], x[:, 1], c = clf.labels_, cmap = 'Paired')
    plt.contourf(xm, ym, Z, alpha = 0.3, cmap = 'Paired')

my_mean_shift(0.2)  #(0.1, 0.3, 0.02)
plt.show()


print('------------------------------------------------------------')	#60個

#7. 怎麼選最好參數、model？

#7-1 製造像真的一様的數據

from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples = 500, centers = 3,
                  n_features = 2,
                  random_state = 0)

plt.scatter(x[:, 0], x[:, 1], c = y, cmap = 'Paired', s = 80)
plt.show()



print('------------------------------------------------------------')	#60個

#7-2 Cross Validation

from sklearn.model_selection import cross_val_score

#試用 SVC

clf_svc = SVC()

#看一下五次的成績。
scores = cross_val_score(clf_svc, x, y, cv = 5)
print(scores)

#很快的算一下平均。
print(scores.mean())

#試用 Decision Tree

from sklearn.tree import DecisionTreeClassifier

clf_dt = DecisionTreeClassifier()

#看一下五次的成績。
scores = cross_val_score(clf_dt, x, y, cv = 5)
print(scores)

#很快的算一下平均。
print(scores.mean())

#試用 Random Forest

from sklearn.ensemble import RandomForestClassifier

clf_rf = RandomForestClassifier(n_estimators = 100)

#看一下五次的成績。
scores = cross_val_score(clf_rf, x, y, cv=5)
print(scores)

#很快的算一下平均。
print(scores.mean())

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('作業完成')

