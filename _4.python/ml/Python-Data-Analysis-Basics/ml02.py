"""

tmptmp

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

#-------------------------------------------------------------------------------

#鳶尾花 Iris 數據集

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

plt.scatter(X[:, 0], X[:, 1], c = Y, cmap = 'Paired')
plt.title('原始資料')
plt.show()

from sklearn.svm import SVC
clf = SVC(gamma = "scale")

clf.fit(x_train, y_train)

Ypred = clf.predict(x_test)

print(Ypred - y_test)

x0 = np.linspace(3.8, 8.2, 500)
y0 = np.linspace(1.8, 4.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha = 0.3)
plt.scatter(X[:, 0], X[:, 1], c = Y)
plt.show()


#PCA 可以救鳶尾花嗎？

from sklearn.decomposition import PCA

pca = PCA(n_components = 2)

pca.fit(x)

X = pca.transform(x)

#我們稍稍的「欣賞一下」 PCA 對我們的資料集做了什麼，來看看某朵鳶尾花的資料。
#pca.transform([[6.3, 2.3, 4.4, 1.3]])
#真的變成平面上一個點！來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c = y, cmap='Paired')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                   test_size = 0.2,
                                                   random_state = 0)

clf = SVC(gamma = 'scale')

clf.fit(x_train, y_train)

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha = 0.3)
plt.scatter(X[:, 0], X[:, 1], c = y)
plt.show()


print(x[87])

print(y[87])

print(pca.transform([[6.3, 2.3, 4.4, 1.3]]))

print(clf.predict([[ 0.81509524, -0.37203706]]))

print(X.shape)

#print(Z.reshape(X.shape))

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


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


print('------------------------------------------------------------')	#60個




#畫完整分類
#和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i,j] for i in np.arange(-4, 4, 0.4) 
 for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s = 50, c = gdc)
plt.show()

x1, x2 = np.meshgrid(np.arange(-0.2, 1.2, 0.02), np.arange(-0.2, 1.2, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])

z = Z.reshape(x1.shape)

plt.contourf(x1, x2, z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], s = 100, c = clf.labels_)
plt.show()

#呈現出來
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha = 0.3)
plt.scatter(x[:, 0], x[:, 1], c = clf.labels_)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('作業完成')

