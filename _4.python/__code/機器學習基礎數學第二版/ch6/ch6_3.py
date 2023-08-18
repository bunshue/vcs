# ch6_3.py
import matplotlib.pyplot as plt
import numpy as np                            
a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_x = 1500
pt_y = a * pt_x + b
print('f(1500) = {}'.format(pt_y))
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x, pt_y, '-o')              # 繪點 f(1500)
plt.text(pt_x-150, pt_y+3, 'f(1500)')   # 輸出文字f(1500)
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線
plt.show()






