# ch10_6.py
import matplotlib.pyplot as plt
import numpy as np

def plot_color_gradients(cmap_list, cmap_name):
    # 建立圖表, 調整圖表高度
    nrows = len(cmap_name)
    width = 6.5                             # 定義圖表寬度
    height = (nrows + 1) * 0.28             # 定義圖表高度
    fig, axs = plt.subplots(nrows=nrows,figsize=(width, height))
    fig.subplots_adjust(left=0.2, right=0.95, top=0.75, bottom=0.1)
    axs[0].set_title(cmap_list + ' colormaps', fontsize=14)
    # 繪製彩色映射圖和此圖的名稱
    for ax, cmap_name in zip(axs, cmap_name):
        ax.imshow(colorbar, aspect='auto', cmap=cmap_name)
        # 更改坐標軸為 ax, 文字因為是靠右對齊, 所以文字從 -0.02開始
        # 同時文字垂直置中對齊
        ax.text(-0.02, 0.5, cmap_name, va='center', ha='right',
                fontsize=10, transform=ax.transAxes)
    # 關閉軸標記
    for ax in axs:
        ax.set_axis_off()
# 主程式開始        
cmaps = [
         ('Sequential', [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         ('Sequential (2)', [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']),
         ('Perceptually Uniform Sequential', [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
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
colorbar = np.linspace(0, 1, 256)               # 建立0 - 1之間有256元素陣列
colorbar = np.vstack((colorbar, colorbar))      # 擴充陣列為矩陣
# cmap_list是色彩分類名稱, cmap_name是類別內的名稱
for cmap_list, cmap_name in cmaps:
    plot_color_gradients(cmap_list, cmap_name)
plt.show()



