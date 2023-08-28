# ch11_8.py
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
# 自行設計色彩映射圖
mycmap = mpl.colors.ListedColormap(['r','g','b'])
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm([2, 4, 6, 8], 3)                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=mycmap),
             cax=ax, orientation='horizontal',
             label='自定義colormap和colorbar')
plt.show()










