#傑卡德相似係數 Jaccard Similarity Coefficient

import numpy as np
import scipy.spatial.distance as dist

mat1 = [1,1,0,1,0,1,0,0,1]
mat2 = [0,1,1,0,0,0,1,1,1]
mat3 = [1,1,0,1,0,1,0,0,1]  #the same as mat1
mat4 = [0,0,1,0,1,0,1,1,0]  #invert of mat1

matV = np.mat([mat1,mat4])

print('dist.jaccard : ')
print(dist.pdist(matV, 'jaccard'))

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import special

print('------------------------------------------------------------')	#60個

a = special.exp10(3)
print('10^3 =', a)
b = special.exp2(3)
print('2^3 =', b)
c = special.sindg(90)
print('sind(90) =', c)
d = special.cosdg(45)
print('cosd(45) =', d)

print('畫出10^x, x=0~1.0')
x = np.linspace(0, 1, 100)
y = special.exp10(x)

plt.plot(x, y)
plt.show()

print('------------------------------------------------------------')	#60個


print('積分')
def func(x):
    return special.exp10(x)

area, err = integrate.quad(func, 0, 1)
print(area)


def half_circle(x):
    return (1-x**2)**0.5

area, err = integrate.quad(half_circle, -1, 1) 
print(area)

print('------------------------------------------------------------')	#60個

import numpy as np
from scipy import linalg

A = np.array([[2,3], [5,7]])
B = linalg.inv(A)
print(B)


A = np.array([[3,8], [4,6]])
B = linalg.det(A)
print(B)


a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = linalg.solve(a, b)
print(x)

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x):
    return x**2 + 15*np.sin(x)
x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x)) 
plt.show()

print('------------------------------------------------------------')	#60個


result = optimize.minimize(f, x0=0)
print(result.x)


plt.plot(x, f(x))
plt.plot(result.x, f(result.x), "o")
plt.show()

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import special

x = np.arange(5, 20)
y = special.exp2(x/3.0)
plt.plot(x, y, 'o')
plt.show()

print('------------------------------------------------------------')	#60個


f = interpolate.interp1d(x, y)
x1 = np.arange(5, 20)
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")
plt.show()


print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1./np.sqrt(2*pi*sigma**2))*e**(-(x-mu)**2/(2.*sigma**2))
    return f

ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]  
plt.plot(ax, ay)
plt.show()


x = [x/10.0 for x in range(-50, 60)]
plt.plot(x, stats.norm.pdf(x, 0, 1),
       'r-',lw=1,alpha=0.6,label='mu=0,sigma=1')
plt.plot(x, stats.norm.pdf(x, 0, 2),
       'b--',lw=1,alpha=0.6,label='mu=0,sigma=2')
plt.plot(x, stats.norm.pdf(x, 2, 1),
       'g-.',lw=1,alpha=0.6,label='mu=2,sigma=1')
plt.legend()
plt.title("Various Normal PDF")
plt.show()

samples = [9, 3, 27]  
   
desc = stats.describe(samples)
print(desc)

samples2 = [[1, 3, 27],  
            [3, 4, 6],  
            [7, 6, 3],  
            [3, 6, 8]]  
   
desc = stats.describe(samples2, axis = 0) 
print(desc)


desc = stats.describe(samples2, axis = 1) 
print(desc)




print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(6, 10, 500)
w = signal.chirp(t,f0=4,f1=2,t1=5,method='linear')
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel('time in sec)')
plt.show()

img = np.load("data/digit8.npy")

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

print('------------------------------------------------------------')	#60個


edge = [
    [0, 1, 0],
    [1,-4, 1],
    [0, 1, 0]
    ]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = signal.convolve2d(img, edge, 
                            boundary="symm", 
                            mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("edge-detection image")
plt.show()


print('------------------------------------------------------------')	#60個


sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
    ]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = signal.convolve2d(img, sharpen, 
                            boundary="symm",
                            mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("sharpen image")
plt.show()

print('------------------------------------------------------------')	#60個


img = np.load("data/digit3.npy")
filters = [[
    [-1, -1, -1],
    [ 1,  1,  1],
    [ 0,  0,  0]],
   [[-1,  1,  0],
    [-1,  1,  0],
    [-1,  1,  0]],
   [[ 0,  0,  0],
    [ 1,  1,  1],
    [-1, -1, -1]],
   [[ 0,  1, -1],
    [ 0,  1, -1],
    [ 0,  1, -1]]]


plt.figure()
plt.subplot(1, 5, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original")

for i in range(2, 6):
    plt.subplot(1, 5, i)
    c = signal.convolve2d(img,filters[i-2],
                          boundary="symm",
                          mode="same")
    plt.imshow(c, cmap="gray")
    plt.axis("off")
    plt.title("filter"+str(i-1))

plt.show()


print('------------------------------------------------------------')	#60個





