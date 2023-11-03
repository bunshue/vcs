from scipy import stats

n = 10
p = 1/2
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)

