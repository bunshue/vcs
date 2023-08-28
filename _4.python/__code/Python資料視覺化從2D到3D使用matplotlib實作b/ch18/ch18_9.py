# ch18_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
months= ['1月','2月','3月','4月','5月','6月',
         '7月','8月','9月','10月','11月','12月']

cost = {
    '房屋貸款':[32000,31500,31000,30500,30000,29500, 
                29000,28500,28000,27500,27000,26500],
    '餐飲支出':[20000,18000,21000,23000,25000,30000, 
                24000,25000,28000,26000,21000,22000],
    '水電費用':[8500,8000,8500,9500,10000,11000, 
                10500,10000,8800,8900,9300,9200],
    '保險支出':[6000,6200,5500,5800,5900,6100, 
                4800,5200,6100,5900,4800,7000]
}
fig, ax = plt.subplots()
ax.set_title("家庭開銷統計",fontsize=16,color='b')
ax.set_xlabel("月份",fontsize=14,color='b')
ax.set_ylabel("費用",fontsize=14,color='b')
# 繪製家庭開銷堆疊折線圖
ax.stackplot(months,cost.values(),labels=cost.keys())
ax.legend()
plt.tight_layout()
plt.show()





  
      
