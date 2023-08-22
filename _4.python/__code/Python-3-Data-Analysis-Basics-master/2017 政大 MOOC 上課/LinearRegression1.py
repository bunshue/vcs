import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression


'''
print('------------------------------------------------------------')	#60個
#線性迴歸

points = 21
x = np.linspace(0, 5, points)

y = 5.0 * x / 5.0
y = 5.0 * x / 5.0 + 0.3 * np.random.randn(points)   #加上noise

plt.scatter(x,y)                #有 noise
plt.plot(x, y, 'b')             #有 noise
plt.plot(x, 5.0 * x / 5.0, 'r')   #無 noise
plt.grid()

plt.show()


#做線性迴歸找出那條線
#做線性迴歸有很多套件, 但我們這裡用 sklearn 裡的 LinearRegression 來做線性迴歸

from sklearn.linear_model import LinearRegression


regr = LinearRegression()
X = x.reshape(points, 1)
regr.fit(X, y)

Y = regr.predict(X)

plt.scatter(x, y)
plt.plot(x, Y, 'g') #線性回歸曲線
plt.plot(x, 5.0 * x / 5.0, 'r')
plt.grid()

plt.show()

'''

from sklearn.model_selection import train_test_split


points = 21
x = np.linspace(0, 5, points)

y = 5.0 * x / 5.0
y = 5.0 * x / 5.0 + 0.3 * np.random.randn(points)   #加上noise

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

plt.scatter(x_train, y_train)


regr = LinearRegression()
X_train = x_train.reshape(len(x_train),1)
regr.fit(X_train,y_train)

Y_train = regr.predict(X_train)

plt.scatter(x_train, y_train)
plt.plot(x_train, Y_train, 'r')
plt.grid()
plt.show()

#用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test),1)
Y_test = regr.predict(X_test)
mse = np.sum((Y_test-y_test)**2) / len(y_test)
print('mse =', mse)
plt.scatter(x_test, y_test)
plt.scatter(x_test, Y_test, c='r')
plt.grid()
plt.show()





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

