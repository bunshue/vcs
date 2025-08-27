"""


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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


#拉格朗日多项式插值
#拉格朗日插值法可以给出一个恰好穿过二维平面上若干个已知点的多项式函数。scipy.interpolate.lagrange(x, y)返回经过(x, y)所有点的多项式系数。

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

def f(x):
    return (1 + np.exp(-x)) / (1 + x ** 4)

x = np.linspace(-1, 1, 10)
x2 = np.linspace(-1, 1, 100)
y = f(x)
p = lagrange(x, y)
plt.plot(x, f(x), "o", label="Function")
plt.plot(x2, np.polyval(p, x2), label="Polynom")
plt.legend(loc='upper right')
plt.grid()
show()

print("------------------------------------------------------------")  # 60個

# 使用NumPy计算拉格朗日插值

xi = np.linspace(-1, 1, 100)[:, None, None]
xj = x[None, :, None]
yj = y[None, :, None]
xm = x[None, None, :]
with np.errstate(divide='ignore', invalid='ignore'):
    ell = (xi - xm) / (xj - xm)
ell[~np.isfinite(ell)] = 1.0
ellj = ell.prod(axis=2, keepdims=True)
yi = (yj * ellj).sum(axis=1, keepdims=True)[:, 0, 0]

plt.plot(x, y, "o")
plt.plot(xi.squeeze(), yi)
plt.grid()
show()

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
