# DataFrame 測試

import sys
import pandas as pd
import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd

idx = ['1','2','3','4','5','6','7','8','9','10','11','12']

column = ['中文名','英文名','體重','全名']

animals = [['鼠', 'mouse', 3, '米老鼠'],
           ['牛', 'ox', 48, '班尼牛'],
           ['虎', 'tiger', 33, '跳跳虎'],
           ['兔', 'rabbit', 8, '彼得兔'],
           ['龍', 'dragon', 38, '逗逗龍'],
           ['蛇', 'snake', 16, '貪吃蛇'],
           ['馬', 'horse', 36, '草泥馬'],
           ['羊', 'goat', 29, '喜羊羊'],
           ['猴', 'monkey', 22, '山道猴'],
           ['雞', 'chicken', 6, '肯德雞'],
           ['狗', 'dog', 12, '貴賓狗'],
           ['豬', 'pig', 42, '佩佩豬']]

print(type(animals))
print(type(animals[1]))

sys.exit()

df = pd.DataFrame(animals, index = idx, columns = column )

print(df)

print('df的方法')
print(df.shape)
print(df.columns)
print(df.index)
print(df.head())
print(df.describe())
print(df.info())
print(df.duplicated())

filename = '動物資料0.csv'
df.to_csv(filename)  #預設為 儲存index行

filename = '動物資料1.csv'
df.to_csv(filename, index = False)  #不儲存index行

filename = '動物資料2.csv'
df.to_csv(filename, index = True)   #儲存index行

for i in range(12):
    print('index :', i, end = '\t')
    print('中文名 :', df.iloc[i, 0], end = '\t')
    print('體重 :', df.iloc[i, 2], end = '\n')

print('全名(第3欄)')
print(df.iloc[0:12, 3])

print('全名(部分)')
print(df.iloc[[3, 6, 9, 11], 3])

print('排序')
df1 = df.sort_values('體重')
print(df1.head())

print('最重 :', df['體重'].max())
print('最輕 :', df['體重'].min())
print('總重 :', df['體重'].sum())
print('平均 :', df['體重'].mean())



print('------------------------------------------------------------')	#60個



df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]])
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index = ['王小明','李小美','陳大同','林小玉'],
                   columns = ['國文','英文','數學','自然','社會'])
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

#字典
scores = {'王小明':{'國文':65,'英文':92,'數學':78,'社會':83,'自然':70},
          '李小美':{'國文':90,'英文':72,'數學':76,'社會':93,'自然':56},
          '陳大同':{'國文':81,'英文':85,'數學':91,'社會':89,'自然':77},
          '林小玉':{'國文':79,'英文':53,'數學':47,'社會':94,'自然':80}}
df = pd.DataFrame(scores)
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

#字典
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
print(type(scores))
print(scores)
df = pd.DataFrame(scores)
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})

df = pd.concat([se1,se2,se3,se4,se5], axis = 0)
df.columns = ['國文','英文','數學','自然','社會']
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})

df = pd.DataFrame({'國文':se1, '英文':se2, '數學':se3, '自然':se4, '社會':se5})
print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

#字典
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
print(df['自然'])
print(df[['國文', '數學', '自然']])
print(df[df['國文'] >= 80])
print(df.values)
print(df.values[1])
print(df.values[1][2])
# loc
print(df.loc['林小玉', '社會'])
print(df.loc['王小明', ['國文', '社會']])
print(df.loc[['王小明', '李小美'], ['數學', '自然']])
print(df.loc['王小明' : '陳大同', '數學' : '社會'])
print(df.loc['陳大同', :])
print(df.loc[:'李小美', '數學' : '社會'])
print(df.loc['李小美':, '數學' : '社會'])
print(df.iloc[3, 4])
# iloc
df.iloc[0, [0, 4]]
df.iloc[[0, 1], [2, 3]]
df.iloc[0:3, 2:5]
df.iloc[2, :]
df.iloc[:2, 2:5]
df.iloc[1:, 2:5]
# head() tail()
df.head(2)
df.tail(2)

print('------------------------------------------------------------')	#60個

#字典
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)

print('原資料 :\n', df, '\n')

# 排序
print(df.sort_values(by = '數學', ascending = False))
print(df.sort_index(axis = 0))
# 修改
df1 = df.loc['王小明']['數學'] = 90

print('修改後的資料 :\n', df, '\n')

df2 = df.loc['王小明', :] = 80

print('修改後的資料 :\n', df, '\n')

# 刪除
df.drop('王小明')
df.drop('數學', axis = 1)
df.drop(['數學', '自然'], axis = 1)
df.drop(df.index[1:4])
df.drop(df.columns[1:4], axis = 1)

print('修改後的資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]

df = pd.DataFrame(datas, columns = columns, index = indexs)

print('原資料 :\n', df, '\n')

print('按照數學遞減排序 ->')
df1 = df.sort_values(by = '數學', ascending = False)
print(df1)
print()

print('按照列標題遞增排序 ->')
df2 = df.sort_index(axis = 0)
print(df2)
print()

print('------------------------------------------------------------')	#60個

datas = [['mouse', 3], ['ox', 48], ['tiger', 33], ['rabbit', 8]]
indexs = ['鼠', '牛', '虎', '兔']
columns = ['英文名', '體重']

df = pd.DataFrame(datas, columns = columns, index = indexs)

print('原資料 :\n', df, '\n')

print('按照數學遞減排序 ->')
df1 = df.sort_values(by = '體重', ascending = False)
print(df1)
print()

print('按照列標題遞增排序 ->')
df2 = df.sort_index(axis = 0)
print(df2)
print()

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns)
df.plot(xticks=range(0,4))

plt.show()

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('最前 2 位學生成績 ->')
print(df.head(2))
print()
print('最後 2 位學生成績 ->')
print(df.tail(2))

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.iloc[1, :] ->')
print(df.iloc[1, :])
print()
print('df.iloc[1][1] ->')
print(df.iloc[1][1])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.loc["陳聰明", :] ->')
print(df.loc["陳聰明", :])
#print(df.loc["陳聰明"])
print()
print('df.loc["陳聰明"]["數學"] ->')
print(df.loc["陳聰明"]["數學"])
print()
print('df.loc[("陳聰明", "熊小娟") ->')
print(df.loc[("陳聰明", "熊小娟"), :])
print()
print('df.loc[:, "數學"] ->')
print(df.loc[:, "數學"])
print()
print('df.loc[("陳聰明", "熊小娟"), ("數學", "自然")] ->')
print(df.loc[("陳聰明", "熊小娟"), ("數學", "自然")])
print()
print('df.loc["陳聰明":"熊小娟", "數學":"社會"] ->')
print(df.loc["陳聰明":"熊小娟", "數學":"社會"])
print()
print('df.loc[:黃美麗, "數學":"社會"] ->')
print(df.loc[:"黃美麗", "數學":"社會"])
print()
print('df.loc["陳聰明":, "數學":"社會"] ->')
print(df.loc["陳聰明":, "數學":"社會"])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df["自然"] ->')
print(df["自然"])
print()
print('df[["國文", "數學", "自然"] ->')
print(df[["國文", "數學", "自然"]])
print()
print('df[df.數學>=80] ->')
print(df[df.數學 >= 80])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print("df.values：")
print(df.values)
print("陳聰明的成績(df.values[1])：")
print(df.values[1])
print("陳聰明的英文成績(df.values[1][2])：")
print(df.values[1][2])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.loc["陳聰明"]["數學"] (原始)：' + str(df.loc["陳聰明"]["數學"]))
df.loc["陳聰明"]["數學"] = 91
print('df.loc["陳聰明"]["數學"] (修改)：' + str(df.loc["陳聰明"]["數學"]))
print()
print('df.loc["陳聰明", :] ->')
df.loc["陳聰明", :] = 80
print(df.loc["陳聰明", :])

print('------------------------------------------------------------')	#60個

df = pd.DataFrame( {"林大明":[65,92,78,83,70], "陳聰明":[90,72,76,93,56], \
    "黃美麗":[81,85,91,89,77], "熊小娟":[79,53,47,94,80] } )

print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('移除陳聰明成績 ->')
df1 = df.drop("陳聰明")
print(df1)
print()
print('移除數學科成績 ->')
df2 = df.drop("數學", axis=1)
print(df2)
print()
print('移除數學科及自然科成績 ->')
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)
print()
print('移除陳聰明到熊小娟成績 ->')
df4 = df.drop(df.index[1:4])
print(df4)
print()
print('移除數學科到自然科成績 ->')
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
print()

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
indexs[0] = "林晶輝"
df.index = indexs
columns[3] = "理化"
df.columns = columns

print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個

#字典
fruits = {"蘋果": [4, 3, 1, 0],
          "香蕉": [0, 4, 6, 2],
          "橘子": [1, 5, 2, 4]}

print(type(fruits))
print(fruits)

df = pd.DataFrame(fruits)

print('原資料 :\n', df, '\n')

print('前3項')
print(df.head(3))   #前3項

print('後2項')
print(df.tail(2))   #後2項

print('------------------------------------------------------------')	#60個

'''
df.to_csv("fruits.csv",index=False,encoding="utf8")
df.to_json("fruits.json")

df2 = pd.read_csv("fruits.csv", encoding="utf8")
df2 = pd.read_json("fruits.json")
print(df2)

for index, row in df.iterrows() :
    print(index, row["蘋果"], row["香蕉"],
          row["橘子"])

'''

print('------------------------------------------------------------')	#60個

sales = [11.22,23.50,12.99,15.95,25.75,11.55]

df = pd.DataFrame(sales)    #串列 轉 DataFrame

print(df.describe())
print(df.count())
print(df.median())
print(df.mean())
print(df.min())
print(df.max())
print(df.std())

print('------------------------------------------------------------')	#60個

print('DataFrame格式的範例')

df = pd.DataFrame({
    "姓名": ["Alice", "Bob", "Charlie"],
    "分數": [78, 65, 90]
})

print('原資料 :\n', df, '\n')

print('------------------------------------------------------------')	#60個





