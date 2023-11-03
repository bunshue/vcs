from scipy import stats

n = 14
p = 0.2
k = 3
v = stats.binom.pmf(k, n, p)
print(k, v)
 