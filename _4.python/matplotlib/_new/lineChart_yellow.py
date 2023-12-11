import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]

plt.plot(x, y)
plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')

plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()
