# ch4_23.py
import pandas as pd

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)
print('資料集長度 : ', len(iris))
print(iris)












