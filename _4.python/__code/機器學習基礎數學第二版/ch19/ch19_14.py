# ch19_14.py
import numpy as np
import statistics as st

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
print(f"Numpy模組母體標準差  : {np.std(x):6.2f}")
print(f"Numpy模組樣本標準差  : {np.std(x,ddof=1):6.2f}")
print(f"Statistics母體標準差 : {st.pstdev(x):6.2f}")
print(f"Statistics樣本標準差 : {st.stdev(x):6.2f}")


