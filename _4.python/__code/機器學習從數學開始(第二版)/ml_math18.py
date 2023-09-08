import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

print('------------------------------------------------------------')	#60個

import random
import math
import matplotlib.pyplot as plt



X = []
Y=[]
for i in range(1000):
    theta = 2 * random.random() * math.pi
    r= random.random() * 5
    x=math.cos(theta)* r +5
    y=math.sin(theta)* r + 5
    X.append(x)
    Y.append(y)




plt.figure(figsize=(6,6))
plt.scatter(X,Y)
len(X)
plt.axis([0, 10, 0, 10])

plt.show()


print('------------------------------------------------------------')	#60個

X = []
Y=[]
for i in range(1000):
    x=random.randint(0,10)+random.random()
    y=random.randint(0,10)+random.random()
    if ((x-5)**2 + (y-5)**2) >25:
        print('Reject ({0},{1})'.format(x,y))
    else :
        X.append(x)
        Y.append(y)
print(len(X))        


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,6))
plt.scatter(X,Y)
print(len(X))
plt.axis([0, 10, 0, 10])

plt.show()


print('------------------------------------------------------------')	#60個

#MH采样

import numpy as np
data = np.random.randn(200)
np.mean(data)


ax = plt.subplot()
sns.distplot(data, kde=False, ax=ax)
_ = ax.set(title='Histogram of observed data', xlabel='x', ylabel='# observations');


plt.show()




print('------------------------------------------------------------')	#60個


from scipy.stats import norm



def sampler(data, samples=100, mu_init=0.2, proposal_width=0.1, plot=False, mu_prior_mu=0, mu_prior_sd=1.):
    mu_current = mu_init
    posterior = [mu_current]
    for i in range(samples):
        mu_proposal = norm(mu_current, proposal_width).rvs()


        likelihood_current = norm(mu_current, 1).pdf(data).prod()
        likelihood_proposal = norm(mu_proposal, 1).pdf(data).prod()
        
   
        prior_current = norm(mu_prior_mu, mu_prior_sd).pdf(mu_current)
        prior_proposal = norm(mu_prior_mu, mu_prior_sd).pdf(mu_proposal)
        
        p_current = likelihood_current * prior_current
        p_proposal = likelihood_proposal * prior_proposal
        

        p_accept = p_proposal / p_current
        

        accept = np.random.rand() < p_accept
        
     
        if accept:
            # Update position
            mu_current = mu_proposal
            posterior.append(mu_current)
        
        
        
    return posterior



tt = sampler(data,samples=5)
print(tt)




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

