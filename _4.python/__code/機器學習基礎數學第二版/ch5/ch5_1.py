# ch5_1.py
import matplotlib.pyplot as plt                                  
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()


