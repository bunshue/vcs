# matplotlib_新進測試14_其他

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

# 氣泡圖
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N) # 點的顏色
area = (30 * np.random.rand(N))**2  # 點的半徑
plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 由於點可能疊加，設置透明度爲0.5
plt.show()





print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


