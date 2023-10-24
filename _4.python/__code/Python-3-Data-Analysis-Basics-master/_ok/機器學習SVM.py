"""
機器學習 SVM

機器學習概要

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數

f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk)

, 我們想知道這

f(x)=y

其中的 y

就是某一個類別。

這種學函數的方法, 又可以分為:

1. supervised learning
2. unsupervised learning

1. supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。
2. unsupervised learning 我們不知道答案, 卻要電腦自己去學!

"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

'''
#Supervised Learning SVM

#6-1 用 SVM 來做分類
#先做個簡單的資料
#假設我們有四個點, 有兩個類別。

#x = np.array([[-3, 2], [-6, 5], [3, -4], [2, -8]])
#y = np.array([1, 1, 2, 2])

#debug
x = np.array([[5, 0], [5, -5], [0, -5], [0, 5], [-5, 5], [-5, 0]])
y = np.array([1, 1, 1, 2, 2, 2])

#我們要畫圖時, 需要把 x中點的 x-座標, y-座標
#分成兩個 list (array)。記得我們要 x全部是這樣叫出來的。
#x[:]

#畫出已知分類狀態

#而 x中前面的元素 (x-座標) 是這樣。當然 y-座標也是類似方法叫出來。
#x[:,0]

#畫出原始資料, s=50 是設定點的大小, c=y 就是指定顏色, 不同類別不同色。
plt.scatter(x[:, 0], x[:, 1], s = 500, c = y, cmap = 'Paired')   #依據y給定顏色
plt.title('原始資料')
plt.grid()
plt.show()

#打開一台 SVM 分類機
#支持向量機, 大家都用英文縮寫 SVM 稱呼。
#是一個用曲線把資料分隔的辦法。
#在高維度的時候自然就是曲面 (超曲面) 分隔資料的方法。

from sklearn.svm import SVC

clf = SVC() #打開一台機器, 就像打開「迴歸機一樣」。
#clf = SVC(gamma='auto')

#學習! 這樣就做完了!!
clf.fit(x, y)

#預測結果
#先來看看我們之前用來學的有沒有做對, 你會發現用法和以前迴歸是完全一樣的。

print('原始 x 資料 :', x)
print('原始 y 資料 :', y, '\t=> 目標')
print('用原始 x 資料預測的結果 :', clf.predict(x))

xx = -5
yy = -4
print('使用(%d, %d)做預測, 結果 :'% (xx, yy), clf.predict([[xx, yy]]))
print(clf.predict([[xx, yy]]))

gd = np.array([[i, j] for i in np.arange(-7, 7, 0.5)
               for j in np.arange(-7, 7, 0.5) ])
#print(len(gd))
#print(gd)

gdc = clf.predict(gd)
plt.scatter(gd[:, 0], gd[:, 1], s = 50, c = 2 - gdc)
plt.scatter(x[:, 0], x[:, 1], s = 500, c = y)   #依據y給定顏色
plt.scatter(xx, yy, c = 'r', s = 800)
plt.grid()
plt.show()

#【技巧】視覺化成果之一
#再來視覺化一下我們的成果, 這次我們用不太一樣的方式, 但技巧都學過了!

x1, x2 = np.meshgrid(np.arange(-7, 7, 0.5), np.arange(-7, 7, 0.5))

X = np.c_[x1.ravel(), x2.ravel()]

c = clf.predict(X)

plt.scatter(X[:, 0], X[:, 1], s = 50, c = c)
plt.grid()
plt.show()


#【技巧】視覺化成果之二
#我們的「傳統手法」。

x1, x2 = np.meshgrid(np.arange(-7, 7, 0.5), np.arange(-7, 7, 0.5))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)

z = Z.reshape(x1.shape)
plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = y)
plt.grid()
plt.show()

#5-2 生個「像樣點」的假數據*
#剛剛我們隨便做的數據又少、又不像真的。
#不如我們就來用 sklearn 生一些「像真的一樣」的數據。

#用 make_classification 製造分類數據

from sklearn.datasets import make_classification

#開始你只需知道, n_features 是指 x 的參數要幾個, n_classes 是你要分成幾類。

x, y = make_classification(n_features = 2,
                           n_redundant = 0,
                           n_informative = 2,
                           n_clusters_per_class = 1,
                           n_classes = 3,
                           random_state = 9487)

print('aaaaaaaaaaaaaaaaaaa')
print(len(x))
print('aaaaaaaaaaaaaaaaaaa')
print(len(y))
print('aaaaaaaaaaaaaaaaaaa')

plt.scatter(x[:, 0], x[:, 1], s = 50, c = y)
plt.grid()
plt.show()

#訓練方式其實是一樣的!

from sklearn.svm import SVC

clf = SVC() #打開一台機器, 就像打開「迴歸機一樣」。

clf.fit(x, y)

#來看預測的結果

print('真實目標 :', y)
print('預測結果 :', clf.predict(x))
print('預測差值 :', clf.predict(x) - y)

#這裡看看我們可愛的 SVM, 把我們訓練資料學得怎麼樣。

plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.predict(x))
plt.grid()
plt.show()

#你有沒有看出哪個分錯了? 我是看不出來。所以我們用個簡單方式, 如果沒錯的會用一個顏色, 錯了就用其他顏色表示。

plt.scatter(x[:, 0], x[:, 1], s = 50, c = clf.predict(x) - y)
plt.grid()
plt.title('畫出預測差異')
plt.show()

#當然再畫個我們最愛的...
#方法一 點圖
gd = np.array([[i,j] for i in np.arange(-4, 4, 0.4)
               for j in np.arange(-3, 4, 0.4)])
gdc = clf.predict(gd)
plt.scatter(gd[:,0], gd[:,1], s=50, c=gdc)
plt.title('點圖')
plt.grid()
plt.show()

#方法二 等高線圖
x1, x2 = np.meshgrid(np.arange(-4, 4, 0.02), np.arange(-3, 4, 0.02))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)

z = Z.reshape(x1.shape)
plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = y)
plt.title('等高線圖')
plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#先做個簡單的資料
#假設我們有四個點, 有兩個類別。
p = np.array([[1, 2], [2, 1], [1, 1], [2, 2]])
c = np.array([1, 2, 1, 2])
plt.scatter(p[:,0], p[:,1], c=c, cmap="Paired")
plt.show()

from sklearn.svm import SVC
clf = SVC(gamma='auto')
clf.fit(p, c)
Ypred = clf.predict(p)
print(Ypred)
print(c)

print(clf.predict([[0,0]]))
print(clf.predict([[1.5, 1.5], [0, 0]]))

x = np.linspace(0.5, 2.5, 10)
y = np.linspace(0.5, 2.5, 10)
X, Y = np.meshgrid(x, y)
P = np.c_[X.ravel(), Y.ravel()]
C = clf.predict(P)
plt.scatter(P[:,0], P[:,1], c=C, cmap='Paired')
plt.show()


x_train = p
y_train = c

x = y = np.arange(0.5, 2.5, 0.02)
X, Y = np.meshgrid(x, y)
P = np.c_[X.ravel(), Y.ravel()]
z = clf.predict(P)
Z = z.reshape(X.shape)
plt.contourf(X, Y, Z, alpha=0.3, cmap='Paired')
plt.scatter(p[:,0], p[:,1], c=c, cmap='Paired')
plt.show()



print('作業完成')

'''

#-------------------------------------------------------------------------------

#iris

from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target

X = x[:, :2]

Y = y

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                   test_size = 0.2,
                                                   random_state = 0)

plt.scatter(X[:,0], X[:,1], c=Y, cmap='Paired')
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
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()



#PCA

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)

pca.fit(x)

X = pca.transform(x)

plt.scatter(X[:, 0], X[:, 1], c = y)

plt.show()


x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                   test_size = 0.2,
                                                   random_state = 0)

clf = SVC(gamma='scale')

clf.fit(x_train, y_train)

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()


print(x[87])

print(y[87])

print(pca.transform([[6.3, 2.3, 4.4, 1.3]]))

print(clf.predict([[ 0.81509524, -0.37203706]]))

print(X.shape)

#print(Z.reshape(X.shape))


