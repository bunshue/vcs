import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條

X = np.arange(len(Benz))
labels = ["2023年","2024年","2025年"]       # 年度刻度標籤
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
barW = 0.25                                 # 長條圖寬度

plt.bar(X+0.00,Benz,color='r',width=barW,label='Benz')
plt.bar(X+barW,BMW,color='g',width=barW,label='BMW')
plt.bar(X+barW*2,Lexus,color='b',width=barW,label='Lexus')

plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("年度", fontsize=14, color='b')
plt.ylabel("數量", fontsize=14, color='b')
plt.legend()                                 # 繪製圖例
plt.xticks(X+barW, labels)                   # 加註年度標籤

plt.show()
