# ch19_8_1.py
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

sc = [60,10,40,80,80,30,80,60,70,90,50,50,50,70,60,80,80,50,60,70,
      70,40,30,70,60,80,20,80,70,50,90,80,40,40,70,60,80,30,20,70]
print(f'平均成績 = {np.mean(sc)}')
print(f'中位成績 = {np.median(sc)}')
print(f'眾數成績 = {st.mode(sc)}')

hist = [0]*9
for s in sc:
    if s == 10: hist[0] += 1
    elif s == 20:
        hist[1] += 1
    elif s == 30:
        hist[2] += 1
    elif s == 40:
        hist[3] += 1
    elif s == 50:
        hist[4] += 1
    elif s == 60:
        hist[5] += 1
    elif s == 70:
        hist[6] += 1
    elif s == 80:
        hist[7] += 1
    elif s == 90:
        hist[8] += 1
width = 1
N = len(hist)
x = np.arange(N)
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.bar(x, hist, width)
plt.ylabel('學生人數')
plt.xlabel('分數')
plt.xticks(x,('10','20','30','40','50','60','70','80','90'))
plt.title('成績表')
plt.show()


