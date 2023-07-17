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

# 篩選女性的資料
print(df_sample[(df_sample['gender'] == 'Female')])

# 篩選男性且大於50歲的資料
print(df_sample[(df_sample['gender'] == 'Male') & (df_sample['age'] > 50)])

# 篩選住在新北市三重區或基隆市中正區的資料
print(df_sample[(df_sample['area'] == '新北市三重區') | (df_sample['area'] == '基隆市中正區')])