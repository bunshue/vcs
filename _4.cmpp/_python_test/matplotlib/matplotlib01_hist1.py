# hist 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10 #資料數
plt.hist(np.random.randn(1000), N, facecolor='yellow', edgecolor='yellow')

#第二張圖
plt.subplot(232)

import matplotlib.pyplot as plt
from numpy.random import normal,rand
x = normal(size=200)

N = 10 #資料數
plt.hist(x,bins=N)


#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()




