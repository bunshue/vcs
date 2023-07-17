import pandas as pd
# 讀取資料
df = pd.read_csv('customer.csv')
# 將age的空值填入0
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=0)
print(df_sample.head())

# 將age的空值填入平均值
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=df_sample['age'].mean())
print(df_sample.head())

# 以前一個值往下填ffill或後一個值往上填bfill
df_sample['gender'] = df_sample['gender'].fillna(method='ffill')
df_sample['area'] = df_sample['area'].fillna(method='ffill')
print(df_sample.head())

# 刪除不完整的資料
print(df.dropna())