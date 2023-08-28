# ch19_4.py
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.plot(x,y,'o--',color='grey',alpha=0.4)
plt.step(x,y,'g',where='mid')
plt.show()


      
