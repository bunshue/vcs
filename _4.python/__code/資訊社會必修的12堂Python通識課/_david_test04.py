import requests

'''
print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

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


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.figure()
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.plot(x, np.sin(x))

plt.figure()
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.plot(x, np.cos(x))
plt.show()


print('------------------------------------------------------------')	#60個

#散點圖範例一
import matplotlib.pyplot as plt
import numpy as np

plt.xlim(-3, 3)
plt.ylim(-3, 3)
x1 = np.random.normal(0, 1, 1024)
y1 = np.random.normal(0, 1, 1024)
plt.scatter(x1, y1, alpha=0.3)
plt.show()

print('------------------------------------------------------------')	#60個


#散點圖範例二
import matplotlib.pyplot as plt
import numpy as np

minutes = [45, 34, 56, 77, 90, 90, 90, 34, 45, 44, 80, 15, 10, 12]
scores =  [90, 80, 100, 65, 5, 30, 55, 100, 90, 80, 60, 5, 0, 10]
plt.xlabel('解題時間')
plt.ylabel('分數')
plt.scatter(minutes, scores)
plt.show()


print('------------------------------------------------------------')	#60個



#直方圖
import matplotlib.pyplot as plt
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
import matplotlib.pyplot as plt
import numpy as np
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

import matplotlib.pyplot as plt
import numpy as np

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
import matplotlib.pyplot as plt

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

import matplotlib.pyplot as plt
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
import matplotlib.pyplot as plt
sns.set()
tips = sns.load_dataset("tips")
plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

print('------------------------------------------------------------')	#60個

import seaborn as sns
import matplotlib.pyplot as plt
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

import matplotlib.pyplot as plt
import xlrd

book = xlrd.open_workbook('election_2018.xls')
sheet = book.sheet_by_index(0)
for row in range(10):
    print(sheet.row_values(row))

    
print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
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
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.show()

'''


print('------------------------------------------------------------')	#60個

''' fail
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

f = open('eduheadlines.txt','r', encoding='utf-8').read()
mask = np.array(Image.open('star.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(f)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
'''

print('------------------------------------------------------------')	#60個

''' fail
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
all_news = ""
for row in rows:
    all_news += row[3]

mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(all_news)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

'''

print('------------------------------------------------------------')	#60個

'''
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
all_news = ""
for row in rows:
    all_news += row[3]

stopwords = list()
with open('stopWords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(all_news) if keyterm not in stopwords]
text = ",".join(keyterms)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
'''

'''
print('------------------------------------------------------------')	#60個

import pandas as pd

data = pd.read_csv('hualien.csv')
target = data[['年度','總人口數','平地原住民','山地原住民']]
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)

print('------------------------------------------------------------')	#60個


import pandas as pd

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
target = target.drop(['年度'], axis=1)
print(target)




print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

data = pd.read_csv('hualien.csv')
target = pd.DataFrame(data[['年度','總人口數','平地原住民','山地原住民']])
target = target.set_index(target['年度'])
fig1 = target.drop(['年度'], axis=1)
fig2 = target.drop(['年度', '總人口數'], axis=1)
fig1.plot(ylim=(0,400000))
fig2.plot.bar(ylim=(0,80000))

#應顯示圖片  但無

'''
print('------------------------------------------------------------')	#60個

''' fail
import xlrd
import pandas as pd
data = pd.read_excel('election_2018.xls')

data.info()
data.head(10)
'''

print('------------------------------------------------------------')	#60個

'''
import pandas as pd
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index('地區')
target.describe()

target.hist(bins=3)

target

import pandas as pd
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['地區', '推薦政黨'])
target

import pandas as pd
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
target


import pandas as pd
data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','出生年次','推薦政黨','得票數']]
target['年齡'] = 2018-target['出生年次']
target = target.drop('出生年次', axis=1)
target = target.set_index(['推薦政黨', '地區']).sort_index()
print("國民黨：\t{:>10,d}票".format(target.loc['中國國民黨']['得票數'].sum()))
print("民進黨：\t{:>10,d}票".format(target.loc['民主進步黨']['得票數'].sum()))
print("其它：\t{:>10,d}票".format(target.loc['無黨籍及未經政黨推薦']['得票數'].sum()))



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import _rebuild

data = pd.read_excel('election_2018.xls')
target = data.fillna(method='ffill')
target = target[['地區','姓名','推薦政黨','得票數']].groupby(by = '推薦政黨')['得票數'].sum()
target.plot.pie(y='推薦政黨')
target

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.font_manager import _rebuild
_rebuild()
plt.rcParams['font.sans-serif'] = [u'SimHei']
sns.set_style("darkgrid",{"font.sans-serif":[u'SimHei', 'Arial']})

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



import matplotlib.pyplot as plt
from twstock import Stock
tsmc = Stock('2330')
data = tsmc.moving_average(tsmc.price, 5)
plt.plot(list(range(len(data))), data)

plt.show()

'''

print('------------------------------------------------------------')	#60個

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
if __name__ == '__main__':    
    a = shape(100, 200)
    b = shape(200, 300)
    print(a.info())
    print(b.info())
    

print('------------------------------------------------------------')	#60個


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
    
class circle(shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def info(self):
        return ("圓形", self.x, self.y, self.r)
    
class rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    
    def info(self):
        return ("矩形", self.x, self.y, self.w, self.h)

if __name__ == '__main__':
    a = shape(100, 200)
    b = shape(200, 300)
    c = circle(100, 200, 50)
    d = rectangle(100, 200, 50, 50)
    shapes = [a, b, c, d]
    for s in shapes:
        print(s.info())
        
print('------------------------------------------------------------')	#60個

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
class circle(shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def info(self):
        return ("圓形", self.x, self.y, self.r)
    
class rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    
    def info(self):
        return ("矩形", self.x, self.y, self.w, self.h)

if __name__ == '__main__':
    d = rectangle(100, 200, 50, 50)
    print(d.info())
    print("往x前進50點，y後退20點")
    d.move(50, -20)
    print(d.info())
    

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import random
class poker():
    def __init__(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        self.card_type = ['黑桃', '紅心', '梅花', '方塊']
        self.index = 0
    
    def decode(self, card):
        suit = self.card_type[card // 13]
        no = card % 13 + 1
        if no == 1:
            no = 'A'
        elif no > 10:
            no = chr((no - 11) + ord('J'))
        return (suit, str(no))
        
    def showAll(self):
        for card in self.deck:
            print(self.decode(card), end='')
        print()
    
    def dealFive(self):
        for i in range(5):
            print(self.decode(self.deck[self.index]), end='')
            self.index += 1
        print()
    
    def oneMore(self):
        print(self.decode(self.deck[self.index]), end='')
        self.index += 1
        print()
    
    def shuffle(self):
        random.shuffle(self.deck)
        self.index = 0

if __name__ == '__main__':
    p = poker()
    p.showAll()
    print("------")
    p.dealFive()
    for i in range(3):
        p.oneMore()
    print("------")
    p.shuffle()
    p.showAll()
    print("------")
    p.dealFive()

print('------------------------------------------------------------')	#60個
