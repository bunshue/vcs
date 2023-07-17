import pandas as pd
# 讀取資料
df = pd.read_csv('customer.csv')
# 資料基本清理
df_sample = df.copy()
df_sample['age'] = df_sample['age'].fillna(value=df_sample['age'].mean())
df_sample['gender'] = df_sample['gender'].fillna(method='ffill')
df_sample['area'] = df_sample['area'].fillna(method='ffill')

# 去除重覆記錄
df_sample.drop_duplicates(subset='id', keep='first', inplace=True)
print(df_sample.head())

# 去除欄位中的空白
df_sample['job'] = df_sample['job'].str.strip()
df_sample['job'] = df_sample['job'].str.replace(' ', '')
print(df_sample.head())

# 轉換值的格式
df_sample['age'] = df_sample['age'].astype('int32')
print(df_sample.head())