import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie",
       figsize=(6, 6),
       explode=explode)
plt.show()