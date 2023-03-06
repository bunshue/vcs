import matplotlib.pyplot as plt

plt.figure(figsize=[8,4])
plt.axes([0,0,0.4,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.5,0,0.4,1])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()