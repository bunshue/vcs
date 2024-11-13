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

"""
超详细Seaborn绘图 ——（一）barplot

Seaborn是基于matplotlib的图形可视化python包。它提供了一种高度交互式界面，便于用户能够做出各种有吸引力的统计图表。Seaborn是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，在大多数情况下使用seaborn能做出很具有吸引力的图，而使用matplotlib就能制作具有更多特色的图。应该把Seaborn视为matplotlib的补充，而不是替代物。同时它能高度兼容numpy与pandas数据结构以及scipy与statsmodels等统计模式。
"""

"""
# 显示正负号与中文不显示问题
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('darkgrid', {'font.sans-serif':['SimHei', 'Arial']})

# 去除部分warning
import warnings
warnings.filterwarnings('ignore')
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

# 还可以选用Seaborn的内置数据集来进行可视化处理

# 首先导入数据集

tips = sns.load_dataset("tips")

cc = tips.head(5)
print(cc)


# 可以通过tips.info()查看数据集的一些具体信息
cc = tips.info()
print(cc)


# 总共有7个特征，244条数据。接下来进行可视化处理

# 通过添加hue来绘制一组由两个变量嵌套分组的垂直条形图

plt.figure(dpi=150)
sns.barplot(x="day", y="tip", data=tips, hue="sex")
plt.show()

"""
其中每个柱条的黑色的线条为误差线
误差线源于统计学，表示数据误差(或不确定性)范围，以更准确的方式呈现数据。误差线可以用标准差(standard deviation,SD)、标准误(standard error,SE)和置信区间表示，使用时可选用任意一种表示方法并作相应说明即可。当误差线比较“长”时，一般要么是数据离散程度大，要么是数据样本少。
"""

print("------------------------------------------------------------")  # 60個


# 绘制水平的条形图

plt.figure(dpi=150)
sns.barplot(y="day", x="tip", data=tips)
plt.show()


# 要是觉得这个默认的色系不好看，可以使用一个不同的调色盘来绘制图案

plt.figure(dpi=150)
sns.barplot(x="size", y="tip", data=tips, palette="Blues_d")
plt.show()


# 对于palette的一些具体说明，会在后续慢慢阐述。

# 用误差条显示平均值的标准误差

plt.figure(dpi=150)
sns.barplot(x="size", y="tip", data=tips, palette="Blues_d", ci=95)
plt.show()


# 还可以个性化误差线（调整线的颜色和厚度）

plt.figure(dpi=150)
sns.barplot(
    x="size",
    y="tip",
    data=tips,
    palette="plasma_r",
    ci=95,
    errcolor="yellow",
    errwidth=2,
    alpha=0.3,
)
plt.show()


# 给误差条增加"端点"

plt.figure(dpi=150)
sns.barplot(
    x="size",
    y="tip",
    data=tips,
    palette="plasma_r",
    ci=95,
    errcolor="yellow",
    errwidth=2,
    capsize=0.1,
    alpha=0.3,
)
plt.show()

# 在使用hue后，柱形本身的宽度会发生改变。若想保持柱形原宽度，可以设置dodge=False

plt.figure(dpi=150)
tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.barplot(x="day", y="total_bill", hue="weekend", data=tips, dodge=False)

plt.show()

# 还可以用plt.bar中的一些参数


plt.figure(dpi=150)
sns.set_style("white")
sns.barplot(
    x="day",
    y="total_bill",
    data=tips,
    linewidth=2.5,
    facecolor=(1, 1, 1, 0),
    errcolor=".2",
    edgecolor=".2",
)
plt.show()

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

# 去除部分warning
import warnings

warnings.filterwarnings("ignore")

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

# 导入tips数据集进行后续的操作

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", data=tips)

plt.show()

# 根据 2 个分类变量嵌套分组绘制一个箱型图

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", hue="sex", data=tips)

plt.show()

# 通过显式传入参数指定顺序控制箱型图的显示顺序

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", hue="sex", data=tips, order=["Sun", "Sat", "Fri", "Thur"])

plt.show()

# 通过palette修改每个类别的颜色

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", hue="sex", data=tips, palette="Set2", saturation=0.4)

plt.show()

# 变成横向的

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(y="day", x="tip", hue="sex", data=tips, palette="Set2", saturation=0.4)

plt.show()

# 修改异常点的大小

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", hue="sex", data=tips, fliersize=1)

plt.show()

"""
#人工改变异常值范围

默认异常值为大于Q3＋1.5IQR或小于Q1-1.5IQR的值。通过whis参数可以改变IQR的因数大小进而改变异常值范围

例如：

对于以下数据集，Q1=1.25，Q3=3.25，IQR=2
因此异常值的返回为(6.25,+∞)、(-∞,-1.75)
所以L中的8为异常值
"""

plt.figure(dpi=150)
L = [3, 2, 1, 0, 4, 8]
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


"""
但是如果通过whis人工修改异常值范围，例如设定whis=3
那么异常值的界限就成了Q3+3*IQR和Q1-3*IQR
即(9.75,+∞)、(-∞,-4.75)

那么8就不是异常值了
"""

plt.figure(dpi=150)
L = [3, 2, 1, 0, 4, 8]
sns.boxplot(L, whis=3)

plt.show()

# 突出中位数的置信区间

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="tip", hue="sex", data=tips, notch=True)

plt.show()

"""
三、boxenplot
boxenplot是为更大的数据集绘制增强的箱型图。这种风格的绘图最初被命名为“信值图”，因为它显示了大量被定义为“置信区间”的分位数。它类似于绘制分布的非参数表示的箱形图，其中所有特征对应于实际观察的数值点。通过绘制更多分位数，它提供了有关分布形状的更多信息，特别是尾部数据的分布。

（一）语法
seaborn.boxenplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None,
                  color=None, palette=None, saturation=0.75, width=0.8, dodge=True,
                  k_depth='proportion',linewidth=None, scale='exponential', outlier_prop=None,
                  ax=None, **kwargs)
1
2
3
4
（二）参数详解
作为增强版的boxplot，boxenplot很多参数和boxplot是相似的。现在就剩下不同的参数进行详解

k_depth：“proportion” 或 “tukey” 或 “trustworthy”
通过增大百分比的粒度控制绘制的盒形图数目。每个参数代表利用不同的统计特性对异常值的数量做出不同的假设。

scale：“linear” 或 “exponential” 或 “area”
用于控制增强箱型图宽度的方法。所有参数都会给显示效果造成影响。 “linear” 通过恒定的线性因子减小宽度，“exponential” 使用未覆盖的数据的比例调整宽度， “area” 与所覆盖的数据的百分比成比例。

outlier_prop：float
被认为是异常值的数据比例。与 k_depth 结合使用以确定要绘制的百分位数。默认值为 0.007 作为异常值的比例。该参数取值应在[0,1]范围内。

"""

# 绘制一个独立的横向增强箱型图

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x=tips["total_bill"])

plt.show()

# 根据分类变量分组绘制一个纵向的增强箱型图

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", data=tips)

plt.show()

# 根据 2 个分类变量嵌套分组绘制一个增强箱型图

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips)

plt.show()

# 改变盒形图数目

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips, k_depth="tukey")

plt.show()

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips, k_depth="trustworthy")

plt.show()

# 控制增强箱型图宽度

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips, scale="linear")

plt.show()

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips, scale="exponential")

plt.show()

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.boxenplot(x="day", y="total_bill", hue="smoker", data=tips, scale="area")

plt.show()

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


# 超详细Seaborn绘图 ——（五）pointplot

"""
pointplot，如其名，就是点图。点图代表散点图位置的数值变量的中心趋势估计，并使用误差线提供关于该估计的不确定性的一些指示。

点图比条形图在聚焦一个或多个分类变量的不同级别之间的比较时更为有用。点图尤其善于表现交互作用：一个分类变量的层次之间的关系如何在第二个分类变量的层次之间变化。

重要的一点是点图仅显示平均值（或其他估计值），但在许多情况下，显示分类变量的每个级别的值的分布可能会带有更多信息。在这种情况下，其他绘图方法，例如箱型图或小提琴图可能更合适。
"""


"""
一、语法
seaborn.pointplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
                  estimator=<function mean>, ci=95, n_boot=1000, units=None,
                  markers='o', linestyles='-', dodge=False, join=True, scale=1,
                  orient=None, color=None, palette=None, errwidth=None, capsize=None, ax=None, **kwargs)
"""


"""
二、参数详解
estimator：调用函数实现向量 -> 标量的映射
在每个分箱内进行估计的统计函数。

ci：float 或 “sd” 或 None
在估计值附近绘制置信区间的尺寸大小。如果是“sd”，则跳过引导阶段并绘制观察数据点的标准差。如果为 None，则不会执行引导过程，并且不会绘制误差块。

n_boot：int
计算置信区间时使用的引导迭代次数

units：data 或 vector data 中变量的名称
采样单元的标识符，用于执行多级引导过程（计算置信区间等）并能够处理重复测量的设定

markers：字符串或字符串列表
用于每个hue色调的级别的标记

linestyles：字符串或字符串列表
用于每个hue色调的级别的线条风格

join：bool
如果为True，则在hue级别相同的点估计值之间绘制线条

scale：float
绘图元素的比例因子

errwidth：float
误差线（和上下限指示线）的厚度

capsize：float
误差线“上下限指示线”的宽度
"""

print("------------------------------------------------------------")  # 60個

# 绘制最简单的pointplot

plt.figure(dpi=150)
tips = sns.load_dataset("tips")
sns.pointplot(x="time", y="total_bill", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

# 绘制两个变量的pointplot

plt.figure(dpi=150)
sns.pointplot(x="time", y="total_bill", hue="smoker", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

# 通过dodge避免重叠

plt.figure(dpi=150)
sns.pointplot(x="time", y="total_bill", hue="smoker", dodge=True, data=tips)


plt.show()

print("------------------------------------------------------------")  # 60個


# 以列表的形式修改每个分类变量标记点的样式以及线的样式

plt.figure(dpi=150)
sns.pointplot(
    x="time",
    y="total_bill",
    hue="smoker",
    data=tips,
    markers=["o", "x"],
    linestyles=["-", "--"],
    dodge=True,
)


plt.show()

print("------------------------------------------------------------")  # 60個

# 取消点与点之间的连线

plt.figure(dpi=150)
sns.pointplot(x="tip", y="day", data=tips, markers="h", join=False)

plt.show()

print("------------------------------------------------------------")  # 60個

# 用中位数作为集中趋势的估计

from numpy import median

plt.figure(dpi=150)
sns.pointplot(x="tip", y="day", data=tips, markers="h", estimator=median)

plt.show()

print("------------------------------------------------------------")  # 60個


# 用误差线显示均值的标准误差

from numpy import median

plt.figure(dpi=150)
sns.pointplot(x="day", y="tip", data=tips, markers="h", errwidth=1, ci=68, capsize=0.2)

plt.show()

print("------------------------------------------------------------")  # 60個

# 显示观测值的标准偏差而不是置信区间

from numpy import median

plt.figure(dpi=150)
sns.pointplot(
    x="day", y="tip", data=tips, markers="h", errwidth=1, ci="sd", capsize=0.2
)

plt.show()

print("------------------------------------------------------------")  # 60個

# 还可以通过ci=None取消误差线的展示

from numpy import median

plt.figure(dpi=150)
sns.pointplot(
    x="day",
    y="tip",
    data=tips,
    markers="h",
    errwidth=1,
    ci=None,
    linestyles=":",
    capsize=0.2,
)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
【資料分析】Seaborn 常用視覺化基礎操作語法彙整

該使用 Seaborn 還是使用 Matplotlib ?

Matplotlib 適合需要高度自定義和控制的情況，尤其是在進行更複雜的、非標準的視覺化時。

Seaborn 適合進行快速的探索性數據分析，或是在需要美觀的統計圖表時使用。
        它特別適合與 Pandas 數據框整合，用於視覺化數據的分佈和關係。

Seaborn 提供了一個簡單且美觀的方式來進行資料視覺化，尤其是在進行統計分析時。
Matplotlib 則提供了更靈活和強大的自定義功能，但可能需要更多的代碼和設置。
兩者常常被結合使用，根據需要選擇適合的工具來進行視覺化。

該選擇什麼圖來表現數據?
散佈圖 sns.scatterplot: 當你想探索兩個連續變數之間的關係時，使用散佈圖。
折線圖 sns.lineplot: 當你需要展示數據隨時間或其他連續變數變化的趨勢時，使用折線圖。
柱狀圖 sns.barplot: 當你想比較分類變數的平均值或總值時，使用柱狀圖。
直方圖 sns.histplot: 當你需要了解數據的分佈狀況時，使用直方圖。
箱線圖 sns.boxplot: 當你想展示數據的集中趨勢及離群點時，使用箱線圖。
熱力圖 sns.heatmap: 當你想可視化變數之間的相關性或矩陣數據時，使用熱力圖。
成對圖 sns.pairplot: 當你需要同時查看多個變數之間的兩兩關係時，使用成對關係圖。

"""

# 散佈圖 sns.scatterplot
# 用於顯示兩個數值變量之間的關係，並可以通過顏色和大小來表示其他維度。

# 加載內建的 iris 數據集
iris = sns.load_dataset("iris")

# 繪製散佈圖
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
plt.show()

"""
適合情境
變數間的關係：當你想要觀察兩個連續變數之間的關係時，散佈圖是理想的選擇。例如，觀察總賬單金額 (total_bill) 與小費 (tip) 之間的關係。
分類變數的影響：你可以使用 hue、style 或 size 參數來檢視分類變數如何影響變數之間的關係。
"""

print("------------------------------------------------------------")  # 60個

# 散佈圖參數調整

# 生成樣本數據
tips = sns.load_dataset("tips")

# 繪製散佈圖
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="day",
    style="time",
    size="size",
    palette="viridis",
    alpha=0.7,
)

plt.title("Scatterplot of Total Bill vs Tip")
plt.show()

"""
參數說明
x：X 軸數據
y：Y 軸數據
hue：根據某變量的值來調整點的顏色
style：根據某變量的值來調整點的樣式
size：根據某變量的值來調整點的大小
palette：設置顏色調色盤
alpha：設置點的透明度
"""
print("------------------------------------------------------------")  # 60個

# 折線圖 sns.lineplot
# 用於顯示數值變量隨著某一維度（通常是時間）變化的趨勢。

# 加載內建的 flights 數據集
flights = sns.load_dataset("flights")

# 繪製折線圖
sns.lineplot(x="year", y="passengers", data=flights)
plt.show()

"""
適合情境
時間序列分析：當你想要觀察變數隨著時間的變化趨勢時，折線圖非常適合。例如，觀察某產品在一段時間內的銷售趨勢。
多組比較：當你有多組數據需要在同一張圖中比較時，使用 hue 和 style 來區分不同的組別。
"""
print("------------------------------------------------------------")  # 60個

# 折線圖參數調整
# 繪製折線圖
sns.lineplot(
    data=tips,
    x="size",
    y="total_bill",
    hue="day",
    style="time",
    markers=True,
    dashes=False,
    errorbar="sd",
)

plt.title("Lineplot of Total Bill by Party Size")
plt.show()

"""
參數說明
x：X 軸數據
y：Y 軸數據
hue：根據某變量的值來調整線條顏色
style：根據某變量的值來調整線條樣式
markers：設置是否顯示標記點
dashes：設置是否顯示虛線
errorbar：設置置信區間
"""
print("------------------------------------------------------------")  # 60個

# 柱狀圖 sns.barplot
# 用於顯示類別變量與數值變量之間的關係，通常用於比較不同組別的平均值。

# 繪製柱狀圖
sns.barplot(x="species", y="sepal_width", data=iris)
plt.show()

"""
適合情境
分類變數的比較：當你想要比較分類變數的平均值或總值時，柱狀圖是理想的選擇。例如，觀察不同日期的總賬單金額的平均值。
組間比較：使用 hue 可以觀察不同組別間的差異，例如性別對總賬單金額的影響。
"""
print("------------------------------------------------------------")  # 60個

# 柱狀圖參數調整

# 繪製條形圖
sns.barplot(
    data=tips, x="day", y="total_bill", hue="sex", errorbar="sd", palette="coolwarm"
)

plt.title("Barplot of Total Bill by Day and Sex")
plt.show()

"""
參數說明
x：X 軸數據（分類變量）
y：Y 軸數據（數值變量）
hue：根據某變量的值來調整柱子的顏色
errorbar：設置置信區間
estimator：設置用於計算條形高度的函數（默認為平均值）
palette：設置顏色調色盤
"""

print("------------------------------------------------------------")  # 60個

# 直方圖 sns.histplot
# 用於顯示數值變量的分佈情況，可以用於單一變量或多變量的直方圖繪製。

# 繪製直方圖
sns.histplot(iris["sepal_length"], kde=True)
plt.show()

"""
適合情境
數據分佈：當你想要了解某個變數的數據分佈時，直方圖是最佳選擇。例如，觀察顧客的小費分佈情況。
多組分佈比較：使用 hue 可以觀察不同組別的數據分佈情況，例如性別對小費分佈的影響。
"""

print("------------------------------------------------------------")  # 60個

# 直方圖參數調整
# 繪製直方圖
sns.histplot(data=tips, x="total_bill", hue="sex", bins=20, kde=True, palette="magma")

plt.title("Histogram of Total Bill")
plt.show()

"""
參數說明
x：X 軸數據
y：Y 軸數據（可選）
hue：根據某變量的值來調整顏色
bins：設置直方圖的分箱數量
multiple：設置如何處理不同類別的數據（例如 stack 或 dodge）
kde：設置是否顯示核密度估計
"""
print("------------------------------------------------------------")  # 60個

# 熱力圖 sns.heatmap
# 用於顯示矩陣數據的顏色編碼表示，通常用於顯示相關矩陣或數據透視表。

"""NG
# 繪製熱力圖
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d")
plt.show()

"""

"""
適合情境
相關矩陣的可視化：當你想要檢視多個變數之間的相關性時，熱力圖是一個很好的工具。例如，觀察各變數之間的相關係數。
矩陣數據的可視化：可以用來表示其他類型的矩陣數據，例如混淆矩陣。
"""

print("------------------------------------------------------------")  # 60個
"""
#熱力圖參數調整
# 繪製熱力圖
correlation_matrix = tips.corr()

sns.heatmap(data=correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, linecolor="black")

plt.title('Correlation Matrix Heatmap')
plt.show()
"""

"""
參數說明
data：矩陣數據（如相關矩陣）
annot：設置是否在每個格子中顯示數值
fmt：設置顯示數值的格式（如 .2f 顯示兩位小數）
cmap：設置顏色地圖
linewidths：設置格子之間的間隔線寬度
linecolor：設置格子之間的間隔線顏色
"""
print("------------------------------------------------------------")  # 60個


# 成對圖 sns.pairplot
# 用於顯示數據集中所有變量之間的成對關係，特別適合初步探索數據的關聯性。

# 繪製成對圖
sns.pairplot(iris, hue="species")
plt.show()

"""
適合情境
變數之間的成對關係：當你想要觀察多個變數之間的成對關係時，
成對關係圖可以幫助你一次性查看所有變數的兩兩關係。
例如，觀察小費數據集中的所有變數之間的關係。
數據探索：在初步探索數據集時，可以快速了解數據集中各變數之間的關聯和分佈情況。
"""

print("------------------------------------------------------------")  # 60個


# 成對圖參數調整
# 繪製成對關係圖
sns.pairplot(data=tips, hue="sex", palette="husl", kind="scatter", diag_kind="kde")

plt.title("Pairplot of Tips Dataset")
plt.show()
"""
參數說明
hue：根據某變量的值來調整顏色
palette：設置顏色調色盤
kind：設置散佈圖的類型（如 scatter 或 kde）
diag_kind：設置對角線圖的類型（如 hist 或 kde）
"""
print("------------------------------------------------------------")  # 60個

# 箱線圖 sns.boxplot
# 用於顯示數值變量的分佈情況及其異常值，通常用於比較多個組別的數值變量。

# 繪製箱線圖
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.show()

"""
適合情境
數據的集中趨勢與離群點：當你需要觀察數據的集中趨勢（如中位數）和數據的離群點時，
箱線圖是非常有用的。例如，觀察不同日期的總賬單金額分佈及離群點。
組間分佈比較：使用 hue 可以比較不同組別之間的數據分佈差異，例如性別對總賬單金額分佈的影響。
"""

print("------------------------------------------------------------")  # 60個

# 箱線圖參數調整
# 繪製箱線圖
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex", palette="Set2", fliersize=5)

plt.title("Boxplot of Total Bill by Day and Sex")
plt.show()

"""
參數說明
x：X 軸數據（分類變量）
y：Y 軸數據（數值變量）
hue：根據某變量的值來調整箱線圖的顏色
palette：設置顏色調色盤
fliersize：設置離群點的大小
width：設置箱線圖的寬度
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
