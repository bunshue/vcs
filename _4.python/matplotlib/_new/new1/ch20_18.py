# ch20_18.py
import matplotlib.pyplot as plt
import numpy as np

# 函數f(x)的係數
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1*x**2 + c1
plt.plot(x, y1, color='b')      # 藍色是 f(x)

# 函數g(x)的係數
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2*x**2 + b2*x + c2
plt.plot(x, y2, color='g')      # 綠色是 g(x)

# 繪製區間
plt.fill_between(x, y1=y1, y2=y2, where=(x>=-1)&(x<=2),
                 facecolor='yellow')

plt.grid()
plt.show()














