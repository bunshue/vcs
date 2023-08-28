# ch24_3.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return np.sin(x)**5 + np.cos(5 + y) * np.cos(x)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = np.linspace(0, 5, 30)
y = np.linspace(0, 5, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure(figsize=(10,4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title('contour函數',fontsize=16,color='b')

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap='Oranges')
plt.title('contourf函數, cmap=Oranges',fontsize=16,color='b')
plt.show()


      
