# ch19_18.py
import numpy as np
import matplotlib.pyplot as plt
temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
     
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()










