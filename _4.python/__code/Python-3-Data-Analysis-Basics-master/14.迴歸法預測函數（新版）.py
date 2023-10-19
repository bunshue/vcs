"""
迴歸法預測函數.py


"""

import sys
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#SVR 迴歸的預測
#數據分析

#1. 線性迴歸

#一條直線
#f(x)=1.2x+0.8

#準備好個 50 個點

x = np.linspace(0, 5, 50)
y = 1.2*x + 0.8

plt.scatter(x, y)
plt.plot(x, y, 'r')
plt.title('理想資料')
plt.show()

#加入 noise 項, 假設 f(x)+ε(x), 也就是都有個 noise 項。

y = 1.2 * x + 0.8 + 0.6 * np.random.randn(50)

plt.scatter(x,y)
plt.plot(x, 1.2*x + 0.8, 'r')
plt.title('理想資料加上雜訊')
plt.show()

#做線性迴歸找出那條線

#方法一
#做線性迴歸有很多套件, 但我們這裡用 sklearn.svm 裡的 SVR 來做各種迴歸。

from sklearn.svm import SVR

svr_lin = SVR(kernel = 'linear', C = 1e3)

"""
x資料不能直接用 要改成X
原來我們 x 的資料型態是
[x1,x2,…,x50],
但 sklearn 希望每個 x 是個向量, 也就是:
[[x1],[x2],…,[x50]]
"""

X = x.reshape(len(x),1)

print(x.shape)
print(X.shape)

svr_lin.fit(X, y)

Y = svr_lin.predict(X)

plt.scatter(x, y)
plt.plot(x, Y, 'r')
plt.plot(x, 1.2*x + 0.8, 'lime')

plt.title('SVR線性迴歸1')
plt.show()


#當然可以預測沒出現過的...
#注意資料的輸入方式。

print(svr_lin.predict([[6.2]]))

print(svr_lin.predict([[6.2], [7.4], [8]]))

sys.exit()

#方法二
#做線性迴歸有很多套件, 但我們這裡用 sklearn 裡的 LinearRegression 來做, 嗯, 線性迴歸。

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

"""
這裡要注意我們本來的 x 是
[x1,x2,…,x50]
但現在要的是
[[x1],[x2],…,[x50]]
"""

X = x.reshape(len(x),1)

regr.fit(X,y)

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

Y = regr.predict(X)

plt.scatter(x, y)

plt.plot(x, Y, 'r')
plt.title('線性迴歸2')
plt.show()

#2. 標準函數訓練及測試
#分訓練資料、測試資料
#一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。
#這是我們可以用 sklearn.cross_validation 裡的 train_test_split 來亂數選一定百分比的資料來用。

from sklearn.model_selection import train_test_split

#把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

#我們在「訓練」這個函數時只有以下這些資料。

plt.scatter(x_train, y_train)
plt.title('原始訓練資料')
plt.show()

#用訓練資料來 fit 函數 方法一
#記得現在我們只用 80% 的資料去訓練。

svr_lin = SVR(kernel='linear', C=1e3)
X_train = x_train.reshape(len(x_train),1)
svr_lin.fit(X_train,y_train)

Y_train = svr_lin.predict(X_train)

plt.scatter(x_train, y_train)

plt.plot(x_train, Y_train, 'r')
plt.title('訓練資料2')
plt.show()

#用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test),1)
Y_test = svr_lin.predict(X_test)
mse = np.sum((Y_test-y_test)**2) / len(y_test)
print('MSE =', mse)

plt.scatter(x_test, y_test)
plt.scatter(x_test, Y_test, c='r')
plt.title('測試結果1')
plt.show()

#用訓練資料來 fit 函數 方法二
#記得現在我們只用 80% 的資料去訓練。

regr = LinearRegression()
X_train = x_train.reshape(len(x_train),1)
regr.fit(X_train,y_train)

Y_train = regr.predict(X_train)

plt.scatter(x_train, y_train)
plt.plot(x_train, Y_train, 'r')
plt.title('線性回歸測試結果')
plt.show()

#用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test),1)

Y_test = regr.predict(X_test)

mse = np.sum((Y_test-y_test)**2) / len(y_test)

print('MSE =', mse)

plt.scatter(x_test, y_test)

plt.scatter(x_test, Y_test, c='r')
plt.title('測試結果2')
plt.show()

#3. 不是線性的目標函數
#這裡我們用個非線性的函數來生假數據:
#f(x)=sin(3.2x)+0.8x
#一樣準備加上一些 noise。
#3. 生成假資料

x = np.linspace(0, 5, 50)
y = np.sin(3.2*x) + 0.8*x + 0.3*np.random.randn(50)

plt.plot(x, y)
plt.title('待處理的資料 f = sin(3.2x)+0.8x+noise')
plt.show()


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

#準備生這個函數
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.3)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=4)

X_train = x_train.reshape(len(x_train), 1)

svr_rbf.fit(X_train,y_train)
svr_lin.fit(X_train,y_train)
svr_poly.fit(X_train,y_train)

#看看訓練成果

X = x.reshape(len(x), 1)
Y_rbf = svr_rbf.predict(X)
Y_lin = svr_lin.predict(X)
Y_poly = svr_poly.predict(X)

plt.scatter(x,y)
plt.plot(x, Y_rbf, label='rbf')
plt.plot(x, Y_lin, label='linear')
plt.plot(x, Y_poly, label='polynomial')

plt.legend()
plt.title('比較各種方法')
plt.show()

#標準線性學

regr_lin = LinearRegression()

X = x.reshape(len(x), 1)

regr_lin.fit(X,y)

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

plt.scatter(x,y)
plt.plot(x, regr_lin.predict(X), 'r')
plt.title('標準線性學')
plt.show()

#果然超級不準, 該如何是好?
#多項式
#我們來用 6 次多項式學

X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])

regr_poly = LinearRegression()

regr_poly.fit(X_poly, y)

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

plt.scatter(x,y)

plt.plot(x, regr_poly.predict(X_poly), 'r')
plt.title('多項式')

plt.show()

#用 RBF
#ϕi=e−∥x−ci∥2/2σ2

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

#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

plt.scatter(x,y)

plt.plot(x, regr_rbf.predict(X_rbf), 'r')
plt.title('RBF')

plt.show()

#三種一起比較

Y_lin = regr_lin.predict(X)
Y_poly = regr_poly.predict(X_poly)
Y_rbf = regr_rbf.predict(X_rbf)

plt.scatter(x,y)
plt.plot(x, Y_lin, label='linear')
plt.plot(x, Y_poly, label='polynomial')
plt.plot(x, Y_rbf, label='rbf')

plt.legend()
plt.title('三種一起比較')
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('作業完成')

