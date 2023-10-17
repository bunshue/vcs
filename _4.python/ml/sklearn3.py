import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

from sklearn import datasets

np.random.seed(3)                           # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x,y)

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train,y_train,label="訓練數據")
plt.scatter(x_test,y_test,label="測試數據")
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import linear_model

x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量

regression = linear_model.LinearRegression()       # 建立線性模組物件
regression.fit(x, y)
a = regression.coef_[0][0]                         # 取出斜率
b = regression.intercept_[0]                       # 取出截距
print(f'斜率  = {a.round(2)}')
print(f'截距  = {b.round(2)}')

y2 = a*x + b
plt.scatter(x, y)                               # 繪製散佈圖
plt.plot(x, y2)                                 # 繪製迴歸直線

sold = a*31 + b
print('氣溫31度時的銷量 = {}'.format(int(sold)))
plt.plot(31, int(sold), '-o') 

plt.show()                      

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()               # 建立線性模組物件
regression.fit(x_train, y_train)
print(f'斜率  = {regression.coef_[0].round(2)}')
print(f'截距  = {regression.intercept_.round(2)}')

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

regression = linear_model.LinearRegression()               # 建立線性模組物件
regression.fit(x_train, y_train)
print(f'斜率  = {regression.coef_[0].round(2)}')
print(f'截距  = {regression.intercept_.round(2)}')

y_pred = regression.predict(x_test)
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
plt.xlim(-3, 3)
plt.ylim(-150, 150)
plt.scatter(x_train,y_train,label="訓練數據")
plt.scatter(x_test,y_test,label="測試數據")
# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color="red")

# 將測試的 y 與預測的 y_pred 計算決定係數
r2 = r2_score(y_test, y_pred)                           
print(f'決定係數 = {r2.round(2)}')

plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets

np.random.seed(3)                                       # 設定隨機數種子值

#np.random.seed(5)                                       # 設定隨機數種子值

# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)                                

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
# 繪圓點, 圓點用黑色外框 
plt.scatter(data[:,0], data[:,1], marker="o", edgecolor="black")

plt.title("無監督學習")

plt.show()

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)
                                  
e = cluster.KMeans(n_clusters=3)        # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

print('------------------------------------------------------------')	#60個

from sklearn import datasets
from sklearn import cluster

np.random.seed(3)                       # 設定隨機數種子值
# 建立 300 個點, n_features = 2
data, label = datasets.make_blobs(n_samples=300, n_features=2)
                                  
e = cluster.KMeans(n_clusters=3)        # k-mean方法建立 3 個群集中心物件
e.fit(data)                             # 將數據帶入物件, 做群集分析
print(e.labels_)                        # 列印群集類別標籤
print(e.cluster_centers_)               # 列印群集中心

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(data[:,0], data[:,1], marker="o", c=e.labels_)
# 用紅色標記群集中心
plt.scatter(e.cluster_centers_[:,0], e.cluster_centers_[:,1],marker="*",
            color="red")
plt.title("無監督學習")
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

