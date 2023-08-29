# ch3_11.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2023, 2024, 2025]                # 年度
labels = ["2023年","2024年","2025年"]
plt.xticks(seq,labels)
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

plt.title("銷售報表", fontsize=24)
plt.xlabel("年度", fontsize=14)
plt.ylabel("數量", fontsize=14)

locs, the_labels = plt.xticks()         # 回傳位置與標籤字串
print(f'locs       = {locs}')
print(f'the_labels = {the_labels}')

plt.show()


