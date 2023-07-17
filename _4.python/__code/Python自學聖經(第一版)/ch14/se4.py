import pandas as pd
dict1 = {'Taipei': '台北', 'Taichung': '台中', 'Kaohsiung': '高雄'}
se = pd.Series(dict1)
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引
print(se['Taipei']) #用索引取值
print(se['Taichung':'Kaohsiung'])