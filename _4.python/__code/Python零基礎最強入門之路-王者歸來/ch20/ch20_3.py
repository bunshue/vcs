# ch20_3.py
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, linewidth=3)
plt.title("Test Chart")
plt.xlabel("Value")
plt.ylabel("Square")
plt.show()
