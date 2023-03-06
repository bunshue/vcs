import pandas as pd
se = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(se)
print(se['b'])
print(se['c':'d'])