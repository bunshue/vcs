
import matplotlib.pyplot as plt
import numpy as np


data = [-1, -4.3, 15, 21, 31]
plt.plot(data) 
plt.show()


plt.plot(data, "o--b")
plt.show()


days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius)
plt.show()


x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, x, cosinus)
plt.show()


print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")
plt.show()



days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "r-o")
plt.grid(True)
plt.show()




print('------------------------------------------------------------')	#60個


days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
plt.xlabel("日數")
plt.ylabel("攝氏溫度")
plt.show()


x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o",
         x, cosinus, "g--")
plt.xlabel("徑度")
plt.ylabel("振幅")
plt.title("Sin 和 Cos 波形")
plt.show()




print('------------------------------------------------------------')	#60個


x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, "r-o", label="sin(x)")
plt.plot(x, cosinus, "g--", label="cos(x)")
plt.legend(loc=1)
plt.show()




print('------------------------------------------------------------')	#60個

days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
print(plt.axis())
plt.show()



days = range(1, 7)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
plt.plot(days, celsius, "g--s")
xmin, xmax, ymin, ymax = 0.5, 6.5, 15, 32.5
plt.axis([xmin, xmax, ymin, ymax])
plt.show()


days = range(1, 7)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日數")
plt.ylabel("攝氏溫度")
plt.axis([0.5, 6.5, 15, 35])
plt.show()





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



