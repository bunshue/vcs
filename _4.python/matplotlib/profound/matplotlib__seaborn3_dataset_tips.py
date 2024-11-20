"""
海生, 自動把圖畫得比較好看

使用海生數據集 load_dataset

tips

"""

print("------------------------------------------------------------")  # 60個

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

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

print("資料來源 : 內建資料 1 計程車小費資料集EDA")

"""
# 計程車小費資料集EDA
共244筆資料, 7個欄位
"""

df = sns.load_dataset("tips")
cc = df.head(30)
print(cc)


df["log_tip"] = np.log(df["tip"])

# 類別變數轉換為數值
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

# 對小費繪製直方圖
sns.histplot(x="tip", data=df)
plt.title("小費統計")
plt.show()

df["log_tip"] = np.log(df["tip"])
sns.kdeplot(x="log_tip", data=df)
plt.show()

# 散佈圖
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

# 三維散佈圖
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

# joint plot
sns.jointplot(data=df, x="total_bill", y="tip", hue="day")
plt.xlabel("全車資")
plt.ylabel("小費")
plt.show()

cc = df.day.unique()
print(cc)

# ['Sun', 'Sat', 'Thur', 'Fri']
# Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']

# 觀察週間對小費的影響

sns.barplot(x="day", y="tip", data=df)
plt.xlabel("星期幾")
plt.ylabel("小費")
plt.show()

# 箱型圖
sns.boxplot(x="day", y="tip", data=df)
plt.xlabel("星期幾")
plt.ylabel("小費")
plt.show()

print("繪製pair plot")
sns.pairplot(data=df, height=1)
plt.title("繪製pair plot")
plt.show()

print("熱力圖")
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=0.5)
plt.title("熱力圖")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據
print(df.head())
print(sns.get_dataset_names())

print("------------------------------")  # 30個

sns.set()
sns.relplot(x="total_bill", y="tip", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.relplot(x="total_bill", y="tip", hue="smoker", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.histplot(df["total_bill"], kde=False)

plt.show()

print("------------------------------")  # 30個

sns.set()
sns.histplot(df["total_bill"], kde=False)
sns.histplot(df["total_bill"], kde=False, bins=20, color="red")
sns.histplot(df["total_bill"], kde=False, bins=30, color="green")

plt.show()

print("------------------------------")  # 30個

sns.set()
sns.kdeplot(df["total_bill"], label="default")
sns.kdeplot(df["total_bill"], bw_adjust=2, label="bw_adjust: 2")
sns.kdeplot(df["total_bill"], bw_adjust=5, label="bw_adjust: 5")
plt.legend()
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.histplot(df["total_bill"], kde=True)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.displot(df["total_bill"], kde=True, rug=True)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.violinplot(x="day", y="total_bill", data=df)

plt.show()

print("------------------------------")  # 30個

sns.set()
sns.violinplot(x="day", y="total_bill", hue="sex", data=df)

plt.show()

print("------------------------------")  # 30個

sns.set()
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.barplot(x="sex", y="total_bill", hue="day", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.countplot(x="sex", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.pointplot(x="sex", y="total_bill", hue="day", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.catplot(x="day", y="total_bill", data=df, kind="bar", hue="sex")
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.catplot(x="day", y="total_bill", data=df, kind="bar", col="sex")
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.catplot(x="sex", y="total_bill", data=df, kind="bar", col="day", col_wrap=2)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.regplot(x="total_bill", y="tip", data=df)
sns.lmplot(x="total_bill", y="tip", data=df)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.regplot(x=df["total_bill"], y=df["tip"])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

tips = sns.load_dataset("tips")  # 示例中的基本數據

# violinplot小提琴圖
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("sns dataset tips 01")

sns.set(style="darkgrid", color_codes=True)  # 帶灰色網格的背景風格

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 4.2.2 連續變量相關圖
# Relplot關係類型圖表
sns.relplot(x="total_bill", y="tip", hue="day", col="time", row="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 02")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 點圖
sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 03")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 線圖
sns.lineplot(x="tip", y="total_bill", hue="sex", style="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 04")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 4.2.3 分類變量圖
# stripplot散點圖
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 05")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# swarmplot散點圖
sns.swarmplot(x="day", y="total_bill", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 06")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# boxplot箱式圖
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 07")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# boxenplot變種箱式圖
sns.boxenplot(x="day", y="total_bill", hue="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 08")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# pointplot分類統計圖
sns.pointplot(
    x="sex",
    y="total_bill",
    hue="smoker",
    data=tips,
    palette={"Yes": "g", "No": "m"},
    markers=["^", "o"],
    linestyles=["-", "--"],
)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 09")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# barplot柱對比圖
sns.barplot(x="smoker", y="total_bill", hue="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 10")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 4.2.4 迴歸圖
# 連續變量回歸圖
sns.lmplot(x="total_bill", y="tip", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 11")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# 分類變量回歸圖
sns.lmplot(x="size", y="total_bill", data=tips, x_estimator=np.mean)

plt.show()

print("------------------------------------------------------------")  # 60個

print("sns dataset tips 12")

tips = sns.load_dataset("tips")  # 示例中的基本數據

# FacetGrid結構化繪圖網格
g = sns.FacetGrid(tips, col="time", row="smoker")  # 按行和列的分類做N個圖
g.map(plt.hist, "total_bill", bins=10)  # 指定做圖方式

plt.show()

print("------------------------------------------------------------")  # 60個

# 印刷品作圖
print("sns dataset tips 13")

sns.set_style("whitegrid")

tips = sns.load_dataset("tips")  # 示例中的基本數據

with sns.cubehelix_palette(
    start=2.7, rot=0, dark=0.5, light=0.8, reverse=True, n_colors=5
):
    # 此處放置具體繪圖函數
    sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

plt.show()

print("------------------------------------------------------------")  # 60個

sns.set()
tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.head())

plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()

print("------------------------------------------------------------")  # 60個


sns.set(style="whitegrid")

tips = sns.load_dataset("tips")
male_tips = tips[tips.sex == "Male"]
female_tips = tips[tips.sex == "Female"]

plt.scatter(male_tips.total_bill, male_tips.tip, label="Male tips")
plt.scatter(female_tips.total_bill, female_tips.tip, label="Female tips")

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

tips = sns.load_dataset("tips")
sns.catplot(x="day", y="tip", data=tips)

print("------------------------------------------------------------")  # 60個

# scatterplot

tips = sns.load_dataset("tips")
fig, axs = plt.subplots(2, 1, figsize=(10, 20))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time", ax=axs[0])
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="size",
    size="size",
    sizes=(20, 80),
    legend="full",
)
axs[0].legend(loc=1)

plt.show()

print("------------------------------------------------------------")  # 60個

# boxplot

fig, axs = plt.subplots(2, 1, figsize=(10, 15))
tips = sns.load_dataset("tips")
sns.boxplot(
    x="day",
    y="total_bill",
    hue="smoker",
    data=tips,
    linewidth=1.5,
    hue_order=["No", "Yes"],
    ax=axs[0],
)
sns.boxplot(x="day", y="total_bill", data=tips, ax=axs[1])
sns.swarmplot(x="day", y="total_bill", data=tips, color=".25", ax=axs[1])

plt.show()

print("------------------------------------------------------------")  # 60個

# catplot

# 分類散點圖
# stript plot

tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips)
plt.show()

# stript plot + jitter
sns.catplot(x="day", y="total_bill", jitter=False, data=tips)
plt.show()

# swarm plot
sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips)
plt.show()


# 分類分布圖
##boxplot
sns.catplot(x="day", y="total_bill", kind="box", data=tips)
plt.show()

sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)
plt.show()

# 小提琴圖(violin plot)
sns.catplot(x="total_bill", y="day", hue="time", kind="violin", data=tips)
plt.show()

sns.catplot(x="day", y="total_bill", hue="sex", kind="violin", split=True, data=tips)
plt.show()

g = sns.catplot(x="day", y="total_bill", kind="violin", data=tips)
sns.swarmplot(x="day", y="total_bill", color="k", size=3, data=tips, ax=g.ax)
plt.show()

print("------------------------------------------------------------")  # 60個

# 使用子圖展示多重關係
tips = sns.load_dataset("tips")
sns.catplot(
    x="day",
    y="total_bill",
    hue="smoker",
    col="time",
    aspect=0.7,
    kind="swarm",
    data=tips,
    sharey=False,
)
plt.subplots_adjust(wspace=0.2)

plt.show()

print("------------------------------------------------------------")  # 60個

## g.map內的plotting function可以是任何matplotlib, sns繪圖方法
tips = sns.load_dataset("tips")

g1 = sns.FacetGrid(tips, col="sex", hue="smoker")
g1.map(plt.scatter, "total_bill", "tip", alpha=0.7)
g1.add_legend()
plt.show()

g2 = sns.FacetGrid(tips, col="sex", hue="smoker")
g2.map(sns.scatterplot, "total_bill", "tip", alpha=0.7)
g2.add_legend()
plt.show()

print("------------------------------------------------------------")  # 60個

# barplot

fig, axs = plt.subplots(1, 2, figsize=(20, 8))
data = sns.load_dataset("tips")
print(data)
##默認分組取平均值，capsize是設置誤差帽條(可和ci混用，用ci設置信心水準，用capsize設定帽蓋長度)
sns.barplot(x="day", y="total_bill", hue="sex", data=data, ax=axs[0], capsize=0.1)
sns.barplot(
    x="tip", y="day", data=data, ci=95, ax=axs[1]
)  # ci表示信心水準(可設置float,sd,None)axs[0].set_title('Plot1')
axs[1].set_title("Plot2")
axs[0].set_ylim(0, 30)
# axs[1].set_xlim(0,4)axs[0].legend(loc=2)
plt.subplots_adjust(wspace=0.2)
plt.show()

##若分組想要取其他種類的統計量，要透過estimator
fig.ax = plt.subplots()
# palette是著色表，可以參考以下網址
# https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette
sns.barplot(
    x="day",
    y="total_bill",
    hue="sex",
    ci=None,
    data=data,
    estimator=np.max,
    palette="Set2",
)

plt.show()

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
