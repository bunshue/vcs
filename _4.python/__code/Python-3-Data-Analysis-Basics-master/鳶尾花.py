"""

鳶尾花

標準的分類問題: 這是哪種鳶尾花

鳶尾花 (Iris)  數據庫是很有名的資料,
就是試著以一朵鳶尾花花萼、花瓣的大小來分出是哪個的大小來分出是哪個亞種的鳶尾花。

我們現在來看看, 可不可以讓電腦辨識, 這是哪個亞種的鳶尾花?

在 sklearn.datasets 有幾個數據庫可以提供給大家玩玩。

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#Iris 鳶尾花數據庫
iris = load_iris()

#看數據庫的說明
print(iris.DESCR)

#看數據庫說明。我們這裡看看 features 有哪些?
print(iris.feature_names)
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#有四個 features: 花萼長度、花萼寬度 和 花瓣長度、花瓣寬度
#sepal 花萼
#petal  花瓣

print(iris.data)

#資料內容
#這些數據中, data 就是我們的 x (輸入), target 是 y (輸出)。
#輸入的數據四個 features 是: 花萼長度、花萼寬度、花瓣長度、花瓣寬度。
#print(iris.data)   many

#輸出就是某筆數據是哪種 (事實上是哪個亞屬) 的鳶尾花, 共分為 0, 1, 2 三種。
#print(iris.target)

#只用部份 features
#我們只選用花萼長度、花萼寬度 (當然只是例子, 事實上四個參數很少, 全部一起來也可以) 當輸入資料。
#準備輸入及輸出數據, 注意 4 個特徵我們只用了兩個。

# :2 是 前兩個 => 花萼
# 2: 是 第2個(含)以後 => 花瓣

x = iris.data
y = iris.target

X = x[:, :2]
Y = y

#只選兩個 features 原因之一是好畫 :)

plt.scatter(X[:,0], X[:,1], s = 50, c = Y)
plt.title('花萼 原始資料')

plt.show()

#試著用我們學過的方式, 看能不能做出一個分類器函數, 來把鳶尾花正確分類!

#準備 inputs 和 outputs

x = iris.data
y = iris.target

#為了表示我們很神 (事實上只是好畫圖), 我們只用兩個 features (花萼長度、寬度)。
X = x[:, :2]
Y = y

#切分訓練及測試資料。
#用 80% 當訓練資料, 留 20% 看我們做得如何?
x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size = 0.2,
                                                    random_state = 87)

#看一下整筆數據的分佈。
plt.scatter(X[:,0], X[:,1], c = Y, cmap = 'Paired')
plt.title('花萼 原始資料')

plt.show()

#看訓練結果
plt.scatter(x_train[:, 0], x_train[:, 1], c = y_train)
plt.title('花萼 訓練結果')
plt.show()

#再一次, 三部曲打造函數學習機。
#第一部曲：打開一台函數學習機

from sklearn.svm import SVC

clf = SVC()

#第二部曲：訓練

clf.fit(x_train, y_train)

SVC()

#第三部曲：預測

y_predict= clf.predict(x_test)

#看看我們模型預測和真實狀況差多少?
print(y_predict - y_test)

#看看有沒有不準的?
y_predict = clf.predict(x_test)

plt.scatter(x_test[:,0], x_test[:,1], c=y_predict - y_test)
plt.show()

#在測試資料中是全對!! 我們畫圖來看看整體表現如何?

x0 = np.linspace(0, 7.5, 500)
y0 = np.linspace(0, 2.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:,0], X[:,1], c=Y)

plt.show()

x0 = np.linspace(3, 8, 500)
y0 = np.linspace(1.5, 4.5, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)

plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()

#畫出結果

x1, x2 = np.meshgrid(np.arange(0,7,0.02), np.arange(0,3,0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()


print('------------------------------------------------------------')	#60個

#PCA 可以救鳶尾花嗎？
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)
#我們來看原來的樣子, 是一個 4 維的向量。
print(x.shape)
print(len(x))
print(x)
print(x[87])

#經 PCA 之後, 濃縮成 2 維向量。
print(X.shape)
print(len(X))
print(X)
print(X[87])

#看看 PCA 後, 來看看整個分布的狀況。

plt.scatter(X[:,0], X[:,1], c=y, cmap='Paired')
plt.show()

#看來好像真的會比較容易切開, 我們來試試是否真的這樣。先來分訓練和測試資料。

x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2,
                                                    random_state = 0)
#再來進入標準程序。
#step 1: 打造函數學習機

clf = SVC()

#step 2: 訓練

clf.fit(x_train, y_train)

SVC()

#step 3: 預測

#這次我們直接畫出來。

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap='Paired')
plt.scatter(X[:,0], X[:,1], c=y, cmap='Paired')

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('作業完成')

