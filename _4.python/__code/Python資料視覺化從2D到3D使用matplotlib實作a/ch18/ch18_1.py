# ch18_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
days = [1,2,3,4,5,6,7]                  # 設定日期
working = [5,4,6,5,8,4,3]               # 設定每天工作時間
playing =  [2,5,3,4,5,8,6]              # 設定每天玩手機的時間
labels = ['工作','玩手機']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 繪製堆疊折線圖
plt.stackplot(days,working,playing,labels=labels)
plt.xlabel('日期',fontsize=12,color='b')
plt.ylabel('時數',fontsize=12,color='b')
plt.title('繪製一週工作和玩手機的時間',fontsize=16,color='b')
plt.xticks(days,xlabels)
plt.legend(loc='upper left')
plt.show()





  
      
