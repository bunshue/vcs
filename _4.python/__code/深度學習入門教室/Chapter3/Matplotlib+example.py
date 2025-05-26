# coding: utf-8
# Matplotlib example

# 必要なライブラリの読込
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# 出力データの準備
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

# グラフの描画
fig, ax = plt.subplots()
ax.plot(t, s)

# グラフのラベルとグリッドを描画
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

# グラフの表示
plt.show()