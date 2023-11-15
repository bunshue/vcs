"""
# plot 集合 子圖

Matplotlib 多圖顯示(subplot/subplot2grid/Subplots)

以下紀錄三種方法:

    plt.subplot()
    plt.subplot2grid()
    plt.subplots()
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#1. plt.subplot()

#1.1 均勻做圖
"""
plt.subplot(2,2,1): 表示把窗口分成2行2列， 並指定位置於位置1
plt.subplot(2,2,1): 表示把窗口分成2行2列， 並指定位置於位置2
"""
plt.subplot(2,2,1) 
plt.plot([0,1],[0,2])

plt.subplot(2,2,2)
plt.plot([0,1],[0,4])

plt.subplot(2,2,3)
plt.plot([0,1],[0,5])

plt.subplot(2,2,4)
plt.plot([0,1],[0,6])

plt.show()

#1.2 不均勻做圖(大小不同)
"""
plt.subplot(3,5,(1,2)): 表示把窗口分成3行5列， 並指定位置於位置1~2
plt.subplot(3,5,(3,5)): 表示把窗口分成3行5列， 並指定位置於位置3~5

plt.subplot(3,4,6): 表示把窗口重新分成3行4列， 並指定位置於位置6(會用新的窗口重新計算位置)
plt.subplot(3,4,(7,8)): 表示把窗口重新分成3行4列， 並指定位置於位置7~8(會用新的窗口重新計算位置)
"""
plt.subplot(3,5,(1,2))
plt.subplot(3,5,(3,5))
plt.tight_layout()

plt.subplot(3,4,6)
plt.subplot(3,4,(7,8))
plt.tight_layout()

plt.show()

#2. plt.subplot2grid()
"""
plt.subplot2grid((3,3),(0,0), colspan = 3)

    使用plt.subplot2grid()做圖
    (3,3): 表示把窗口分成3行3列
    (0,0): 表示從未置(0,0)開始做圖
    colspan: column範圍
    rowspan: row範圍
"""
ax1 = plt.subplot2grid((3,3),(0,0), colspan = 3)
ax2 = plt.subplot2grid((3,3),(1,0), colspan = 2, rowspan = 1)
ax3 = plt.subplot2grid((3,3),(1,2), colspan = 1, rowspan = 2)
ax4 = plt.subplot2grid((3,3),(2,0), colspan = 1, rowspan = 1)

ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

ax5 = plt.subplot2grid((3,3),(2,1), colspan = 1, rowspan = 1)
plt.tight_layout()
plt.show()

#3. plt.subplots()
"""
    使用plt.subplot2s()做圖
    (2,2): 表示把窗口分成2行2列
    ax1, ax2 代表第一行由左至右的兩個位置(座標(1,1), (1,2))
    ax3, ax4 代表第二行由左至右的兩個位置(座標(2,1), (2,2))
    sharex: 是否共享座標軸X (使用相同座標軸)
    sharey: 是否共享座標軸 (使用相同座標軸)
"""
f, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex = False ,sharey=False,figsize=(10,6))
data = np.arange(1,10,0.5)

df1 =  pd.DataFrame(data)
df2 =  pd.DataFrame(data**2)
df3 =  pd.DataFrame(data**3)
df4 =  pd.DataFrame(data**4)

ax1.plot(df1)
ax2.plot(df2)
ax3.plot(df3)
ax4.plot(df4)

plt.show()

print('------------------------------------------------------------')	#60個

print('一次畫一大堆範例... 久')

#1. 讀入 MNSIT 數據集
from keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下5行
path = 'C:/_git/vcs/_4.python/ml/mnist.npz'
mnist = np.load(path)  
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

fig = plt.figure(figsize = (8, 8))
for i in range(256):
    ax = plt.subplot2grid((16, 16), (int(i / 16), int(i % 16)))
    ax.imshow(x_train[i], cmap = plt.cm.gray)
    ax.axis('off')
plt.suptitle('畫前100筆資料')
plt.show()

print('------------------------------------------------------------')	#60個


