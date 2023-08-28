# ch18_8.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
days = [x for x in range(0, 7)]             # 一週時間    
suspected = [22, 25, 45, 58, 69, 82, 95]    # 疑似病例 
cured = [8, 12, 16, 25, 43, 56, 68]         # 康原病例
deaths = [2, 2, 6, 7, 10, 12, 13]           # 往生人數
colors = ['orange','green','red']
labels = ['疑似病例','康原病例','往生人數']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 建立堆疊折線圖
plt.stackplot(days, suspected,cured,deaths,colors=colors,
              labels=labels,baseline ='weighted_wiggle') 
plt.legend(loc='lower left') 
plt.title('病例數據統計資料',fontsize=16,color='b')
plt.xlabel('一週時間',fontsize=12,color='b')
plt.ylabel('全部病例數',fontsize=12,color='b')
plt.xticks(days,xlabels)
plt.show()





  
      
