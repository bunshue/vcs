# ch19_10.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

sc1 = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]

sc2 = [50,10,60,80,70,30,80,60,30,90,50,50,90,70,60,50,80,50,60,70,
      60,50,30,70,70,80,10,80,70,50,90,80,40,50,70,60,80,40,20,70]

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist([sc1,sc2],9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')
plt.show()


