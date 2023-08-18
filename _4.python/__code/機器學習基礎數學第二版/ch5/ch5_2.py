# ch5_2.py
import matplotlib.pyplot as plt                                 
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.plot(x, y, '-*')   
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()


