import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np

print('------------------------------------------------------------')	#60個
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示
print('------------------------------------------------------------')	#60個

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額

print(f"相關係數 = {np.corrcoef(temperature,rev).round(2)}")
plt.scatter(temperature, rev)
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print('------------------------------------------------------------')	#60個

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(coef.round(2))
print(reg)         

print('------------------------------------------------------------')	#60個

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")

print('------------------------------------------------------------')	#60個

temperature = [25,31,28,22,27,30,29,33,32,26]           # 天氣溫度
rev = [900,1200,950,600,720,1000,1020,1500,1420,1100]   # 營業額 

coef = np.polyfit(temperature, rev, 1)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
     
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print('------------------------------------------------------------')	#60個

temperature = [22,25,26,27,28,29,30,31,32,33]           # 天氣溫度
rev = [600,900,1100,720,950,1020,1000,1200,1420,1500]   # 營業額

coef = np.polyfit(temperature, rev, 2)                  # 迴歸直線係數
reg = np.poly1d(coef)                                   # 線性迴歸方程式
print(reg)     
plt.scatter(temperature, rev)
plt.plot(temperature,reg(temperature),color='red')
plt.title('天氣溫度與冰品銷售')
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





