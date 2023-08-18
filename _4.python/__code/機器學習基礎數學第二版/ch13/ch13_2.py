# ch13_2.py
import matplotlib.pyplot as plt
from random import randint

min = 1
max = 6                                         # 骰子有幾面
times = 10000                                   # 擲骰子次數

dice = [0] * 7                                  # 建立擲骰子的串列
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
    
del dice[0]                                     # 刪除索引0資料
    
for i, c in enumerate(dice, 1):
    print('{} = {} 次'.format(i, c))
    
x = [i for i in range(1, max+1)]                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, dice, width, color='g')              # 繪製長條圖
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()




