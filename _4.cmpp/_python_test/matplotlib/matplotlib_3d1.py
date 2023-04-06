'''
參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/
'''

#線形圖
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
z = np.add(x, y)

ax.plot(x, y, z)
plt.show()


#散點圖
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

count = 100
range = 100

xs = np.random.rand(count) * range
ys = np.random.rand(count) * range
zs = np.random.rand(count) * range

ax.scatter(xs, ys, zs, s=zs, c=zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()


#線框圖

'''
import numpy as np

x = np.arange(1, 4)
y = np.arange(11, 16)
print(x)
print(y)

X, Y = np.meshgrid(x, y)
print(X)
print(Y)
'''

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 3), np.power(Y, 4))

surf = ax.plot_wireframe(X, Y, Z)

plt.show()


#曲面圖



import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 3), np.power(Y, 2))

surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


#等高線
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = np.add(-np.power(X, 4), np.power(Y, 4))

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.plot_wireframe(X, Y, Z, alpha=0.1)
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)

plt.show()

#柱狀圖
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

np.random.seed(59)
month = np.arange(1, 12)
years = [2016, 2017, 2018, 2019]

def get_color(value_array):
    color = []
    for v in value_array:
        if (v < 50):
            color.append('y')
        elif (v < 100):
            color.append('g')
        elif (v < 150):
            color.append('b')
        elif (v < 200):
            color.append('c')
        elif (v < 250):
            color.append('m')
        else:
            color.append('r')
    return color

for year, c in zip(years, ['b','c','r','m']):
    value = np.random.rand(len(month)) * 300
    ax.bar(month, value, year, zdir='y', color=get_color(value), alpha=0.7)
    for i in np.arange(0, 12):
        ax.bar

ax.set_xlabel('Month')
ax.set_xticks(np.arange(1, 13))
ax.set_ylabel('Year')
ax.set_yticks(np.arange(2016, 2020))
ax.set_zlabel('Precipitation')

plt.show()



#多邊形


import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

np.random.seed(59)
month = np.arange(0, 13)
years = [2016, 2017, 2018, 2019]

precipitation = []
for year in years:
    value = np.random.rand(len(month)) * 300
    value[0], value[-1] = 0, 0
    precipitation.append(list(zip(month, value)))

poly = PolyCollection(precipitation, facecolors=['b','c','r','m'])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=years, zdir='y')
ax.set_xlabel('Month')
ax.set_xlim3d(0, 12)
ax.set_ylabel('Year')
ax.set_ylim3d(2015, 2020)
ax.set_zlabel('Precipitation')
ax.set_zlim3d(0, 300)

plt.show()
