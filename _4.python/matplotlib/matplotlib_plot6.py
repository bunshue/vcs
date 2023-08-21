# plot 集合

'''
無 numpy 的 matplotlib

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


data = [3, 8, 3, 4, 2]

plt.plot(data, "r-o")   #未指明x, 則x為 0 ~ n-1


#第二張圖
plt.subplot(232)


days = range(1, 7)  #1 2 3 4 5 6
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")




#第三張圖
plt.subplot(233)

speed = [4, 4, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 20, 22, 23, 24, 24, 24, 24, 25]
dist = [2, 10, 4, 22, 16, 10, 18, 26, 34, 17, 28, 14, 20, 24, 28, 26, 34, 34, 46, 26, 36, 60, 80, 20, 26, 54, 32, 40, 32, 40, 50, 42, 56, 76, 84, 36, 46, 68, 32, 48, 52, 56, 64, 66, 54, 70, 92, 93, 120, 85]

plt.plot(speed, dist)




#第四張圖
plt.subplot(234)




#第五張圖
plt.subplot(235)






#第六張圖
plt.subplot(236)






plt.show()





print('------------------------------------------------------------')	#60個



