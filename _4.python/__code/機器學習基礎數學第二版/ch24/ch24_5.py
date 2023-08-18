# ch24_5.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

np.random.seed(3)                                       # 設計隨機數種子
x, y = datasets.make_regression(n_features=1, noise=20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

e_model = linear_model.LinearRegression()               # 建立線性模組物件
e_model.fit(x_train, y_train)
print(f'斜率  = {e_model.coef_[0].round(2)}')
print(f'截距  = {e_model.intercept_.round(2)}')

y_pred = e_model.predict(x_test)
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















