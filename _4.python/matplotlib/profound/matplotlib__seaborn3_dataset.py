"""
海生, 自動把圖畫得比較好看

使用海生數據集 load_dataset

Seaborn是基於Matplotlib的Python繪圖庫，並有繪圖指令簡單、圖樣風格精美等優點。
Seaborn is a Python visualization library based on matplotlib.
It is easy to use and provides a high-level interface for drawing attractive statistical graphics.
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

print("取得 sns 資料集")

cc = sns.get_dataset_names()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fmri = sns.load_dataset("fmri")

sns.set()
sns.relplot(x="timepoint", y="signal", data=fmri, kind="line")

sns.relplot(x="timepoint", y="signal", ci=None, data=fmri, kind="line")
sns.relplot(x="timepoint", y="signal", ci="sd", data=fmri, kind="line")
sns.relplot(x="timepoint", y="signal", estimator=None, data=fmri, kind="line")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fmri = sns.load_dataset("fmri")  # 觀察fmri的資料型態是pandas
print(type(fmri))
print(fmri.head())

ax = sns.lineplot(x="timepoint", y="signal", data=fmri, err_style=None)
plt.show()

ax = sns.lineplot(x="timepoint", y="signal", data=fmri, err_style="band")
plt.show()

ax = sns.lineplot(x="timepoint", y="signal", data=fmri, err_style="bars")
plt.show()

fig, axs = plt.subplots(1, 2, sharey=True)
sns.lineplot(x="timepoint", y="signal", hue="event", data=fmri, ax=axs[0])
sns.lineplot(x="timepoint", y="signal", data=fmri, err_style="bars", ax=axs[1])
# 設定hue="event"會畫出，不同的event對應的signal數值vs.timepoint
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fmri = sns.load_dataset("fmri")

# 畫出不同region和event組合下不同的subject的signal vs. timepoint
sns.relplot(
    x="timepoint",
    y="signal",
    hue="subject",
    col="region",
    row="event",
    height=3,
    kind="line",
    estimator=None,
    data=fmri,
)
plt.show()

print(fmri.query("region == 'frontal'"))
# 大量水平變量狀況下，若展開多個圖，可以用col_wrap來指定圖片數目達到多少時換行，此利用以5為例
g = sns.relplot(
    x="timepoint",
    y="signal",
    hue="event",
    style="event",
    col="subject",
    col_wrap=5,
    height=2,
    aspect=1,
    linewidth=1.5,
    kind="line",
    data=fmri.query("region == 'frontal'"),
)
# height:圖片高
# aspect:圖片寬
# linewidth:線寬
# kind:指定繪圖方式
g.fig.suptitle("suptitle", x=0.5, y=1.1)
plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
print(iris.head())

sns.set()
sns.jointplot(x="petal_length", y="petal_width", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.jointplot(x="petal_length", y="petal_width", kind="hex", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.jointplot(x="petal_length", y="petal_width", kind="kde", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.pairplot(iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.pairplot(iris, kind="scatter", diag_kind="kde", hue="species", palette="husl")
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.stripplot(x="species", y="sepal_length", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.stripplot(x="species", y="sepal_length", jitter=False, data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.swarmplot(x="species", y="sepal_length", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.boxplot(x="species", y="petal_length", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.boxplot(x="petal_length", y="species", data=iris)
plt.show()

print("------------------------------")  # 30個

sns.set()
sns.boxplot(data=iris, orient="h")

plt.show()

print("------------------------------------------------------------")  # 60個

# pairplot
iris = sns.load_dataset("iris")
iris.head()
sns.pairplot(data=iris, hue="species")

plt.show()

print("------------------------------------------------------------")  # 60個

# violinplot

fig, axs = plt.subplots(1, 2)
iris = sns.load_dataset("iris")
sns.violinplot(x="species", y="sepal_length", data=iris, ax=axs[0])
sns.violinplot(x=iris.species, y=iris.sepal_length, ax=axs[1])

plt.show()

print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
iris.head()

sns.set()
sns.pairplot(iris, hue="species", height=3)
print(iris)

plt.show()

print("------------------------------------------------------------")  # 60個

# iris

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
print("------------------------------------------------------------")  # 60個

anscombe = sns.load_dataset("anscombe")

sns.set()
sns.lmplot(
    x="x",
    y="y",
    col="dataset",
    hue="dataset",
    data=anscombe,
    col_wrap=2,
    ci=None,
    height=4,
)
plt.show()

print("------------------------------")  # 30個

anscombe = sns.load_dataset("anscombe")

sns.set()
sns.lmplot(x="x", y="y", data=anscombe.query("dataset=='II'"), order=2)

plt.show()

print("------------------------------")  # 30個

anscombe = sns.load_dataset("anscombe")

sns.set()
sns.residplot(x="x", y="y", data=anscombe.query("dataset=='III'"))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 熱力圖
planets = sns.load_dataset("planets")
corr = planets[["number", "orbital_period", "mass", "distance"]].corr(method="pearson")
sns.heatmap(corr, cmap="YlGnBu")

plt.show()

print("------------------------------")  # 30個

plt.subplots()
planets = sns.load_dataset("planets")
print(planets)

# discrtete的tuple個對應到x軸和y軸，log_scale同理
sns.histplot(
    data=planets,
    x="year",
    y="distance",
    bins=30,
    discrete=(True, False),
    cbar=True,
    log_scale=(False, True),
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

titanic = sns.load_dataset("titanic")
print(titanic.head())

sns.countplot(x="class", hue="survived", data=titanic)
plt.show()

sns.countplot(x="sex", hue="survived", data=titanic)
plt.show()

print("------------------------------")  # 30個

# 分類統計估計圖 #barplot
titanic = sns.load_dataset("titanic")
g1 = sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic, ci=None)
plt.show()

g2 = sns.catplot(
    x="survived",
    hue="class",
    kind="count",
    palette="pastel",
    edgecolor=".6",
    data=titanic,
)
# catplot本身是個FacetGrid
g1.ax.set_title("Survived vs. sex between differenrt class")
plt.show()

# 點圖(point plot)
sns.catplot(
    x="class",
    y="survived",
    hue="sex",
    palette={"male": "g", "female": "m"},
    markers=["^", "o"],
    linestyles=["-", "--"],
    kind="point",
    data=titanic,
)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# histplot
penguins = sns.load_dataset("penguins")
print(penguins)

fig, axs = plt.subplots(1, 2)
sns.histplot(data=penguins, x="flipper_length_mm", ax=axs[0], kde=True)
sns.histplot(data=penguins, y="flipper_length_mm", ax=axs[1], bins=15)
axs[0].set_title("Histplot1")
axs[1].set_title("Histplot2")

plt.show()

fig, axs = plt.subplots(3, 2)
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", ax=axs[0][0])
sns.histplot(
    data=penguins, x="flipper_length_mm", hue="species", ax=axs[0][1], multiple="stack"
)
sns.histplot(
    data=penguins, x="flipper_length_mm", hue="species", ax=axs[1][0], element="step"
)
sns.histplot(
    data=penguins, x="flipper_length_mm", hue="species", ax=axs[1][1], element="poly"
)

axs[0][0].set_title("Add hue")
axs[0][1].set_title("Add hue+ stack")
axs[1][0].set_title("set element=step")
axs[1][1].set_title("set element=poly")

sns.histplot(
    data=penguins, x="flipper_length_mm", ax=axs[2][0], bins=20, stat="density"
)
sns.histplot(
    data=penguins,
    x="flipper_length_mm",
    ax=axs[2][1],
    bins=20,
    stat="probability",
    fill=False,
)
axs[2][0].set_title("stat=density")
axs[2][1].set_title("stat=probability, fill=False")

plt.show()

# X 和 Y都指定的histplot

plt.subplots()
penguins1 = penguins
sns.histplot(
    data=penguins1,
    x="bill_depth_mm",
    y="body_mass_g",
    hue="species",
    cbar=True,
    cbar_kws=dict(shrink=0.75),
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# jointplot

penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
plt.show()

sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.show()

sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="reg")
plt.show()

g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6)
plt.show()

g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_marginals(sns.rugplot, color="r", height=-0.15, clip_on=False)
plt.show()

# FacetGrid

# 以上兩種搭配一起用

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# heatmap

flights = sns.load_dataset("flights")
flights = flights.pivot(index="month", columns="year", values="passengers")
print(flights)

ax = sns.heatmap(flights)
plt.show()

ax = sns.heatmap(flights, annot=True, fmt="d")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用mask來只畫出部分熱力圖
random_data = np.random.randn(10, 200)
corr = np.corrcoef(random_data)
mask = np.zeros_like(corr)
print(mask)
mask[np.triu_indices_from(mask)] = True
print(mask)
fig, ax = plt.subplots()
sns.heatmap(corr, ax=ax, mask=mask, vmax=0.3, square=True)

plt.show()

grid_kws = {"height_ratios": (0.95, 0.05), "hspace": 0.3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(
    flights, ax=ax, cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"}
)

plt.show()

print("------------------------------------------------------------")  # 60個
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

# 熱力圖 sns.heatmap
# 用於顯示矩陣數據的顏色編碼表示，通常用於顯示相關矩陣或數據透視表。

flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

sns.heatmap(flights_pivot, annot=True, fmt="d")
plt.show()

"""
適合情境
相關矩陣的可視化：當你想要檢視多個變數之間的相關性時，熱力圖是一個很好的工具。
例如，觀察各變數之間的相關係數。
矩陣數據的可視化：可以用來表示其他類型的矩陣數據，例如混淆矩陣。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

flights = sns.load_dataset("flights")
flights.head()

flights_wide = flights.pivot(index="year", columns="month", values="passengers")

flights_wide.head()  # 畫出不同月份乘客人數和年份的關係

sns.lineplot(data=flights_wide)
plt.show()

# 和上例是等效的，但是每組以不同“顏色”線分開
sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.show()

# 和上例是等效的，但是每組以不同“破折號”種類分開
sns.lineplot(data=flights, x="year", y="passengers", style="month")
plt.show()

# 和上例是等效的，但是每組以不同“粗細的線”分開
sns.lineplot(data=flights, x="year", y="passengers", size="month")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
小提琴圖 Violinplot
小提琴圖特點類似盒鬚圖，但更能夠展示資料分佈密度。 
Violinplots are really close from a boxplots, but are better at showing the density of data.
"""

sns.set(style="whitegrid")

# 使用seaborn官方提供的資料 Load the example dataset of brain network correlations
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

# 取用指定資料 Pull out a specific subset of networks
used_networks = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17]
used_columns = df.columns.get_level_values("network").astype(int).isin(used_networks)
df = df.loc[:, used_columns]

# 運算相關矩陣以及平均 Compute the correlation matrix and average over networks
corr_df = df.corr().groupby(level="network").mean()
corr_df.index = corr_df.index.astype(int)
corr_df = corr_df.sort_index().T

# 設定窗口 Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 6))

# 繪製小提琴圖(以較窄的寬度) Draw a violinplot with a narrower bandwidth than the default
sns.violinplot(data=corr_df, palette="Set3", bw=0.2, cut=1, linewidth=1)

# 最終化圖形 Finalize the figure
ax.set(ylim=(-0.7, 1.05))
sns.despine(left=True, bottom=True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
熱圖 Heatmap
熱圖以顏色變化來顯示資料，以色彩深淺直觀的來顯示數值大小。
Heatmap show individual values in a matrix with different colors, allowing us to feel the data intuitively by just looking at the matrix.
"""

sns.set()

# 載入資料 Load data
flights_long = sns.load_dataset("flights")

flights = flights_long.pivot(index="month", columns="year", values="passengers")

# 繪製顯示數值的熱圖 Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=0.5, ax=ax)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
核密度估計 KDE plot
多個雙變量的核密度估計圖。
Multiple bivariate KDE plots.
"""

sns.set(style="darkgrid")
iris = sns.load_dataset("iris")

# 指定鳶尾花子集 Subset the iris dataset by species
setosa = iris.query("species == 'setosa'")
virginica = iris.query("species == 'virginica'")

# 設定視窗 Set up the figure
f, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")

# 繪製核密度估計圖 Draw the two density plots
ax = sns.kdeplot(
    x=setosa.sepal_width,
    y=setosa.sepal_length,
    cmap="Reds",
    shade=True,
    shade_lowest=False,
)
ax = sns.kdeplot(
    x=virginica.sepal_width,
    y=virginica.sepal_length,
    cmap="Blues",
    shade=True,
    shade_lowest=False,
)

# 加上標籤 Add labels to the plot
red = sns.color_palette("Reds")[-2]
blue = sns.color_palette("Blues")[-2]
ax.text(2.5, 8.2, "virginica", size=16, color=blue)
ax.text(3.8, 4.5, "setosa", size=16, color=red)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
群集熱圖 Clustermap
群集熱圖有兩個部分 - 數值色塊熱圖與分類樹狀圖。從數值色塊可以直觀觀測數據，而樹狀圖則可提供分組歸類結果。
Clustermap contains two parts - heatmap and tree plot. The heatmap gives us intuition of the value, yet the tree plot show the clustering result.
"""

sns.set()
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
used_columns = df.columns.get_level_values("network").astype(int).isin(used_networks)
df = df.loc[:, used_columns]

used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
used_columns = df.columns.get_level_values("network").astype(int).isin(used_networks)
df = df.loc[:, used_columns]

# 為不同類別創建色盤 Create a categorical palette to identify the networks
network_pal = sns.husl_palette(8, s=0.45)
network_lut = dict(zip(map(str, used_networks), network_pal))

# 將色盤轉為向量，繪製在矩陣旁 Convert the palette to vectors that will be drawn on the side of the matrix
networks = df.columns.get_level_values("network")
network_colors = pd.Series(networks, index=df.columns).map(network_lut)

# 繪圖 Draw the full plot
sns.clustermap(
    df.corr(),
    center=0,
    cmap="vlag",
    row_colors=network_colors,
    col_colors=network_colors,
    linewidths=0.75,
    figsize=(13, 13),
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# import statsmodels.api as sm # 示例使用了statsmodels庫中的自帶的數據
# import matplotlib as mpl

print("------------------------------------------------------------")  # 60個
