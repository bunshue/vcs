import sys
import keras
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from sklearn import linear_model

#x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
#y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量
#x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
#y = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
xs = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]], dtype = float)
ys = np.array([[0.0], [1.0], [2.0], [5.0], [4.0], [5.0]], dtype = float)

regression = linear_model.LinearRegression()       # 建立線性模組物件
regression.fit(xs, ys)
a = regression.coef_[0][0]                         # 取出斜率
b = regression.intercept_[0]                       # 取出截距
print(f'斜率  = {a.round(2)}')
print(f'截距  = {b.round(2)}')

#畫 理論值 y = x
plt.plot([-1, 12], [-1, 12], 'lime', lw = 3, label = '理論值 y = x')

y2 = a * xs + b
plt.plot(xs, ys, 'b-o', lw = 1, ms = 10, label = '實驗值')
plt.plot(xs, y2, 'r', lw = 2, label = '迴歸直線')    # 繪製迴歸直線

xx = 10
predicted = a * xx + b
print(f"x = 10 的 預測值 = {predicted}")
plt.plot(xx, predicted, 'ro', lw = 1, ms = 12, label = '預測值')

xmin, xmax, ymin, ymax = -1, 12, -1, 12
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets

np.random.seed(3)               # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100,
                                n_features=1,
                                noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x,y)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)                           # 設計隨機數種子
x, y = datasets.make_regression(n_samples=100,
                                n_features=1,
                                noise=20)
# 數據分割為x_train,y_train訓練數據, x_test,y_test測試數據
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train, y_train, label = '訓練數據')
plt.scatter(x_test, y_test, label = '測試數據')
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                               # 設計隨機數種子
print('製作原始資料 x, y')
x, y = datasets.make_regression(n_samples = 10,
                                n_features = 1,
                                noise = 20)

# 數據分割為x_train,y_train訓練數據80%, x_test,y_test測試數據20%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

regression = linear_model.LinearRegression()       # 建立線性模組物件
regression.fit(x_train, y_train)
print(f'斜率  = {regression.coef_[0].round(2)}')
print(f'截距  = {regression.intercept_.round(2)}')
            
print('預測')
y_pred = regression.predict(x_test)           

plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x, y, c = 'blue', marker = 'o', lw = 8, label = '原始資料')
plt.scatter(x_train, y_train, c = 'red', marker = 'o', lw = 4, label = "訓練數據")
plt.scatter(x_test, y_test, c = 'green', marker = 'o', lw = 4, label = "測試數據")

# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color = "red", label = '迴歸直線')

print('x_test')
print(x_test)
print('y_pred')
print(y_pred)

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)                           

print(f'決定係數 = {r2.round(2)}')

"""
print('原始資料')
print(x)
print()
print(y)
print('train')
print(x_train)
print()
print(y_train)
print('test')
print(x_test)
print()
print(y_test)
"""

plt.legend()

plt.show()



