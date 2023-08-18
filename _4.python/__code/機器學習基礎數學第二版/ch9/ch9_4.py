# ch9_4.py
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    ''' 求解方程式 '''
    return (3*x**2 - 12*x + 10)

a = 3
b = -12
c = 10
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1-0.2, r1_y+0.3, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.2, r2_y+0.3, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = 3*x**2 - 12*x + 10
plt.plot(x, y)
plt.show()












