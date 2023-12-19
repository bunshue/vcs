# scatter 集合
# 散布圖 Scatter Chart

import sys
import numpy as np
import matplotlib.pyplot as plt
import random
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

np.random.randint(0, 3, 10)
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
X, Y = np.meshgrid(x, y)
plt.scatter(
    X.ravel(),
    Y.ravel(),
    c=[0, 1, 2, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1],
    cmap="Paired",
)

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
