# ch5_2.py
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import numpy as np

def fmax(x):
    ''' 計算最大值 '''
    return (-(-3*x**2 + 12*x - 9))

def f(x):
    ''' 求解方程式 '''
    return (-3*x**2 + 12*x - 9)

a = -3
b = 12
c = -9
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1+0.1,r1_y+-0.2,'('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 標記
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.5,r2_y-0.2,'('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 標記
print('root2 = ', r2)                       # print(r2)

# 計算最大值
r = minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(r.x-0.25,f(r.x)-0.7,'('+str(round(r.x,2))+','+
         str(round(f(r.x),2))+')') 
plt.plot(r.x, f(r.x), '-o')                 # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = -3*x**2 + 12*x - 9
plt.plot(x, y, color='b')
plt.grid()
plt.show()












