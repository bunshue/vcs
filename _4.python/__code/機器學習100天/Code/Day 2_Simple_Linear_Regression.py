# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#机器??100天——第二天：???性回?
#第一步：?据??理

#?入相??据
dataset = pd.read_csv('../datasets/studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 
#???性回?
# Fitting Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
#使用??集?模型?行??
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#???果

Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# 畫出來
#散??
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')

#散??
plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()



print(X_test,Y_test)


