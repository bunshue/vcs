# ch20_1.py
import matplotlib.pyplot as plt

x = [x for x in range(9)]       # 產生0, 1, ... 8串列
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x, squares)            # 串列squares數據是y軸的值
plt.show()


