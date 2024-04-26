# 新進測試02

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import math

degrees = [x * 15 for x in range(0, 25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x, y)
plt.show()


degrees = np.arange(0, 360)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

plt.plot(x, y)
plt.show()


print("------------------------------------------------------------")  # 60個

#相同斜率平行移動
import matplotlib.pyplot as plt

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [(2 * y - 2) for y in x]
y3 = [(2 * y + 2) for y in x]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#plt.show()

print(x)



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
