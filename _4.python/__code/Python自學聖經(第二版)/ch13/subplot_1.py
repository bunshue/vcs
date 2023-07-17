import matplotlib.pyplot as plt

listx = [1,2,3,4,5]

listy1 = [15,50,80,40,70]
plt.subplot(2,1,1)
plt.ylim(0, 100)
plt.plot(listx, listy1, 'r-s')

listy2 = [80,20,60,50,20]
plt.subplot(2,1,2)
plt.ylim(0, 100)
plt.plot(listx, listy2, 'g--o')

plt.show()

#plt.rcParams['figure.figsize'] = [10, 10]
#plt.rcParams['figure.dpi'] = 72
#plt.rcParams.keys