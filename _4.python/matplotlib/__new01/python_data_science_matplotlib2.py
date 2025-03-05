"""
python_data_science_matplotlib2

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

# Text and Annotation

import matplotlib as mpl

plt.style.use("seaborn-whitegrid")

# Example: Effect of Holidays on US Births

"""
births.csv 15547筆資料 5欄位
year,month,day,gender,births
1969,1,1,F,4046
1969,1,1,M,4440
1969,1,2,F,4454
1969,1,2,M,4548
"""
births = pd.read_csv("data/births.csv")

quartiles = np.percentile(births["births"], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query("(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)")

births["day"] = births["day"].astype(int)

births.index = pd.to_datetime(
    10000 * births.year + 100 * births.month + births.day, format="%Y%m%d"
)
births_by_date = births.pivot_table("births", [births.index.month, births.index.day])
births_by_date.index = [
    pd.datetime(2012, month, day) for (month, day) in births_by_date.index
]

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
show()


# 畫上一些註解

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# Add labels to the plot
style = dict(size=10, color="gray")

ax.text("2012-1-1", 3950, "New Year's Day", **style)
ax.text("2012-7-4", 4250, "Independence Day", ha="center", **style)
ax.text("2012-9-4", 4850, "Labor Day", ha="center", **style)
ax.text("2012-10-31", 4600, "Halloween", ha="right", **style)
ax.text("2012-11-25", 4450, "Thanksgiving", ha="center", **style)
ax.text("2012-12-25", 3850, "Christmas ", ha="right", **style)

# Label the axes
ax.set(title="USA births by day of year (1969-1988)", ylabel="average daily births")

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter("%h"))
show()


# Transforms and Text Position

fig, ax = plt.subplots(facecolor="lightgray")
ax.axis([0, 10, 0, 10])

# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure)
show()


ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
fig.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Arrows and Annotation

fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis("equal")

ax.annotate(
    "local maximum",
    xy=(6.28, 1),
    xytext=(10, 4),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

ax.annotate(
    "local minimum",
    xy=(5 * np.pi, -1),
    xytext=(2, -6),
    arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=-90"),
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)

# Add labels to the plot
ax.annotate(
    "New Year's Day",
    xy=("2012-1-1", 4100),
    xycoords="data",
    xytext=(50, -30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"),
)

ax.annotate(
    "Independence Day",
    xy=("2012-7-4", 4250),
    xycoords="data",
    bbox=dict(boxstyle="round", fc="none", ec="gray"),
    xytext=(10, -40),
    textcoords="offset points",
    ha="center",
    arrowprops=dict(arrowstyle="->"),
)

ax.annotate(
    "Labor Day",
    xy=("2012-9-4", 4850),
    xycoords="data",
    ha="center",
    xytext=(0, -20),
    textcoords="offset points",
)
ax.annotate(
    "",
    xy=("2012-9-1", 4850),
    xytext=("2012-9-7", 4850),
    xycoords="data",
    textcoords="data",
    arrowprops={
        "arrowstyle": "|-|,widthA=0.2,widthB=0.2",
    },
)

ax.annotate(
    "Halloween",
    xy=("2012-10-31", 4600),
    xycoords="data",
    xytext=(-80, -40),
    textcoords="offset points",
    arrowprops=dict(
        arrowstyle="fancy",
        fc="0.6",
        ec="none",
        connectionstyle="angle3,angleA=0,angleB=-90",
    ),
)

ax.annotate(
    "Thanksgiving",
    xy=("2012-11-25", 4500),
    xycoords="data",
    xytext=(-120, -60),
    textcoords="offset points",
    bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
    arrowprops=dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=80,rad=20"),
)


ax.annotate(
    "Christmas",
    xy=("2012-12-25", 3850),
    xycoords="data",
    xytext=(-30, 0),
    textcoords="offset points",
    size=13,
    ha="right",
    va="center",
    bbox=dict(boxstyle="round", alpha=0.1),
    arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1),
)

# Label the axes
ax.set(title="USA births by day of year (1969-1988)", ylabel="average daily births")

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter("%h"))

ax.set_ylim(3600, 5400)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Customizing Ticks

# Major and Minor Ticks

plt.style.use("classic")

ax = plt.axes(xscale="log", yscale="log")
ax.grid()
show()

# tick properties—locations and labels

print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())

print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

# Hiding Ticks or Labels

ax = plt.axes()
ax.plot(np.random.rand(50))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
show()

# Notice that we've removed the labels (but kept the ticks/gridlines) from the x axis, and removed the ticks (and thus the labels as well) from the y axis. Having no ticks at all can be useful in many situations—for example, when you want to show a grid of images. For instance, consider the following figure, which includes images of different faces, an example often used in supervised machine learning problems (see, for example, In-Depth: Support Vector Machines):

fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

# Get some face data from scikit-learn
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces().images

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")
show()


# Reducing or Increasing the Number of Ticks

fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# For every axis, set the x and y major locator
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
fig.show()

# Fancy Tick Formats

# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label="Sine")
ax.plot(x, np.cos(x), lw=3, label="Cosine")

# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.axis("equal")
ax.set_xlim(0, 3 * np.pi)
show()

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
fig.show()


def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)


ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
fig.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Settings-and-Stylesheets

# Customizing Matplotlib: Configurations and Stylesheets

# Plot Customization by Hand

plt.style.use("classic")

x = np.random.randn(1000)
plt.hist(x)
show()

# use a gray background
ax = plt.axes(facecolor="#E6E6E6")
ax.set_axisbelow(True)

# draw solid white grid lines
plt.grid(color="w", linestyle="solid")

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

# hide top and right ticks
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors="gray", direction="out")
for tick in ax.get_xticklabels():
    tick.set_color("gray")
for tick in ax.get_yticklabels():
    tick.set_color("gray")

# control face and edge color of histogram
ax.hist(x, edgecolor="#E6E6E6", color="#EE6666")
show()

# Changing the Defaults: rcParams

IPython_default = plt.rcParams.copy()

from matplotlib import cycler

colors = cycler(
    "color", ["#EE6666", "#3388BB", "#9988DD", "#EECC55", "#88BB44", "#FFBBBB"]
)
plt.rc(
    "axes",
    facecolor="#E6E6E6",
    edgecolor="none",
    axisbelow=True,
    grid=True,
    prop_cycle=colors,
)
plt.rc("grid", color="w", linestyle="solid")
plt.rc("xtick", direction="out", color="gray")
plt.rc("ytick", direction="out", color="gray")
plt.rc("patch", edgecolor="#E6E6E6")
plt.rc("lines", linewidth=2)

# With these settings defined, we can now create a plot and see our settings in action:

plt.hist(x)
show()

print("------------------------------------------------------------")  # 60個

# Let's see what simple line plots look like with these rc parameters:

for i in range(4):
    plt.plot(np.random.rand(10))
show()

print("------------------------------------------------------------")  # 60個

# Stylesheets

cc = plt.style.available[:5]
print(cc)

"""
plt.style.use('stylename')

with plt.style.context('stylename'):
    make_a_plot()
"""


def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(["a", "b", "c"], loc="lower left")
    plt.show()


# Default style

# reset rcParams
IPython_default = plt.rcParams.copy()
plt.rcParams.update(IPython_default)
show()


hist_and_lines()

# FiveThiryEight style

with plt.style.context("fivethirtyeight"):
    hist_and_lines()

# ggplot


with plt.style.context("ggplot"):
    hist_and_lines()

# Bayesian Methods for Hackers

with plt.style.context("bmh"):
    hist_and_lines()

# Dark background

with plt.style.context("dark_background"):
    hist_and_lines()

# Grayscale

with plt.style.context("grayscale"):
    hist_and_lines()

# Seaborn style

import seaborn

hist_and_lines()


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
