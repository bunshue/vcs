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


print("------------------------------------------------------------")  # 60個

