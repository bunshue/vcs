import matplotlib.pyplot as plt

listx = [31,15,20,25,12,18,45,21,33,5,18,22,37,42,10]
listy = [68,20,61,32,45,56,10,18,70,64,43,66,19,77,21]
scale = [x**3 for x in [5,4,2,6,7,1,8,9,2,3,2,4,5,7,2]]

plt.xlim(0,50)
plt.ylim(0,80)
plt.scatter(listx, listy, c='r', s=scale, marker='o', alpha=0.5)

plt.show()