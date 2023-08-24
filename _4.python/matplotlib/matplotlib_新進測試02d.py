import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x2 = np.arange(100)
y2 = x2 * np.random.rand(100)

plt.scatter(x2, y2)
plt.show()

'''

plt.hist(y2, bins = 5)
plt.show()



plt.bar(x2, y2)
plt.show()


plt.plot(x2, y2)
plt.show()

'''

#箱形圖  便於確認資料分布的視覺化方法
plt.boxplot(y2)
plt.show()



'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
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
'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



