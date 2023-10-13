import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

x = np.linspace(0.1, 1000, 100000)          # 建立含100000個元素的陣列
y = [(1+1/x)**x for x in x]
plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0.1, 1000, 100000)          # 建立含100000個元素的陣列
y = [(1+1/x)**x for x in x]
#plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(-5, 5, 10000)               # 建立含10000個元素的陣列
y = [1/(1+np.e**-x) for x in x]
plt.axis([-5, 5, 0, 1])
plt.plot(x, y, label="Logistic function")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0.01, 0.99, 100)               # 建立含1000個元素的陣列
y = [np.log(x/(1-x)) for x in x]
plt.axis([0, 1, -5, 5])
plt.plot(x, y, label="Logit function")
plt.plot(0.5, np.log(0.5/(1-0.5)),'-o')

plt.legend(loc="best")                          # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

