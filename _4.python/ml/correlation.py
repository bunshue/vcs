"""

correlation

"""
import seaborn as sns  # 海生, 自動把圖畫得比較好看

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
hours_phone_used = [0, 0, 0, 1, 1.3, 1.5, 2, 2.2, 2.6, 3.2, 4.1, 4.4, 4.4, 5]
work_performance = [87, 89, 91, 90, 82, 80, 78, 81, 76, 85, 80, 75, 73, 72]

x = np.array(hours_phone_used)
y = np.array(work_performance)
n = len(x)
x_mean = x.mean()
y_mean = y.mean()
print("資料數:", n)
print("x平均:", x_mean)
print("y平均:", y_mean)

diff = (x - x_mean) * (y - y_mean)
print("x偏差*y編差和:", diff.sum())
covar = diff.sum() / n
print("共變異數:", covar)

corr = covar / (x.std() * y.std())
print("相關係數:", corr)

print("------------------------------")  # 30個

df = pd.DataFrame({"手機使用時間(小時)": hours_phone_used, "工作效率": work_performance})

print("用pd算相關係數")
print("相關係數:", df.corr())

df.plot(kind="scatter", x="手機使用時間(小時)", y="工作效率")
plt.title("手機使用時數與工作效率")
plt.show()

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
plt.show()

print("------------------------------------------------------------")  # 60個
'''
""" data/correlation.csv
     A    B    C    D
0  0.5  0.9  0.4  NaN
1  0.8  0.6  NaN  NaN
2  0.7  0.3  0.8  0.9
3  0.8  0.3  NaN  0.2
4  0.9  NaN  0.7  0.3
5  0.2  0.7  0.6  NaN
"""

df = pd.read_csv("data/correlation.csv")

""" 目前無法造出有NaN的df
datas = [
    [0.5, 0.9, 0.4, "NaN"],
    [0.8, 0.6, "NaN", "NaN"],
    [0.7, 0.3, 0.8, 0.9],
    [0.8, 0.3, "NaN", 0.2],
    [0.9, "NaN", 0.7, 0.3],
    [0.2, 0.7, 0.6, "NaN"],
    ]
columns = ["A", "B", "C", "D"]
df = pd.DataFrame(np.array(datas), columns=columns)
"""
print(df)
cc = df.info()
print(cc)

# 將df的 相關係數 轉 html
#df.corr().to_html("test_csv_corr2html.html")

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
#plt.show()

print("------------------------------------------------------------")  # 60個

"""
数据相关性分析中，经常用到data.corr()函数，data.corr()表示了data中的两个变量之间的相关性，取值范围为[-1,1],取值接近-1，表示反相关，类似反比例函数，取值接近1，表正相关。
DataFrame.corr()函数使用说明如下：

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性                                           数据便会有误差。
kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
spearman：非线性的，非正太分析的数据的相关系数
min_periods：样本最少的数据量
返回值：各类型之间的相关系数DataFrame表格。
"""

df = pd.DataFrame(
    [[1, 6, 7, 5, 1], [2, 10, 8, 3, 4], [3, 4, 0, 10, 2]],
    columns=["val1", "val2", "val3", "val4", "val5"],
)
print(df)


# 5个变量的数据如表所示
# 各变量数据相关性的热力图

sns.heatmap(
    df.corr(), linewidths=0.1, vmax=1.0, square=True, linecolor="white", annot=True
)
plt.show()

# 从图中可以看出，val2和val3的相关性最高为0.83，其次是val2和val5。

print("------------------------------------------------------------")  # 60個

"""
pandas相关系数-DataFrame.corr()参数详解

DataFrame.corr(method='pearson', min_periods=1)

参数说明：
method：可选值为{‘pearson’, ‘kendall’, ‘spearman’}
               pearson：Pearson相关系数来衡量两个数据集合是否在一条线上面，即针对线性数据的相关系数计算，针对非线性数据便会有误差。
                kendall：用于反映分类变量相关性的指标，即针对无序序列的相关系数，非正太分布的数据
                spearman：非线性的，非正太分布的数据的相关系数
min_periods：样本最少的数据量

返回值：各类型之间的相关系数DataFrame表格。
"""

x = [a for a in range(11)]


def y1_x(x):
    return x * 2


def y2_x(x):
    return x**2 // 4


def y3_x(x):
    return (x - 5) ** 2


def y4_x(x):
    return 10 - x


y1 = [y1_x(i) for i in x]
y2 = [y2_x(i) for i in x]
y3 = [y3_x(i) for i in x]
y4 = [y4_x(i) for i in x]

print("x :", x)
print("y1 :", y1)
print("y2 :", y2)
print("y3 :", y3)
print("y4 :", y4)

df = pd.DataFrame({"x": x, "y1": y1, "y2": y2, "y3": y3, "y4": y4})
print(df)
print(df.columns)

columns = ["x", "2倍", "平方除4", "(減5)平方", "10-x"]
df.columns = columns

df.plot(kind="line", legend=True, title="線圖", figsize=[10, 5])

cc = df.head()
print(cc)

cc = df.corr()
print(cc)

plt.figure(figsize=(12, 8))
plt.subplot(221)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="spearman")
print(cc)
plt.subplot(222)
sns.heatmap(cc, annot=True, cmap="coolwarm")

cc = df.corr(method="kendall")
print(cc)
plt.subplot(223)
sns.heatmap(cc, annot=True, cmap="coolwarm")

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


