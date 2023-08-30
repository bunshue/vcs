'''
# plot 集合

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import requests
import pandas as pd

import sys

'''
print('------------------------------------------------------------')	#60個

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.ylim((-1.2, 1.2))
plt.plot(x, np.sin(x), label="SIN", linestyle="--")
plt.plot(x, np.cos(x), label="COS", color="red")
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.legend()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.figure()
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.plot(x, np.sin(x))

plt.show()


print('------------------------------------------------------------')	#60個

#散點圖範例一

plt.xlim(-3, 3)
plt.ylim(-3, 3)
x1 = np.random.normal(0, 1, 1024)
y1 = np.random.normal(0, 1, 1024)
plt.scatter(x1, y1, alpha=0.3)
plt.show()

print('------------------------------------------------------------')	#60個

#散點圖範例二

minutes = [45, 34, 56, 77, 90, 90, 90, 34, 45, 44, 80, 15, 10, 12]
scores =  [90, 80, 100, 65, 5, 30, 55, 100, 90, 80, 60, 5, 0, 10]
plt.xlabel('解題時間')
plt.ylabel('分數')
plt.scatter(minutes, scores)

plt.show()

print('------------------------------------------------------------')	#60個

#直方圖
minutes = [45, 34, 56, 77, 90, 90, 90, 34, 45, 44, 80, 15, 10, 12]
scores =  [90, 80, 100, 65, 5, 30, 55, 100, 90, 80, 60, 5, 0, 10]

plt.figure()
plt.xlabel('解題時間(分)')
plt.ylabel('人數')
plt.hist(minutes, bins=4, edgecolor='white', linewidth=1.2)

plt.figure()
plt.xlabel('分數')
plt.ylabel('人數')
plt.hist(scores, bins=4, color='red', edgecolor='white', linewidth=1.2)

plt.show()

print('------------------------------------------------------------')	#60個

#圓餅圖

toyota = [8, 4, 3]
lexus =  [0, 2, 10]
mazda =  [5, 4, 1]
subaru = [3, 6, 0]
labels = ['<100', '100~149', '>=150']

plt.subplot(2,2,1)
plt.pie(toyota, radius=1.2, labels=labels, shadow=True)
plt.title('Toyota')

plt.subplot(2,2,2)
plt.pie(lexus, radius=1.2, labels=labels, shadow=True)
plt.title('Lexus')

plt.subplot(2,2,3)
plt.pie(mazda, radius=1.2, labels=labels, shadow=True)
plt.title('Mazda')

plt.subplot(2,2,4)
plt.pie(subaru, radius=1.2, labels=labels, shadow=True)
plt.title('Subaru')

plt.show()

print('------------------------------------------------------------')	#60個

lexus_models = {
    'CT-200h': 139, 
    'ES': 167, 
    'GS': 221, 
    'IS': 173,
    'LC': 539,
    'LS': 337,
    'LX': 465,
    'NX': 155,
    'RC': 243,
    'RX': 224,
    'RX L': 260,
    'UX': 139
               }
lexus_prices = np.array(list(lexus_models.values()), dtype=np.int64)
lexus = list()
lexus.append(np.count_nonzero(lexus_prices<=150))
lexus.append(np.count_nonzero((lexus_prices>150)&(lexus_prices<=200)))
lexus.append(np.count_nonzero((lexus_prices>200)&(lexus_prices<=300)))
lexus.append(np.count_nonzero(lexus_prices>300))
labels = ['<=150', '151~200', '201~300', '>300']
explode = [0.2, 0, 0, 0]
plt.pie(lexus, explode=explode, autopct='%1.0f%%', 
        radius=2.0, labels=labels, shadow=True)
plt.title('Lexus Models Prices')
plt.show()

print('------------------------------------------------------------')	#60個

#長條圖範例

ranking = {
    'Toyota RAV4': 2958,
    'CMC Veryca': 1312,
    'Nissan Kicks': 1267,
    'Honda CRV': 1209,
    'Toyota Sienta': 1163,
    'Toyota Yaris': 936, 
    'Toyota': 911,
    'Ford Focus': 873,
    'M-Benz C-Class': 749,
    'Honda HR-V':704
}

plt.bar(range(len(ranking.values())), 
        ranking.values(), width=0.8)
plt.xticks(range(len(ranking.values())), 
           ranking.keys(), rotation=45)
plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns

sns.set()
ranking = {
    'Toyota RAV4': 2958,
    'CMC Veryca': 1312,
    'Nissan Kicks': 1267,
    'Honda CRV': 1209,
    'Toyota Sienta': 1163,
    'Toyota Yaris': 936, 
    'Toyota': 911,
    'Ford Focus': 873,
    'M-Benz C-Class': 749,
    'Honda HR-V':704
}

plt.bar(range(len(ranking.values())), 
        ranking.values(), width=0.8)
plt.xticks(range(len(ranking.values())), 
           ranking.keys(), rotation=45)
plt.show()


print('------------------------------------------------------------')	#60個

import seaborn as sns
sns.get_dataset_names()

import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.head())


print('------------------------------------------------------------')	#60個

import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")
plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
male_tips = tips[tips.sex=='Male']
female_tips = tips[tips.sex=='Female']
plt.scatter(male_tips.total_bill, male_tips.tip, label="Male tips")
plt.scatter(female_tips.total_bill, female_tips.tip, label="Female tips")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns

tips = sns.load_dataset("tips")
sns.catplot(x='day', y='tip', data=tips)


print('------------------------------------------------------------')	#60個

import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.head())

print('------------------------------------------------------------')	#60個

import seaborn as sns

titanic = sns.load_dataset("titanic")
sns.countplot(x = 'class', hue = 'survived', data = titanic)

print('------------------------------------------------------------')	#60個

import seaborn as sns

titanic = sns.load_dataset("titanic")
sns.countplot(x = 'sex', hue = 'survived', data = titanic)

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
print(tainan)
plt.bar(range(len(tainan)), tainan.values(), facecolor="#99ccff")
plt.xticks(range(len(tainan)), tainan.keys())
plt.ylim((0, 400000))
for x, y in zip(range(len(tainan)), tainan.values()):
    plt.text(x-0.05, y+5000, "{:>8,.0f}".format(y), ha='center')
#plt.rcParams['font.sans-serif'] = [u'SimHei']

plt.show()

'''

print('------------------------------------------------------------')	#60個


'''
print('------------------------------------------------------------')	#60個

data = pd.read_csv('hualien.csv')
target = data[['年度','總人口數','平地原住民','山地原住民']]
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)




print('------------------------------------------------------------')	#60個

import seaborn as sns

#plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
fig1 = target.drop(['年度'], axis=1)
fig2 = target.drop(['年度', '總人口數'], axis=1)
fig1.plot(ylim=(0,400000))
fig2.plot.bar(ylim=(0,80000))

#應顯示圖片  但無

print('------------------------------------------------------------')	#60個

'''


'''
import xlrd

#pd.read_excel kilo可用  sugar不可用
data = pd.read_excel('election_2018.xls')

data.info()
data.head(10)
'''

print('------------------------------------------------------------')	#60個

'''

#pd.read_excel kilo可用  sugar不可用
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index('地區')
target.describe()

target.hist(bins=3)

target

#pd.read_excel kilo可用  sugar不可用
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區', '推薦政黨'])
target

#pd.read_excel kilo可用  sugar不可用
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
target

#pd.read_excel kilo可用  sugar不可用
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

#pd.read_excel kilo可用  sugar不可用
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

#pd.read_excel kilo可用  sugar不可用
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
'''


print('------------------------------------------------------------')	#60個

''' stock OK
from twstock import Stock
tsmc = Stock('2330')
print(tsmc.price)

from twstock import Stock
tsmc = Stock('2330')
print(tsmc.moving_average(tsmc.price, 5))
print(tsmc.moving_average(tsmc.capacity, 5))





from twstock import Stock
tsmc = Stock('2330')
data = tsmc.moving_average(tsmc.price, 5)
plt.plot(list(range(len(data))), data)

plt.show()

'''


'''

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

'''

