"""

projection

特殊投影


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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="特殊投影",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(221, projection="aitoff")
# 地理投影圖表 Aitoff
plt.title("地理投影 = Aitoff",c='b')
plt.grid(True)

# 第二張圖
plt.subplot(222, projection="hammer")
# 地理投影圖表 Hammer
plt.title("地理投影 = Hammer",c='b')
plt.grid(True)

# 第三張圖
plt.subplot(223, projection="lambert")
# 地理投影圖表 Lambert
plt.title("地理投影 = Lambert",c='b')
plt.grid(True)

# 第四張圖
plt.subplot(224, projection="mollweide")
# 地理投影圖表 Mollweide
plt.title("地理投影 = Mollweide",c='b')
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
