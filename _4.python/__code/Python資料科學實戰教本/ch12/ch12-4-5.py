import numpy as np
from scipy import stats
import math

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均:", sum(population)/10000.0)
  
sample_size = 20
sample = np.random.choice(a=population, size=sample_size)    

sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev/math.sqrt(sample_size-1)
print("樣本計算出的母體標準差:", sigma)
t_critical = stats.t.ppf(q=0.975, df=sample_size-1)
print("t分數:", t_critical)
margin_of_error = t_critical * sigma
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
print(confidence_interval)
conf_int = stats.t.interval(alpha=0.95,
                            df=sample_size-1,
                            loc=sample_mean, 
                            scale=sigma)
print(conf_int[0], conf_int[1])
