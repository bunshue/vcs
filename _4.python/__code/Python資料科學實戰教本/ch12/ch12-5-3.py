import numpy as np
from scipy import stats
import math

population_mean = 500
sample = np.array([502.2, 501.6, 499.8, 502.8,
                   498.6, 502.2, 499.2, 503.4,
                   499.2])  
sample_size = len(sample)
sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev/math.sqrt(sample_size-1)
print("樣本計算出的母體標準差:", sigma)
t_obtained = (sample_mean-population_mean)/sigma
print("檢定統計量:", t_obtained)
print(stats.ttest_1samp(a=sample, popmean=population_mean))

t_critical = stats.t.ppf(q=0.975, df=sample_size-1)
print("t分數:", t_critical)
 