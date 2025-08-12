"""
python_data_science_matplotlib4

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Visualization with Seaborn

plt.style.use("classic")

# Now we create some random walk data:

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend("ABCDEF", ncol=2, loc="upper left")
show()

sns.set()


# same plotting code as above!
plt.plot(x, y)
plt.legend("ABCDEF", ncol=2, loc="upper left")
show()

# Exploring Seaborn Plots

# Histograms, KDE, and densities

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=["x", "y"])

for col in "xy":
    plt.hist(data[col], alpha=0.5)
show()

# Rather than a histogram, we can get a smooth estimate of the distribution using a kernel density estimation, which Seaborn does with sns.kdeplot:

for col in "xy":
    sns.kdeplot(data[col], shade=True)
show()


sns.distplot(data["x"])
sns.distplot(data["y"])
show()


sns.kdeplot(data)
show()


with sns.axes_style("white"):
    sns.jointplot(x="x", y="y", data=data, kind="kde")
show()


with sns.axes_style("white"):
    sns.jointplot(x="x", y="y", data=data, kind="hex")
show()

# Pair plots

iris = sns.load_dataset("iris")
cc = iris.head()
print(cc)

sns.pairplot(iris, hue="species", size=2.5)
show()


# Faceted histograms

# Sometimes the best way to view data is via histograms of subsets. Seaborn's FacetGrid makes this extremely simple. We'll take a look at some data that shows the amount that restaurant staff receive in tips based on various indicator data:

tips = sns.load_dataset("tips")
cc = tips.head()
print(cc)

tips["tip_pct"] = 100 * tips["tip"] / tips["total_bill"]

grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15))
show()

# 使用 Factor plots factorplot => catplot

with sns.axes_style(style="ticks"):
    g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box")
    g.set_axis_labels("Day", "Total Bill")
show()

# Joint distributions

with sns.axes_style("white"):
    sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
show()

# The joint plot can even do some automatic kernel density estimation and regression:

sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
show()

# Bar plots

# Time series can be plotted using sns.catplot. In the following example, we'll use the Planets data that we first saw in Aggregation and Grouping:

planets = sns.load_dataset("planets")
cc = planets.head()
print(cc)

with sns.axes_style("white"):
    g = sns.catplot(x="year", data=planets, aspect=2, kind="count", color="steelblue")
    g.set_xticklabels(step=5)
show()

# We can learn more by looking at the method of discovery of each of these planets:

with sns.axes_style("white"):
    g = sns.catplot(
        x="year",
        data=planets,
        aspect=4.0,
        kind="count",
        hue="method",
        order=range(2001, 2015),
    )
    g.set_ylabels("Number of Planets Discovered")
show()

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
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
