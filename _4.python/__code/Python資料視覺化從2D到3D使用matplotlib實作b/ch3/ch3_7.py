# ch3_7.py
import matplotlib.pyplot as plt

x = [0.5,1.0,10,50,100]
y = [5,10,35,20,25]
labels = ['A','B','C','D','E']
plt.xticks(x,labels)
plt.plot(x,y,"-o")
plt.show()


