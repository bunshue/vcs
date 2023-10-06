import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')

plt.figure(figsize = (15, 9), facecolor = 'white')
point_numbers = range(rw.num_points)
plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)

# 畫出第1點和最後一點
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

plt.show()
