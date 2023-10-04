"""
import seaborn as sns       #海生, 自動把圖畫得比較好看

平常只要打入

sns.set()

seaborn 就接手了, 不過因為我們要用中文字型, 所以要這樣子打。
sns.set(rc={'font.family':'Noto Sans CJK TC'})

"""


import sys
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns       #海生, 自動把圖畫得比較好看

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

print('------------------------------------------------------------')	#60個

plt.title('二項式分布 Binomial')
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)

plt.show()

print('------------------------------------------------------------')	#60個

plt.title('二項式分布 Binomial')
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.show()

print('------------------------------------------------------------')	#60個

sns.set(color_codes = True)
x = np.linspace(-10, 10, 200)
y = np.sinc(x)

plt.plot(x,y)

plt.show()

print('------------------------------------------------------------')	#60個

N = 200
data = np.random.randn(N)
print(np.mean(data))

ax = plt.subplot()
sns.histplot(data, kde = False, ax = ax)
_ = ax.set(title = 'Histogram', xlabel = 'x', ylabel = 'y');

plt.show()

print('------------------------------------------------------------')	#60個

sns.get_dataset_names()

tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.head())

print('------------------------------------------------------------')	#60個

sns.set()
tips = sns.load_dataset("tips")
plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()

print('------------------------------------------------------------')	#60個

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

tips = sns.load_dataset("tips")
sns.catplot(x='day', y='tip', data=tips)

print('------------------------------------------------------------')	#60個

titanic = sns.load_dataset("titanic")
print(titanic.head())

print('------------------------------------------------------------')	#60個

titanic = sns.load_dataset("titanic")
sns.countplot(x = 'class', hue = 'survived', data = titanic)

print('------------------------------------------------------------')	#60個

titanic = sns.load_dataset("titanic")
sns.countplot(x = 'sex', hue = 'survived', data = titanic)

print('------------------------------------------------------------')	#60個

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

plt.bar(range(len(ranking.values())), ranking.values(), width=0.8)
plt.xticks(range(len(ranking.values())), ranking.keys(), rotation=45)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

