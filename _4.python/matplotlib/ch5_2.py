import matplotlib.pyplot as plt                                  

import numpy as np


print('------------------------------------------------------------')	#60個


x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()



print('------------------------------------------------------------')	#60個

                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.plot(x, y, '-*')   
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

                                
x = np.linspace(0, 1000, 100)
y = 0.03 * x - 18
plt.axis([0, 1000, -20, 15])            # 標記刻度範圍
plt.plot(x, y)   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加格線
plt.show()


print('------------------------------------------------------------')	#60個

                                
x = [x for x in range(0, 11)]
y = [2 * y for y in x]
plt.xticks(x)
plt.axis([0, 10, 0, 20])                # 標記刻度範圍
plt.plot(x, y)   
plt.grid()                              # 加格線
plt.show()


print('------------------------------------------------------------')	#60個

                                
x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [(2 * y - 2) for y in x]
y3 = [(2 * y + 2) for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()


print('------------------------------------------------------------')	#60個

                                
x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()


print('------------------------------------------------------------')	#60個

                                
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




print('------------------------------------------------------------')	#60個






