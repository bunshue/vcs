'''
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x_st = 0.15
y_st = 0.60
w = 0.7
h = 0.3
pic1 = fig.add_axes([x_st, y_st, w, h])

pic1.set_ylabel('Voltage [V]')
pic1.set_title('A sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = pic1.plot(t, s, color='blue', lw=2)

# Fixing random state for reproducibility
np.random.seed(1234567)

#設定圖表在整個視窗的位置與大小
x_st = 0.15
y_st = 0.10
w = 0.7
h = 0.3
pic2 = fig.add_axes([x_st, y_st, w, h])
N = 10 #資料數
n, bins, patches = pic2.hist(np.random.randn(1000), N,
                            facecolor='yellow', edgecolor='yellow')
pic2.set_xlabel('Time [s]')

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0, 100)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

fig, ax = plt.subplots(figsize=(5, 3))
fig.subplots_adjust(bottom=0.15, left=0.2)
ax.plot(x1, y1*10000)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Damped oscillation [V]')


plt.show()




import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sinc(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.margins(0.2, 0.2)

plt.show()


xx, yy = np.meshgrid(x, x)
zz = np.sinc(np.sqrt((xx - 1)**2 + (yy - 1)**2))

fig, ax = plt.subplots(ncols=2, figsize=(12, 8))
ax[0].imshow(zz)
ax[0].set_title("default margins")
ax[1].imshow(zz)
ax[1].margins(0.2)
ax[1].set_title("margins(0.2)")

plt.show()

'''


#直方圖
import matplotlib.pyplot as plt
from numpy.random import normal,rand
x = normal(size=200)

N = 10 #資料數
plt.hist(x,bins=N)
plt.show()

'''
#散點圖
import matplotlib.pyplot as plt
from numpy.random import rand
a = rand(100)
b = rand(100)
plt.scatter(a,b)
plt.show()
'''






