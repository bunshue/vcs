
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

print('兩Y軸不同刻度, plot + plot')

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()

ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")

ax2 = ax.twinx()

ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")

ax.set_title('兩Y軸不同刻度 plot + plot', size=20)

plt.show()

print('------------------------------------------------------------')	#60個

print('兩Y軸不同刻度, plot + bar')

import matplotlib.gridspec as gridspec

x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) *10

fig = plt.figure(figsize=(12, 8))	#圖像大小[英吋]
gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()

ax.plot(x, y, marker="", alpha=0.8)
ax.grid(20)

axx = ax.twinx()
axx.bar(x, y2,
        alpha=0.2,
        label="hold_volume",
        color="pink",
)
ax.set_title('兩Y軸不同刻度 plot + bar', size=20)

plt.show()

print('------------------------------------------------------------')	#60個


