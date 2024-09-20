"""

#機器學習100天——第二天：簡單線性回歸


"""

import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
#讀取資料
dataset = pd.read_csv('data/studentscores.csv')
print(dataset)
df = dataset.sort_values("Scores",ascending=False)
print(df)
dataset.head(30)

print(dataset.head(30))

#這里我們需要使用pandas的iloc(區分于loc根據index來索引，iloc利用行號來索引)方法來對數據進行處理，第一個參數為行號，:表示全部行，第二個參數 ：1表示截到第1列(也就是取第0列)

#X = dataset.iloc[ : ,   : 1 ].values
#Y = dataset.iloc[ : , 1 ].values

X = dataset.iloc[ 0: 25,   : 1 ].values
Y = dataset.iloc[ 0: 25, -1: ].values
print("X:",X)
print("Y:",Y)

#導入sklearn庫的cross_validation類來對數據進行訓練集、測試集劃分



from sklearn.model_selection import train_test_split
#拆分數據，0.25作為測試集
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 
print(X_train,X_test)
print(Y_train,Y_test)


#訓練線性回歸
# Fitting Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
#使用訓練集對模型進行訓練
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#預測結果

Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# 畫出來
#散點圖
plt.scatter(X_train , Y_train, color = 'red')
#線圖
plt.plot(X_train , regressor.predict(X_train), 'bo-')
#plt.plot(X_train , regressor.predict(X_train), color ='blue')

plt.show()

#散點圖
plt.scatter(X_test , Y_test, color = 'red')
#線圖
plt.plot(X_test ,Y_pred, 'bo-')
#plt.plot(X_test , regressor.predict(X_test), color ='blue')

plt.show()

print(X_test,Y_test)

'''

#another

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#讀取資料
dataset = pd.read_csv('data/studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 

#第二步：訓練集使用簡單線性回歸模型來訓練

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#第三步：預測結果

Y_pred = regressor.predict(X_test)

#第四步：可視化
#訓練集結果可視化

plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
plt.show()

#測試集結果可視化

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()

