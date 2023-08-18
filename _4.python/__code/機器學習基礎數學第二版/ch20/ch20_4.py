# ch20_4.py
import numpy as np

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)

xi_x = [v - x_mean  for v in x]
yi_y = [v - y_mean  for v in y]

data1 = [0]*10
data2 = [0]*10
data3 = [0]*10
for i in range(len(x)):
    data1[i] = xi_x[i] * yi_y[i]
    data2[i] = xi_x[i]**2
    data3[i] = yi_y[i]**2

v1 = np.sum(data1)
v2 = np.sum(data2)
v3 = np.sum(data3)
r = v1 / ((v2**0.5)*(v3**0.5))
print('coefficient = {}'.format(r))








