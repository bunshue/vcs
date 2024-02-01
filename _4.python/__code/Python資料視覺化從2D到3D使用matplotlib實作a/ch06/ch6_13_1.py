import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
ax = plt.subplot()
ax.plot(squares)
ax.set_aspect('equal')

plt.show()



