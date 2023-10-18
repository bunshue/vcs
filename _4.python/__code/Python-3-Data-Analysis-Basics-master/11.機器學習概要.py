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
print(clf.predict([[-0.8,-1]]))

gd = np.array([[i,j] for i in np.arange(-8, 4, 0.6) 
 for j in np.arange(-10, 6, 0.8)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s = 50, c = gdc)

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

plt.scatter(gd[:,0], gd[:,1], s=50, c=gdc)
plt.show()

print('------------------------------------------------------------')	#60個

#3. K-Means 會自動分類!
#我們介紹一個很好用的 unsupervised learning, 叫 K-Means。我們可以指定把我們資料分成幾類, 然後它就會快速分好!

x = np.random.rand(100, 2)
plt.scatter(x[:, 0], x[:, 1], s = 50)
plt.show()

#製做一個 K-Means 分類器
#和前面 SVM 很像。

from sklearn.cluster import KMeans

#告訴 K-Means 要分成幾類 (我們這裡是 3 類)。

clf = KMeans(n_clusters = 3)

clf.fit(x)

#訓練好的結果, 在神秘的 labels_ 之下。

print(clf.labels_)

plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.labels_)
plt.show()

#畫完整分類
#和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i,j] for i in np.arange(-4, 4, 0.4) 
 for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:,0], gd[:,1], s=50, c=gdc)
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('作業完成')

