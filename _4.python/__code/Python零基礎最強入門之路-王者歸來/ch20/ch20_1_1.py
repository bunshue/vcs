# ch20_1_1.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)       # 串列squares數據是y軸的值
plt.axis([0, 8, 0, 70]) # x軸刻度0-8, y軸刻度0-70    
plt.show()


