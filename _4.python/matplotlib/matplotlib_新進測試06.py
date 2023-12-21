# 新進測試06

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

th = np.arange(0,360,10)
#print(th)

x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x,y)


plt.show()

print("求arctan 3.4的角度")
rad = np.arctan(3.4)
print(rad)
th = np.degrees(rad)
print(th)



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



