"""
3D plot 集合 3

3D 曲面與輪廓設計

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

from mpl_toolkits.mplot3d import axes3d

print("------------------------------------------------------------")  # 60個



"""

# 建立影像和 3D 軸物件
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# 建立 3D 圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



ax = plt.figure()
ax.add_subplot(projection='3d')


ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
ax.set_title('繪製曲線表面',fontsize=14,color='b')

ax.set_title('wireframe( )函數的實例',fontsize=16,color='b');


"""





