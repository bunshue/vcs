# ch27_16.py  
from matplotlib import pyplot as plt
from matplotlib.patches import Arrow

fig = plt.figure()
ax = fig.subplots()

arr1 = Arrow(3, 3, 2, 0)
arr2 = Arrow(3, 3, 0, 1.75, color='g', width=0.6)
arr3 = Arrow(3, 3, -1.5,0, color ='m', width=0.4)
arr4 = Arrow(3, 3, 0,-1, color ='r', width=0.2)
ax.add_patch(arr1)
ax.add_patch(arr2)
ax.add_patch(arr3)
ax.add_patch(arr4)
ax.set_xlim(0,6)
ax.set_ylim(0,6)
ax.set_aspect('equal')
ax.grid(True)
plt.show()




