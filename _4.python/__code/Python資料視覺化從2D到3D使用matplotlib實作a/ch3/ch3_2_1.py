# ch3_2_1.py
import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
plt.plot(squares)
plt.axis('equal')
plt.show()



