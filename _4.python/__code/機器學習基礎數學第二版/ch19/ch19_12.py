# ch19_12.py
import numpy as np
import statistics as st
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print(f"Numpy模組母體變異數  : {np.var(x):6.2f}")
print(f"Numpy模組樣本變異數  : {np.var(x,ddof=1):6.2f}")
print(f"Statistics母體變異數 : {st.pvariance(x):6.2f}")
print(f"Statistics樣本變異數 : {st.variance(x):6.2f}")


