import numpy as np
a = np.genfromtxt('scores.csv', delimiter=',', skip_header=1)
print(a.shape)