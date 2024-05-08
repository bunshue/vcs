"""
# plot 集合

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

data = pd.read_csv('data/hualien.csv')
target = data[['年度','總人口數','平地原住民','山地原住民']]
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個

data = pd.read_csv('data/hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個

data = pd.read_csv('data/hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
fig1 = target.drop(['年度'], axis=1)
fig2 = target.drop(['年度', '總人口數'], axis=1)
fig1.plot(ylim=(0,400000))
fig2.plot.bar(ylim=(0,80000))

plt.show()

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
