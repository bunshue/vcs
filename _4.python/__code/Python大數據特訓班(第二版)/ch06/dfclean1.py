import pandas as pd
# 讀取資料
df = pd.read_csv('customer.csv')
# 空值的處理
print('各個欄位有空值的狀況:')
print(df.isnull().sum())
print('有空值的記錄筆數:', df.isnull().any(axis=1).sum())
print('有空值的欄位數:', df.isnull().any(axis=0).sum())
print('age欄有空值的記錄:')
print(df[df['age'].isnull()])