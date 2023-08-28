# ch3_15.py
import matplotlib.pyplot as plt

x = [0,1,2,3,4]
y = [5,10,35,20,25]
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 16
plt.plot(x,y,"-o")
plt.show()


