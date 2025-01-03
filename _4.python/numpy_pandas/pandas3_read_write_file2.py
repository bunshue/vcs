"""
使用pandas讀寫檔案
1111. csv檔
2222. json
3333. excel
4444. html與其他

# 讀取, 匯入DataFrame, 檔案轉df
pd.read_csv(filename)
pd.read_json(filename)
pd.read_html(filename)
pd.read_excel(filename)
pd.read_sql(query, engine)
pd.read_pickle(filename)

# 寫入, 匯出DataFrame, df轉檔案
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)  #df轉html
df.to_excel(filename)
df.to_sql(table, con = engine)
df.to_pickle(filename)
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


def show():
    return
    plt.show()


print("------------------------------------------------------------")  # 60個

print("---- 1111 csv --------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("---- 2222 json --------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)

filename = "tmp_score444.json"
df.to_json(filename, force_ascii=False)
print("df寫入json檔案 :", filename)

print("------------------------------")  # 30個

print("pd讀取json檔案 :", filename)
data = pd.read_json(filename, typ="series")
print(data)

print("------------------------------------------------------------")  # 60個

""" lack file
# 匯入JSON格式的檔案
df2 = pd.read_json("tmp_dists.json")
print(df2)
"""

print("------------------------------------------------------------")  # 60個


print("---- 3333 excel --------------------------------------------------------")  # 60個

print("讀寫Excel文件")

print("df轉excel")
df = pd.DataFrame({"Name": ["Smith", "Lucy"], "Age": ["25", "20"], "Sex": ["男", "女"]})
df.to_excel("tmp_a.xlsx")

print("pd讀取excel")
df1 = pd.read_excel("tmp_a.xlsx")
print(df1)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame({"A": ["foo", "bar", "baz"], "B": [1, 2, 3]})

df.to_excel("tmp_cc.xlsx", index=False)

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)

filename = "tmp_score555.xlsx"
# df.to_excel(filename, encoding="utf-8-sig") fail
df.to_excel(filename)
print("df寫入excel檔案 :", filename)

print("------------------------------")  # 30個

filename = "tmp_score555.xlsx"
print("pd讀取excel檔案 :", filename)
print("跳過索引")
# data = pd.read_excel(filename, encoding="utf-8-sig",index_col=0) fail
data = pd.read_excel(filename, index_col=0)
print(data)

print("------------------------------------------------------------")  # 60個

filename = (
    "C:/_git/vcs/_4.python/write_read_file/_4.office/data/python_ReadWrite_EXCEL4.xlsx"
)
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename)
# print(df)

header = df.iloc[2]  # 取得標題
df1 = df[3:].copy()  # 去除前三列
df1 = df1.rename(columns=header)  # 重置標題
df2 = df1.drop(columns=["縣市代碼", "村里代碼", "村里名稱", "村里代碼"], axis=1)  # 去除四行資料
df3 = df2.drop_duplicates()  # 移除重複資料

print("------------------------------------------------------------")  # 60個

# 多重索引
df = pd.read_excel("data/test.xlsx", header=[0, 1])  # 指定前兩行爲列索引
print(df)
print(df.columns.values)  # 查看列索引內容

df.columns = ["_".join(col).strip() for col in df.columns.values]  # 重置字段名
print(df)

print("------------------------------------------------------------")  # 60個

print("df轉excel")
from sklearn import datasets

print("load_iris()轉df")

iris = datasets.load_iris()
X = iris.data
y = iris.target  # 資料集目標

import xlsxwriter

df = pd.DataFrame(X, columns=iris.feature_names)

df["target"] = y

print(df)

writer = pd.ExcelWriter("tmp_iris.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer.close()

print("------------------------------------------------------------")  # 60個

print("df轉excel")
from sklearn import datasets

diabetes = datasets.load_diabetes()

import xlsxwriter

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

df["target"] = diabetes.target

writer = pd.ExcelWriter("tmp_diabetes.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer._save()

print("------------------------------------------------------------")  # 60個

# 將 糖尿病 資料 儲存成 csv/excel 檔案

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

import xlsxwriter

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

df["target"] = diabetes.target

print(df.head())
df.to_csv("tmp_diabetes.csv", sep="\t")

writer = pd.ExcelWriter("tmp_diabetes.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer._save()

print("------------------------------------------------------------")  # 60個

# pip install xlsxwriter

# print("pd讀取csv檔案 :", filename)
# data = pd.read_csv('data/ExpensesRecord.csv')

filename = "data/ExpensesRecord.xls"
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, "sheet")

# url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
# print("pd讀取html檔案 :", url)
# data = pd.read_html(url)

print(df.head(5))

from pandas import ExcelWriter

filename = "tmp_test.xlsx"
writer = ExcelWriter(filename, engine="xlsxwriter")
df.to_excel(writer, sheet_name="sheet2")
writer.save()

print("df寫入excel檔案 :", filename)

print("------------------------------------------------------------")  # 60個

# pip install xlsxwriter

filename = "C:/_git/vcs/_4.python/numpy_pandas/data/ExpensesRecord.xls"

df = pd.read_excel(filename, "sheet")
# data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head(5))

from pandas import ExcelWriter

filename = "tmp_write_read_csv14.xlsx"

writer = ExcelWriter(filename, engine="xlsxwriter")
df.to_excel(writer, sheet_name="sheet2")
writer.save()

"""
writer=pd.ExcelWriter('tmp_AAPL1.xlsx')  #檔案名稱
df.to_excel(writer,'AAPL')  #寫入資料
writer.save()   #儲存

from pandas import ExcelWriter

writer = ExcelWriter('tmp_aapl2.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')

df.to_csv("tmp_aapl3.csv")
"""
print("------------------------------------------------------------")  # 60個

print(
    "---- 4444 html與其他 --------------------------------------------------------"
)  # 60個

""" NG
print("使用pandas讀取網頁表單");
    
url = 'https://www.tiobe.com/tiobe-index/'
print("pd讀取html檔案 :", url)

print('跳過標題')
tables = pd.read_html(url, header=0, keep_default_na=False)

print("結果");
print(tables[0])
"""
print("------------------------------------------------------------")  # 60個

# 原物料商品行情
url = "http://www.stockq.org/market/commodity.php"
print("pd讀取html檔案 :", url)
tables = pd.read_html(url)

n = 1
for table in tables:
    print("第 " + str(n) + " 個表格：")
    print(table.head())
    print()
    n += 1

print("------------------------------------------------------------")  # 60個

# 原物料商品行情
url = "http://www.stockq.org/market/commodity.php"
print("pd讀取html檔案 :", url)
tables = pd.read_html(url)

print(tables)

"""
table = tables[7]
table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))

print(table)
"""
print("------------------------------------------------------------")  # 60個

""" NG
#由網址讀取資料檔

url='https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
print("pd讀取html檔案 :", url)
df = pd.read_html(url)
print(df)
"""
print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

filename = "tmp_vehicles1.json"
df.to_json(filename)
print("df寫入json檔案 :", filename)

filename = "tmp_vehicles2.json"
df.to_json(filename, force_ascii=False)
print("df寫入json檔案 :", filename)

filename = "tmp_vehicles1.json"
print("pd讀取json檔案 :", filename)
df2 = pd.read_json(filename)
print(df2)

print("------------------------------------------------------------")  # 60個
"""
url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'

df = pd.read_html(url)
print(df[0].head(5) )

url ='http://news.baidu.com/tech'

#df = pd.read_html(url)
#print(df[0].head(5) )
"""
print("------------------------------------------------------------")  # 60個

filename = "data/AAPL.xlsx"
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, "AAPL")
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print("------------------------------------------------------------")  # 60個

filename = "data/AAPL.xlsx"
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, "AAPL")
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
print(df["Date"] == "2018-01-05")
print(df[df["Date"] == "2018-01-05"])
print(df[(df["Date"] >= "2018-07-05") & (df["Date"] <= "2018-07-10")])
print(df[df["Open"] > 194.2])
print(df[["Date", "Open"]])
print(df[["Date", "Open"]][:5])
print(df.sort_values(by=["Volume"])[:5])
print(df.sort_values(by=["Volume"], ascending=False)[:5])
print(df["Open"][:30].rolling(7).mean())

print("------------------------------------------------------------")  # 60個

filename = "data/AAPL.xlsx"
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, "AAPL")
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
print(df[df["Date"] == "2018-01-05"])
print(df[(df["Date"] >= "2018-07-05") & (df["Date"] <= "2018-07-10")])
print(df[df["Open"] > 194.2])
print(df[["Date", "Open"]][:5])
print(df.sort_values(by=["Volume"])[:5])
print(df.sort_values(by=["Volume"], ascending=False)[:5])
print(df["Open"][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df["diff"] = df["Close"] - df["Open"]
df["year"] = pd.DatetimeIndex(df["Date"]).year
df["month"] = pd.DatetimeIndex(df["Date"]).month
print(df.head())
print("April Volume sum=%.2f" % df[df["month"] == 4][["Volume"]].sum())
print("April Open mean=%.2d" % df[df["month"] == 4][["Open"]].mean())

print("------------------------------------------------------------")  # 60個

filename = "data/AAPL.xlsx"
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, "AAPL")
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
print(df[df["Date"] == "2018-01-05"])
print(df[(df["Date"] >= "2018-07-05") & (df["Date"] <= "2018-07-10")])
print(df[df["Open"] > 194.2])
print(df[["Date", "Open"]][:5])
print(df.sort_values(by=["Volume"])[:5])
print(df.sort_values(by=["Volume"], ascending=False)[:5])
print(df["Open"][:30].rolling(7).mean())

# 4 Calculation
print("--------------------")
df["diff"] = df["Close"] - df["Open"]
df["year"] = pd.DatetimeIndex(df["Date"]).year
df["month"] = pd.DatetimeIndex(df["Date"]).month
df["day"] = pd.DatetimeIndex(df["Date"]).day
print(df.head())
print("April Volume sum=%.2f" % df[df["month"] == 4][["Volume"]].sum())
print("April Open mean=%.2d" % df[df["month"] == 4][["Open"]].mean())

#  5 matplotlib
df.plot(x="Date", y="Open", grid=True, color="blue")
show()

df.plot(y="diff", grid=True, color="red", kind="hist")
show()

fig, ax = plt.subplots()
for name, group in df.groupby("month"):
    group.plot(x="day", y="Open", ax=ax, label=name)
show()

fileds = ["Open", "Close", "High"]
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x="Date", y=name, ax=ax, label=name)
show()

dfMonths = df.loc[df["month"].isin([1, 2, 3, 4, 5, 6, 7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(values="High", columns="month", index="day")
dfMonthsPivot.plot(kind="box", title="Months High")
show()

print("------------------------------------------------------------")  # 60個

print("df 轉 pickle")

df = pd.DataFrame({"Name": ["Smith", "Lucy"], "Age": ["25", "20"], "Sex": ["男", "女"]})
print(df.info())
df.to_pickle("tmp.pkl")

df1 = pd.read_pickle("tmp.pkl")
print(df1.info())

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("df 轉 檔案")

data = {
    "中文名": ["鼠", "牛", "虎", "兔"],
    "英文名": ["mouse", "ox", "tiger", "rabbit"],
    "體重": [3, 48, 33, 8],
    "全名": ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"],
}
df = pd.DataFrame(data, index=["1", "2", "3", "4"])

df.to_json("tmp_write_read_csv06a.json")
df.to_json("tmp_write_read_csv06b.json", force_ascii=False)

print("檔案 轉 df")
df = pd.read_json("tmp_write_read_json06a.json")
print(df)
df = pd.read_json("tmp_write_read_json06b.json")
print(df)

print("------------------------------------------------------------")  # 60個

print("pd寫入excel")

writer = pd.ExcelWriter("tmp_test1111.xlsx")
print(type(writer))

# 建立數據一
df1 = pd.DataFrame({"name": ["david", "tom", "chiou"], "id": [123, 456, 789]})
df1.to_excel(writer, sheet_name="sheet1", index=False)

# 建立數據二
df2 = pd.DataFrame({"電話": ["0912-112233", "0987-556677"], "地址": ["台北市", "埔里鎮"]})
df2.to_excel(writer, sheet_name="工作表二")

# 儲存至 Excel文件中
writer._save()

""" tmp
# 開始批次擷取
with pd.ExcelWriter('tmp_711.xlsx') as writer:
        print(county,"下載中…")
        county = "AAAAAA"
        df.to_excel(writer, sheet_name=county,index=False)
        
# 儲存至 Excel文件中
writer._save()        
print("下載完畢")
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

df = pd.DataFrame({"Math": [90, 91, 92, 93, 94], "English": np.arange(80, 85, 1)})
print(df[["Math", "English"]])


"""
df.to_json("tmp_datas11.json")

df2 = pd.read_json("tmp_datas11.json")
print(df2)

for index, row in df.iterrows() :
    print(index, row["蘋果"], row["香蕉"],
          row["橘子"])
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
