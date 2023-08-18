# ch5_4.py
import matplotlib.pyplot as plt
                                
x = [x for x in range(0, 11)]
y = [2 * y for y in x]
plt.xticks(x)
plt.axis([0, 10, 0, 20])                # 標記刻度範圍
plt.plot(x, y)   
plt.grid()                              # 加格線
plt.show()


