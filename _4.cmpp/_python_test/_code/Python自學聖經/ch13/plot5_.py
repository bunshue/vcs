import matplotlib.pyplot as plt
month = [1,2,3,4,5,6,7,8,9,10,11,12]
listy1 = [128,210,199,121,105,98,152,107,150,122,180,220]
plt.plot(month, listy1, 'r-.s', lw=2, ms=10, label="Taipei")
listy2 = [150,200,180,110,100,80,80,100,130,120,110,200]
plt.plot(month, listy2, 'g--*', lw=2, ms=10, label="Taichung")
plt.legend()
plt.xticks(month)
plt.ylim(50, 250)
plt.title("Sales Report", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.show()