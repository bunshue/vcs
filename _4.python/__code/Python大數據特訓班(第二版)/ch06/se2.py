import pandas as pd
dict1 = {'a': 100, 'b': 200, 'c': 300}
se = pd.Series(dict1)
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引