"""
加州房價

用線性迴歸預測加州房價

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

print('------------------------------------------------------------')	#60個

#用線性迴歸預測加州房價

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

#可以看看說明, 一共有 8 個特徵 (features), 20,640 筆數據。
print(housing['DESCR'])

#單獨把特徵的名稱找出來。
print(housing.feature_names)

#特徵的數據是在 .data 中, 現在來建一個 Data Frame。
cal = pd.DataFrame(housing.data, columns = housing.feature_names)
print(cal.head())

#把要預測的房價也放進來。
cal['MEDV'] = housing.target
print(cal.head())

#可以用 seaborn 畫個美美的房價分佈圖。

import seaborn as sns
sns.distplot(cal.MEDV, bins = 30)
plt.show()

#再來可以做一個相關係數矩陣 (Correlation Matrix), 並且畫出 "heat map"。
correlation_matrix = cal.corr().round(2)

sns.set(rc = {'figure.figsize' : (11.7, 8.27)})

sns.heatmap(correlation_matrix, annot = True)
plt.show()


#接下來我們把輸入輸出分好
X = cal.loc[:, "MedInc" : "Longitude"].values
Y = cal.MEDV

#切一下訓練及測試資料

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size = 0.2,
                                                    random_state = 9487)

#三部曲打造函數學習機

from sklearn.linear_model import LinearRegression

#第一部曲: 開一台函數學習機

model = LinearRegression()

#第二部曲: 訓練
model.fit(x_train, y_train)

LinearRegression()

#第三部曲: 測試
y_predict = model.predict(x_test)

#現在來計算我們預測的成績。
from sklearn.metrics import mean_squared_error, r2_score


mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print("MSE =", mse)
print("R2 =", r2)

#用很有創意的方法, 把圖給畫出來。

plt.scatter(y_test, y_predict)
plt.xlim(0, 5.5)
plt.ylim(0, 5.5)
plt.plot([0, 5.5], [0, 5.5], 'r')

plt.show()



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('作業完成')

