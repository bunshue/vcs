import os
import sys
import time
import random

import numpy as np
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個

#随机漫步算法

n_person = 2000
n_times = 500

t = np.arange(n_times)
steps = 2 * np.random.randint(2, size=(n_person, n_times)) - 1

amount = np.cumsum(steps, axis=1)
sd_amount = amount ** 2
mean_sd_amount = sd_amount.mean(axis=0)

plt.figure(figsize=(8, 6))
plt.xlabel(r"$t$", fontsize=16)
plt.tick_params(labelsize=12)
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$", fontsize=24)
plt.plot(t, np.sqrt(mean_sd_amount), 'g.', t, np.sqrt(t), 'r-');

plt.show()

print("------------------------------------------------------------")  # 60個

#多项式拟合



n_dots = 20
n_order = 3

x = np.linspace(0, 1, n_dots)
y = np.sqrt(x) + 0.2*np.random.rand(n_dots)
p = np.poly1d(np.polyfit(x, y, n_order))
print(p.coeffs)

t = np.linspace(0, 1, 200)
#plt.figure(figsize=(16, 12), dpi=200)
plt.plot(x, y, 'ro', t, p(t), '-');


plt.show()



print("------------------------------------------------------------")  # 60個
#蒙特卡罗方法求圆周率

n_dots = 1000000
x = np.random.random(n_dots)
y = np.random.random(n_dots)
distance = np.sqrt(x ** 2 + y ** 2)
in_circle = distance[distance < 1]

pi = 4 * float(len(in_circle)) / n_dots
print(pi)



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
