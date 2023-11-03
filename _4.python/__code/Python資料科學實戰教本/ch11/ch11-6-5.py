from scipy import stats

n = 5
p = 1/6
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)
