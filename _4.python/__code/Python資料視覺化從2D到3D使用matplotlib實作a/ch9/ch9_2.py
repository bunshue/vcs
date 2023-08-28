# ch9_2.py
import matplotlib.pyplot as plt

x = [x for x in range(1,6)]
y = [(y * y) for y in x]
plt.scatter(x,y,color='lightgreen',edgecolor='b',s=60)
plt.show()



