# ch18_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
population = {
    '非洲':[180, 200, 210, 230, 280],
    '歐洲':[300, 310, 340, 370, 410],
    '美洲':[290, 330, 350, 365, 380],
    '亞洲':[1200, 1250, 1300, 1600, 1900],
    '大洋洲':[88, 95, 110, 130, 150]
}
year = ['1980','1990','2000','2010','2020']
plt.stackplot(year,population.values(),labels=population.keys())
plt.legend(loc='upper left')
plt.xlabel('年度',color='b')
plt.ylabel('百萬人',color='b')
plt.title('世界人口統計',fontsize=16,color='b')
plt.show()





  
      
