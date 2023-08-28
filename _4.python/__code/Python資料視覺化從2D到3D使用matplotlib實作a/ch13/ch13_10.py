# ch13_10.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條
year = ["2023年","2024年","2025年"]         # 年度  

barH = 0.35                                 # 橫條圖高度
plt.barh(year,Benz,color="green",height=barH,label="Benz")
plt.barh(year,BMW,color="yellow",height=barH,
        left=np.array(Benz),label="BMW")
plt.barh(year,Lexus,color="red",height=barH,
        left=np.array(Benz)+np.array(BMW),label="Lexus")
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("數量", fontsize=12, color='b')
plt.ylabel("年度", fontsize=12, color='b')
plt.legend()
plt.show()


