import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression


print('------------------------------------------------------------')	#60個
print('線性迴歸')

points = 11
x = np.linspace(0, 10, points)

y0 = x
plt.plot(x, y0, 'r')   #無 noise, 畫預設 y = x 紅線

y1 = y0 + 0.5 * np.random.randn(points)   #加上noise

plt.scatter(x, y1, s = 100)                #有 noise
plt.plot(x, y1, 'b')             #有 noise

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#做線性迴歸
#做線性迴歸有很多套件, 用 sklearn 裡的 LinearRegression 來做線性迴歸

regr = LinearRegression()
X = x.reshape(points, 1)

regr.fit(X, y1)#學習

Y = regr.predict(X)

plt.plot(x, Y, 'g', lw = 5) #線性回歸曲線

plt.plot(x, y0, 'r')   #無 noise, 畫預設 y = x 紅線
plt.scatter(x, y1, s = 100)                #有 noise
plt.plot(x, y1, 'b')             #有 noise

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#標準函數訓練及測試
#分訓練資料、測試資料
#一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用
#sklearn.cross_validation 裡的 train_test_split
#來亂數選一定百分比的資料來用。

from sklearn.model_selection import train_test_split

points = 11
x = np.linspace(0, 10, points)

y0 = x
plt.plot(x, y0, 'r')   #無 noise, 畫預設 y = x 紅線

y1 = y0 + 0.5 * np.random.randn(points)   #加上noise

#把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。
x_train, x_test, y_train, y_test = train_test_split(x, y1, test_size=0.2, random_state=1)
#x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=9487)
                                                   
print(len(x_train))
print(x_train)
print(len(x_test))
print(x_test)
print(y_train)
print(y_test)

X_train = x_train.reshape(len(x_train), 1)

regr = LinearRegression()

regr.fit(X_train, y_train)#學習

Y_train = regr.predict(X_train)

plt.scatter(x_train, y_train, s = 100, c = 'r')
plt.plot(x_train, Y_train, 'g', lw = 5) #線性回歸曲線

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test),1)
Y_test = regr.predict(X_test)
mse = np.sum((Y_test-y_test)**2) / len(y_test)
print('MSE =', mse)
plt.scatter(x_test, y_test, c='r', s = 100)
plt.scatter(x_test, Y_test, c='g', s = 100)
plt.scatter(x, y0, c='b', s = 100)


from sklearn.metrics import mean_squared_error, r2_score

Y_test = regr.predict(X_test)
mse = mean_squared_error(y_test, Y_test)
r2 = r2_score(y_test, Y_test)

print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")
print("MSE =", mse)
print("R2 =", r2)

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#不是線性的目標函數


#f(x) = sin(3.2x) + 0.8x

x = np.linspace(0, 5, 50)
y = np.sin(3.2*x) + 0.8*x + 0.3*np.random.randn(50)
plt.plot(x, y)

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#標準線性學
regr_lin = LinearRegression()

X = x.reshape(len(x), 1)

regr_lin.fit(X,y)#學習

plt.scatter(x,y)
plt.plot(x, regr_lin.predict(X), 'r')

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#多項式
#我們來用 6 次多項式學

X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])

regr_poly = LinearRegression()

regr_poly.fit(X_poly, y)#學習

plt.scatter(x,y)
plt.plot(x, regr_poly.predict(X_poly), 'r')

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#用 RBF!!

def RBF(x, center, sigma):
    k = np.exp(-(x - center)**2/(2*sigma**2))
    return k

sigma = 0.3

X_rbf = np.array([[RBF(k, 0.5, sigma), 
                  RBF(k, 1.5, sigma),
                  RBF(k, 2.5, sigma),
                  RBF(k, 3.5, sigma),
                  RBF(k, 4.5, sigma)] for k in x])

regr_rbf = LinearRegression()

regr_rbf.fit(X_rbf, y)

plt.scatter(x,y)
plt.plot(x, regr_rbf.predict(X_rbf), 'r')

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

#三種一起比較
Y_lin = regr_lin.predict(X)
Y_poly = regr_poly.predict(X_poly)
Y_rbf = regr_rbf.predict(X_rbf)

plt.scatter(x,y)

plt.plot(x, Y_lin, label='linear')
plt.plot(x, Y_poly, label='polynomial')
plt.plot(x, Y_rbf, label='rbf')

plt.legend()

plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個




'''
#波士頓房價資料

import seaborn as sns

import pandas as pd
import numpy as np

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


#plt.plot([1, 9],[1, 9],'r', lw = 10)




