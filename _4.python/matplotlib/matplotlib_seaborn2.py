import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

import seaborn as sns #海生, 自動把圖畫得比較好看

import seaborn as sns
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

'''

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
'''

