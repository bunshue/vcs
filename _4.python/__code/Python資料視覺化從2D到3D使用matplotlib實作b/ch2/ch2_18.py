# ch2_18.py
import matplotlib.pyplot as plt

temperature = [23, 22, 20, 24, 22, 22, 23, 20, 17, 18,
               20, 20, 16, 14, 14, 20, 20, 20, 15, 14,
               14, 14, 14, 16, 16, 16, 18, 21, 21, 20,
               16]
x = [x for x in range(1,len(temperature)+1)]        
plt.plot(x, temperature)
plt.title("Weather Report", fontsize=24)
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.show()


