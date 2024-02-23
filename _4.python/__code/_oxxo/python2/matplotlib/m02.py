import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties as font

# 連結中文字體，範例為微軟正黑體
zhfont1 = font(fname="matplotlib/font/msjh.ttf")

x = np.arange(1, 10, dtype=int)
y = x * 0.2
a = np.arange(1, 10, 0.1)
b = np.sin(a)
plt.title("哈囉", fontproperties=zhfont1)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, 'or')  # 第三個為參數，o 表示原點，r 表示紅色
plt.plot(a, b, ':b')  # 第三個為參數，o 表示原點，r 表示紅色
plt.show()
