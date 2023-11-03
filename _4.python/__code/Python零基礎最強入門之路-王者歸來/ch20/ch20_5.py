# ch20_5.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, linewidth=3)
plt.title("Test Chart", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square", fontsize=16)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()


