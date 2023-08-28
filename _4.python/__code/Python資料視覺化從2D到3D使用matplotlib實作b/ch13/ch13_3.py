# ch13_3.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
def dice_generator(num, sides):
    ''' 處理隨機數 '''
    for i in range(num):              
        ranNum = np.random.randint(1, sides+1)    # 產生 1-6 隨機數
        dice.append(ranNum)
def dice_count(sides):
    '''計算1-6個出現次數'''
    for i in range(1, sides+1):
        frequency = dice.count(i)           # 計算i出現在dice串列的次數
        times.append(frequency)          
num = 600                                   # 擲骰子次數
sides = 6                                   # 骰子有幾面
dice = []                                   # 建立擲骰子的串列
times = []                                  # 儲存每一面骰子出現次數串列
dice_generator(num, sides)                  # 產生擲骰子的串列
dice_count(sides)                           # 將骰子串列轉成次數串列                          
x = np.arange(6)                            # 長條圖x軸座標
width = 0.35                                # 長條圖寬度
plt.bar(x,times,width,color='orange',hatch='o')  # 繪製長條圖
plt.ylabel('出現次數',color='b')
plt.title('測試 600次 ',fontsize=16,color='b')
plt.xticks(x, ('1', '2', '3', '4', '5', '6'), color='b')
plt.yticks(np.arange(0, 150, 15), color='b')
plt.show()

