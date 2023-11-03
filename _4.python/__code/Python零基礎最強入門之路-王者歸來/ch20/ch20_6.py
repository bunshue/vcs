# ch20_6.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64]
seq = [1,2,3,4,5,6,7,8]
plt.plot(seq, squares, linewidth=3)
plt.title("Test Chart", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square", fontsize=16)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()


