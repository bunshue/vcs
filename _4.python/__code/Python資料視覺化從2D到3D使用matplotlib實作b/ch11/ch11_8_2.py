# ch11_8_2.py
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
top = mpl.cm.get_cmap('Oranges_r', 128)     # Oranges_r色彩
bottom = mpl.cm.get_cmap('Greens', 128)     # Greens色彩
# 組合Orange和Greens色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
mycmap = mpl.colors.ListedColormap(newcolors)                                  
fig.colorbar(mpl.cm.ScalarMappable(cmap=mycmap),
             cax=ax, orientation='horizontal',
             label='組合Oranges_r和Greens')
plt.show()


