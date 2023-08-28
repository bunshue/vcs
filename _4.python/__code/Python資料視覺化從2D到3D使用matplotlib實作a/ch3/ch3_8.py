# ch3_8.py
import matplotlib.pyplot as plt

x = [0.5,1.0,10,50,100]
y = [5,10,35,20,25]
value = range(len(x))
plt.plot(value,y,"-o")
plt.xticks(value,x)
plt.show()


