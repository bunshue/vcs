import matplotlib.pyplot as plt

plt.figure(figsize=[8,8])
plt.subplot(121)
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.subplot(122)
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()