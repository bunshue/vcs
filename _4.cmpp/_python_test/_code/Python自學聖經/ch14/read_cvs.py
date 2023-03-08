import pandas as pd

data = pd.read_csv("scores2.csv", header=0, index_col=0)
print('打印資料')
print(data)
print('打印資料型態')
print(type(data))
