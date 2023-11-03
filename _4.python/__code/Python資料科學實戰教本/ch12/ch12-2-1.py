import numpy as np
from scipy.stats import norm
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

sigma = 1
mu = 0
x = np.linspace(-10, 10, 1000)
dist = norm(mu, sigma)
plt.plot(x, dist.pdf(x), ls="-", c="black",
            label="mu=0,sigma=1")
plt.xlim(-5, 5)
plt.ylim(0, 0.45)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("標準常態分配(Standard Normal Distribution)")
plt.legend()
plt.show()