
'''
plt之基本設定

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

import random

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (10, 8), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


def conversion(R, G, B):
    y = R * .299000 + G * .587000 + B * .114000
    u = R * -.168736 + G * -.331264 + B * .500000 + 128
    v = R * .500000 + G * -.418688 + B * -.081312 + 128
    u2 = B - y
    v2 = R - y
    #print(u - u2, end = ' ')
    return y, u, v, u2, v2

N = 81
X = np.linspace(0, 80, N)
R = np.linspace(0, 80, N)
G = np.linspace(80, 160, N)
B = np.linspace(160, 240, N)
Y = np.linspace(0, 80, N)
U = np.linspace(0, 80, N)
V = np.linspace(0, 80, N)
U2 = np.linspace(0, 80, N)
V2 = np.linspace(0, 80, N)

'''
print(X)
print(R)
print(G)
print(B)
'''

for i in range(N):
    Y[i], U[i], V[i], U2[i], V2[i] = conversion(R[i], G[i], B[i])

plt.plot(X, R, "r-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, G, "g-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, B, "b-o", markevery = 5)   #隔 5 個畫一個 marker

plt.plot(X, Y, "y-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, U, "m-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, V, "c-o", markevery = 5)   #隔 5 個畫一個 marker

plt.plot(X, U2, "m-*", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, V2, "c-*", markevery = 5)   #隔 5 個畫一個 marker



'''
plt.xlabel('x label', fontsize = "10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize = "10") # 設定 y 軸標題內容及大小
plt.title('Plot title', fontsize = "18") # 設定圖表標題內容及大小
'''

#plt.title(label = '231')
plt.title('圖形標題')
plt.xlabel('x軸標記')
plt.ylabel('y軸標記')
#plt.axis('equal')       #軸比例
#xmin, xmax, ymin, ymax = 0.5, 6.5, 15, 32.5
#plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
#plt.axis([0.5, 6.5, 15, 35])
#plt.axes([0.2, 0.2, 0.4, 0.4]) #設定各軸顯示範圍

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍

#plt.legend()

#print(plt.axis())


#plt.grid(True)  #顯示格線
plt.grid(color='0.8')   #顯示格線


plt.show()



'''
    R[i] = random.randrange(0, 256)       #0~255之間的整數
    G[i] = random.randrange(0, 256)       #0~255之間的整數
    B[i] = random.randrange(0, 256)       #0~255之間的整數

'''
