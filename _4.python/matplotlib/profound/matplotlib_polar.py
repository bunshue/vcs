"""
極座標繪圖


"""

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

pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r)
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(15)
pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r,'-',marker='*',color='g')
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(15)
pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r,'--',marker='D',color='m')
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(15)
pts = 12
theta = np.linspace(0,2*np.pi,pts,endpoint=False)
r = 50*np.random.rand(pts)
plt.polar(theta,r,'*',color='b',markersize=10)
plt.show()

print("------------------------------------------------------------")  # 60個

radian = np.arange(0, (2 * np.pi), 0.01)
for r in range(1,3):
    for rad in radian:
        plt.polar(rad,r,'b.')
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
    plt.polar(rad,r,'r.')
plt.show()

print("------------------------------------------------------------")  # 60個

a = 1
radian = np.arange(0,(6 * np.pi),0.01)
for rad in radian:
    r =  a - (a*np.sin(rad))
    plt.polar(rad,r,'r.')
plt.show()

print("------------------------------------------------------------")  # 60個

# 螺旋圖

print('同樣的圖形, 用 pylab 畫')

import pylab

pylab.rc("grid", color="#aaaaaa", linewidth=1, linestyle="-")

pylab.figure(figsize=(6, 6))  # 圖像大小[英吋]
ax = pylab.axes([0.1, 0.1, 0.8, 0.8], polar=True)

t = pylab.arange(-4 * pylab.pi, 4 * pylab.pi, 0.1)
pylab.polar(t, 1.19**t, linewidth=2)

xt, yt = pylab.xticks()[0], pylab.yticks()[0]
pylab.xticks(xt, ["" for q in range(len(xt))])
pylab.yticks(yt, ["" for q in range(len(yt))])

# 存圖命令
# pylab.savefig('logarithmic_spiral.svg')

pylab.show()

print("------------------------------------------------------------")  # 60個

print('同樣的圖形, 用 plt 畫')

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (6, 6))  # 圖像大小[英吋]

ax = pylab.axes([0.1, 0.1, 0.8, 0.8], polar=True)

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
