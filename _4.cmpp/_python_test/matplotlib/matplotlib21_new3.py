import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

'''
#散點圖
a = rand(100)
b = rand(100)
plt.scatter(a,b)

plt.show()
'''



#Hyperlinks
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

fig = plt.figure()  #開新圖片

s = plt.scatter([1, 2, 3], [4, 5, 6])
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/scatter.svg'
fig.savefig(filename)
print('已存圖' + filename)

fig = plt.figure()  #開新圖片

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])

im.set_url('https://www.google.com/')
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/image.svg'
fig.savefig(filename)
print('已存圖' + filename)

plt.show()









