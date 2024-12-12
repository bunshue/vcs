"""
海生, 自動把圖畫得比較好看

sns.set() 繪圖風格設置

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

# 海生設定

# sns.set()  # 無參數, 海生預設設定, 會清除中文設定
# sns.set(....) # 海生風格設定

# sns.set()  # 無參數, 海生預設設定, 會清除中文設定
# sns.set(color_codes=True)
sns.set(rc={"figure.figsize": (6, 4)})

# sns.set_style("whitegrid")
# sns.set_style("darkgrid", {"axes.axisbelow": False})
# sns.set_style("darkgrid", {"axes.axisbelow": False, "font.sans-serif": ["Microsoft JhengHei"]})

# 海生的中文設定 5 行
font_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_font/TaipeiSansTCBeta-Regular.ttf"
)
import matplotlib as mpl
import matplotlib.font_manager as fm

fm.fontManager.addfont(font_filename)
mpl.rc("font", family="Taipei Sans TC Beta")

print("------------------------------------------------------------")  # 60個

print("使用海生")

plt.plot(x, y)
plt.title("使用海生")

plt.show()

print("------------------------------------------------------------")  # 60個

"""
N = 1000
xx = np.random.randn(N)
print(np.mean(xx))
print('海生函數 histplot')
sns.histplot(xx, kde=False)
"""

print("------------------------------------------------------------")  # 60個

N = 1000  # 樣本數
μ = 87  # 平均值
σ = 2.5  # 標準差
xx = np.random.randn(N) * σ + μ

print("平均值 :", xx.mean())
print("標準差 :", xx.std())

num_bins = 50  # 直方圖顯示時的束數
plt.hist(xx, num_bins, density=True)  # 直方圖

plt.show()

print("------------------------------------------------------------")  # 60個

N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
xx = np.random.normal(mu, sigma, N)  # 隨機數

n, bins, patches = plt.hist(
    xx, bins=num_bins, density=True, color="green", rwidth=0.5, alpha=0.5
)  # 直方圖

# 繪製曲線圖
sns.kdeplot(xx)
plt.title("用海生畫常態分佈")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 10000  # 樣本數
N = 1000  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

mu, sigma = 100, 15  # 平均值, 標準差
xx = np.random.normal(mu, sigma, N)  # 隨機數

plt.figure(figsize=(12, 6))

plt.subplot(131)

count, bins, ignored = plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(132)

plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.subplot(133)

plt.hist(xx, num_bins, density=True)  # 直方圖
sns.kdeplot(xx)  # 核密度估計圖, 多了外圍那圈
plt.title("常態分布 + kdeplot")

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, axes = plt.subplots(1, 2, figsize=(6, 4))

ax1 = sns.lineplot(x=x, y=y, ax=axes[0])
ax2 = sns.scatterplot(x=x, y=y, ax=axes[1])

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame()
df["x"] = x
df["sin"] = y0
df["cos"] = y1
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.relplot(x="x", y="value", kind="scatter", col="variable", data=df2)

plt.show()

print("------------------------------------------------------------")  # 60個

sns.lineplot(x=x, y=y)
sns.despine()  # ?

plt.show()

print(sns.axes_style())

print("------------------------------------------------------------")  # 60個

sns.lineplot(x=x, y=y)

plt.title("Sinus三角函數的波型")
plt.xlim(-2, 12)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame()
df["x"] = x
df["sin"] = y0
df["cos"] = y1
print(df.head())

df2 = pd.melt(df, id_vars=["x"], value_vars=["sin", "cos"])
print(df2.head())

sns.relplot(
    x="x", y="value", kind="scatter", col="variable", height=4, aspect=1.2, data=df2
)

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_data/Kobe_stats.csv")

data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]

sns.relplot(x="Season", y="PTS", data=data, kind="line")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
超详细Seaborn绘图 ——（一）barplot

Seaborn是基于matplotlib的图形可视化python包。它提供了一种高度交互式界面，便于用户能够做出各种有吸引力的统计图表。Seaborn是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，在大多数情况下使用seaborn能做出很具有吸引力的图，而使用matplotlib就能制作具有更多特色的图。应该把Seaborn视为matplotlib的补充，而不是替代物。同时它能高度兼容numpy与pandas数据结构以及scipy与statsmodels等统计模式。
"""

"""
# 显示正负号与中文不显示问题
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('darkgrid', {'font.sans-serif':['SimHei', 'Arial']})

"""


"""
二、barplot
（一）语法
seaborn.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,\
                estimator=<function mean>,ci=95, n_boot=1000, units=None, orient=None,\
                color=None, palette=None, saturation=0.75,\
                errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)
"""
"""
条形图以矩形条的方式展示数据的点估值和置信区间

输入数据的格式可以不同，包括：

以列表，numpy array 或者 pandas 中的 Series object 表示的向量。这些向量可以直接传入 x, y, 以及 hue 参数。
长表, x 值，y 值和色相变量决定了数据是如何绘制的。
宽表，每个列的数值都会被绘制出来.
数组或者列表的向量。
大多数情况下，可以使用 numpy 的对象或者 python 的对象，但是用 pandas 对象更好，因为相关的列名会被标注在图标上。 另外，为了控制绘图元素 也可以可以用分类类型来组合不同的变量。
"""

"""
（二）参数详解
x、y、hue：< data中的变量名词或者向量 >
data中用于绘制图表的变量名

data：< DataFrame, 数组, 数组列表 >
是用于绘图的数据集

order、hue_order：< 字符串列表 >
绘制类别变量的顺序，若没有，则会从数据对象中推断绘图顺序

estimator：< 映射向量 -> 标量 >
统计函数用于估计每个分类纸条中的值

ci：< float or “sd” or None >
估计值周围的置信区间大小。若输入的是sd，会跳过bootstrapping的过程，只绘制数据的标准差；
若输入的是None，不会执行bootstrapping，而且错误条也不会绘制

n_boot：< int >
计算置信区间需要的 Boostrap 迭代次数。

units：< data中的变量名词或向量 >
采样单元的标识符，用于执行多级 bootstrap 并解释重复测量设计。

orient：< “v” 或 “h” >
绘图的方向（垂直或水平）。这通常是从输入变量的数据类型推断出来的，但是可以用来指定“分类”变量是数字还是宽格式数据。

color：< matplotlib color >
作用于所有元素的颜色，或者渐变色的种子。

palette：< palette name, list, or dict >
不同级别的 hue 变量的颜色。 颜色要能被 [color_palette()]解释(seaborn.color_palette.html#seaborn.color_palette “seaborn.color_palette”), 或者一个能映射到 matplotlib 颜色的字典。

saturation：< float >
原始饱和度与绘制颜色的比例。大的色块通常在稍微不饱和的颜色下看起来更好，但是如果希望打印颜色与输入颜色规格完全匹配，请将其设置为1。

errcolor：< matplotlib color >
表示置信区间的线的颜色。

errwidth：< float >
误差条的线的厚度。

capsize：< float >
误差条端部的宽度。

dodge : < 布尔型 >
当使用色调嵌套时，元素是否应该沿分类轴移动。

ax：< matplotlib Axes >
指定一个 Axes 用于绘图，如果不指定，则使用当前的 Axes。

kwargs：< key, value mappings >
其他的关键词参数在绘图时通过 plt.bar 传入。
"""

"""
（三）实例
首先最简单的画个柱形图
"""

plt.figure(dpi=150)
x = ["金融", "农业", "制造业", "新能源"]
y = [164, 86, 126, 53]
sns.barplot(x=x, y=y)
# sns.barplot(y)
# 通过saturation调整饱和度，默认值为0.75
plt.show()


sns.barplot(x=x, y=y, saturation=0.2)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 超详细Seaborn绘图 ——（二）boxplot & boxenplot

"""
箱形图（Box-plot）又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资料的统计图。
它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比较。箱形图最大的优点就是不受异常值的影响（异常值也称为离群值），可以以一种相对稳定的方式描述数据的离散分布情况。
"""

"""
一、基础概念
一个boxplot主要包含六个数据节点，将一组数据从大到小排列，分别计算出他的上边缘（上限），上四分位数Q3，中位数，下四分位数Q1，下边缘（下限），还有一个异常值。

举例来说：
对于这样一个箱线图

中位数=8.5
中位数，即二分之一分位数。所以计算的方法就是将一组数据（此处中位数，特别指是从大到小排列的有序序列）按从小到大的顺序，取中间这个数。
如果原始序列长度n是奇数，那么中位数所在位置是(n+1)/2；如果原始序列长度n是偶数，那么中位数所在位置是n/2，n/2+1，中位数的值等于这两个位置的数的算数平均数

上四分位数Q3=9
确定四分位数的位置。虽然具体的计算目前有3*(n+1)/4与(n-1)/4两种，但一般使用3*(n+1)/4

下四分位数Q1=7
这个下四分位数所在位置计算方法同上。不过是(n+1)/4

四分位间距IQR(ΔQ)=2
四分位间距=Q3-Q1

上限=10
上限是非异常范围内的最大值。

下限=5
下限限是非异常范围内的最小值。

中位数（Q2）=8.5
中位数常用于度量数据的中心。一半观测值小于等于该值，而另一半则大于等于该值。

平均数=8
平均数就不用多说了

异常值
规定大于上四分位数1.5倍四分位数差 的值，或者小于下四分位数1.5倍四分位数差的值，划为异常值

箱线图的作用：

1.直观明了地识别数据批中的异常值
其实箱线图判断异常值的标准以四分位数和四分位距为基础，四分位数具有一定的耐抗性，多达25%的数据可以变得任意远而不会很大地扰动四分位数，所以异常值不会影响箱形图的数据形状，箱线图识别异常值的结果比较客观。由此可见，箱线图在识别异常值方面有一定的优越性。

2.利用箱线图判断数据批的偏态和尾重
对于标准正态分布的样本，只有极少值为异常值。异常值越多说明尾部越重，自由度越小（即自由变动的量的个数）；
而偏态表示偏离程度，异常值集中在较小值一侧，则分布呈左偏态；异常值集中在较大值一侧，则分布呈右偏态。

3.利用箱线图比较几批数据的形状
同一数轴上，几批数据的箱线图并行排列，几批数据的中位数、尾长、异常值、分布区间等形状信息便昭然若揭。如上图，可直观得看出第三季度各分公司的销售额大体都在下降。
但箱形图也有他的局限性，比如：不能精确地衡量数据分布的偏态和尾重程度；对于批量比较大的数据，反映的信息更加模糊以及用中位数代表总体评价水平有一定的局限性。

二、boxplot
（一）语法
seaborn.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, 
                orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, 
                linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)
1
2
3
输入数据可以通过多种格式传入，包括：

格式为列表，numpy 数组或 pandas Series 对象的数据向量可以直接传递给x，y和hue参数。
对于长格式的 DataFrame，x，y，和hue参数会决定如何绘制数据。
对于宽格式的 DataFrame，每一列数值列都会被绘制。
一个数组或向量的列表。
（二）参数详解
x, y, hue：数据或向量数据中的变量名称
用于绘制长格式数据的输入。

data：DataFrame，数组，数组列表
用于绘图的数据集。如果x和y都缺失，那么数据将被视为宽格式。否则数据被视为长格式。

order, hue_order：字符串列表
控制分类变量（对应的条形图）的绘制顺序，若缺失则从数据中推断分类变量的顺序。

orient：“v”或“h”
控制绘图的方向（垂直或水平）。这通常是从输入变量的 dtype 推断出来的，但是当“分类”变量为数值型或绘制宽格式数据时可用于指定绘图的方向。

color：matplotlib颜色
所有元素的颜色，或渐变调色板的种子颜色。

palette：调色板名称，列表或字典
用于hue变量的不同级别的颜色。可以从color_palette()得到一些解释，或者将色调级别映射到matplotlib颜色的字典。

saturation：float
控制用于绘制颜色的原始饱和度的比例。通常大幅填充在轻微不饱和的颜色下看起来更好，如果您希望绘图颜色与输入颜色规格完美匹配可将其设置为1。

width：float
不使用色调嵌套时完整元素的宽度，或主要分组变量一个级别的所有元素的宽度。

dodge：bool
使用色调嵌套时，元素是否应沿分类轴移动。

fliersize：float
用于表示异常值观察的标记的大小。

linewidth：float
构图元素的灰线宽度。

whis：float
控制在超过高低四分位数时 IQR （四分位间距）的比例，因此需要延长绘制的触须线段。超出此范围的点将被识别为异常值。

notch：boolean
是否使矩形框“凹陷”以指示中位数的置信区间。还可以通过plt.boxplot的一些参数来控制

ax：matplotlib轴
绘图时使用的 Axes 轴对象，否则使用当前 Axes 轴对象

kwargs：键值映射
其他在绘图时传给plt.boxplot的参数

"""

# 显示正负号与中文不显示问题
plt.rcParams["axes.unicode_minus"] = False
sns.set_style("darkgrid", {"font.sans-serif": ["SimHei", "Arial"]})

plt.figure(dpi=150)
L = [3, 2, 1, 0, 4]
sns.boxplot(L)
plt.show()


s = pd.Series(L)
print("平均数：", s.median())
print("")
print("下四分位数：", s.quantile(0.25))
print("")
print("中位数:", s.quantile(0.5))
print("")
print("上四分位数：", s.quantile(0.75))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 超详细Seaborn绘图 ——（三）violinplot

"""
一、基础概念
二、语法
三、参数详解
四、实例
一、基础概念
小提琴图是箱线图与核密度图的结合，箱线图展示了分位数的位置，核密度图则展示了任意位置的密度，通过小提琴图可以知道哪些位置的数据点聚集的较多，因其形似小提琴而得名。
"""

"""
其外围的曲线宽度代表数据点分布的密度，中间的箱线图则和普通箱线图表征的意义是一样的，代表着中位数、上下分位数、极差等。
"""

"""
二、语法
seaborn.violinplot(x=None, y=None, hue=None, data=None,
                   order=None, hue_order=None, bw='scott',
                   cut=2, scale='area', scale_hue=True, gridsize=100, 
                   width=0.8,inner='box', split=False, dodge=True,
                   orient=None, linewidth=None,color=None, palette=None,
                   saturation=0.75, ax=None, **kwargs)
"""

"""
三、参数详解
bw：{‘scott’, ‘silverman’, float}
内置变量值或浮点数的比例因子都用来计算核密度的带宽。实际的核大小由比例因子乘以每个分箱内数据的标准差确定。

cut：{float}
以带宽大小为单位的距离，以控制小提琴图外壳延伸超过内部极端数据点的密度。设置为 0 以将小提琴图范围限制在观察数据的范围内。（例如，在 ggplot 中具有与 trim=True 相同的效果）

scale：{“area”, “count”, “width”}
该方法用于缩放每张小提琴图的宽度。若为 area ，每张小提琴图具有相同的面积。若为 count ，小提琴的宽度会根据分箱中观察点的数量进行缩放。若为 width ，每张小提琴图具有相同的宽度。

scale_hue：{bool}
当使用色调参数 hue 变量绘制嵌套小提琴图时&
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
嶺圖 Overlapping densities Ridge plot (FacetGrid)
"""

sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

# 創建資料 Create the data
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
m = df.g.map(ord)
df["x"] += m

# 初始化網格化對象 Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-0.25, light=0.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=0.5, palette=pal)

# 繪製密度 Draw the densities in a few steps
g.map(sns.kdeplot, "x", clip_on=False, shade=True, alpha=1, lw=1.5, bw=0.2)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw=0.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)


# 定義成函數 Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(
        0,
        0.2,
        label,
        fontweight="bold",
        color=color,
        ha="left",
        va="center",
        transform=ax.transAxes,
    )


g.map(label, "x")

# 讓子圖重疊 Set the subplots to overlap
g.fig.subplots_adjust(hspace=-0.25)

# 移除一些不必要的座標資訊 Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x, y = np.random.multivariate_normal([0, 0], [[1, -0.5], [-0.5, 1]], size=300).T
# pal = sns.dark_palette("green", as_cmap=True) 沒什麼差別
sns.kdeplot(x=x, y=y)
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# sns折線圖的繪製範例
# sns.set(style="whitegrid", font="meiryo")

# 調整資料的格式
# sns.set(style="white", font="meiryo")

# ax.legend(loc="lower left", bbox_to_anchor=(1, 0))


# 海生函數 廢棄
sns.lineplot(data=y)
sns.displot(x)
sns.histplot(x)


# plt.xkcd()  #加此行變成搞笑風格

# 多此二行 變成海生風格

plt.rcParams[
    "font.sans-serif"
] = "Microsoft JhengHei"  # 海生設定中文字型 將字體換成 Microsoft JhengHei


sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)
# sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.title("二項式分布 Binomial")

plt.show()

print("------------------------------------------------------------")  # 60個
