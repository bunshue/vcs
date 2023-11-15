"""
使用pandas讀寫檔案
1111. csv檔
2222. json
3333. excel
4444. html與其他


"""



import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('---- 1111 csv --------------------------------------------------------')	#60個
'''
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
'''



import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


'''
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
'''

print('------------------------------------------------------------')	#60個


#由網址讀取資料檔

import pandas as pd
url='https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
df = pd.read_html(url)
print(df)


print('------------------------------------------------------------')	#60個



