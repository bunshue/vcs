# ch13_6.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
Benz = [3367, 4120, 5539]                       # Benz線條
BMW = [4000, 3590, 4423]                        # BMW線條
Lexus = [5200, 4930, 5350]                      # Lexus線條
year = ["2023年","2024年","2025年"]             # 年度  

barW = 0.35                                     # 長條圖寬度
plt.bar(year,Benz,color="green",width=barW,label="Benz")
plt.bar(year,BMW,color="yellow",width=barW,
        bottom=np.array(Benz),label="BMW")
plt.bar(year,Lexus,color="red",width=barW,
        bottom=np.array(Benz)+np.array(BMW),label="Lexus")
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("年度", fontsize=14, color='b')
plt.ylabel("數量", fontsize=14, color='b')
plt.legend()
plt.show()


