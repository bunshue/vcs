import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("3圖比較")

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, ax = plt.subplots(1, 3, figsize=(20, 15))

ax[0].plot(x,y0, label="sin")
ax[1].plot(x,y1, label="cos")
ax[2].plot(x,y2, label="tan")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

