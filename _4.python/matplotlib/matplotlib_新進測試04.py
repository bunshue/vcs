import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
sin_line, = plt.plot(x, y1, label = "Sin", linestyle = '--')                         
cos_line, = plt.plot(x, y2, label = "Cos", lw = 3)

sin_legend = plt.legend(handles = [sin_line], loc = 1)  # 建立sin圖表物件
plt.gca().add_artist(sin_legend)    # 手動將sin圖例加入圖表

plt.legend(handles = [cos_line], loc = 4)               # 建立cos圖表

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]            # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]       # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.figure(1)                               # 建立圖表1              
plt.plot(seq, data1, '-*')                  # 繪製圖表1
plt.title("Test Chart 1", fontsize=24)

plt.figure(2)                               # 建立圖表2
plt.plot(seq, data2, '-o')                  # 以下皆是繪製圖表2
plt.title("Test Chart 2", fontsize=24)
plt.xlabel("x-Value", fontsize=14)
plt.ylabel("y-Value", fontsize=14)

plt.show()

print('------------------------------------------------------------')	#60個



import matplotlib.pyplot as plt

#plt.figure(figsize=(7,2))
my_kwargs = dict(ha='center', va='center', fontsize=50, c='b')
plt.text(0.5, 0.5, '歡迎來到美國', **my_kwargs)

plt.show()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





