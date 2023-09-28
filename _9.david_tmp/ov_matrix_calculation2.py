
'''
ims ov sensor test

'''


import numpy as np
import matplotlib.pyplot as plt

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (10, 8), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)


"""
y = R * .299000 + G * .587000 + B * .114000
u = R * -.168736 + G * -.331264 + B * .500000 + 128
v = R * .500000 + G * -.418688 + B * -.081312 + 128
"""

#A = np.matrix([[30, 50], [60, 80], [50, 60]])

A = np.matrix([
    [0.299000, 0.587000, 0.114000],
    [-0.168736, -0.331264, 0.500000],
    [0.500000, -0.418688, -0.081312]])

print(type(A))
print(A)

OFFSET = np.mat([[0], [128], [128]])

R, G, B = 10, 20, 30
RGB = np.mat([[R], [G], [B]])
print(A * RGB + OFFSET)

R, G, B = 50, 100, 150
RGB = np.mat([[R], [G], [B]])
print(A * RGB + OFFSET)

R, G, B = 100, 200, 50
RGB = np.mat([[R], [G], [B]])
print(A * RGB + OFFSET)

R = [10, 50, 100]
G = [20, 100, 200]
B = [30, 150, 50]

N = 81
X = np.linspace(0, 80, N)
R = np.linspace(0, 80, N)
G = np.linspace(80, 160, N)
B = np.linspace(160, 240, N)


RGB = np.mat([R, G, B])

YUV = A * RGB + OFFSET
'''
print(type(YUV))
print('YUV')
print(YUV)

print('Y')
print(YUV[0])
print('U')
print(YUV[1])
print('V')
print(YUV[2])
'''


Y = YUV[0,:]
U = YUV[1,:]
V = YUV[2,:]

print('Y')
print(len(Y))
print(Y)

plt.plot(X, R, "r-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, G, "g-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(X, B, "b-o", markevery = 5)   #隔 5 個畫一個 marker

XX = np.mat([X])

plt.plot(XX, Y, "y-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(XX, U, "m-o", markevery = 5)   #隔 5 個畫一個 marker
plt.plot(XX, V, "c-o", markevery = 5)   #隔 5 個畫一個 marker

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

