"""

第26章：流線圖

"""

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



#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch26\ch26_1.py

# ch26_1.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = np.arange(0, 5) 
y = np.arange(0, 5) 
X, Y = np.meshgrid(x, y)                # 建立 X, Y
U = np.ones((5,5))                      # 建立 U
V = np.zeros((5,5))                     # 建立 V
plt.streamplot(X, Y, U, V, density=0.5)
plt.title("流線圖",fontsize=14,color='b')
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch26\ch26_2.py

# ch26_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-3, 3) 
y = np.arange(-3, 3) 
X, Y = np.meshgrid(x, y)                # 建立 X, Y
U = -1 + X**2 - Y                       # 定義速度 U
V = 1 - X + Y**2                        # 定義速度 V
plt.streamplot(X, Y, U, V, density = 1) 
plt.title("流線圖",fontsize=14,color='b')
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch26\ch26_3.py

# ch26_3.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-3, 3) 
y = np.arange(-3, 3) 
X, Y = np.meshgrid(x, y)                    # 建立 X, Y
U = -1 + X**2 - Y                           # 定義速度 U
V = 1 - X + Y**2                            # 定義速度 V
speed = np.sqrt(U**2 + V**2)
# 建立圖表網格物件
fig = plt.figure()
gs = gridspec.GridSpec(nrows=2, ncols=2)
# 使用預設環境建立流線圖
ax0 = fig.add_subplot(gs[0, 0])
ax0.streamplot(X, Y, U, V)
ax0.set_title('使用預設環境建立流線圖')
# 流線圖 1, 使用 cmap='spring' 色彩映射
ax1 = fig.add_subplot(gs[0, 1])
strobj = ax1.streamplot(X,Y,U,V,color=U,linewidth=2,cmap='spring')
fig.colorbar(strobj.lines)                  # 建立資料條
ax1.set_title("使用 cmap='spring' 色彩映射")
# 流線圖 2, x 和 y 軸密度不同, 使用黑色流線
ax2 = fig.add_subplot(gs[1, 0])
ax2.streamplot(X, Y, U, V, color='k', density=[0.5, 1])
ax2.set_title('使用黑色流線, x 和 y 軸密度不同')
# 流線圖 3, 沿著速度線變更線條寬度, 同時更改密度為 0.6
ax3 = fig.add_subplot(gs[1, 1])
lw = 5*speed / speed.max()
strobj = ax3.streamplot(X,Y,U,V,density=0.6,color=U,
                        cmap='summer',linewidth=lw)
fig.colorbar(strobj.lines)                  # 建立資料條
ax3.set_title('沿著速度線變更線條寬度')
plt.tight_layout()
plt.show()





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


