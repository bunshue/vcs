import os
import sys
import time
import random

import numpy as np
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個
'''
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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrame 是二维数组对象
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
print(df)

print(df.iloc[0])


print('顯示A欄')
print(df.A)

print("Row data type: {}".format(type(df.iloc[0])))
print("Column data type: {}".format(type(df.A)))

print('df之大小')
print(df.shape)

print('df之頭3行')
print(df.head(3))

print('df之尾2行')
print(df.tail(2))

print('顯示df之欄')
print(df.columns)
print('顯示df之index')
print(df.index)
print('顯示df之describe')
print(df.describe())

print('排序')
print(df.sort_index(axis=1, ascending=False))

print('依B欄排序')
print(df.sort_values(by='B'))

print('顯示df之3:5')
print(df[3:5])

print('顯示df之A B D欄')
print(df[['A', 'B', 'D']])

print('顯示')
print(df.loc[3, 'A'])

print('顯示')
print(df.iloc[3, 0])

print('顯示')
print(df.iloc[2:5, 0:2])

print('顯示')
print(df[df.C > 0])

print('加入TAG')
df["TAG"] = ["cat", "dog", "cat", "cat", "cat", "dog"]
print(df)

print(df.groupby('TAG').sum())

print('顯示')

n_items = 366
ts = pd.Series(np.random.randn(n_items), index=pd.date_range('20000101', periods=n_items))

print('顯示ts大小')
print(ts.shape)

print('顯示ts頭5項')
print(ts.head(5))

print('顯示')
print(ts.resample("1m").sum())

plt.figure(figsize=(10, 6))
cs = ts.cumsum()
cs.plot();
plt.show()

plt.figure(figsize=(10, 6))
ts.resample("1m").sum().plot.bar();
plt.show()

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df.to_csv('data.csv')


df = pd.read_csv('data.csv', index_col=0)
print(df.shape)
print(df.head(5))

print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 200, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(20, 6), dpi=80)
plt.subplot(1, 2, 1)
# 使用默认设置画出余弦曲线
plt.plot(X, C)
# 使用默认设置画出正弦曲线
plt.plot(X, S)

plt.subplot(1, 2, 2)
# 移动坐标轴边线
# 坐标轴总共有四个连线，我们通过设置透明色隐藏上方和右方的边线
# 通过 set_position() 移动左侧和下侧的边线
# 通过 set_ticks_position() 设置坐标轴的刻度线的显示位置
ax = plt.gca()  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# 设置坐标刻度的字体大小，增加半透明背景
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
# 设置坐标轴的长度
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# 设置坐标轴的刻度和标签
plt.xticks((-np.pi, -np.pi/2, np.pi/2, np.pi),
          label=(r'$-\pi$', r'$-\pi/2$', r'$+\pi/2$', r'$+\pi$'))
plt.yticks([-1, -0.5, 0, 0.5, 1])


# 画出余弦曲线，并设置线条颜色，宽度，样式
plt.plot(X, C, color="blue", linewidth=2.0, linestyle="-")
# 画出正弦曲线，并设置线条颜色，宽度，样式
plt.plot(X, S, color="red", linewidth=2.0, linestyle="-")

# 在左上角添加铭牌
plt.legend(loc='upper left')

# 在坐标轴上标示相应的点
t = 2 * np.pi / 3
# 画出 cos(t) 所在的点在 X 轴上的位置，即画出 (t, 0) -> (t, cos(t)) 线段，使用虚线
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle="--")
# 画出标示的坐标点，即在 (t, cos(t)) 处画一个大小为 50 的蓝色点
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# 画出标示点的值，即 cos(t) 的值
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 画出 sin(t) 所在的点在 X 轴上的位置，即画出 (t, 0) -> (t, sin(t)) 线段，使用虚线
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=1.5, linestyle="--")
# 画出标示的坐标点，即在 (t, sin(t)) 处画一个大小为 50 的红色点
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
# 画出标示点的值，即 sin(t) 的值
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 把结果显示在屏幕上
plt.show()

print("------------------------------------------------------------")  # 60個


plt.figure(figsize=(18, 4))
plt.subplot(2, 2, 1)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 2)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 3)
plt.xticks(())
plt.yticks(())

plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 4)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
        size=20, alpha=.5)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(18, 4))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

axes_2 = plt.subplot(G[1:, 0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)

axes_4 = plt.subplot(G[1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


plt.figure(figsize=(18, 4))

plt.axes([.1, .1, .8, .8])
plt.xticks(())
plt.yticks(())
plt.text(.2, .5, 'axes([0.1, 0.1, .8, .8])', ha='center', va='center',
        size=20, alpha=.5)

plt.axes([.5, .5, .3, .3])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, 'axes([.5, .5, .3, .3])', ha='center', va='center',
        size=16, alpha=.5)

plt.show()


print("------------------------------------------------------------")  # 60個

def tickline():
    plt.xlim(0, 10), plt.ylim(-1, 1), plt.yticks([])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
    ax.plot(np.arange(11), np.zeros(11))
    return ax

locators = [
                'plt.NullLocator()',
                'plt.MultipleLocator(base=1.0)',
                'plt.FixedLocator(locs=[0, 2, 8, 9, 10])',
                'plt.IndexLocator(base=3, offset=1)',
                'plt.LinearLocator(numticks=5)',
                'plt.LogLocator(base=2, subs=[1.0])',
                'plt.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9, 10])',
                'plt.AutoLocator()',
            ]

n_locators = len(locators)

size = 1024, 60 * n_locators
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)


for i, locator in enumerate(locators):
    plt.subplot(n_locators, 1, i + 1)
    ax = tickline()
    ax.xaxis.set_major_locator(eval(locator))
    plt.text(5, 0.3, locator[3:], ha='center', size=16)

plt.subplots_adjust(bottom=.01, top=.99, left=.01, right=.99)
plt.show()
'''



print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt
import numpy as np


def plt_scatter():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    plt.subplot(1, 2, 1)
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.xlim(-1.5, 1.5)
    plt.xticks(())
    plt.ylim(-1.5, 1.5)
    plt.yticks(())

def plt_fill_between():
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)

    plt.subplot(1, 2, 2)

    plt.plot(X, Y + 1, color='blue', alpha=1.00)
    plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

    plt.plot(X, Y - 1, color='blue', alpha=1.00)
    plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
    plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)

    plt.xlim(-np.pi, np.pi)
    plt.xticks(())
    plt.ylim(-2.5, 2.5)
    plt.yticks(())

plt.figure(figsize=(16, 6))
plt_scatter()
plt_fill_between()
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

def plt_bar():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.subplot(1, 2, 1)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')

    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

    plt.xlim(-.5, n)
    plt.xticks(())
    plt.ylim(-1.25, 1.25)
    plt.yticks(())

def plt_contour():
    def f(x,y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X,Y = np.meshgrid(x, y)

    plt.subplot(1, 2, 2)

    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    plt.clabel(C, inline=1, fontsize=10)

    plt.xticks(())
    plt.yticks(())
    
plt.figure(figsize=(16, 6))
plt_bar()
plt_contour()
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


def plt_imshow():
    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    plt.subplot(1, 2, 1)
    n = 10
    x = np.linspace(-3, 3, 4 * n)
    y = np.linspace(-3, 3, 3 * n)
    X, Y = np.meshgrid(x, y)
    #plt.imshow(f(X, Y), cmap='hot', origin='low')
    plt.imshow(f(X, Y), cmap='hot')
    plt.colorbar(shrink=.83)

    plt.xticks(())
    plt.yticks(())
    
def plt_pie():
    plt.subplot(1, 2, 2)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    
    plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
    plt.axis('equal')
    plt.xticks(())
    plt.yticks()
    
plt.figure(figsize=(16, 6))
plt_imshow()
plt_pie()
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


def plt_grid():
    ax = plt.subplot(1, 2, 1)
    
    ax.set_xlim(0,4)
    ax.set_ylim(0,3)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
def plt_polar():
    ax = plt.subplot(1, 2, 2, polar=True)
    
    N = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r,bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r/10.))
        bar.set_alpha(0.5)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
plt.figure(figsize=(16, 6))
plt_grid()
plt_polar()
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

