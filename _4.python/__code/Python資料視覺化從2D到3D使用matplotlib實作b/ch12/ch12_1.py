# ch12_1.py
import matplotlib.pyplot as plt
import numpy as np

img = np.array([[0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 18],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35]])               
plt.imshow(img, cmap='Blues')
plt.colorbar()
plt.show()


