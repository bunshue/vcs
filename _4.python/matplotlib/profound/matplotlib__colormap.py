"""
colorbar
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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

def show():
    plt.show()
    pass

print("------------------------------------------------------------")  # 60個

N = 1000  # 數據數量
x = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)  # 均值是 0, 標準差是 1
color = x + y  # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)  # 定義色彩條的數值區間
plt.scatter(x, y, s=60, alpha=0.5, c=color, cmap="jet", norm=norm)
plt.xlim(-3, 3)
plt.xticks(())  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())  # 不顯示 y 刻度
plt.colorbar()  # 建立色彩條

show()

print("------------------------------------------------------------")  # 60個

N = 1000
x = np.random.rand(N)
y = np.random.rand(N)
#plt.scatter(x, y, c=x)
#plt.scatter(x, y, c=y)

plt.scatter(x, y, c=y, cmap="brg")
#plt.scatter(x, y, c=y, cmap="hsv")
#plt.scatter(x, y, c=x, cmap="GnBu")


plt.colorbar()  # 建立色彩條, 預設為直向
#plt.colorbar(orientation="horizontal")  # 建立橫向色彩條

show()

print("------------------------------------------------------------")  # 60個

"""
x = np.arange(100)
y = x
t = x
#plt.scatter(x, y, c=t, cmap='rainbow')

plt.scatter(x, y, s=50, c=x, cmap='hsv')

plt.show()
"""

pts = np.arange(-2, 2, 0.01)
x, y = np.meshgrid(pts, pts)
z = np.sqrt(x**2 + y**2)

ticks = np.arange(0, 500, 100)
seq = np.arange(-2, 3)

plt.imshow(z, cmap="rainbow")
plt.xticks(ticks, seq)
plt.yticks(ticks, seq)

plt.colorbar()  # 在圖右邊增加color bar
plt.title(r"建立$\sqrt{x^2 + y^2}$網格影像")

plt.show()

print("------------------------------------------------------------")  # 60個

"""
import matplotlib.pyplot as plt
import numpy as np

cmaps = [('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Diverging', [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
         ('Qualitative', [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c']),
         ('Miscellaneous', [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
            'gist_ncar'])]

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)

    axs[0].set_title(f"{cmap_category} colormaps", fontsize=14)

    for ax, cmap_name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=cmap_name)
        ax.text(-.01, .5, cmap_name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()


for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list)

plt.show()
"""

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
norm = plt.Normalize(vmin=2, vmax=8)  # 定義色彩條的數值區間
fig.colorbar(
    mpl.cm.ScalarMappable(norm=norm, cmap="spring"),
    cax=ax,
    orientation="horizontal",
    label="自定義colorbar條",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
# 自行設計色彩映射圖
mycmap = mpl.colors.ListedColormap(["r", "g", "b"])
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm([2, 4, 6, 8], 3)
fig.colorbar(
    mpl.cm.ScalarMappable(norm=mynorm, cmap=mycmap),
    cax=ax,
    orientation="horizontal",
    label="自定義colormap和colorbar",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
top = mpl.cm.get_cmap("Oranges", 128)  # Oranges色彩
bottom = mpl.cm.get_cmap("Greens", 128)  # Greens色彩
# 組合Orange和Greens色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)), bottom(np.linspace(0, 1, 128))))
mycmap = mpl.colors.ListedColormap(newcolors)
fig.colorbar(
    mpl.cm.ScalarMappable(cmap=mycmap),
    cax=ax,
    orientation="horizontal",
    label="組合Oranges和Greens",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
top = mpl.cm.get_cmap("Oranges_r", 128)  # Oranges_r色彩
bottom = mpl.cm.get_cmap("Greens", 128)  # Greens色彩
# 組合Orange和Greens色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)), bottom(np.linspace(0, 1, 128))))
mycmap = mpl.colors.ListedColormap(newcolors)
fig.colorbar(
    mpl.cm.ScalarMappable(cmap=mycmap),
    cax=ax,
    orientation="horizontal",
    label="組合Oranges_r和Greens",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
cmap = mpl.cm.plasma  # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend="both")
fig.colorbar(
    mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
    cax=ax,
    orientation="horizontal",
    label="使用extend=both",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
cmap = mpl.cm.plasma  # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend="min")
fig.colorbar(
    mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
    cax=ax,
    orientation="horizontal",
    label="使用extend=min",
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)  # 設定色彩條bottom的位置
cmap = mpl.cm.plasma  # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend="max")
fig.colorbar(
    mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
    cax=ax,
    orientation="horizontal",
    label="使用extend=max",
)
show()

print("------------------------------------------------------------")  # 60個

colName = ["sepal_len", "sepal_wd", "petal_len", "petal_wd", "species"]
iris = pd.read_csv("_data/iris.csv", names=colName)
x = iris["petal_len"].values  # 花瓣長度
y = iris["sepal_len"].values  # 花萼長度

fig, ax = plt.subplots()
mycmap = mpl.colors.ListedColormap(["b", "g", "r"])
norm = mpl.colors.BoundaryNorm([0, 2, 5, 7], mycmap.N)
plt.scatter(x, y, c=x, cmap=mycmap, norm=norm)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=mycmap), ax=ax)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

from matplotlib import colormaps
cc = list(colormaps)
print(cc)

from colorspacious import cspace_converter
import matplotlib as mpl

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list


#Sequential

#Perceptually Uniform Sequential colormaps
plot_color_gradients('Perceptually Uniform Sequential',
                     ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])
show()

#Sequential colormaps
plot_color_gradients('Sequential',
                     ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])
show()

#Sequential2

#Sequential (2) colormaps
plot_color_gradients('Sequential (2)',
                     ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                      'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'])
show()

#Diverging
#Diverging colormaps

plot_color_gradients('Diverging',
                     ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
                      'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'])
show()

#Cyclic
#Cyclic colormaps
plot_color_gradients('Cyclic', ['twilight', 'twilight_shifted', 'hsv'])
show()

#Qualitative
#Qualitative colormaps
plot_color_gradients('Qualitative',
                     ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c'])
show()

#Miscellaneous

#Miscellaneous colormaps

plot_color_gradients('Miscellaneous',
                     ['flag', 'prism', 'ocean', 'gist_earth', 'terrain',
                      'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
                      'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                      'turbo', 'nipy_spectral', 'gist_ncar'])
show()


#Lightness of Matplotlib colormaps

mpl.rcParams.update({'font.size': 12})

# Number of colormap per subplot for particular cmap categories
_DSUBS = {'Perceptually Uniform Sequential': 5, 'Sequential': 6,
          'Sequential (2)': 6, 'Diverging': 6, 'Cyclic': 3,
          'Qualitative': 4, 'Miscellaneous': 6}

# Spacing between the colormaps of a subplot
_DC = {'Perceptually Uniform Sequential': 1.4, 'Sequential': 0.7,
       'Sequential (2)': 1.4, 'Diverging': 1.4, 'Cyclic': 1.4,
       'Qualitative': 1.4, 'Miscellaneous': 1.4}

# Indices to step through colormap
x = np.linspace(0.0, 1.0, 100)

# Do plot
for cmap_category, cmap_list in cmaps.items():

    # Do subplots so that colormaps have enough space.
    # Default is 6 colormaps per subplot.
    dsub = _DSUBS.get(cmap_category, 6)
    nsubplots = int(np.ceil(len(cmap_list) / dsub))

    # squeeze=False to handle similarly the case of a single subplot
    fig, axs = plt.subplots(nrows=nsubplots, squeeze=False,
                            figsize=(7, 2.6*nsubplots))

    for i, ax in enumerate(axs.flat):

        locs = []  # locations for text labels

        for j, cmap in enumerate(cmap_list[i*dsub:(i+1)*dsub]):

            # Get RGB values for colormap and convert the colormap in
            # CAM02-UCS colorspace.  lab[0, :, 0] is the lightness.
            rgb = mpl.colormaps[cmap](x)[np.newaxis, :, :3]
            lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)

            # Plot colormap L values.  Do separately for each category
            # so each plot can be pretty.  To make scatter markers change
            # color along plot:
            # https://stackoverflow.com/q/8202605/

            if cmap_category == 'Sequential':
                # These colormaps all start at high lightness, but we want them
                # reversed to look nice in the plot, so reverse the order.
                y_ = lab[0, ::-1, 0]
                c_ = x[::-1]
            else:
                y_ = lab[0, :, 0]
                c_ = x

            dc = _DC.get(cmap_category, 1.4)  # cmaps horizontal spacing
            ax.scatter(x + j*dc, y_, c=c_, cmap=cmap, s=300, linewidths=0.0)

            # Store locations for colormap labels
            if cmap_category in ('Perceptually Uniform Sequential',
                                 'Sequential'):
                locs.append(x[-1] + j*dc)
            elif cmap_category in ('Diverging', 'Qualitative', 'Cyclic',
                                   'Miscellaneous', 'Sequential (2)'):
                locs.append(x[int(x.size/2.)] + j*dc)

        # Set up the axis limits:
        #   * the 1st subplot is used as a reference for the x-axis limits
        #   * lightness values goes from 0 to 100 (y-axis limits)
        ax.set_xlim(axs[0, 0].get_xlim())
        ax.set_ylim(0.0, 100.0)

        # Set up labels for colormaps
        ax.xaxis.set_ticks_position('top')
        ticker = mpl.ticker.FixedLocator(locs)
        ax.xaxis.set_major_locator(ticker)
        formatter = mpl.ticker.FixedFormatter(cmap_list[i*dsub:(i+1)*dsub])
        ax.xaxis.set_major_formatter(formatter)
        ax.xaxis.set_tick_params(rotation=50)
        ax.set_ylabel('Lightness $L^*$', fontsize=12)

    ax.set_xlabel(cmap_category + ' colormaps', fontsize=14)

    fig.tight_layout(h_pad=0.0, pad=1.5)
    show()

#Grayscale conversion

mpl.rcParams.update({'font.size': 14})

# Indices to step through colormap.
x = np.linspace(0.0, 1.0, 100)

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list):
    fig, axs = plt.subplots(nrows=len(cmap_list), ncols=2)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99,
                        wspace=0.05)
    fig.suptitle(cmap_category + ' colormaps', fontsize=14, y=1.0, x=0.6)

    for ax, name in zip(axs, cmap_list):

        # Get RGB values for colormap.
        rgb = mpl.colormaps[name](x)[np.newaxis, :, :3]

        # Get colormap in CAM02-UCS colorspace. We want the lightness.
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        L = lab[0, :, 0]
        L = np.float32(np.vstack((L, L, L)))

        ax[0].imshow(gradient, aspect='auto', cmap=mpl.colormaps[name])
        ax[1].imshow(L, aspect='auto', cmap='binary_r', vmin=0., vmax=100.)
        pos = list(ax[0].get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs.flat:
        ax.set_axis_off()

    show()


for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list)


   
    

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


print("------------------------------------------------------------")  # 60個
