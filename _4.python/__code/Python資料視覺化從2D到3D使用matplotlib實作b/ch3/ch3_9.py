# ch3_9.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
week = [0,1,2,3,4,5,6]
temperature = [23,25,29,31,26,30,24]
labels = ['Sunday','Monday','Tuesday','Wednesday',
          'Thursday','Friday','Saturday']
plt.xticks(week,labels)
plt.plot(temperature,"-o")
plt.title("一週的平均溫度", fontsize=24)
plt.xlabel("星期", fontsize=14)
plt.ylabel("溫度", fontsize=14)
plt.show()


