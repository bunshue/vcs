import pandas as pd
# 讀取資料
df = pd.read_csv('customer.csv')
# 資料基本清理
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=df_sample['age'].mean())
df_sample['gender'] = df_sample['gender'].fillna(method='ffill')
df_sample['area'] = df_sample['area'].fillna(method='ffill')
df_sample.drop_duplicates(subset='id', keep='first', inplace=True)
df_sample['job'] = df_sample['job'].str.strip()
df_sample['job'] = df_sample['job'].str.replace(' ', '')
df_sample['age'] = df_sample['age'].astype('int32')

#客戶中男女生的平均年齡
print(df_sample.groupby('gender')['age'].mean())
print('-'*30)

#客戶中住各區的人數
print(df_sample.groupby('area')['id'].count())
print('-'*30)

#客戶中男女生的平均年齡、最年長及最年輕的年齡
print(df_sample.groupby('gender')['age'].agg(['mean', 'max', 'min']))