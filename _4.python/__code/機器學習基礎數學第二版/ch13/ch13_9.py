# ch13_9.py
import matplotlib.pyplot as plt
import numpy as np

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數 
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()
    





