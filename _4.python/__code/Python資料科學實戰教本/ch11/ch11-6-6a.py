from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

x = [x/10.0 for x in range(-50, 60)]
plt.plot(x, stats.norm.pdf(x, 0, 1),
       'r-', lw=1, alpha=0.6, label='mu=0,sigma=1')
plt.plot(x, stats.norm.pdf(x, 0, 2),
       'b--', lw=1, alpha=0.6, label='mu=0,sigma=2')
plt.plot(x, stats.norm.pdf(x, 2, 1),
       'g-.', lw=1, alpha=0.6, label='mu=2,sigma=1')
plt.legend()
plt.title("常態分配PDF的機率")
plt.show()
