# ch10_5.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([22, 26, 23, 28, 27, 32, 30])      # 溫度
y = np.array([15, 35, 21, 62, 48, 101, 86])     # 飲料銷售數量

a, b = np.polyfit(x, y, 1)                      # 迴歸直線
print(f'斜率 a = {a:5.2f}')
print(f'截距 b = {b:5.2f}')

y2 = a*x + b
plt.scatter(x, y)                               # 繪製散佈圖
plt.plot(x, y2)                                 # 繪製迴歸直線

sold = a*31 + b
print('氣溫31度時的銷量 = {}'.format(int(sold)))
plt.plot(31, int(sold), '-o') 
plt.show()                      

