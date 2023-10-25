"""
機器學習入門


"""

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

'''

"""
01.讀入基本套件

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數
f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk), 我們想知道這
f(x)=y,其中的 y 就是某一個類別。

這種學函數的方法, 又可以分為:

    supervised learning
    unsupervised learning

其中的 supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。而 unsupervised learning 就神了, 我們不知道答案, 卻要電腦自己去學!

做數據分析, 幾乎每一次都要讀入這些套件!
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 用 Seaborn 畫圖, 並設好圖的大小

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})


#02. 關於 overfitting

#我們在數據分析, 就是收集了歷史資料, 比如說這些數據。

X = np.random.randn(6)
Y = np.random.randn(6)
plt.scatter(X, Y, c='r', s=100)
plt.grid()
plt.title('aaaa')
plt.show()

x = np.linspace(0, 1, 200)
y = -(x-1)**2+1
plt.plot(x,y)
plt.grid()
plt.title('aaaa')
plt.show()


#真實世界看來比較像是這樣...

X = np.linspace(0, 1, 20)
Y = -(X-1)**2+1 + 0.08*np.random.randn(20)
plt.scatter(X,Y, c='r',s=50)
plt.plot(x,y)
plt.grid()
plt.title('aaaa')
plt.show()

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x),'r')
plt.scatter(X,Y, c='r',s=50)
plt.plot(x,y)
plt.ylim(0, 2)
plt.grid()
plt.title('這叫很低的 bias, 很高的 variance')
plt.show()

"""
03. 迴歸法預測函數
03-1. 假的數據真的迴歸
做一條直線

我們來一條線, 比如說 f(x)=1.2x+0.8

準備好個 1000 個點 (現場建議, 雖然多了一點...)

加入 noise 項, 看來更真實 大概的想法就是, 我們真實世界的問題, 化成函數, 我們假設背後有個美好的函數。但相信我們很少看到真實世界的資料那麼漂亮。在統計上, 我們就是假設

𝑓(𝑥)+𝜀(𝑥)

也就是都有個 noise 項。
"""

x = np.linspace(0, 1, 300)

y = 1.2*x + 0.8 + 0.2*np.random.randn(300)

#畫出圖形來。

plt.scatter(x,y)

plt.grid()
plt.title('aaaa')
plt.show()

"""
分訓練資料、測試資料

一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用

sklearn.model_selection 裡的 train_test_split

來亂數選一定百分比的資料來用。
"""
from sklearn.model_selection import train_test_split

#把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                   test_size=0.2,
                                                   random_state=9487)

#len(x_train)    #80%
#len(x_test)     #20%

"""
【重點】注意輸入格式

只有一個 feature 時, 我們要小心的是, 很多機器學習、深度學習的套件, 都不希望我們用

x=[x1,x2,…,xn]

這樣子去做, 而是希望變成

x=[[x1],[x2],…,[xn]]

這種形式!
"""

xx = np.array([3, 9, 8, 1, 2])
yy = np.array([1, 3, 9, 2, 4])

"""
xx.shape
xx.reshape(5,1)
xx = xx.reshape(len(xx),1)
"""

#正式轉我們的訓練資料

x_train = x_train.reshape(len(x_train),1)
x_test = x_test.reshape(len(x_test), 1)

#step 1. 開一台「線性迴歸機」

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

#step 2. fit 學習、訓練

regr.fit(x_train, y_train)

#step 3. predict 預測

Ypred = regr.predict(x_test)

# x: x_test
# y: Ypred
# x_test.ravel()

plt.plot(x_test.ravel(), Ypred, 'r')

plt.scatter(x_test.ravel(), y_test)

plt.grid()
plt.title('aaaa')
plt.show()


#計算分數
from sklearn.metrics import mean_squared_error, r2_score
mse_t = mean_squared_error(y_train, regr.predict(x_train))
r2_t = r2_score(y_train, regr.predict(x_train))
print('訓練資料')
print('MSE =', mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, Ypred)
r2 = r2_score(y_test, Ypred)
print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")


""" 無資料
03-2 房價預測
讀入資料

SciKit-Learn 有許多 "Toy Datasets" 可以讓我們玩玩。

今天我們要使用的是「波士頓房價資料」。

from sklearn.datasets import load_boston

boston_dataset = load_boston()

print(boston_dataset.DESCR)

.. _boston_dataset:



Boston house prices dataset

---------------------------



**Data Set Characteristics:**  



    :Number of Instances: 506 



    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.



    :Attribute Information (in order):

        - CRIM     per capita crime rate by town

        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.

        - INDUS    proportion of non-retail business acres per town

        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)

        - NOX      nitric oxides concentration (parts per 10 million)

        - RM       average number of rooms per dwelling

        - AGE      proportion of owner-occupied units built prior to 1940

        - DIS      weighted distances to five Boston employment centres

        - RAD      index of accessibility to radial highways

        - TAX      full-value property-tax rate per $10,000

        - PTRATIO  pupil-teacher ratio by town

        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

        - LSTAT    % lower status of the population

        - MEDV     Median value of owner-occupied homes in $1000's



    :Missing Attribute Values: None



    :Creator: Harrison, D. and Rubinfeld, D.L.



This is a copy of UCI ML housing dataset.

https://archive.ics.uci.edu/ml/machine-learning-databases/housing/





This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.



The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic

prices and the demand for clean air', J. Environ. Economics & Management,

vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics

...', Wiley, 1980.   N.B. Various transformations are used in the table on

pages 244-261 of the latter.



The Boston house-price data has been used in many machine learning papers that address regression

problems.   

     

.. topic:: References



   - Belsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.

   - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.


boston_dataset.feature_names

array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
,       'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7')

boston_dataset.data[:5]

array([[6.3200e-03, 1.8000e+01, 2.3100e+00, 0.0000e+00, 5.3800e-01,
,        6.5750e+00, 6.5200e+01, 4.0900e+00, 1.0000e+00, 2.9600e+02,
,        1.5300e+01, 3.9690e+02, 4.9800e+00],
,       [2.7310e-02, 0.0000e+00, 7.0700e+00, 0.0000e+00, 4.6900e-01,
,        6.4210e+00, 7.8900e+01, 4.9671e+00, 2.0000e+00, 2.4200e+02,
,        1.7800e+01, 3.9690e+02, 9.1400e+00],
,       [2.7290e-02, 0.0000e+00, 7.0700e+00, 0.0000e+00, 4.6900e-01,
,        7.1850e+00, 6.1100e+01, 4.9671e+00, 2.0000e+00, 2.4200e+02,
,        1.7800e+01, 3.9283e+02, 4.0300e+00],
,       [3.2370e-02, 0.0000e+00, 2.1800e+00, 0.0000e+00, 4.5800e-01,
,        6.9980e+00, 4.5800e+01, 6.0622e+00, 3.0000e+00, 2.2200e+02,
,        1.8700e+01, 3.9463e+02, 2.9400e+00],
,       [6.9050e-02, 0.0000e+00, 2.1800e+00, 0.0000e+00, 4.5800e-01,
,        7.1470e+00, 5.4200e+01, 6.0622e+00, 3.0000e+00, 2.2200e+02,
,        1.8700e+01, 3.9690e+02, 5.3300e+00]])

boston = pd.DataFrame(boston_dataset.data,

                     columns=boston_dataset.feature_names)

boston.head()

, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33
,

boston['MEDV'] = boston_dataset.target

boston.head()

, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	MEDV
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98	24.0
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14	21.6
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03	34.7
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94	33.4
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33	36.2
,

sns.distplot(boston.MEDV, bins=30)

<matplotlib.axes._subplots.AxesSubplot at 0x7ffae2eabac8>

correlation_matrix = boston.corr().round(2)

sns.heatmap(correlation_matrix, annot=True)

<matplotlib.axes._subplots.AxesSubplot at 0x7ffae2f0a940>

boston.head()

, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	MEDV
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98	24.0
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14	21.6
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03	34.7
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94	33.4
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33	36.2
,

X = boston.loc[:,"CRIM":"LSTAT"].values

Y = boston.MEDV

x_train, x_test, y_train, y_test = train_test_split(X, Y,

                                                   test_size=0.2,

                                                   random_state=9487)

regr = LinearRegression()

regr.fit(x_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
,         normalize=False)

Ypred = regr.predict(x_test)

mse = mean_squared_error(y_test, Ypred)

r2 = r2_score(y_test, Ypred)

​

print("MSE =", mse)

print("R2 =", r2)

MSE = 23.62871172175499

R2 = 0.7432212177482068

plt.scatter(y_test, Ypred, s=100)

plt.xlim(0, 55)

plt.ylim(0, 55)

plt.plot([0,55],[0,55],'r')

plt.grid()
plt.title('aaaa')
plt.show()

X = boston[['NOX', 'AGE', 'DIS']].values

boston.columns

Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
,       'PTRATIO', 'B', 'LSTAT', 'MEDV'],
,      dtype='object')

X = boston[['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',

       'PTRATIO', 'B', 'LSTAT']].values

X

array([[6.3200e-03, 1.8000e+01, 2.3100e+00, ..., 1.5300e+01, 3.9690e+02,
,        4.9800e+00],
,       [2.7310e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9690e+02,
,        9.1400e+00],
,       [2.7290e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9283e+02,
,        4.0300e+00],
,       ...,
,       [6.0760e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
,        5.6400e+00],
,       [1.0959e-01, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9345e+02,
,        6.4800e+00],
,       [4.7410e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
,        7.8800e+00]])

x_train, x_test, y_train, y_test = train_test_split(X, Y,

                                                    test_size=0.2,

                                                    random_state=9487)

regr = LinearRegression()

regr.fit(x_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
,         normalize=False)

Ypred = regr.predict(x_test)

mse = mean_squared_error(y_test, Ypred)

r2 = r2_score(y_test, Ypred)

​

print('MSE =', mse)

print('r2 =', r2)

MSE = 23.620687554217824

r2 = 0.743308418269041
"""

'''

#07. 怎麼選最好參數、model？
#7-1. 製造像真的一様的數據

#from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_blobs

x, y = make_blobs(n_samples = 500,
                  centers = 3,
                  n_features = 2,
                  random_state = 0)

plt.scatter(x[:, 0], x[:, 1], c = y, cmap = 'Paired', s = 80)

plt.grid()
plt.title('aaaa')
plt.show()

#07-2. Cross Validation

from sklearn.model_selection import cross_val_score

#試用 SVC

from sklearn.svm import SVC

clf_svc = SVC(gamma = 'scale')

scores = cross_val_score(clf_svc, x, y, cv = 5)

"""
看一下五次的成績。
scores
array([0.94117647, 0.95049505, 0.97979798, 0.87878788, 0.91919192])
很快的算一下平均。
scores.mean()
0.9338898595741927
"""

#試用 Decision Tree

from sklearn.tree import DecisionTreeClassifier

clf_dt = DecisionTreeClassifier()
scores = cross_val_score(clf_dt, x, y, cv=5)

"""
scores
array([0.92156863, 0.89108911, 0.94949495, 0.90909091, 0.88888889])
scores.mean()
0.9120264967673238
"""

#試用 Random Forest

from sklearn.ensemble import RandomForestClassifier

clf_rf = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(clf_rf, x, y, cv=5)

"""
scores

array([0.92156863, 0.92079208, 0.96969697, 0.88888889, 0.88888889])

scores.mean()

0.9179670908267298
"""


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('作業完成')

