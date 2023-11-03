import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, lw=8, ls='-.')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()
