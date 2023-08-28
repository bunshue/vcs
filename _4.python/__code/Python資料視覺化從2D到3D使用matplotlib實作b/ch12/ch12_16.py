# ch12_16.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
z = np.add.outer(range(8), range(8)) % 2
im1 = plt.imshow(z, cmap='gray')
plt.show()


      
