# 新進測試03

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

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. 善用 enumerate

L = ['a', 'b', 'c']

for i in L:
    print(i)

#加上編號。

for i in range(3):
    print(i+1, L[i])

#試試 enumerate 會做什麼。

print(list(enumerate(L)))

#用 for 迴圈一一顯示出來。

for i in enumerate(L):
    print(i)

#用 unpacking 取出內容, 再修正編號從 1 開始。

for i, s in enumerate(L):
    print(i + 1, s)

#2. 畫多個圖

x = np.linspace(-10, 10, 200)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


#用 2×2的排列方式畫圖。

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))

plt.subplot(2, 2, 3)
plt.plot(x, x)

plt.subplot(2, 2, 4)
plt.plot(x, x**2)

plt.show()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



