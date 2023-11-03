import matplotlib.pyplot as plt 
import seaborn as sns
import math

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

sns.set()
fig, axes = plt.subplots(1,2, figsize=(6,4))
ax1 = sns.lineplot(x=x, y=sinus, ax=axes[0])
ax2 = sns.scatterplot(x=x, y=cosinus, ax=axes[1])
plt.show()
