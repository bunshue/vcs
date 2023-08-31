'''

matplotlib_無法subplot的

一次顯示一圖

'''

import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個


x1 = np.linspace(-5, 5, 101)
y1 = np.sin(x1)

fig, ax = plt.subplots()
ax.set_title("Sin")
ax.set_xlabel("rad")
ax.plot(x1, y1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()

print('------------------------------------------------------------')	#60個

π = np.pi

θ = np.linspace(0, 2*π, 500)


r = 3
x = r * np.cos(θ)
y = r * np.sin(θ)

#gca 的意思是 "Get Current Axes"。
ax = plt.gca()
ax.set_aspect('equal')

plt.plot(x, y)


plt.show()


print('------------------------------------------------------------')	#60個


r = 1 - np.sin(θ)

x = r * np.cos(θ)
y = r * np.sin(θ)

ax = plt.gca()
ax.set_aspect('equal')

plt.plot(x, y, 'r')

plt.show()



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

