import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
# 指定圖表標題文字
ax.set_title("Sin和Cos三角函數的波型", fontsize="large")
# 更改刻度的外觀
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize("large")
    tick.set_fontname("Times New Roman")
    tick.set_color("blue")
    tick.set_weight("bold")   
plt.show()

