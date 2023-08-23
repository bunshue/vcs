
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
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (10, 8), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

offset = 0.3

#x = np.linspace(-10, 10, 21)
#y00 = x ** 2

x = np.linspace(-2*np.pi, 2*np.pi, 41)
y00 = np.cos(x)

y01 = y00 + offset * 1
y02 = y00 + offset * 2
y03 = y00 + offset * 3
y04 = y00 + offset * 4
y05 = y00 + offset * 5
y06 = y00 + offset * 6
y07 = y00 + offset * 7
y08 = y00 + offset * 8
y09 = y00 + offset * 9
y10 = y00 + offset * 10
y11 = y00 + offset * 11
y12 = y00 + offset * 12
y13 = y00 + offset * 13
y14 = y00 + offset * 14
y15 = y00 + offset * 15
y16 = y00 + offset * 16
y17 = y00 + offset * 17
y18 = y00 + offset * 18
y19 = y00 + offset * 19
y20 = y00 + offset * 20


plt.plot(x, y01, "r-o", lw = 5)
plt.plot(x, y02, "g--")
plt.plot(x, y03, "b:o")
plt.plot(x, y04, "g--s")
plt.plot(x, y05, 'g.-')
plt.plot(x, y06, 'y--o')
#plt.plot(x, y07, 'y--o')
plt.plot(x, y07, c = '#00a676', lw = 5)
#plt.plot(x, y08, marker='o')
plt.plot(x, y08, lw=3, marker='o', ms=10)
plt.plot(x, y09, lw=3, marker='o', ms=10, markevery=4)   #隔 4 個畫一個 marker


#連線
plt.plot(x, y10, color = 'red')

#linestyle 虛線樣式
plt.plot(x, y11, color = 'red', linestyle = "--")

#linestyle 虛點樣式
plt.plot(x, y12, color = 'red', linestyle = "-.")

#linestyle 虛點樣式「:」
plt.plot(x, y13, color = 'red', linestyle = ":")

#marker 點「.」標記
#因為需要展示出效果，因此把 linestyle 設為實線，linewidth 為 2.0，markersize 設為 8
plt.plot(x, y14, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = ".")

#marker 圓「o」標記
plt.plot(x, y15, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = "o")

#marker 星「*」標記
plt.plot(x, y16, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = "*")

#marker 矩形「s」標記
plt.plot(x, y17, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = "s")

plt.plot(x, y18, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = ".", label = "Test")

# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(x, y19, color = 'red', linestyle = "-", linewidth = "2", markersize = "8", marker = ".", label = "Plot 1")

# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(x, y20, color = 'blue', linestyle = "-", linewidth = "2", markersize = "8", marker = ".", label = "Plot 2")




'''
plt.title('Plot title', fontsize = 18) # 設定圖表標題內容及大小
plt.xlabel('x label', fontsize = 10) # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize = 10) # 設定 y 軸標題內容及大小

'''

#plt.title(label = '231')
plt.title('圖形標題')
plt.xlabel('x軸標記')
plt.ylabel('y軸標記')

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
          ['$0$', '$\pi/2$', '$-\pi$', '$-3\pi/2$', '$-2\pi$']);

#plt.axis('equal')       #軸比例
#xmin, xmax, ymin, ymax = 0.5, 6.5, 15, 32.5
#plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
#plt.axis([0.5, 6.5, 15, 35])
#plt.axes([0.2, 0.2, 0.4, 0.4]) #設定各軸顯示範圍, 參數是串列

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍
#邊界的設定
#plt.xlim(-6,6)
#plt.ylim(-1.2,1.2)

#plt.legend()
plt.legend(loc='best')
plt.legend()

plt.legend(loc='upper right')

'''
plt.legend(loc=6)

plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.legend(loc=6, bbox_to_anchor=(1,1))

plt.tight_layout(pad=7)
'''

#print(plt.axis())


#plt.grid(True)  #顯示格線
plt.grid(color='0.8')   #顯示格線

plt.text(0, 0, 'This is a lion-mouse')

plt.show()


