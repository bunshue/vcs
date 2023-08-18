# ch1_32.py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))
plt.show()


