'''
plt之基本設定

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'text 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


#第一張圖
plt.subplot(231)

from random import randint

def dice_generator(times, sides):
    #處理隨機數
    for i in range(times):              
        ranNum = randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)
          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列

h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('頻率')
plt.title('測試 10000 次')


#第二張圖
plt.subplot(232)

import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數

plt.plot(x, y1, label='Sin')                    
plt.plot(x, y2, label='Cos')
plt.legend()

plt.grid(c='y',linestyle='--',lw=1) # 顯示虛線格線


#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個


