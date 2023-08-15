
import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, sinus, "r-o")
plt.subplot(2, 1, 2)
plt.plot(x, cosinus, "g--")
plt.show()

print('------------------------------')  #30個


x = np.linspace(0, 10, 50)
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), "r-o")
plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), "g--")
plt.show()



print('------------------------------')  #30個


x = np.linspace(0, 10, 50)
plt.subplot(231)
plt.plot(x, np.sin(x))
plt.subplot(232)
plt.plot(x, np.cos(x))
plt.subplot(233)
plt.plot(x, np.tan(x))
plt.subplot(234)
plt.plot(x, np.sinh(x))
plt.subplot(235)
plt.plot(x, np.cosh(x))
plt.subplot(236)
plt.plot(x, np.tanh(x))
plt.show()



print('------------------------------')  #30個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
plt.show()




print('------------------------------')  #30個

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.show()


print('------------------------------')  #30個

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Cos(x)", color="blue")
ax2.legend(loc="best")
plt.show()



print('------------------------------')  #30個








