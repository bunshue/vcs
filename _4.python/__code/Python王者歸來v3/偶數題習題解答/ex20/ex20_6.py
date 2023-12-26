# ex20_6.py
import matplotlib.pyplot as plt
import numpy as np

# 函數的係數
a = -1
b = 2
# 繪製區間圖形
x = np.linspace(-2, 4, 1000)
y = a*x**2 + b*x
plt.plot(x, y, color='b')
plt.fill_between(x, y1=y, y2=0, where=(x>=-2)&(x<=5),
                 facecolor='lightgreen')

plt.grid()
plt.show()














