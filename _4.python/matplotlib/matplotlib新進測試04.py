"""


"""


print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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

# Import matplotlib convention
import matplotlib.pyplot as plt

#Anatomy of a figure

import numpy as np
import matplotlib.pyplot as plt

# Prepare Data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create Plot
fig, ax = plt.subplots()

# Plot Data
ax.plot(x, y)

# Customize Plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine Function')
ax.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個

#Basic Plots

# Create a scatter plot
X = np.random.uniform(0, 1, 100)
Y = np.random.uniform(0, 1, 100)
plt.scatter(X, Y)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a bar plot
X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
plt.bar(X, Y)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create an image plot using imshow
Z = np.random.uniform(0, 1, (8, 8))
plt.imshow(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a contour plot
Z = np.random.uniform(0, 1, (8, 8))
plt.contourf(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a pie chart
Z = np.random.uniform(0, 1, 4)
plt.pie(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a histogram
Z = np.random.normal(0, 1, 100)
plt.hist(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create an error bar plot
X = np.arange(5)
Y = np.random.uniform(0, 1, 5)
plt.errorbar(X, Y, Y / 4)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a box plot
Z = np.random.normal(0, 1, (100, 3))
plt.boxplot(Z)

plt.show()

print("------------------------------------------------------------")  # 60個

#Tweak

# Create a plot with a black solid line
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y, color="black")

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a plot with a dashed line
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y, linestyle="--")

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a plot with a thicker line
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y, linewidth=5)

plt.show()

# Create a plot with markers
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y, marker="o")

plt.show()

print("------------------------------------------------------------")  # 60個

#Organize

# Create a plot with two lines on the same axes
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
plt.plot(X, Y1, X, Y2)

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (vertically stacked)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(X, Y1, color="C1")
ax2.plot(X, Y2, color="C0")

plt.show()

print("------------------------------------------------------------")  # 60個

# Create a figure with two subplots (horizontally aligned)
X = np.linspace(0, 10, 100)
Y1, Y2 = np.sin(X), np.cos(X)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(Y1, X, color="C1")
ax2.plot(Y2, X, color="C0")

plt.show()

print("------------------------------------------------------------")  # 60個

#Label

# Create data and plot a sine wave
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y)

plt.show()

print("------------------------------------------------------------")  # 60個

# Modify plot properties
X = np.linspace(0, 10, 100)
Y = np.sin(X)
plt.plot(X, Y)
plt.title("A Sine wave")
plt.xlabel("Time")
plt.ylabel(None)

plt.show()

print("------------------------------------------------------------")  # 60個

#Figure, axes & spines

# Create a 3x3 grid of subplots
fig, axs = plt.subplots(3, 3)

# Set face colors for specific subplots
axs[0, 0].set_facecolor("#ddddff")
axs[2, 2].set_facecolor("#ffffdd")

# Create a 3x3 grid of subplots
fig, axs = plt.subplots(3, 3)

# Add a grid specification and set face color for a specific subplot
gs = fig.add_gridspec(3, 3)
ax = fig.add_subplot(gs[0, :])
ax.set_facecolor("#ddddff")

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Remove top and right spines from the subplot
ax.spines["top"].set_color("None")
ax.spines["right"].set_color("None")

print("------------------------------------------------------------")  # 60個

#Ticks & labels

# Import the necessary libraries
from matplotlib.ticker import MultipleLocator as ML
from matplotlib.ticker import ScalarFormatter as SF

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set minor tick locations and formatter for the x-axis
ax.xaxis.set_minor_locator(ML(0.2))
ax.xaxis.set_minor_formatter(SF())

# Rotate minor tick labels on the x-axis
ax.tick_params(axis='x', which='minor', rotation=90)

print("------------------------------------------------------------")  # 60個

#Lines & markers

# Generate data and create a plot
X = np.linspace(0.1, 10 * np.pi, 1000)
Y = np.sin(X)
plt.plot(X, Y, "C1o:", markevery=25, mec="1.0")

plt.show()

print("------------------------------------------------------------")  # 60個

#Scales & projections

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set x-axis scale to logarithmic
ax.set_xscale("log")

# Plot data with specified formatting
ax.plot(X, Y, "C1o-", markevery=25, mec="1.0")

plt.show()

print("------------------------------------------------------------")  # 60個

#Text & ornaments

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Fill the area between horizontal lines with a curve
ax.fill_betweenx([-1, 1], [0], [2*np.pi])

# Add a text annotation to the plot
ax.text(0, -1, r" Period $\Phi$")

plt.show()

print("------------------------------------------------------------")  # 60個

#Legend

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Plot sine and cosine curves with specified colors and labels
ax.plot(X, np.sin(X), "C0", label="Sine")
ax.plot(X, np.cos(X), "C1", label="Cosine")

# Add a legend with customized positioning and formatting
ax.legend(bbox_to_anchor=(0, 1, 1, 0.1), ncol=2, mode="expand", loc="lower left")

plt.show()

print("------------------------------------------------------------")  # 60個

#Annotation

# Create a figure with a single subplot
fig, ax = plt.subplots()

ax.plot(X, Y, "C1o:", markevery=25, mec="1.0")

# Add an annotation "A" with an arrow
ax.annotate("A", (X[250], Y[250]), (X[250], -1),
            ha="center", va="center",
            arrowprops={"arrowstyle": "->", "color": "C1"})

plt.show()

print("------------------------------------------------------------")  # 60個

#Colors

import math

from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def plot_colortable(colors, *, ncols=4, sort_colors=True):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig

# CSS Colors
plot_colortable(mcolors.CSS4_COLORS)

plt.show()

print("------------------------------------------------------------")  # 60個

# Get a list of named colors
named_colors = plt.colormaps()  
print("Colors:",named_colors)

print("------------------------------------------------------------")  # 60個

# 存檔

plt.savefig('tmp_aaa.png')

# Save the figure as a PNG file with higher resolution (300 dpi)
fig.savefig("tmp_bbb.png", dpi=300)

# Save the figure as a PDF file
fig.savefig("tmp_ccc.pdf")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
