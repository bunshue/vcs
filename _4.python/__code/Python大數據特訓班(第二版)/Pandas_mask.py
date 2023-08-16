'''
Pandas資料應用專題

健保藥局查詢程式

【口罩何處尋？ 健保藥局查詢程式】
相關資料網頁

    健保特約機構口罩剩餘數量明細清單
    https://data.nhi.gov.tw/Datasets/DatasetDetail.aspx?id=656&Mid=A111088
    健保特約醫事機構-藥局
    https://data.nhi.gov.tw/Datasets/DatasetDetail.aspx?id=329&Mid=A111068
    
'''

print('Pandas資料讀取與顯示')

import pandas as pd

df = pd.read_csv('https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001')

# df.head()
# df.tail()
# df.head(10)
df[['醫事機構名稱','電話','地址','備註']].tail(10)

print('Pandas資料排序')

# df1 = df[['醫事機構名稱','電話','地址','備註']]
df1.sort_values(['地址', '電話'], ascending=[True, False])

print('Pandas資料篩選')

mask = df1['地址'].str.startswith("苗栗縣")
df1[mask]

print('Pandas 新增欄位(columns)')

df1.insert(1, "縣市", df1['地址'].str.slice(0,3,1))
df1.insert(2, "地區", df1['地址'].str.slice(3,6,1))

df1

print('Pandas 資料統計')

df2 = df1[['醫事機構名稱','縣市']].groupby('縣市').count()
df2.columns=['總計']
df2.sort_values('總計', ascending=False)

print('口罩何處尋 健保藥局查詢程式')

import pandas

# df = pd.read_csv('https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001')

df1 = df[['醫事機構名稱','電話','地址','備註']]

keyword = input('請輸入查詢縣市：')

if keyword != '':
    mask = df1['地址'].str.startswith(keyword.replace('台', '臺'))
    if len(df1[mask]) > 0:
        display(df1[mask])
    else:
        print('請輸入正確資料！')
else:
    print('請重新輸入查詢縣市資料')
    
