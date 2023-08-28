# ch18_2.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
days = [1,2,3,4,5,6,7]              # 設定日期
working = [8,8,9,8,8,2,2]           # 設定每天工作時間
playing = [4,5,3,8,6,12,10]         # 設定每天玩手機的時間
eating = [2,2,3,2,3,4,4]            # 設定每天吃飯時間
sleeping = [10,9,9,6,7,6,8]          # 設定每天睡眠時間
labels = ['工作','玩手機','吃飯','睡眠']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
colors = ['orange','lightgreen','yellow','lightblue']
# 繪製堆疊折線圖
plt.stackplot(days,working,playing,eating,sleeping,
              labels=labels,colors=colors)
plt.xlabel('日期',fontsize=12,color='b')
plt.ylabel('時數',fontsize=12,color='b')
plt.title('繪製一週時間分配圖',fontsize=16,color='b')
plt.xticks(days,xlabels)
plt.legend()
plt.show()





  
      
