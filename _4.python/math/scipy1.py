"""
scipy

SciPy是一個開源的Python演算法庫和數學工具包。
SciPy包含的模組有最佳化、線性代數、積分、插值、特殊函數、快速傅立葉轉換、
訊號處理和圖像處理、常微分方程式求解和其他科學與工程中常用的計算。

scipy.integrate
scipy.special
scipy.interpolate
scipy.optimize
scipy.stats
scipy.signal

scipy.stats.norm

"""

import scipy
import math

'''
print('---- scipy.integrate --------------------------------------------------------')	#60個

# 計算半徑為r的圓的圓周
def calc_area(r):
    return 2 * math.pi * r

# 半徑2～5範圍的圓周總和
s = scipy.integrate.quad(calc_area, 2, 5)
print(s)

# 廁所衛生紙長度
x = s[0] / 0.011
print(x)

print('------------------------------------------------------------')	#60個

#SciPy.integrate.quad()函式

# f(x) = x**2 + 2x + 5
def func(x):
    return x**2 + 2*x + 5

print(scipy.integrate.quad(func, -3, 3))

#(47.99999999999999, 5.32907051820075e-13)

print('------------------------------------------------------------')	#60個

print('積分')
def func(x):
    return scipy.special.exp10(x)

area, err = scipy.integrate.quad(func, 0, 1)
print(area)

def half_circle(x):
    return (1-x**2)**0.5

area, err = scipy.integrate.quad(half_circle, -1, 1) 
print(area)

print('------------------------------------------------------------')	#60個


print('---- scipy.special --------------------------------------------------------')	#60個


import numpy as np
import matplotlib.pyplot as plt
import scipy


a = scipy.special.exp10(3)
print('10^3 =', a)

b = scipy.special.exp2(3)
print('2^3 =', b)

c = scipy.special.sindg(90)
print('sind(90) =', c)

d = scipy.special.cosdg(45)
print('cosd(45) =', d)

print('畫出10^x, x=0~1.0')
x = np.linspace(0, 1, 100)
y = scipy.special.exp10(x)

plt.plot(x, y)

plt.show()



print('------------------------------------------------------------')	#60個


print('---- scipy.interpolate --------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
#from scipy import interpolate
import scipy

x = np.arange(5, 20)
y = scipy.special.exp2(x/3.0)
plt.plot(x, y, 'o')

plt.show()

print('------------------------------------------------------------')	#60個

f = scipy.interpolate.interp1d(x, y)
x1 = np.arange(5, 20)
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

plt.show()

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個




print('---- scipy.optimize --------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt

import scipy

def f(x):
    return x**2 + 15*np.sin(x)
x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x)) 

plt.show()

print('------------------------------------------------------------')	#60個

result = scipy.optimize.minimize(f, x0=0)
print(result.x)

plt.plot(x, f(x))
plt.plot(result.x, f(result.x), "o")

plt.show()



print('------------------------------------------------------------')	#60個


print('---- scipy.stats --------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import scipy

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
plt.plot(x, scipy.stats.norm.pdf(x, 0, 1),
       'r-',lw=1,alpha=0.6,label='mu=0,sigma=1')
plt.plot(x, scipy.stats.norm.pdf(x, 0, 2),
       'b--',lw=1,alpha=0.6,label='mu=0,sigma=2')
plt.plot(x, scipy.stats.norm.pdf(x, 2, 1),
       'g-.',lw=1,alpha=0.6,label='mu=2,sigma=1')
plt.legend()
plt.title("Various Normal PDF")

plt.show()

samples = [9, 3, 27]  
   
desc = scipy.stats.describe(samples)
print(desc)

samples2 = [[1, 3, 27],  
            [3, 4, 6],  
            [7, 6, 3],  
            [3, 6, 8]]  
   
desc = scipy.stats.describe(samples2, axis = 0) 
print(desc)


desc = scipy.stats.describe(samples2, axis = 1) 
print(desc)




print('------------------------------------------------------------')	#60個


print('---- scipy.signal --------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import scipy

t = np.linspace(6, 10, 500)
w = scipy.signal.chirp(t,f0=4,f1=2,t1=5,method='linear')
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel('time in sec)')

plt.show()

img = np.load('scipy_data/digit8.npy')

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
c_digit = scipy.signal.convolve2d(img, edge, 
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
c_digit = scipy.signal.convolve2d(img, sharpen, 
                            boundary="symm",
                            mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("sharpen image")

plt.show()

print('------------------------------------------------------------')	#60個

img = np.load('scipy_data/digit3.npy')
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
    c = scipy.signal.convolve2d(img,filters[i-2],
                          boundary="symm",
                          mode="same")
    plt.imshow(c, cmap="gray")
    plt.axis("off")
    plt.title("filter"+str(i-1))

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import numpy as np
import scipy

A = np.array([[2,3], [5,7]])
B = scipy.linalg.inv(A)
print(B)

A = np.array([[3,8], [4,6]])
B = scipy.linalg.det(A)
print(B)

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = scipy.linalg.solve(a, b)
print(x)





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#傑卡德相似係數 Jaccard Similarity Coefficient

import sys
import numpy as np
import scipy.spatial.distance as dist

mat1 = [1,1,0,1,0,1,0,0,1]
mat2 = [0,1,1,0,0,0,1,1,1]
mat3 = [1,1,0,1,0,1,0,0,1]  #the same as mat1
mat4 = [0,0,1,0,1,0,1,1,0]  #invert of mat1

matV = np.mat([mat1,mat4])
print(type(matV))
print(matV)
print('dist.jaccard : ')
print(dist.pdist(matV, 'jaccard'))

print('------------------------------------------------------------')	#60個

'''



print('---- scipy.stats.norm --------------------------------------------------------')	#60個

import numpy as np
#from scipy.stats import norm
import scipy

#MH采样

data = np.random.randn(200)
print('平均 :', np.mean(data))

def sampler(data, samples=100, mu_init=0.2, proposal_width=0.1, plot=False, mu_prior_mu=0, mu_prior_sd=1.):
    mu_current = mu_init
    posterior = [mu_current]
    for i in range(samples):
        mu_proposal = scipy.stats.norm(mu_current, proposal_width).rvs()


        likelihood_current = scipy.stats.norm(mu_current, 1).pdf(data).prod()
        likelihood_proposal = scipy.stats.norm(mu_proposal, 1).pdf(data).prod()
   
        prior_current = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_current)
        prior_proposal = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_proposal)
        
        p_current = likelihood_current * prior_current
        p_proposal = likelihood_proposal * prior_proposal

        p_accept = p_proposal / p_current

        accept = np.random.rand() < p_accept
        
     
        if accept:
            # Update position
            mu_current = mu_proposal
            posterior.append(mu_current)
        
        
        
    return posterior



tt = sampler(data, samples=5)
print(tt)




print('------------------------------------------------------------')	#60個





