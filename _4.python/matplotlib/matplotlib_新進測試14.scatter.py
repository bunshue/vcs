# matplotlib_新進測試13_scatter

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


x0 = np.arange(0, 5, 1)
y0 = np.arange(0, 5, 1)
x, y = np.meshgrid(x0, y0)
z = np.c_[x.ravel(), y.ravel()]

print(len(x))
print(x.shape)
print(x)
print(len(y))
print(y.shape)
print(y)
print(len(z))
print(z.shape)
print(z)

# ravel 拉平法
print("x.ravel() = ", x.ravel())
print("y.ravel() = ", y.ravel())

plt.scatter(z[:, 0], z[:, 1], s=100)
plt.show()

print("------------------------------------------------------------")  # 60個

x, y = np.meshgrid(np.linspace(0, 4, 5), np.linspace(0, 4, 5))

# ravel 拉平法
X = x.ravel()
Y = y.ravel()
plt.scatter(X, Y, s=100)

plt.show()



print("------------------------------------------------------------")  # 60個



#for animation

X = np.random.rand(6)
Y = np.random.rand(6)

def myplot(n=1):
    plt.scatter(X, Y, c='r', s=100)
    x = np.linspace(0, 1, 1000)
    y = 0.5*np.sin(n*x) + 0.5
    plt.plot(x, y)

myplot(10)

plt.show()

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

def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])              # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])       # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
plt.show()

print("------------------------------------------------------------")  # 60個

def loc(index):
    # 處理座標的移動
    x_mov = random.choice([-3, 3])              # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])       # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
#plt.axes().get_xaxis().set_visible(False)   # 隱藏x軸座標
#plt.axes().get_yaxis().set_visible(False)   # 隱藏y軸座標

plt.show()


print("------------------------------------------------------------")  # 60個



print("散佈圖")

fig, ax = plt.subplots()

N = 50
x = np.random.randint(30, size=N)
y = np.random.randint(30, size=N)
c = np.random.randint(30, size=N)
size = np.exp(np.random.randint(10, size=N) * 200)
sc = ax.scatter(x=x, y=y, c=c, s=c, alpha=0.5, label="scatter plot")

ax.set_xlabel("X軸", loc="left")
ax.set_ylabel("Y軸", loc="top")
ax.legend(loc=1)
cbar = fig.colorbar(sc)
cbar.set_label("Z軸", loc="center")

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt

def plt_scatter():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)

    plt.subplot(1, 2, 1)
    plt.scatter(X, Y, s=75, c=T, alpha=.5)

    plt.xlim(-1.5, 1.5)
    plt.xticks(())
    plt.ylim(-1.5, 1.5)
    plt.yticks(())

def plt_fill_between():
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)

    plt.subplot(1, 2, 2)

    plt.plot(X, Y + 1, color='blue', alpha=1.00)
    plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

    plt.plot(X, Y - 1, color='blue', alpha=1.00)
    plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
    plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)

    plt.xlim(-np.pi, np.pi)
    plt.xticks(())
    plt.ylim(-2.5, 2.5)
    plt.yticks(())

plt.figure(figsize=(16, 6))
plt_scatter()
plt_fill_between()
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

