import sys
import pandas as pd
import numpy as np

df = pd.read_csv("data/qunar_routes.csv")
print (df.head())
print (df.info())
print (df)

print('ttttt1')

print(df.路線信息)
print()
print(df.路線信息.str.extract('(\d+)天\d+晚'))

df["天數"]=df.路線信息.str.extract('(\d+)天\d+晚')
print('ttttt2')
df["酒店評分"]=df.酒店信息.str.extract('(\d\.\d)分')
print('ttttt3')
df["酒店等級"]=df.酒店信息.str.extract('\n(.*)')
print('ttttt4')
df["價格"]=df.路線信息.str.extract('(\d+)起/人')
print('ttttt5')
print (df.head())
print (df.info())

print('酒店等級 :', df["酒店等級"])
print('酒店評分 :', df["酒店評分"])
print('價格 :', df["價格"])

class_map = {"其他":0,"經濟型":1,"舒適型":2,"高檔型":3,"豪華型":4}
df["酒店等級"]=df["酒店等級"].map(class_map)


