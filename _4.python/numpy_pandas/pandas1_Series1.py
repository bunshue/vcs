import pandas as pd

print('------------------------------------------------------------')	#60個

se = pd.Series([1,2,3,4,5])
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引

print('------------------------------------------------------------')	#60個

se = pd.Series([1,2,3,4,5])
print(se[2])
print(se[2:5])

print('------------------------------------------------------------')	#60個

se = pd.Series(['a','b','c','d','e'])
print(se[1:3])

print('------------------------------------------------------------')	#60個

se = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(se)
print(se['b'])
print(se['c':'d'])

print('------------------------------------------------------------')	#60個

dict1 = {'Taipei': '台北', 'Taichung': '台中', 'Kaohsiung': '高雄'}
se = pd.Series(dict1)
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引
print(se['Taipei']) #用索引取值
print(se['Taichung':'Kaohsiung'])

print('------------------------------------------------------------')	#60個



