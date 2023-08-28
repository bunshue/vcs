# ch24_4.py
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (x**2)/10 + (y**2)/4

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure(figsize=(10,4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title('contour() 橢圓輪廓平面',fontsize=16,color='b')

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap='GnBu')
plt.title('contourf() 填充橢圓輪廓圓平面',fontsize=16,color='b')
plt.colorbar()                  # 色彩條
plt.show()


      
