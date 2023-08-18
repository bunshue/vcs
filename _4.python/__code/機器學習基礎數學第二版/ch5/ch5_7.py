# ch5_7.py
import matplotlib.pyplot as plt
                                
x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y + 2 for y in x]
y3 = [4 * y - 3 for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()


