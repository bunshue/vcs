# ch3_2.py
import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
plt.plot(squares)
xmin, xmax, ymin, ymax = plt.axis()
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"ymin = {ymin}")
print(f"ymax = {ymax}")
plt.show()



