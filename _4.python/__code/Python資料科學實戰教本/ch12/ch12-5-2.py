import numpy as np
from scipy import stats
import math

population_mean = 70
sample_size = 100
sample_mean = 71.5
print("樣本平均:", sample_mean)
sigma = 2.5
print("母體標準差:", sigma)
z_obtained = (sample_mean-population_mean)/(sigma/math.sqrt(sample_size))
print("Z檢定統計量:", z_obtained)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)
 