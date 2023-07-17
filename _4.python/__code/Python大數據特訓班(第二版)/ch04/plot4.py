import matplotlib.pyplot as plt

listx = [0,800,1500,3200,4100,5000]
listy = [20,60,32,45,78,56]
plt.plot(listx, listy)
plt.xticks(range(0,5500,500))
plt.tick_params(axis='both', labelsize=10, color='red')
plt.show()