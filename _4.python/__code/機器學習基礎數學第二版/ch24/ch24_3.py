# ch24_3.py
import matplotlib.pyplot as plt                                  
import numpy as np
from sklearn import linear_model

x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量

e_model = linear_model.LinearRegression()       # 建立線性模組物件
e_model.fit(x, y)
a = e_model.coef_[0][0]                         # 取出斜率
b = e_model.intercept_[0]                       # 取出截距
print(f'斜率  = {a.round(2)}')
print(f'截距  = {b.round(2)}')

y2 = a*x + b
plt.scatter(x, y)                               # 繪製散佈圖
plt.plot(x, y2)                                 # 繪製迴歸直線

sold = a*31 + b
print('氣溫31度時的銷量 = {}'.format(int(sold)))
plt.plot(31, int(sold), '-o') 
plt.show()                      

