import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2023, 2024, 2025]                # 年度
labels = ["2023年","2024年","2025年"]
plt.xticks(seq,labels)
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(bbox_to_anchor=(1,1),title='汽車品牌')
plt.tight_layout(pad=7)
plt.title("銷售報表", fontsize=24)
plt.xlabel("年度", fontsize=14)
plt.ylabel("數量", fontsize=14)

plt.show()

