import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(-20, 20, 100)
ay = ax*0.5
by = np.sin(ax)
cx = 10
cy = cx*0.5

plt.plot(ax, ay, color='red', linewidth=3.0, linestyle='dashed', label='x0.5', zorder=2)
plt.plot(ax, by, color='blue', linewidth=2.0, linestyle='solid', label='sin', zorder=2)
# 繪製垂直虛線
plt.plot([cx, cx,],[cy, 0,], color='black', linewidth=1.0, linestyle='dashed', zorder=1, alpha=0.5)

# 加上單一圓點
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(cx, cy, s=100, color='red', zorder=2)

# 繪製 annotate
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.annotate.html
plt.annotate('test', xy=(cx+0.5, cy-0.2), xycoords='data', xytext=(+36, -36),
             textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))


plt.legend(loc='best')

plt.ylim((-10, 10))  # 設定 x 和 y 的邊界值
plt.xlim((-20, 20))

xx = plt.gca()  # 設定座標軸位置
xx.spines['right'].set_color('none')
xx.spines['top'].set_color('none')
xx.spines['bottom'].set_position(('data', 0))
xx.spines['left'].set_position(('data', 0))



plt.show()
