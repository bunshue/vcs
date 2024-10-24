"""
想要做什麼的暫存



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#標準
L0 = 71.36
A0 = -32.718
B0 = 1.636

#量測結果
L1 = 77.705
A1 = -19.471
B1 = 3.858

diff1 = (L0-L1) * (L0-L1)
diff2 = (A0-A1) * (A0-A1)
diff3 = (B0-B1) * (B0-B1)

diff = math.sqrt(diff1+diff2+diff3)

print(diff)

print("------------------------------------------------------------")  # 60個

N = 10
MIN = 10
MAX = 15

data_list_same_found = []

data_list = []
for i in range(N):
    num = random.randint(MIN, MAX)
    data_list.append(num)

print(type(data_list))
print(data_list)

"""
#debug
data_list = [14, 11, 11, 13, 11, 12]
print(data_list)
"""

# 建立一個長度N的陣列 都放著 False
data_list_same = N * [False]
print(data_list_same)

compoare_count = 0
for i in range(N):
    same_data = False
    if data_list_same[i] == True:
        print("已經被找到過, 跳過")
        continue
    for j in range(i + 1, N):
        print("compare ", i, j, end=" ")
        compoare_count += 1
        if data_list[i] == data_list[j]:
            if same_data == False:
                print("找到相同")
                same_data = True
                data_list_same[i] = True
                data_list_same[j] = True
                data_list_same_found.append(data_list[i])
                data_list_same_found.append(data_list[j])
            else:
                print("又找到相同")
                data_list_same[j] = True
                data_list_same_found.append(data_list[j])
        else:
            print("不同")
    print()
print()

print("共比較 :", compoare_count, "次")

print(data_list_same)
print()
print(data_list_same_found)
print()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
