"""
Python Matplotlib.pyplot.hist()用法及代码示例

Matplotlib是Python中的一个库，它是数字的-NumPy库的数学扩展。
Pyplot是Matplotlib模块的基于状态的接口，该模块提供了MATLAB-like接口。
matplotlib.pyplot.hist()函数

matplotlib库的pyplot模块中的hist()函数用于绘制直方图。

用法： matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype=’bar’, align=’mid’, orientation=’vertical’, rwidth=None, log=False, color=None, label=None, stacked=False, \*, data=None, \*\*kwargs)

参数：此方法接受以下描述的参数：

    x:此参数是数据序列。
    bins:此参数是可选参数，它包含整数，序列或字符串。
    range:此参数是可选参数，它是箱子的上下限。
    density:此参数是可选参数，它包含布尔值。
    weights:此参数是可选参数，并且是一个权重数组，与x的形状相同。
    bottom:此参数是每个容器底部基线的位置。
    histtype:此参数是可选参数，用于绘制直方图的类型。 {‘bar’，‘barstacked’，‘step’，‘stepfilled’}
    align:此参数是可选参数，它控制如何绘制直方图。 {‘left’，‘mid’，‘right’}
    rwidth:此参数是可选参数，它是条形图的相对宽度，是箱宽度的一部分
    log:此参数是可选参数，用于将直方图轴设置为对数刻度
    color:此参数是一个可选参数，它是一个颜色规格或一系列颜色规格，每个数据集一个。
    label:此参数是可选参数，它是一个字符串或匹配多个数据集的字符串序列。

返回值：这将返回以下内容：

    n:这将返回直方图箱的值。
    垃圾桶：这将返回箱子的边。
    补丁：这将返回用于创建直方图的单个补丁的列表。

"""

"""
以上实例中我们生成了三组不同的随机数据，并使用 hist() 函数绘制了它们的直方图。通过设置不同的均值和标准差，我们可以生成具有不同分布特征的随机数据。

我们设置了 bins 参数为 30，这意味着将数据范围分成 30 个等宽的区间，然后统计每个区间内数据的频数。
我们设置了 alpha 参数为 0.5，这意味着每个直方图的颜色透明度为 50%。

我们使用 label 参数设置了每个直方图的标签，以便在图例中显示。

然后使用 legend() 函数显示图例。最后，我们使用 title()、xlabel() 和 ylabel() 函数设置了图表的标题和坐标轴标签。
"""
"""
plt.hist()參數設置

arr: 需要計算直方圖的一維數組；
bins: 直方圖的柱數，可選項，默認為10；
density: : 是否將得到的直方圖向量歸一化。默認為0；
color：顏色序列，默認為None；
facecolor: 直方圖顏色；
edgecolor: 直方圖邊框顏色；
alpha: 透明度；
histtype: 直方圖類型，『bar』, 『barstacked』, 『step』, 『stepfilled』；

"""

# hist 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個
'''
#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)

print('以直方圖顯示常態分佈')
x = np.random.randn(N)  #常態分佈數字

n, bins, patches = plt.hist(x, num_bins, facecolor = 'yellow', edgecolor = 'yellow')
print(n)
print(bins)

#第二張圖
plt.subplot(232)

normal_samples = np.random.normal(size = N) # 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples, bins = num_bins)

#第三張圖
plt.subplot(233)

uniform_samples = np.random.uniform(size = N) # 生成 N 組介於 0 與 1 之間均勻分配隨機變數
plt.hist(uniform_samples, bins = num_bins)

#第四張圖
plt.subplot(234)

print('描繪頻率分布圖')

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_onigiri.csv'
dat = pd.read_csv(filename, encoding = 'UTF-8')

print(type(dat))
print(dat)

# 頻率分布圖
plt.hist(dat['店長'], bins = range(0, 200, 10), alpha = 0.5)
plt.hist(dat['太郎'], bins = range(0, 200, 10), alpha = 0.5)

print('計算平均數、變異數、標準差')

print('店長---------')
print('平均:', np.mean(dat['店長']))
print('變異數:', np.var(dat['店長']))
print('標準差:', np.std(dat['店長']))

print('太郎---------')
print('平均:', np.mean(dat['太郎']))
print('變異數:', np.var(dat['太郎']))
print('標準差:', np.std(dat['太郎']))

#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)


# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density = True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)


#第二張圖
plt.subplot(232)


np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100
   
n, bins, patches = plt.hist(x, num_bins,
                            density = 1,
                            color ='green',
                            alpha = 0.7)
   
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
  
plt.plot(bins, y, '--', color ='black')
  
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis') 
  
plt.title('matplotlib.pyplot.hist() function Example\n\n',
          fontweight ="bold")

#第三張圖
plt.subplot(233)

np.random.seed(10**7) 
n_bins = 20
x = np.random.randn(10000, 3) 
    
colors = ['green', 'blue', 'lime'] 
  
plt.hist(x, n_bins, density = True,  
         histtype ='bar', 
         color = colors, 
         label = colors) 
  
plt.legend(prop ={'size':10}) 
  
plt.title('matplotlib.pyplot.hist() function Example\n\n', 
          fontweight ="bold") 

#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合 3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)

# 生成三组随机数据
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 绘制直方图
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()


#第二張圖
plt.subplot(232)

#同坐標軸的多個頻次直方圖

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)


#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合 4', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)

# 生成一组随机数据
data = np.random.randn(1000)

# 绘制直方图
plt.hist(data, bins=30, color='skyblue', alpha=0.8)

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('Value')
plt.ylabel('Frequency')


#第二張圖
plt.subplot(232)

plt.style.use('seaborn-white')
data = np.random.randn(1000)
plt.hist(data)


#第三張圖
plt.subplot(233)


plt.hist(data, bins=30, density=True, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none')


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)
 
# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)
 
# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

plt.show()

print('------------------------------------------------------------')	#60個

# 生成随机数据
data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
plt.hist(data, bins=10)

# 设置图形标题和坐标轴标签
plt.title('RUNOOB hist() Tes')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')

plt.show()
'''
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個



"""
二維頻次直方圖

就像將一維數組分為區間創建一維頻次直方圖一樣，我們也可以將二維數組按照二維區 間進行切分，來創建二維頻次直方圖。

1.plt.hist2d:二維頻次直方圖

繪製二維頻次直方圖最簡單的方法，就是使用Matplotlib的plt.hist2d函數。
"""

"""NG
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

plt.show()
"""

"""
2.plt.hexbin:六邊形區間劃分

二維頻次直方圖是由與坐標軸正交的方塊分割而成的，還有一種常用的方式是用正六邊形分割。Matplotlib 提供了 plt.hexbin 滿足此類需求，將二維數據集分割成蜂窩狀。
"""

"""NG
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
plt.show()

"""
