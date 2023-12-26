# ch20_35.py
import matplotlib.pyplot as plt
from random import randint

def dice_generator(times, sides):
    ''' 處理隨機數 '''
    for i in range(times):              
        ranNum = randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]          
times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.8)             # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')
plt.show()

