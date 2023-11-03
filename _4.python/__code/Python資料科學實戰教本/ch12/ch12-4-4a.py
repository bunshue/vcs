import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
population_mean = sum(population)/10000.0
  
sample_size = 1000
intervals = []
sample_means = []

for sample in range(25):
    sample = np.random.choice(a=population, size=sample_size)    
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    sample_stdev = sample.std()
    sigma = sample_stdev/math.sqrt(sample_size-1)
    z_critical = stats.norm.ppf(q=0.975)
    margin_of_error = z_critical * sigma
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    intervals.append(confidence_interval)

plt.figure(figsize=(9,9))
plt.errorbar(x=np.arange(0.1,25,1),
             y=sample_means,
             yerr=[(top-bot)/2 for top,bot in intervals],
             fmt="o")
plt.hlines(xmin=0, xmax=25,
           y=population_mean,linewidth=2.0,color="red")
plt.show()