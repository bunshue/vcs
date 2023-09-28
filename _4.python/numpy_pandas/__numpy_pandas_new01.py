'''
numpy的使用

'''
import numpy as np

print('------------------------------------------------------------')	#60個

x = np.array( [[40, 70, 25], [75, 80, 65], [80, 90, 100]])

print(x.shape)
print(x)

y = x.reshape(1,9)
print(y.shape)
print(y)

y = x.ravel()
print(y.shape)
print(y)

print('------------------------------------------------------------')	#60個

m = np.random.randn(100)
print(m.shape)
m = m.reshape(10,10)
print(m.shape)

print('------------------------------------------------------------')	#60個

import pandas as pd

df = pd.read_csv("http://bit.ly/gradescsv")

print(df.head())

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



