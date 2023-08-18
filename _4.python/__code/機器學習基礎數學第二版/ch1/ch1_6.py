# ch1_6.py
import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10)       # 串列squares數據是y軸的值, 線條寬度是10
plt.title('Test Chart', fontsize=24)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Square', fontsize=16)
plt.show()


