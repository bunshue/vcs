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

plt.figure()    # 地理投影圖表 Aitoff
plt.subplot(projection="aitoff")
plt.title("地理投影 = Aitoff",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Hammer
plt.subplot(projection="hammer")
plt.title("地理投影 = Hammer",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Lambert
plt.subplot(projection="lambert")
plt.title("地理投影 = Lambert",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Mollweide
plt.subplot(projection="mollweide")
plt.title("地理投影 = Mollweide",c='b')
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
