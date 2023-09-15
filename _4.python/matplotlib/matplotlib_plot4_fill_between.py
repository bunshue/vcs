# plot 集合

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
plt.figure(num = 'plot 集合 fill_between', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 0, y, color='green', alpha=0.1)


#第二張圖
plt.subplot(232)

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(3*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, -1, y, color='yellow', alpha=0.3)


#第三張圖
plt.subplot(233)

# 函數f(x)的係數
a1 = 1
c1 = -2
x = np.linspace(-2, 3, 1000)
y1 = a1*x**2 + c1
plt.plot(x, y1, color='b')      # 藍色是 f(x)

# 函數g(x)的係數
a2 = -1
b2 = 2
c2 = 2
x = np.linspace(-2, 3, 1000)
y2 = a2*x**2 + b2*x + c2
plt.plot(x, y2, color='g')      # 綠色是 g(x)

# 繪製區間
plt.fill_between(x, y1=y1, y2=y2, where=(x>=-1)&(x<=2),
                 facecolor='yellow')

plt.grid()


#第四張圖
plt.subplot(234)

t = np.linspace(-np.pi*1.5, np.pi*1.5, 100)
c = np.sinc(t)

plt.plot(t, c)
plt.fill(t, c)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)





plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

