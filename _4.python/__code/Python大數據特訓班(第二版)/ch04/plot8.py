import matplotlib.pyplot as plt
year = [2016,2017,2018,2019,2020]
city1 = [100,180,90,220,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="Taipei")
city2 = [160,50,120,140,110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="Kaohsiung")
plt.legend()
plt.ylim(0, 250)
plt.xticks(year)
plt.title("Sales Report", fontsize=18)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)
plt.show()