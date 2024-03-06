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

print("subplot 100張圖")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

import matplotlib.image as img

# print('使用 matplotlib 顯示一圖')
image = img.imread(filename)

N = 100
for i in range(N):
    plt.subplot(10, N // 10, i + 1)
    plt.imshow(image)

plt.show()


print("------------------------------------------------------------")  # 60個
