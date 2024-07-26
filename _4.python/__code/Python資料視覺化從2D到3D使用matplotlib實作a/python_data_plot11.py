# plot 集合

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
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

print("------------------------------------------------------------")  # 60個
'''
N = 1000                        # 數據數量
np.random.seed(10)              # 設定隨機數種子值
x = np.random.normal(0, 1, N)   # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)   # 均值是 0, 標準差是 1
color = x + y                   # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)
plt.scatter(x,y,s=60,alpha=0.5,c=color,cmap='jet',norm=norm)
plt.xlim(-3, 3)
plt.xticks(())                  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())                  # 不顯示 y 刻度
plt.colorbar()                  # 建立色彩條

plt.show()


print("------------------------------------------------------------")  # 60個

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, c=x)
plt.colorbar()                  # 建立色彩條

plt.show()

print("------------------------------------------------------------")  # 60個

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, c=y)
plt.colorbar()                  # 建立色彩條

plt.show()

print("------------------------------------------------------------")  # 60個

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, c=x)
plt.colorbar(orientation='horizontal')  # 建立橫向色彩條

plt.show()

print("------------------------------------------------------------")  # 60個

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)

fig, ax = plt.subplots(2,1)
# 建立子圖 0 的散點圖和色彩條
ax0 = ax[0].scatter(x, y, c=y, cmap='brg')
fig.colorbar(ax0, ax=ax[0])
# 建立子圖 1 的散點圖和色彩條
ax1 = ax[1].scatter(x, y, c=y, cmap='hsv')
fig.colorbar(ax1, ax=ax[1])

plt.show()

print("------------------------------------------------------------")  # 60個

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)

fig, ax = plt.subplots(3,1)
# 建立子圖 0 和 1 的散點圖和色彩條
ax0 = ax[0].scatter(x, y, c=x, cmap='GnBu')

ax1 = ax[1].scatter(x, y, c=x, cmap='GnBu')
fig.colorbar(ax0, ax=(ax[0],ax[1]))     # 共用色彩條

# 建立子圖 2 的散點圖和色彩條
ax2 = ax[2].scatter(x, y, c=y, cmap='hsv')
fig.colorbar(ax2, ax=ax[2])

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
norm = plt.Normalize(vmin=2, vmax=8)        # 定義色彩條的數值區間
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap='spring'),
             cax=ax, orientation='horizontal',
             label='自定義colorbar條')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
# 自行設計色彩映射圖
mycmap = mpl.colors.ListedColormap(['r','g','b'])
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm([2, 4, 6, 8], 3)                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=mycmap),
             cax=ax, orientation='horizontal',
             label='自定義colormap和colorbar')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
top = mpl.cm.get_cmap('Oranges', 128)       # Oranges色彩
bottom = mpl.cm.get_cmap('Greens', 128)     # Greens色彩
# 組合Orange和Greens色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
mycmap = mpl.colors.ListedColormap(newcolors)                                  
fig.colorbar(mpl.cm.ScalarMappable(cmap=mycmap),
             cax=ax, orientation='horizontal',
             label='組合Oranges和Greens')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
top = mpl.cm.get_cmap('Oranges_r', 128)     # Oranges_r色彩
bottom = mpl.cm.get_cmap('Greens', 128)     # Greens色彩
# 組合Orange和Greens色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
mycmap = mpl.colors.ListedColormap(newcolors)                                  
fig.colorbar(mpl.cm.ScalarMappable(cmap=mycmap),
             cax=ax, orientation='horizontal',
             label='組合Oranges_r和Greens')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
cmap = mpl.cm.plasma                        # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='both')                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
             cax=ax, orientation='horizontal',
             label='使用extend=both')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
cmap = mpl.cm.plasma                        # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='min')                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
             cax=ax, orientation='horizontal',
             label='使用extend=min')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
cmap = mpl.cm.plasma                        # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='max')                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
             cax=ax, orientation='horizontal',
             label='使用extend=max')
plt.show()
'''
print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)
x = iris['petal_len'].values        # 花瓣長度
y = iris['sepal_len'].values        # 花萼長度

fig, ax = plt.subplots()
mycmap = mpl.colors.ListedColormap(['b','g','r'])
norm = mpl.colors.BoundaryNorm([0,2,5,7], mycmap.N)
plt.scatter(x, y, c=x, cmap=mycmap, norm=norm)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm,cmap=mycmap),ax=ax)
plt.show()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

