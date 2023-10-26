"""
房價波士頓

用線性迴歸預測波士頓房價

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

print('------------------------------------------------------------')	#60個


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


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('回帰問題における評価方法')

"""
from sklearn.datasets import load_boston
data = load_boston()
X = data.data[:, [5,]]
y = data.target

from sklearn.linear_model import LinearRegression
model_lir = LinearRegression()
model_lir.fit(X, y)
y_pred = model_lir.predict(X)

print(model_lir.coef_)
print(model_lir.intercept_)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(X, y, color='pink', marker='s', label='data set')
ax.plot(X, y_pred, color='blue', label='regression curve')
ax.legend()
plt.show()
"""


print('------------------------------------------------------------')	#60個



'''
#波士頓房價資料

import seaborn as sns

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
print(raw_df.head())
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
print(data)
target = raw_df.values[1::2, 2]
print(target)

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
print(housing)

from sklearn.datasets import fetch_openml
housing = fetch_openml(name="house_prices", as_frame=True)

print(housing)


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(housing.MedHouseVal, bins=30)


plt.grid()
plt.show()


'''


print('------------------------------------------------------------')	#60個



print('作業完成')

