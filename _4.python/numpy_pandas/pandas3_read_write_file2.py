import sys
import pandas as pd
import numpy as np

def format_data(df):
    #用missing填充缺失值，并去除首尾空格
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("missing")
            df[column]=df[column].apply(lambda x: x.strip())


    #清洗數據：將位置只保留省份，面料只保留第一個
    #df["銷量"]=df["銷量"].apply(lambda x: int(x.replace("人付款","")))
    df["位置"]=df["位置"].apply(lambda x: x.split(" ")[0])
    df["面料"]=df["面料"].apply(lambda x: x.split(",")[0])
    
    return df

df = pd.read_csv('data/dress.csv')
# print (df.head())

#刪除缺失值個數>100的列
for column in df.columns:
    isnullList=df[column].isnull()
    nullCnt = (len(isnullList[isnullList==True]))
    if nullCnt > 100:
        del df[column]
#         print ("del column:" + column)

#刪除不重要的特征
del df["貨號"]
del df["年份季節"]
del df["品牌"]
del df["銷量"]

df = format_data(df)

print('aaaaaaaaaaaaaaaaaaaaaaaaa')
print(df)
sys.exit()


