# scatter 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'scatter 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

#散點圖
a = rand(100)
b = rand(100)
plt.scatter(a,b)


#第二張圖
plt.subplot(232)

#Hyperlinks
import numpy as np
import matplotlib.pyplot as plt

s = plt.scatter([1, 2, 3], [4, 5, 6])
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
'''
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/scatter.svg'
fig.savefig(filename)
print('已存圖' + filename)
'''

#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()


