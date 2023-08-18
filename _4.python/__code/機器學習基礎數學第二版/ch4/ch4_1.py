# ch4_1.py
import matplotlib.pyplot as plt
unitprice = 90                                  # 一斤的價格
x = [x for x in range(1, 11)]                   # x代表斤
y = [y * unitprice for y in x]                  # 不同重量的價格
plt.plot(x, y, '-*')   
plt.xlabel("x-weight")
plt.ylabel("y-money")
plt.show()


