# ch13_9.py
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
barH = 0.25                                 # 橫條圖高度
plt.barh(X+0.00,Benz,color='r',height=barH,label='Benz')
plt.barh(X+barH,BMW,color='g',height=barH,label='BMW')
plt.barh(X+barH*2,Lexus,color='b',height=barH,label='Lexus')
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("數量", fontsize=14, color='b')
plt.ylabel("年度", fontsize=14, color='b')
plt.legend()                                 # 繪製圖例
plt.yticks(X+barH, labels)                   # 加註年度標籤
plt.show()


