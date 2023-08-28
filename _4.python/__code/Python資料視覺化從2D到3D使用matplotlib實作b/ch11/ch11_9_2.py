# ch11_9_2.py
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
cmap = mpl.cm.plasma                        # 使用 plasma
bounds = [-1, 3, 5, 7, 11, 15]
# 建立色彩邊界值
mynorm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='max')                                   
fig.colorbar(mpl.cm.ScalarMappable(norm=mynorm, cmap=cmap),
             cax=ax, orientation='horizontal',
             label='使用extend=max')
plt.show()










