# ch19_9.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {st.mode(sc)}')
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.hist(sc, 9)

plt.ylabel('學生人數')
plt.xlabel('分數')
plt.title('成績表')
plt.show()


