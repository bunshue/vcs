import matplotlib.pyplot as plt
year = [2015,2016,2017,2018,2019]
city1 = [128,150,199,180,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="Taipei")
city2 = [120,145,180,170,120]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="Taichung")
plt.legend()
plt.ylim(50, 250)
plt.xticks(year)
plt.title("Sales Report", fontsize=18)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)
plt.show()