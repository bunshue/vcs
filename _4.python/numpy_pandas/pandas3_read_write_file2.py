"""
使用pandas讀寫檔案
1111. csv檔
2222. json
3333. excel
4444. html與其他


# 讀取, 匯入DataFrame, 檔案轉df
df.read_csv(filename)
df.read_json(filename)
df.read_html(filename)
df.read_excel(filename)
df.read_sql(query, engine)

# 寫入, 匯出DataFrame, df轉檔案
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(table, con = engine)

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


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
df.to_html("tmp8-2-2a-02.html")
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

filename = "tmp_vehicles.csv"
df.to_csv(filename, index=False, encoding="big5")
print("df寫入csv檔案 :", filename)

filename = "tmp_vehicles.csv"
print("pd讀取csv檔案 :", filename)
df1 = pd.read_csv(filename, encoding="big5")
print(df1)

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
""" fail in kilo
# pip install xlsxwriter

#print("pd讀取csv檔案 :", filename)
#data = pd.read_csv('data/ExpensesRecord.csv')

filename = 'data/ExpensesRecord.xls'
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, 'sheet')

#url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
#print("pd讀取html檔案 :", url)
#data = pd.read_html(url)

print(df.head(5) )

from pandas import ExcelWriter

filename = 'tmp_test.xlsx'
writer = ExcelWriter(filename, engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')
writer.save()

print("df寫入excel檔案 :", filename)
"""
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

""" no file AAPL.xlsx
filename = 'AAPL.xlsx'
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, 'AAPL')
print(df.head())
print(type(df))

# 2
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print('------------------------------------------------------------')	#60個

filename = 'AAPL.xlsx'
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, 'AAPL')
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

filename = 'AAPL.xlsx'
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, 'AAPL')
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

filename = 'AAPL.xlsx'
print("pd讀取excel檔案 :", filename)
df = pd.read_excel(filename, 'AAPL')
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
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


# NYC 311 service request dataset
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, dtype="unicode")

cc = requests["Incident Zip"].unique()
print(cc)

print("------------------------------------------------------------")  # 60個

# Fixing the nan values and string/float confusion

na_values = ["NO CLUE", "N/A", "0"]
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, na_values=na_values, dtype={"Incident Zip": str})

cc = requests["Incident Zip"].unique()
print(cc)

# What's up with the dashes?

rows_with_dashes = requests["Incident Zip"].str.contains("-").fillna(False)
cc = len(requests[rows_with_dashes])
print(cc)

print(requests[rows_with_dashes])

# But then my friend Dave pointed out that 9-digit zip codes are normal.
# Let's look at all the zip codes with more than 5 digits, make sure they're okay, and then truncate them.
long_zip_codes = requests["Incident Zip"].str.len() > 5
cc = requests["Incident Zip"][long_zip_codes].unique()
print(cc)

requests["Incident Zip"] = requests["Incident Zip"].str.slice(0, 5)

# Earlier I thought 00083 was a broken zip code, but turns out Central Park's zip code 00083!
# Shows what I know. I'm still concerned about the 00000 zip codes, though: let's look at that.
cc = requests[requests["Incident Zip"] == "00000"]
print(cc)

zero_zips = requests["Incident Zip"] == "00000"
requests.loc[zero_zips, "Incident Zip"] = np.nan

# fail
# unique_zips = requests['Incident Zip'].unique()
# unique_zips.sort()
# cc = unique_zips
# print(cc)
zips = requests["Incident Zip"]
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse, and why?)
is_close = zips.str.startswith("0") | zips.str.startswith("1")
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~(is_close) & zips.notnull()

cc = zips[is_far]
print(cc)

cc = requests[is_far][["Incident Zip", "Descriptor", "City"]].sort_values(
    "Incident Zip"
)
print(cc)

cc = requests["City"].str.upper().value_counts()
print(cc)

print("------------------------------------------------------------")  # 60個

# Putting it together

na_values = ["NO CLUE", "N/A", "0"]
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, na_values=na_values, dtype={"Incident Zip": str})


def fix_zip_codes(zips):
    # Truncate everything to length 5
    zips = zips.str.slice(0, 5)
    # Set 00000 zip codes to nan
    zero_zips = zips == "00000"
    zips[zero_zips] = np.nan
    return zips


requests["Incident Zip"] = fix_zip_codes(requests["Incident Zip"])

cc = requests["Incident Zip"].unique()
print(cc)

print("------------------------------------------------------------")  # 60個

# Parsing Unix timestamps

# Read it, and remove the last row
popcon = pd.read_csv(
    "data/popularity-contest",
    sep=" ",
)[:-1]
popcon.columns = ["atime", "ctime", "package-name", "mru-program", "tag"]

print(popcon[:5])

popcon["atime"] = popcon["atime"].astype(int)
popcon["ctime"] = popcon["ctime"].astype(int)

popcon["atime"] = pd.to_datetime(popcon["atime"], unit="s")
popcon["ctime"] = pd.to_datetime(popcon["ctime"], unit="s")

print(popcon["atime"].dtype)

print(popcon[:5])

print("------------------------------------------------------------")  # 60個

popcon = popcon[popcon["atime"] > "1970-01-01"]

# 不包含lib的
nonlibraries = popcon[~popcon["package-name"].str.contains("lib")]

cc = nonlibraries.sort_values("ctime", ascending=False)[:10]
print(cc)

print("------------------------------------------------------------")  # 60個

# use_pivot_sum

filename = "data\ordersList.csv"
print("pd讀取csv檔案 :", filename)
print("跳過標題")
df = pd.read_csv(filename, encoding="utf-8", header=0)

print(
    df.pivot_table(
        index="品名",
        columns="客戶名稱",
        values="金額",
        fill_value=0,
        margins=True,
        aggfunc="sum",
    )
)

print(
    df.pivot_table(index="品名", columns="客戶名稱", values="金額", fill_value=0, margins=True)
)

print("------------------------------------------------------------")  # 60個

print("df 轉 pickle")

df = pd.DataFrame({"Name": ["Smith", "Lucy"], "Age": ["25", "20"], "Sex": ["男", "女"]})
print(df.info())
df.to_pickle("tmp.pkl")

df1 = pd.read_pickle("tmp.pkl")
print(df1.info())


print("------------------------------------------------------------")  # 60個

print("df 轉 檔案")

data = {
    "中文名": ["鼠", "牛", "虎", "兔"],
    "英文名": ["mouse", "ox", "tiger", "rabbit"],
    "體重": [3, 48, 33, 8],
    "全名": ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"],
}
df = pd.DataFrame(data, index=["1", "2", "3", "4"])

df.to_csv("tmp_write_read_csv06.csv", index=False, encoding="big5")
df.to_json("tmp_write_read_csv06a.json")
df.to_json("tmp_write_read_csv06b.json", force_ascii=False)

print("檔案 轉 df")

df = pd.read_csv("tmp_write_read_csv06.csv", encoding="big5")
print(df)
df = pd.read_json("tmp_write_read_csv06a.json")
print(df)
df = pd.read_json("tmp_write_read_csv06b.json")
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {"中文名": ["鼠", "牛", "虎", "兔"], "英文名": ["mouse", "ox", "tiger", "rabbit"]}
)
print(df[["中文名", "英文名"]])

print("------------------------------------------------------------")  # 60個

import pandas as pd

cities = pd.read_csv("data/california_cities.csv")

print(cities.head())

# extracting the data we ar interested in
latitude, longitude = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

# to scatter the points, using size and color but without label
import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()
plt.scatter(
    longitude,
    latitude,
    label=None,
    c=np.log10(population),
    cmap="viridis",
    s=area,
    linewidth=0,
    alpha=0.5,
)
# plt.axis(aspect='equal') NG
plt.xlabel("Longitude")
plt.ylabel("Longitude")
plt.colorbar(label="log$_{10}$(population)")
plt.clim(3, 7)
# now we will craete a legend, we will plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c="k", alpha=0.3, s=area, label=str(area) + "km$^2$")
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="City Areas")
plt.title("Area and Population of California Cities")
plt.show()

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}
df = pd.DataFrame(dists)
print(df)
df.to_html("tmp8-2-1.html")

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}

ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eigth",
    "ninth",
    "tenth",
    "eleventh",
    "twelvth",
    "thirteenth",
]
df = pd.DataFrame(dists, index=ordinals)
print(df)
df.to_html("tmp8-2-1a.html")

print("------------------------------")  # 30個

df2 = pd.DataFrame(dists)
df2.index = ordinals
print(df2)

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}

ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eigth",
    "ninth",
    "tenth",
    "eleventh",
    "twelvth",
    "thirteenth",
]
df = pd.DataFrame(dists, columns=["name", "city", "population"], index=ordinals)
print(df)
df.to_html("tmp8-2-1b.html")

print("------------------------------")  # 30個

df2 = pd.DataFrame(dists, index=ordinals)
df2.columns = ["name", "city", "population"]
print(df2)

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}

df = pd.DataFrame(dists, columns=["name", "population"], index=dists["city"])
print(df)
df.to_html("tmp8-2-1c.html")

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}

ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eigth",
    "ninth",
    "tenth",
    "eleventh",
    "twelvth",
    "thirteenth",
]
df = pd.DataFrame(dists, columns=["name", "population"], index=dists["city"])
print(df.T)
df.T.to_html("tmp8-2-1d.html")

print("------------------------------------------------------------")  # 60個

print("pd寫入excel")
# excel_write.py
import pandas as pd

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


print("------------------------------------------------------------")  # 60個

sys.exit()

df = pd.DataFrame({"Math": [90, 91, 92, 93, 94], "English": np.arange(80, 85, 1)})
print(df[["Math", "English"]])


filename = "tmp_動物資料0.csv"
df.to_csv(filename)  # 預設為 儲存index行

filename = "tmp_動物資料1.csv"
df.to_csv(filename, index=False)  # 不儲存index行

filename = "tmp_動物資料2.csv"
df.to_csv(filename, index=True)  # 儲存index行

"""
df.to_csv("tmp_datas11.csv",index=False,encoding="utf8")
df.to_json("tmp_datas11.json")

df2 = pd.read_csv("tmp_datas11.csv", encoding="utf8")
df2 = pd.read_json("tmp_datas11.json")
print(df2)

for index, row in df.iterrows() :
    print(index, row["蘋果"], row["香蕉"],
          row["橘子"])

"""

print("------------------------------------------------------------")  # 60個

print("df存成csv檔")
df.to_csv("tmp_olympics.csv")


print("csv檔案轉df")
df = pd.read_csv("data/student.csv")
print(df)

df.to_pickle("tmp_student.pickle")


print("------------------------------------------------------------")  # 60個
