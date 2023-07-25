# se1.py
import pandas as pd
se = pd.Series([1,2,3,4])
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引

# se2.py
import pandas as pd
dict1 = {'a': 100, 'b': 200, 'c': 300}
se = pd.Series(dict1)
print(se)           #顯示Series
print(se.values)    #顯示值
print(se.index)     #顯示索引



# se3.py
import pandas as pd
se = pd.Series([1,2,3,4,5])
print(se[2])
print('-' * 6)
print(se[2:5])

# df1.py
import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]])
print(df)

# df2.py
import pandas as pd
df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]],
                   index=['王小明','李小美','陳大同','林小玉'],
                   columns=['國文','英文','數學','自然','社會'])
print(df)

# df3.py
import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
print(df)

# df4.py
import pandas as pd
se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
df = pd.DataFrame({ '國文':se1,'英文':se2,'數學':se3,'自然':se4,
							 '社會':se5} )
print(df)

# df5.py
import pandas as pd
se1 = pd.Series({'王小明':65,'李小美':90,'陳大同':81,'林小玉':79})
se2 = pd.Series({'王小明':92,'李小美':72,'陳大同':85,'林小玉':53})
se3 = pd.Series({'王小明':78,'李小美':76,'陳大同':91,'林小玉':47})
se4 = pd.Series({'王小明':83,'李小美':93,'陳大同':89,'林小玉':94})
se5 = pd.Series({'王小明':70,'李小美':56,'陳大同':94,'林小玉':80})
df = pd.concat([se1,se2,se3,se4,se5], axis=1)
df.columns=['國文','英文','數學','自然','社會']
print(df)

# df6.py
import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
print(df["自然"])
print(df[["國文", "數學", "自然"]])
print(df[df["國文"] >= 80])
print(df.values)
print(df.values[1])
print(df.values[1][2])
# loc
print(df.loc["林小玉", "社會"])
print(df.loc["王小明", ["國文","社會"]])
print(df.loc[["王小明", "李小美"], ["數學", "自然"]])
print(df.loc["王小明":"陳大同", "數學":"社會"])
print(df.loc["陳大同", :])
print(df.loc[:"李小美", "數學":"社會"])
print(df.loc["李小美":, "數學":"社會"])
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



# df7.py
import pandas as pd
scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)
# 排序
print(df.sort_values(by="數學", ascending=False))
print(df.sort_index(axis=0))
# 修改
df1 = df.loc["王小明"]["數學"] = 90
print(df)
df2 = df.loc["王小明", :] = 80
print(df)
# 刪除
df.drop("王小明")
df.drop("數學", axis=1)
df.drop(["數學", "自然"], axis=1)
df.drop(df.index[1:4])
df.drop(df.columns[1:4], axis=1)

# read_csv.py
import pandas as pd
data = pd.read_csv("scores2.csv", header=0, index_col=0)
print(data)
print(type(data))


# read_html.py
import pandas as pd
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])


# to_csv.py
import pandas as pd
scores = {' 國文':{' 王小明':65,' 李小美':90,' 陳大同':81,' 林小玉':79},
          ' 英文':{' 王小明':92,' 李小美':72,' 陳大同':85,' 林小玉':53},
          ' 數學':{' 王小明':78,' 李小美':76,' 陳大同':91,' 林小玉':47},
          ' 自然':{' 王小明':83,' 李小美':93,' 陳大同':89,' 林小玉':94},
          ' 社會':{' 王小明':70,' 李小美':56,' 陳大同':94,' 林小玉':80}}
df = pd.DataFrame(scores)
df.to_csv('scores3.csv', encoding='utf-8-sig')


# pd_plot1.py
import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB

plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
g1 = df.plot(kind='bar', title='長條圖', figsize=[10,5])
g2 = df.plot(kind='barh', title='橫條圖', figsize=[10,5])
g3 = df.plot(kind='bar', stacked=True, title='堆疊圖', figsize=[10,5])




# pd_plot2.py
import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
g1 = df.iloc[0].plot(kind='line', legend=True, xticks=range(2015,2020), title='公司分區年度銷售表', figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True, xticks=range(2015,2020))
g1 = df.iloc[2].plot(kind='line', legend=True, xticks=range(2015,2020))



# pd_plot3.py
import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
df.plot(kind='pie', subplots=True, figsize=[20,20])


# dfclean1.py
import pandas as pd
# 讀取資料
df = pd.read_csv('customer.csv')
# 空值的處理
print('各個欄位有空值的狀況:')
print(df.isnull().sum())
print('有空值的記錄筆數:', df.isnull().any(axis=1).sum())
print('有空值的欄位數:', df.isnull().any(axis=0).sum())
print('age欄有空值的記錄:')
print(df[df['age'].isnull()])


# dfclean2.py
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



# dfclean3.py
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

# dffilter.py
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



# dfgroupby.py
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




















