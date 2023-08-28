# ch14_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
np.random.seed(10)
sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數 
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
# 設定 bins = sides = 6    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("骰子出現次數 : ",h[0])
plt.ylabel('次數')
plt.xlabel('骰子點數')
plt.title('測試 10000 次')
plt.show()
    





