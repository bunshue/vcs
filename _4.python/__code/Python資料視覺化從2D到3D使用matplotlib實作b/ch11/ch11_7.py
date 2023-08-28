# ch11_7.py
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)             # 設定色彩條bottom的位置
norm = plt.Normalize(vmin=2, vmax=8)        # 定義色彩條的數值區間
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap='spring'),
             cax=ax, orientation='horizontal',
             label='自定義colorbar條')
plt.show()










