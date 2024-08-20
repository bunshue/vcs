"""
無 scikit-learn(sklearn)的

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

#統率, 武力, 智力, 政治, 魅力
main_features = [87, 86, 82, 78, 100]             # 劉備 特徵值
people_names = [                     # 比較人物人名
    '諸葛亮',
    '關羽',
    '張飛',
    '趙雲',
    '曹操',
    '司馬懿',
    '孫權',
    '周瑜',
    '呂布',
]

people_features = [                   # 比較人物特徵值
    [99, 42, 100, 100, 92],
    [92, 100, 74, 51, 83],
    [86, 99, 78, 36, 57],
    [79, 94, 77, 82, 91],
    [100, 85, 93, 96, 95],
    [95, 62, 98, 95, 84],
    [72, 84, 76, 85, 93],
    [93, 71, 94, 81, 92],
    [84, 98, 61, 12, 55],
]

dist = []                           # 儲存人物相似度值
for feature in people_features:
    distances = 0
    for i in range(len(feature)):
        distances += (main_features[i] - feature[i]) ** 2
    dist.append(math.sqrt(distances))
    
min_ = min(dist)                    # 求最小值
min_index = dist.index(min_)        # 最小值的索引

print(f"與 劉備 最相似的人物 : {people_names[min_index]}")
print(f"相似度值 : {dist[min_index]}")
for i in range(len(dist)):
    print(f"人物 : {people_names[i]}, 相似度 : {dist[i]:6.2f}")

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

#numpy cumsum()函数简介
#函数作用：求数组的所有元素的累计和，可通过参数axis指定求某个轴向的统计值。

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])

print(a)

print('累計和')
cc = a.cumsum()
print(cc)
#array([ 1,  3,  6, 10, 15, 21], dtype=int32)

print('累計和, axis=0')
cc = np.cumsum(a, axis=0)
print(cc)

print('累計和, axis=1')
cc = np.cumsum(a, axis=1)
print(cc)

#隨機漫步算法

n_person = 2000
n_times = 500

t = np.arange(n_times)
steps = 2 * np.random.randint(2, size=(n_person, n_times)) - 1

amount = np.cumsum(steps, axis=1)
sd_amount = amount ** 2
mean_sd_amount = sd_amount.mean(axis=0)

plt.figure(figsize=(8, 6))

plt.xlabel(r"$t$", fontsize=16)
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$", fontsize=24)

plt.plot(t, np.sqrt(mean_sd_amount), 'g.')
plt.plot(t, np.sqrt(t), 'r-')

plt.title('隨機漫步算法')

plt.show()

print("------------------------------------------------------------")  # 60個

#多項式擬合

N = 10
n_order = 3 # 3階

x = np.linspace(0, 1, N)
y = x + 0.4*(np.random.rand(N)-0.5)
p = np.poly1d(np.polyfit(x, y, n_order))
print(p.coeffs)

t = np.linspace(0, 1, 100)

plt.plot(x, x, 'r-', label='理論')
plt.plot(x, y, 'go', label='實驗')
plt.plot(t, p(t), 'b-', label='擬合')
plt.legend()

plt.title('多項式擬合, ' + str(n_order) + " 階")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 20

x = np.linspace(0, 1, N)                   # [0, 1] 之间创建 20 个点
#y = np.sqrt(x) + 0.2*np.random.rand(N) - 0.1
y = x + 0.2*np.random.rand(N) - 0.1

def plot_polynomial_fit(x, y, order):
    p = np.poly1d(np.polyfit(x, y, order))

    # 画出拟合出来的多项式所表达的曲线以及原始的点
    t = np.linspace(0, 1, 200)
    #plt.plot(x, y, 'ro', t, p(t), '-', t, np.sqrt(t), 'r--')
    plt.plot(x, x, 'r-', label='理論')
    plt.plot(x, y, 'go', label='實驗')
    plt.plot(t, p(t), 'b-', label='擬合')
    return p

plt.figure(figsize=(18, 4))
titles = ['Under Fitting', 'Fitting', 'Over Fitting']
models = [None, None, None]

order = 1
plt.subplot(131)
models[0] = plot_polynomial_fit(x, y, order)
plt.title(titles[0] + ", " +str(order) + ", 階", fontsize=20)

order = 3
plt.subplot(132)
models[1] = plot_polynomial_fit(x, y, order)
plt.title(titles[1] + ", " +str(order) + ", 階", fontsize=20)

order = 10
plt.subplot(133)
models[2] = plot_polynomial_fit(x, y, order)
plt.title(titles[2] + ", " +str(order) + ", 階", fontsize=20)

plt.legend()
plt.show()

print("------------------------------")  # 30個

for m in models:
    print('model coeffs: {0}'.format(m.coeffs))

print("------------------------------")  # 30個

# 针对一阶多项式的模型，不同的参数拟合出来的直线和训练样本对应的位置关系
coeffs_1d = [0.2, 0.6]

plt.figure(figsize=(9, 6))
t = np.linspace(0, 1, 200)
plt.plot(x, y, 'ro', t, models[0](t), '-', t, np.poly1d(coeffs_1d)(t), 'r-')
plt.annotate(r'L1: $y = {1} + {0}x$'.format(coeffs_1d[0], coeffs_1d[1]),
             xy=(0.8, np.poly1d(coeffs_1d)(0.8)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'L2: $y = {1} + {0}x$'.format(models[0].coeffs[0], models[0].coeffs[1]),
             xy=(0.3, models[0](0.3)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.show()


print("------------------------------------------------------------")  # 60個

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

print('df之內容')
print(df)

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
cs.plot()
plt.show()

plt.figure(figsize=(10, 6))
ts.resample("1m").sum().plot.bar()
plt.show()

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df.to_csv('tmp_data.csv')

df = pd.read_csv('tmp_data.csv', index_col=0)
print(df.shape)
print(df.head(5))

print("------------------------------------------------------------")  # 60個

#逻辑回归模型成本函数

def f_1(x):
    return -np.log(x)

def f_0(x):
    return -np.log(1 - x)

X = np.linspace(0.01, 0.99, 100)
f = [f_1, f_0]
titles = ["y=1: $-log(h_\\theta(x))$", "y=0: $-log(1 - h_\\theta(x))$"]
plt.figure(figsize=(12, 4))
for i in range(len(f)):
    plt.subplot(1, 2, i + 1)
    plt.title(titles[i])
    plt.xlabel("$h_\\theta(x)$")
    plt.ylabel("$Cost(h_\\theta(x), y)$")
    plt.plot(X, f[i](X), 'r-')

plt.suptitle('邏輯回歸模型成本函數')

plt.show()

print("------------------------------------------------------------")  # 60個

print('L1/L2 范数')

def L1(x):
    return 1 - np.abs(x)

def L2(x):
    return np.sqrt(1 - np.power(x, 2))

def contour(v, x):
    return 5 - np.sqrt(v - np.power(x + 2, 2))    # 4x1^2 + 9x2^2 = v

def format_spines(title):    
    ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
    ax.spines['right'].set_color('none')            # 隐藏坐标轴
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')           # 设置刻度显示位置
    ax.spines['bottom'].set_position(('data',0))    # 设置下方坐标轴位置
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))      # 设置左侧坐标轴位置

    plt.title(title)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

plt.figure(figsize=(8.4, 4), dpi=144)

x = np.linspace(-1, 1, 100)
cx = np.linspace(-3, 1, 100)

plt.subplot(1, 2, 1)
format_spines('L1 norm')
plt.plot(x, L1(x), 'r-', x, -L1(x), 'r-')
plt.plot(cx, contour(20, cx), 'r--', cx, contour(15, cx), 'r--', cx, contour(10, cx), 'r--')

plt.subplot(1, 2, 2)
format_spines('L2 norm')
plt.plot(x, L2(x), 'b-', x, -L2(x), 'b-')
plt.plot(cx, contour(19, cx), 'b--', cx, contour(15, cx), 'b--', cx, contour(10, cx), 'b--')

plt.show()

print("------------------------------------------------------------")  # 60個

def entropy(px):
    return - (px * np.log2(px))

x = np.linspace(0.01, 1, 100)
plt.figure(figsize=(5, 3), dpi=200)
plt.title('$Entropy(x) = - P(x) * log_2(P(x))$')
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel('P(x)')
plt.ylabel('Entropy')
plt.plot(x, entropy(x), 'r-')

plt.show()

print("------------------------------------------------------------")  # 60個

def gini_impurity(px):
    return px * (1 - px)

x = np.linspace(0.01, 1, 100)
plt.figure(figsize=(5, 3), dpi=200)
plt.title('$Gini(x) = P(x) (1 - P(x))$')
plt.xlim(0, 1)
plt.ylim(0, 0.6)
plt.xlabel('P(x)')
plt.ylabel('Gini Impurity')
plt.plot(x, entropy(x), 'r-')

plt.show()

print("------------------------------------------------------------")  # 60個

def gaussian_kernel(x, mean, sigma):
    return np.exp(- (x - mean)**2 / (2 * sigma**2))

x = np.linspace(0, 6, 500)
mean = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(10, 3), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)
plt.title('Gaussian for $\sigma={0}$'.format(sigma1))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, gaussian_kernel(x, mean, sigma1), 'r-')

# sub plot 2
plt.subplot(1, 2, 2)
plt.title('Gaussian for $\sigma={0}$'.format(sigma2))

plt.xlim(0, 2)
plt.ylim(0, 1.1)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, gaussian_kernel(x, mean, sigma2), 'r-')

plt.show()

print("------------------------------------------------------------")  # 60個

def normal_distribution(x, mean, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(- (x - mean)**2 / (2 * sigma**2))

x = np.linspace(0, 6, 500)
mean1 = 1
mean2 = 1
sigma1 = 0.1
sigma2 = 0.3

plt.figure(figsize=(10, 3), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)
plt.title('Gaussian Distribution for $\mu={0}, \sigma={1}$'.format(mean1, sigma1))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, normal_distribution(x, mean1, sigma1), 'r-')

# sub plot 2
plt.subplot(1, 2, 2)
plt.title('Gaussian Distribution for $\mu={0}, \sigma={1}$'.format(mean2, sigma2))

plt.xlim(0, 2)
plt.ylim(0, 5)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.plot(x, normal_distribution(x, mean2, sigma2), 'r-')

plt.show()

print(normal_distribution(6, 5.855, np.sqrt(3.5033e-02)))

print("------------------------------------------------------------")  # 60個

dots = np.array([[1, 1.5], [2, 1.5], [3, 3.6], [4, 3.2], [5, 5.5]])

def cross_point(x0, y0):
    """
    1. line1: y = x
    2. line2: y = -x + b => x = b/2
    3. [x0, y0] is in line2 => b = x0 + y0

    => x1 = b/2 = (x0 + y0) / 2
    => y1 = x1
    """
    x1 = (x0 + y0) / 2
    return x1, x1


plt.figure(figsize=(8, 6), dpi=144)
plt.title('2-dimension to 1-dimension')

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()                                  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')            # 隐藏坐标轴
ax.spines['top'].set_color('none')

plt.scatter(dots[:, 0], dots[:, 1], marker='s', c='b')
plt.plot([0.5, 6], [0.5, 6], '-r')
for d in dots:
    x1, y1 = cross_point(d[0], d[1])
    plt.plot([d[0], x1], [d[1], y1], '--b')
    plt.scatter(x1, y1, marker='o', c='r')
plt.annotate(r'projection point',
             xy=(x1, y1), xycoords='data',
             xytext=(x1 + 0.5, y1 - 0.5), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'vector $u^{(1)}$',
             xy=(4.5, 4.5), xycoords='data',
             xytext=(5, 4), fontsize=10,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




