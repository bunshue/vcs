import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.datasets import load_iris

'''
以Iris dataset為例，鳶尾花資料集是非常著名的生物資訊資料集之一，
取自美國加州大學歐文分校的機器學習資料庫http://archive.ics.uci.edu/ml/datasets/Iris
資料的筆數為150筆，共有五個欄位：
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
'''

print('------------------------------------------------------------')	#60個

iris = load_iris()

x = iris.data[:,:2]
y = iris.target
plt.scatter(x[:,0], x[:,1], s=50, c=y, alpha=0.6)


plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

plt.scatter(x_train[:,0], x_train[:,1], c=y_train)

plt.show()

print('------------------------------------------------------------')	#60個

#step1. 打造函數學習機

from sklearn.svm import SVC

clf = SVC()

#step2. fit
clf.fit(x_train, y_train)

#step3. predict
y_pred = clf.predict(x_test)

plt.scatter(x_test[:,0], x_test[:,1], c=y_pred - y_test)


plt.show()

print('------------------------------------------------------------')	#60個

X, Y = np.meshgrid(np.arange(4, 8, 0.02), np.arange(2, 4.5, 0.02))

x_data = np.c_[X.ravel(), Y.ravel()]

data_pred = clf.predict(x_data)

Z = data_pred.reshape(X.shape)


plt.contourf(X, Y, Z, alpha=0.3)
plt.scatter(x[:,0], x[:,1], c=y)

plt.show()

print('------------------------------------------------------------')	#60個

#K-Means
X = np.random.rand(500, 2)

plt.scatter(X[:,0], X[:,1])

#step1. 打造函數學習機

from sklearn.cluster import KMeans
clf = KMeans(n_clusters=3)

#step2. fit

clf.fit(X)

#step3. predict

y_prd = clf.predict(X)

plt.scatter(X[:,0], X[:,1], c=y_prd)

plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



