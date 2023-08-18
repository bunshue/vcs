# ch19_20.py
import numpy as np
import matplotlib.pyplot as plt
temperature = [22,25,26,27,28,29,30,31,32,33]           # 天氣溫度
rev = [600,900,1100,720,950,1020,1000,1200,1420,1500]   # 營業額

coef = np.polyfit(temperature, rev, 2)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(reg)     
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()










