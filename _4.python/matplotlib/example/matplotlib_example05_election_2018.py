import sys

print('------------------------------------------------------------')	#60個

import xlrd

book = xlrd.open_workbook('election_2018.xls')
sheet = book.sheet_by_index(0)
for row in range(10):
    print(sheet.row_values(row))

print('------------------------------------------------------------')	#60個

import xlrd

book = xlrd.open_workbook('election_2018.xls')
sheet = book.sheet_by_index(0)
rows = sheet.nrows
table = list()
for row in range(rows):
    table.append(sheet.row_values(row))
for row in range(rows):
    if table[row][0] == '':
        table[row][0] = table[row-1][0]

tainan = dict()
for row in range(rows):
    if table[row][0] == '臺南市':
        tainan[table[row][1]] = table[row][6]

print(type(tainan))
print(tainan)


print('------------------------------------------------------------')	#60個

import pandas as pd

import xlrd

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用
data = pd.read_excel('election_2018.xls')

data.info()
data.head(10)

print('------------------------------------------------------------')	#60個

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index('地區')
target.describe()

target.hist(bins=3)

target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區', '推薦政黨'])
target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
target

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
print("國民黨：\t{:>10,d}票".format(target.loc['中國國民黨']['得票數'].sum()))
print("民進黨：\t{:>10,d}票".format(target.loc['民主進步黨']['得票數'].sum()))
print("其它：\t{:>10,d}票".format(target.loc['無黨籍及未經政黨推薦']['得票數'].sum()))

import seaborn as sns

#如果明明有的字型, matplotlib 說找不到的話, 有可能需要讓 matplotlib 清掉原本的 cache。
#matplotlib.font_manager._rebuild()
#from matplotlib.font_manager import _rebuild

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','推薦政黨','得票數']].groupby(by = '推薦政黨')['得票數'].sum()
target.plot.pie(y='推薦政黨')
target

import seaborn as sns

#如果明明有的字型, matplotlib 說找不到的話, 有可能需要讓 matplotlib 清掉原本的 cache。
#matplotlib.font_manager._rebuild()
#from matplotlib.font_manager import _rebuild
#_rebuild()

#plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

#pd.read_excel kilo可用  sugar不可用, sugar降版成 pandas 1.3.5 可用

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區'])
tainan = target.loc['臺南市'][['姓名','得票數']]
tainan = tainan.set_index(['姓名'])
tainan.plot.pie(y='得票數')
tainan.plot.bar()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

