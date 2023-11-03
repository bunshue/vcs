import numpy as np
from scipy import stats

observed = np.array([20, 16, 34, 40, 38, 32])
expected = np.array([30, 30, 30, 30, 30, 30])

df = len(observed) - 1
print("自由度:", df)
chi_squared_stat = (((observed-expected)**2)/expected).sum()
print("卡方檢定統計量:", chi_squared_stat)

chi_squared, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
print(chi_squared, p_value)

crit = stats.chi2.ppf(q = 0.95, df=df)
print("臨界區: ", crit)
