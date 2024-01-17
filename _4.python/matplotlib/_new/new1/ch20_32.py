# ch20_32.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('得票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton')) # x 軸刻度
plt.yticks(np.arange(0, 450, 30))           # y 軸刻度
plt.show()


