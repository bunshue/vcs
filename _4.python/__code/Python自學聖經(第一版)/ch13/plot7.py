import matplotlib.pyplot as plt

listx = [1000,2000,3000,4000,5000]
listy = [15,50,80,70,50]
plt.plot(listx, listy)
plt.xticks(listx)
plt.tick_params(axis='both', labelsize=16, color='red')
plt.show()