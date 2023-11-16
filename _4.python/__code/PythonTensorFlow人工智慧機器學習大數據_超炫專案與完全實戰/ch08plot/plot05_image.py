import matplotlib.pyplot as plt
import matplotlib.image as img

t=[10, 20, 30, 40]

plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

image = img.imread('powenko.png')
imgplot = plt.imshow(image)

plt.plot(t, t, 'r--')
plt.text(70, 10, 'Hello! powenko.com')
plt.savefig('my.png')

plt.show()
