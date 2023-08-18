# ch1_31.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體

Benz = [3367, 4120, 5539]               # Benz線條
BMW = [4000, 3590, 4423]                # BMW線條
Lexus = [5200, 4930, 5350]              # Lexus線條

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')
plt.title("銷售報表", fontsize=24)
plt.xlabel("年度", fontsize=14)
plt.ylabel("銷售量", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()


