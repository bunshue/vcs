import matplotlib.pyplot as plt
import random

def loc(index):
    ''' 處理座標的移動 '''
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

