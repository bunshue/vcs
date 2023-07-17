import matplotlib.pyplot as plt

plt.figure(figsize=[8,8])
plt.subplot(221)
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.subplot(222)
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.subplot(223)
plt.title(label='Chart 3')
plt.plot([1,2,3],'b:o')

plt.subplot(224)
plt.title(label='Chart 4')
plt.plot([1,2,3],'y--o')

plt.show()