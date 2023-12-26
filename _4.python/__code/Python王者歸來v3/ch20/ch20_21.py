# ch20_21.py
import matplotlib.pyplot as plt
import numpy as np

num = 100
while True:
    x = np.random.random(100)           # 建立x軸100個隨機數字
    y = np.random.random(100)           # 建立y軸100個隨機數字
    plt.scatter(x,y,s=100,c=x,cmap='brg')   # 繪製散點圖
    plt.show()
    yORn = input("是否繼續 ?(y/n) ")    # 詢問是否繼續
    if yORn == 'n' or yORn == 'N':      # 輸入n或N則程式結束
        break
    

