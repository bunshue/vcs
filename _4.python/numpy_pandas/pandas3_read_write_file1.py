"""
使用pandas讀寫檔案
1111. csv檔
2222. json
3333. excel
4444. html與其他


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print('---- 1111 csv --------------------------------------------------------')	#60個

print('pandas DataFrame資料輸出到csv檔')

scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)

print("另存新檔");
filename = 'C:/_git/vcs/_1.data/______test_files2/score_this.csv'
df.to_csv(filename, encoding = 'utf-8-sig')
print("寫入完成")

print('------------------------------------------------------------')	#60個

print('pandas 讀取 csv檔')

print("讀取 .csv 檔 1")
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv'
na = np.genfromtxt(filename, delimiter = ',', skip_header = 1)
print("資料寬高")
print(na.shape)

print('國文最高分數：', na[:,1].max())
print('英文最低分數：', na[:,2].min())
print('數學平均分數：', na[:,3].mean())
total1 = na[:,1] + na[:,2] + na[:,3]
print(total1)
print('全班最高總分：',total1.max())

total2 = na[:,1:4].sum(axis=1)
print(total2)
print('全班最高總分：',total2.max())

print('------------------------------------------------------------')	#60個
print('pandas 讀取 csv檔')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores2.csv'
data = pd.read_csv(filename, header=0, index_col=0)
print('打印資料')
print(data)
#print('打印資料型態')
#print(type(data))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files2/score333.csv'

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_csv(filename, encoding="utf-8-sig")

print('------------------------------------------------------------')	#60個

data = pd.read_csv(filename, encoding="utf-8-sig",index_col=0)

print(data)

print('------------------------------------------------------------')	#60個

df = pd.read_csv("http://bit.ly/gradescsv")

print(df.head())

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/grades.csv')

print(df.head())

print(df["國文"])


print(df.國文)


cg = df.國文.values


print(cg)


print(cg.mean())

print(cg.std())


df.國文.plot()
plt.show()


df.國文.hist(bins = 15)
plt.show()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/grades.csv')

print(df.head())

#print(df["國文"])

print(df.國文.mean())
print(df.國文.std())
print(df.describe())    #顯示統計資料
print('係數矩陣 :', df.corr())

#只算兩科間的相關係數當然也可以。
print(df.國文.corr(df.數學))

df["總級分"] = df[["國文", "英文", "數學", "社會", "自然"]].sum(1)
print(df.head())

df["主科"] = df.數學*1.5 + df.英文

print(df.head())

print(df.sort_values(by = "總級分", ascending = False).head(20))

print(df.sort_values(by = ["主科", "總級分"], ascending = False).head(20))

print('------------------------------------------------------------')	#60個

def format_data(df):
    #用missing填充缺失值，並去除首尾空格
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

print('------------------------------------------------------------')	#60個

print('用 Groupby 看美國哪裡最容易看到 UFO')
df = pd.read_csv("http://bit.ly/uforeports")

print(df.head())


df_state = df.groupby("State").count()

print(df_state)

df_state.sort_values(by = "Time", ascending = False)


print(df_state)


df_state.sort_values(by = "Time", ascending = False, inplace = True)

print(df_state.head(10))

df_state[:10].Time.plot(kind = 'bar')

plt.show()

print('------------------------------------------------------------')	#60個

print('---- 2222 json --------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files2/score444.json'

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_json(filename, force_ascii=False)

print('------------------------------------------------------------')	#60個

data = pd.read_json(filename, typ='series')

print(data)

print('------------------------------------------------------------')	#60個




print('---- 3333 excel --------------------------------------------------------')	#60個



filename = 'C:/_git/vcs/_1.data/______test_files2/score555.xlsx'

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_excel(filename, encoding="utf-8-sig")


print('------------------------------------------------------------')	#60個

data = pd.read_excel(filename, encoding="utf-8-sig",index_col=0)

print(data)


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_excel/python_ReadWrite_EXCEL4.xlsx'

print('讀取xlsx檔')
df = pd.read_excel(filename)

header = df.iloc[2]  #取得標題
df1 = df[3:].copy()  #去除前三列
df1 = df1.rename(columns = header)  #重置標題
df2 = df1.drop(columns=['縣市代碼', '村里代碼', '村里名稱', '村里代碼'], axis=1)  #去除四行資料
df3 = df2.drop_duplicates()  #移除重複資料

filename = 'C:/_git/vcs/_1.data/______test_files2/district.csv'

print('寫出到csv檔')
df3.to_csv(filename, encoding = 'big5', index = False)


print('------------------------------------------------------------')	#60個


print('---- 4444 html與其他 --------------------------------------------------------')	#60個

print("使用pandas讀取網頁表單");
    
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)

print("結果");
print(tables[0])

print('------------------------------------------------------------')	#60個

#原物料商品行情
tables = pd.read_html("http://www.stockq.org/market/commodity.php")

n = 1
for table in tables:
    print("第 " + str(n) + " 個表格：")
    print(table.head())
    print()
    n += 1

print('------------------------------------------------------------')	#60個

#原物料商品行情
tables = pd.read_html("http://www.stockq.org/market/commodity.php")

print(tables)

"""
table = tables[7]
table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))

print(table)
"""
print('------------------------------------------------------------')	#60個

#由網址讀取資料檔

url='https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
df = pd.read_html(url)
print(df)

print('------------------------------------------------------------')	#60個

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 

df.to_csv("vehicles.csv",index=False,encoding="big5")

df.to_json("vehicles1.json")
df.to_json("vehicles2.json", force_ascii = False)

"""
#匯出DataFrame
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(table, con = engine)

#匯入DataFrame
df.read_csv(filename)
df.read_json(filename)
df.read_html(filename)
df.read_excel(filename)
df.read_sql(query, engine)
"""

df1 = pd.read_csv("vehicles.csv", encoding="big5")
df2 = pd.read_json("vehicles.json")
print(df1)
print(df2)

print('------------------------------------------------------------')	#60個

# pip install xlsxwriter

#data = pd.read_csv('data/ExpensesRecord.csv')
df = pd.read_excel('data/ExpensesRecord.xls', 'sheet')
#data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head(5) )

from pandas import ExcelWriter

writer = ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')
writer.save()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/ExpensesRecord.csv')
print(df.head(5) )
df.to_csv("test.csv")

print('------------------------------------------------------------')	#60個

"""
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0].head(5) )

#df = pd.read_html('http://news.baidu.com/tech')
#print(df[0].head(5) )
"""

print('------------------------------------------------------------')	#60個

DataFrame = pd.read_csv('data/ExpensesRecord.csv')
print(DataFrame["說明"])
print(DataFrame[["說明","支出金額"]] )

df = pd.DataFrame({'Math': [90, 91,92, 93, 94],'English': np.arange(80,85,1) })
print(df[["Math","English"]])

print('------------------------------------------------------------')	#60個

DataFrame = pd.read_csv('data/ExpensesRecord.csv')
DataFrame["單價"]=DataFrame["支出金額"]/DataFrame["數量"]
print(DataFrame[["數量","支出金額","單價"]] )

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df['Date'] == '2018-01-05')
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

print('------------------------------------------------------------')	#60個

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'
print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
print(df[df['Open'] > 194.2])
print(df[['Date','Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())

#  5 matplotlib
df.plot(x='Date', y='Open',grid=True, color='blue')
plt.show()

df.plot( y='diff',grid=True, color='red',kind='hist')
plt.show()

fig, ax = plt.subplots()
for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
plt.show()

fileds=['Open','Close','High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
plt.show()

dfMonths = df.loc[df['month'].isin([1,2,3,4,5,6,7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values = 'High', columns = 'month', index = 'day')
dfMonthsPivot.plot(kind = 'box',title = 'Months High')
plt.show()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

print('用pandas讀取csv檔, 並分析之')
# 讀入csv檔
filename = "data/python_ReadWrite_CSV7_onigiri.csv"
dat = pd.read_csv(filename, encoding="UTF-8")

print(type(dat))
print(dat)

bins=range(0, 200, 10)
for b in bins:
    print(b)

print("計算平均數、變異數、標準差")

print("店長---------")
print("平均:", np.mean(dat["店長"]))
print("變異數:", np.var(dat["店長"]))
print("標準差:", np.std(dat["店長"]))

print("太郎---------")
print("平均:", np.mean(dat["太郎"]))
print("變異數:", np.var(dat["太郎"]))
print("標準差:", np.std(dat["太郎"]))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個



