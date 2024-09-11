# Data Preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#��??100�ѡX�X�ĤG�ѡG???�ʦ^?
#�Ĥ@�B�G?�u??�z

#?�J��??�u
dataset = pd.read_csv('../datasets/studentscores.csv')
X = dataset.iloc[ : ,   : 1 ].values
Y = dataset.iloc[ : , 1 ].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0) 
#???�ʦ^?
# Fitting Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
#�ϥ�??��?�ҫ�?��??
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

#???�G

Y_pred = regressor.predict(X_test)
print(Y_pred)
print(Y_test)

# �e�X��
#��??
plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')

#��??
plt.scatter(X_test , Y_test, color = 'red')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()



print(X_test,Y_test)


