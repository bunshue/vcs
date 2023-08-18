# ch6_4.py
import matplotlib.pyplot as plt
import numpy as np                            
a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03 
print('獲利48萬需有 {} 來客數'.format(int(pt_x)))
plt.plot(x, y)                                      # 繪函數直線
plt.plot(pt_x, pt_y, '-o')                          # 繪點
plt.text(pt_x-150, pt_y+3, '('+str(int(pt_x))+','+str(pt_y)+')')   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                                          # 加格線
plt.show()






