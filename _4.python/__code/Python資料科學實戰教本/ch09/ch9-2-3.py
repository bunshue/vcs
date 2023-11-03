import matplotlib.pyplot as plt

x = [21,42,23,4,5,26,77,88,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.title(str(n) + "\n" + str(bins))
plt.show()

