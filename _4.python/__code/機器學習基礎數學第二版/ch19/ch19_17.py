# ch19_17.py
import numpy as np

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")     











