"""
極座標繪圖


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

pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
"""
plt.polar(theta,r)
plt.polar(theta,r,'-',marker='*',color='g')
plt.polar(theta,r,'--',marker='D',color='m')
"""
plt.polar(theta,r,'*',color='b',markersize=10)

plt.show()

print("------------------------------------------------------------")  # 60個

a = 6           # 主軸半徑
b = 3           # 次軸半徑

radian = np.arange(0, (2 * np.pi), 0.01)
for rad in radian:
    r = (a*b)/np.sqrt((a*np.sin(rad))**2 + (b*np.cos(rad))**2)
    plt.polar(rad,r,'b.')
plt.show()

print("------------------------------------------------------------")  # 60個

radian = np.arange(0, (2 * np.pi), 0.01)
for r in range(1,3):
    for rad in radian:
        plt.polar(rad,r,'b.')
plt.show()

print("------------------------------------------------------------")  # 60個

radian = np.arange(0,(6 * np.pi),0.01)
for rad in radian:
    r = rad
    plt.polar(rad,r,'b.')
plt.show()

print("------------------------------------------------------------")  # 60個

a = 1
radian = np.arange(0,(6 * np.pi),0.01)
for rad in radian:
    r =  a + (a*np.cos(rad))
    #r =  a - (a*np.sin(rad))
    plt.polar(rad,r,'r.')
plt.show()

print("------------------------------------------------------------")  # 60個

print('螺旋圖')

plt.figure(figsize = (6, 6))  # 圖像大小[英吋]

ax = plt.axes([0.1, 0.1, 0.8, 0.8], polar=True)

t = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
plt.polar(t, 1.19**t, linewidth=2)

xt, yt = plt.xticks()[0], plt.yticks()[0]

plt.xticks(xt, ["" for q in range(len(xt))])
plt.yticks(yt, ["" for q in range(len(yt))])

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


np.random.seed(15)
np.random.seed(15)
