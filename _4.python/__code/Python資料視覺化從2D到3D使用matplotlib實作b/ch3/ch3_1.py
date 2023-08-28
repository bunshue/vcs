# ch3_1.py
import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
plt.plot(squares)
plt.axis([0, 9, 0, 70])
plt.show()


