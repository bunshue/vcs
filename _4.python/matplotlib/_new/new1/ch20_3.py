# ch20_3.py
import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10)       # 線條寬度是10
plt.title('Test Chart', fontsize=24)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Square')
plt.show()


