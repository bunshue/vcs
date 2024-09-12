"""

#机器学习100天——第二天：简单线性回归


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

#这里我们需要使用pandas的iloc(区分于loc根据index来索引，iloc利用行号来索引)方法来对数据进行处理，第一个参数为行号，:表示全部行，第二个参数 ：1表示截到第1列(也就是取第0列)

#X = dataset.iloc[ : ,   : 1 ].values
#Y = dataset.iloc[ : , 1 ].values

X = dataset.iloc[ 0: 25,   : 1 ].values
Y = dataset.iloc[ 0: 25, -1: ].values
print("X:",X)
print("Y:",Y)

#导入sklearn库的cross_validation类来对数据进行训练集、测试集划分



from sklearn.model_selection import train_test_split
#拆分数据，0.25作为测试集
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 
print(X_train,X_test)
print(Y_train,Y_test)


#训练线性回归
# Fitting Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
#使用训练集对模型进行训练
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#预测结果

Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# 畫出來
#散点图
plt.scatter(X_train , Y_train, color = 'red')
#线图
plt.plot(X_train , regressor.predict(X_train), 'bo-')
#plt.plot(X_train , regressor.predict(X_train), color ='blue')

plt.show()

#散点图
plt.scatter(X_test , Y_test, color = 'red')
#线图
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

#第二步：训练集使用简单线性回归模型来训练

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#第三步：预测结果

Y_pred = regressor.predict(X_test)

#第四步：可视化
#训练集结果可视化

plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
plt.show()

#测试集结果可视化

plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()

