import os
import sys
import time
import random

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

import numpy as np
from sklearn.linear_model import LogisticRegression

print('------------------------------------------------------------')	#60個

input_data = np.array([
    [0, 0],
    [0.25, 0.25],
    [0.5, 0.5],
    [1, 1],
])

output_data = [
    0,
    0,
    1,
    1
]

logit_model = LogisticRegression()

logit_model.fit(input_data, output_data)

tt = logit_model.coef_
print(tt)

tt = logit_model.intercept_
print(tt)

predicted_output = logit_model.predict(input_data)
print(predicted_output)

print('------------------------------------------------------------')	#60個

#          編號              圖像大小[英吋]      解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '預測曲線', figsize = (16, 8), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#左圖
plt.subplot(121)

plt.scatter(
    x=input_data[:,0],
    y=input_data[:,1],
    color=[('red' if x == 1 else 'blue') for x in output_data]
)

for x in output_data:
    print(x)


print(input_data[:,0])
print(input_data[:,1])

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Actual')
plt.grid()

#右圖
plt.subplot(122)

plt.scatter(
    x=input_data[:,0], 
    y=input_data[:,1], 
    color=[('red' if x == 1 else 'blue') for x in predicted_output]
)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Predicted')
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/bank-additional-full.csv', sep = ';')

print(df.shape)
print(df.head())

df['conversion'] = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

print(df.head())

print('------------------------------------------------------------')	#60個

print('Aggregate Conversion Rate')
print('total conversions: %i out of %i' % (df.conversion.sum(), df.shape[0]))
print('conversion rate: %0.2f%%' % (df.conversion.sum() / df.shape[0] * 100.0))

print('Conversion Rates by Number of Contacts')

pd.DataFrame(df.groupby(by='campaign')['conversion'].sum())

print(df.groupby(by='campaign')['conversion'].sum())

pd.DataFrame(df.groupby(by='campaign')['conversion'].count())

print(df.groupby(by='campaign')['conversion'].count())

conversions_by_contacts = df.groupby(
    by='campaign'
)['conversion'].sum() / df.groupby(
    by='campaign'
)['conversion'].count() * 100.0


print(pd.DataFrame(conversions_by_contacts))


print('------------------------------------------------------------')	#60個

ax = conversions_by_contacts[:10].plot(
    grid=True,
    figsize=(10, 7),
    xticks=conversions_by_contacts.index[:10],
    title='Conversion Rates by Number of Contacts'
)

ax.set_ylim([0, 15])
ax.set_xlabel('number of contacts')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個

print('Conversion Rates by Age')

#Line Chart
pd.DataFrame(df.groupby(by='age')['conversion'].sum())
print('age.sum()')
print(df.groupby(by='age')['conversion'].sum())

pd.DataFrame(df.groupby(by='age')['conversion'].count())
print('age.count()')
print(df.groupby(by='age')['conversion'].count())

print('age.group()')
conversions_by_age = df.groupby(
    by='age'
)['conversion'].sum() / df.groupby(
    by='age'
)['conversion'].count() * 100.0

print(pd.DataFrame(conversions_by_age))


ax = conversions_by_age.plot(grid = True, figsize = (10, 7), title = 'Conversion Rates by Age')

ax.set_xlabel('age')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個

#Age Groups
df['age_group'] = df['age'].apply(
    lambda x: '[18, 30)' if x < 30 else '[30, 40)' if x < 40 \
        else '[40, 50)' if x < 50 else '[50, 60)' if x < 60 \
        else '[60, 70)' if x < 70 else '70+'
)

print('df.head()')
print(df.head())

pd.DataFrame(df.groupby(by='age_group')['conversion'].sum())
print('age.sum()')
print(df.groupby(by='age_group')['conversion'].sum())

pd.DataFrame(df.groupby(by='age_group')['conversion'].count())
print('age.count()')
print(df.groupby(by='age_group')['conversion'].count())

conversions_by_age_group = df.groupby(
    by='age_group'
)['conversion'].sum() / df.groupby(
    by='age_group'
)['conversion'].count() * 100.0

print('age.group')
print(pd.DataFrame(conversions_by_age_group))

ax = conversions_by_age_group.loc[
    ['[18, 30)', '[30, 40)', '[40, 50)', '[50, 60)', '[60, 70)', '70+']
].plot(
    kind='bar',
    color='skyblue',
    grid=True,
    figsize=(10, 7),
    title='Conversion Rates by Age Groups'
)

ax.set_xlabel('age')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個

print('Conversions vs. Non-Conversions')

# Marital Status

conversions_by_marital_status_df = pd.pivot_table(df, values='y', index='marital', columns='conversion', aggfunc=len)
print(conversions_by_marital_status_df)


conversions_by_marital_status_df.columns = ['non_conversions', 'conversions']

print(conversions_by_marital_status_df)

conversions_by_marital_status_df.plot(
    kind='pie',
    figsize=(15, 7),
    startangle=90,
    subplots=True,
    autopct=lambda x: '%0.1f%%' % x
)

plt.show()

print('------------------------------------------------------------')	#60個

print('Education')

conversions_by_education_df = pd.pivot_table(df, values='y', index='education', columns='conversion', aggfunc=len)
print(conversions_by_education_df)

conversions_by_education_df.columns = ['non_conversions', 'conversions']

print(conversions_by_education_df)


conversions_by_education_df.plot(
    kind='pie',
    figsize=(15, 7),
    startangle=90,
    subplots=True,
    autopct=lambda x: '%0.1f%%' % x,
    legend=False
)

plt.show()




print('------------------------------------------------------------')	#60個

#Last Contact Duration

tt = df.groupby('conversion')['duration'].describe()

print(tt)


duration_df = pd.concat([
    df.loc[df['conversion'] == 1, 'duration'].reset_index(drop=True), 
    df.loc[df['conversion'] == 0, 'duration'].reset_index(drop=True)
], axis=1)

duration_df.columns = ['conversions', 'non_conversions']

duration_df = duration_df / (60*60)

print(duration_df)


ax = duration_df.plot(
    kind='box',
    grid=True,
    figsize=(10, 10),
)

ax.set_ylabel('last contact duration (hours)')
ax.set_title('Last Contact Duration')

plt.show()


print('------------------------------------------------------------')	#60個
#Conversions by Age Groups & Marital Status

age_marital_df = df.groupby(['age_group', 'marital'])['conversion'].sum().unstack('marital').fillna(0)
print(age_marital_df)

age_marital_df = age_marital_df.divide(
    df.groupby(
        by='age_group'
    )['conversion'].count(), 
    axis=0
)

print(age_marital_df)


ax = age_marital_df.loc[
    ['[18, 30)', '[30, 40)', '[40, 50)', '[50, 60)', '[60, 70)', '70+']
].plot(
    kind='bar', 
    grid=True,
    figsize=(10,7)
)

ax.set_title('Conversion rates by Age & Marital Status')
ax.set_xlabel('age group')
ax.set_ylabel('conversion rate (%)')

plt.show()


print('------------------------------------------------------------')	#60個

ax = age_marital_df.loc[
    ['[18, 30)', '[30, 40)', '[40, 50)', '[50, 60)', '[60, 70)', '70+']
].plot(
    kind='bar', 
    stacked=True,
    grid=True,
    figsize=(10,7)
)

ax.set_title('Conversion rates by Age & Marital Status')
ax.set_xlabel('age group')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

