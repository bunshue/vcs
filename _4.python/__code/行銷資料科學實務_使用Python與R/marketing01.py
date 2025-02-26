
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
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

import matplotlib

print('------------------------------------------------------------')	#60個

from sklearn.linear_model import LogisticRegression

print('------------------------------------------------------------')	#60個
'''
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
plt.figure(num = '預測曲線', figsize = (12, 8), dpi = 100, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

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
    figsize=(12, 8),
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


ax = conversions_by_age.plot(grid = True, figsize = (12, 8), title = 'Conversion Rates by Age')

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
    figsize=(12, 8),
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
    figsize=(12, 8),
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
    figsize=(12, 8),
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
    figsize=(12, 8),
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
    figsize=(12, 8)
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
    figsize=(12, 8)
)

ax.set_title('Conversion rates by Age & Marital Status')
ax.set_xlabel('age group')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('讀取資料')

df = pd.read_csv('data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv')

print(df.shape)

print('打印df.head()')
print(df.head())

df['Engaged'] = df['Response'].apply(lambda x: 0 if x == 'No' else 1)

print('打印df.head()')
print(df.head())

print('------------------------------------------------------------')	#60個

print('分析資料')

print('columns資料')
print(list(df.columns))

print('Engagement Rate')

engagement_rate_df = pd.DataFrame(
    df.groupby('Engaged').count()['Response'] / df.shape[0] * 100.0
)

print(engagement_rate_df)

print('轉置')
print(engagement_rate_df.T)

print('------------------------------------------------------------')	#60個

print('By Renew Offer Type')

engagement_by_offer_type_df = pd.pivot_table(
    df, values='Response', index='Renew Offer Type', columns='Engaged', aggfunc=len
).fillna(0.0)

engagement_by_offer_type_df.columns = ['Not Engaged', 'Engaged']

print(engagement_by_offer_type_df)

engagement_by_offer_type_df.plot(
    kind='pie',
    figsize=(15, 7),
    startangle=90,
    subplots=True,
    autopct=lambda x: '%0.1f%%' % x
)

plt.show()

print('------------------------------------------------------------')	#60個

print('By Sales Channel')

engagement_by_sales_channel_df = pd.pivot_table(
    df, values='Response', index='Sales Channel', columns='Engaged', aggfunc=len
).fillna(0.0)

engagement_by_sales_channel_df.columns = ['Not Engaged', 'Engaged']

print(engagement_by_sales_channel_df)

engagement_by_sales_channel_df.plot(
    kind='pie',
    figsize=(15, 7),
    startangle=90,
    subplots=True,
    autopct=lambda x: '%0.1f%%' % x
)

plt.show()

print('------------------------------------------------------------')	#60個

print('Total Claim Amount Distributions')

ax = df[['Engaged', 'Total Claim Amount']].boxplot(
    by='Engaged',
    showfliers=False,
    figsize=(7,5)
)

ax.set_xlabel('Engaged')
ax.set_ylabel('Total Claim Amount')
ax.set_title('Total Claim Amount Distributions by Enagements')

plt.suptitle("")
plt.show()

print('------------------------------------------------------------')	#60個

#df畫箱圖
ax = df[['Engaged', 'Total Claim Amount']].boxplot(
    by = 'Engaged',
    showfliers = True,
    figsize=(7, 5)
)

ax.set_xlabel('Engaged')
ax.set_ylabel('Total Claim Amount')
ax.set_title('Total Claim Amount Distributions by Enagements')

plt.suptitle("")
plt.show()

print('------------------------------------------------------------')	#60個

print('Income Distributions')

#df畫箱圖
ax = df[['Engaged', 'Income']].boxplot(
    by='Engaged',
    showfliers=True,
    figsize=(7,5)
)

ax.set_xlabel('Engaged')
ax.set_xlabel('Income')
ax.set_title('Income Distributions by Enagements')

plt.suptitle("")
plt.show()

print('------------------------------------------------------------')	#60個

print('打印Engaged資料')
tt = df.groupby('Engaged').describe()['Income'].T
print(tt)

print('------------------------------------------------------------')	#60個

print('Regression Analysis with Continuous Variables Only')

#import statsmodels.formula.api as sm   old
import statsmodels.api as sm

print('打印.describe()資料')
print(df.describe())

print(df['Income'].dtype)

print(df['Customer Lifetime Value'].dtype)

print('------------------------------------------------------------')	#60個

continuous_vars = [
    'Customer Lifetime Value', 'Income', 'Monthly Premium Auto', 
    'Months Since Last Claim', 'Months Since Policy Inception', 
    'Number of Open Complaints', 'Number of Policies', 
    'Total Claim Amount'
]

logit = sm.Logit(df['Engaged'], df[continuous_vars])

logit_fit = logit.fit()

print('打印.summbary()資料')
print(logit_fit.summary())

print('------------------------------------------------------------')	#60個

print('Regression Analysis with Categorical Variables')
print('打印.describe()資料')
print(df.describe())

print('Different ways to handle categorical variables')

#1. factorize
labels, levels = df['Education'].factorize()
print('labels')
print(labels)
print('levels')
print(levels)

#2. pandas' Categorical variable series
categories = pd.Categorical(
    df['Education'], 
    categories=['High School or Below', 'Bachelor', 'College', 'Master', 'Doctor']
)

print('categories.categories')
print(categories.categories)
print('categories.codes')
print(categories.codes)

#3. dummy variables

print(pd.get_dummies(df['Education']).head(10))

print('------------------------------------------------------------')	#60個

#Adding Gender
gender_values, gender_labels = df['Gender'].factorize()
df['GenderFactorized'] = gender_values

print('gender_values')
print(gender_values)
print('gender_labels')
print(gender_labels)

print(df)

print('------------------------------------------------------------')	#60個

#Adding Education Level

categories = pd.Categorical(
    df['Education'], 
    categories=['High School or Below', 'Bachelor', 'College', 'Master', 'Doctor']
)

print('categories.codes')
print(categories.codes)
print('categories.categories')
print(categories.categories)

df['EducationFactorized'] = categories.codes

print('打印df.head()')
print(df.head())

print('------------------------------------------------------------')	#60個

#Regression Analysis with Categorical Variables

logit = sm.Logit(
    df['Engaged'], 
    df[[
        'GenderFactorized',
        'EducationFactorized'
    ]]
)

logit_fit = logit.fit()

print(logit_fit)

print('打印.summbary()資料')
print(logit_fit.summary())

print('------------------------------------------------------------')	#60個

#Regression Analysis with Both Continuous and Categorical Variables

logit = sm.Logit(
    df['Engaged'], 
    df[['Customer Lifetime Value',
        'Income',
        'Monthly Premium Auto',
        'Months Since Last Claim',
        'Months Since Policy Inception',
        'Number of Open Complaints',
        'Number of Policies',
        'Total Claim Amount',
        'GenderFactorized',
        'EducationFactorized'
    ]]
)

logit_fit = logit.fit()

print(logit_fit)

print('打印.summbary()資料')
print(logit_fit.summary())

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
'''
#From Engagement to Conversions

#1. Loading Data
df = pd.read_csv('data/bank-full.csv', sep=";")

print(df.shape)
print(df.head())

df['conversion'] = df['y'].apply(lambda x: 0 if x == 'no' else 1)
print(df.head())

#2. Data Analysis
print(list(df.columns))


#Conversion Rate
conversion_rate_df = pd.DataFrame(
    df.groupby('conversion').count()['y'] / df.shape[0] * 100.0
)

print(conversion_rate_df)

print(conversion_rate_df.T)

#Conversion Rates by Marital Status

conversion_rate_by_marital = df.groupby(
    by='marital'
)['conversion'].sum() / df.groupby(
    by='marital'
)['conversion'].count() * 100.0

print(conversion_rate_by_marital)

ax = conversion_rate_by_marital.plot(
    kind='bar',
    color='skyblue',
    grid=True,
    figsize=(10, 7),
    title='Conversion Rates by Marital Status'
)

ax.set_xlabel('Marital Status')
ax.set_ylabel('conversion rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個

#Conversion Rates by Job

conversion_rate_by_job = df.groupby(
    by='job'
)['conversion'].sum() / df.groupby(
    by='job'
)['conversion'].count() * 100.0

print(conversion_rate_by_job)

ax = conversion_rate_by_job.plot(
    kind='barh',
    color='skyblue',
    grid=True,
    figsize=(10, 7),
    title='Conversion Rates by Job'
)

ax.set_xlabel('conversion rate (%)')
ax.set_ylabel('Job')

plt.show()

print('------------------------------------------------------------')	#60個

#Default Rates by Conversions

default_by_conversion_df = pd.pivot_table(
    df, 
    values='y', 
    index='default', 
    columns='conversion', 
    aggfunc=len
)

print(default_by_conversion_df)

default_by_conversion_df.columns = ['non_conversions', 'conversions']

print(default_by_conversion_df)

default_by_conversion_df.plot(
    kind='pie',
    figsize=(15, 7),
    startangle=90,
    subplots=True,
    autopct=lambda x: '%0.1f%%' % x
)

plt.show()

print('------------------------------------------------------------')	#60個

#Bank Balance by Conversions

ax = df[['conversion', 'balance']].boxplot(
    by='conversion',
    showfliers=True,
    figsize=(10, 7)
)

ax.set_xlabel('Conversion')
ax.set_ylabel('Average Bank Balance')
ax.set_title('Average Bank Balance Distributions by Conversion')

plt.suptitle("")
plt.show()

print('------------------------------------------------------------')	#60個

ax = df[['conversion', 'balance']].boxplot(
    by='conversion',
    showfliers=False,
    figsize=(10, 7)
)

ax.set_xlabel('Conversion')
ax.set_ylabel('Average Bank Balance')
ax.set_title('Average Bank Balance Distributions by Conversion')

plt.suptitle("")
plt.show()

print('------------------------------------------------------------')	#60個

#Conversions by Number of Contacts

conversions_by_num_contacts = df.groupby(
    by='campaign'
)['conversion'].sum() / df.groupby(
    by='campaign'
)['conversion'].count() * 100.0

print(pd.DataFrame(conversions_by_num_contacts))

ax = conversions_by_num_contacts.plot(
    kind='bar',
    figsize=(10, 7),
    title='Conversion Rates by Number of Contacts',
    grid=True,
    color='skyblue'
)

ax.set_xlabel('Number of Contacts')
ax.set_ylabel('Conversion Rate (%)')

plt.show()

print('------------------------------------------------------------')	#60個

#3. Encoding Categorical Variables

print(list(df.columns))

print(df.describe())

categorical_vars = [
    'job',
    'marital',
    'education',
    'default',
    'housing',
    'loan',
    'contact',
    'month'
]

print(df[categorical_vars].nunique())

#encoding 'month'

print(df['month'].unique())

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

df['month'] = df['month'].apply(
    lambda x: months.index(x) + 1
)

print(df['month'].unique())

print(df.groupby('month').count()['conversion'])

#encoding 'job'

print(df['job'].unique())

jobs_encoded_df = pd.get_dummies(df['job'])
jobs_encoded_df.columns = ['job_%s' % x for x in jobs_encoded_df.columns]

print(jobs_encoded_df.head())

df = pd.concat([df, jobs_encoded_df], axis=1)
print(df.head())

#encoding 'marital'

marital_encoded_df = pd.get_dummies(df['marital'])
marital_encoded_df.columns = ['marital_%s' % x for x in marital_encoded_df.columns]

print(marital_encoded_df.head())

df = pd.concat([df, marital_encoded_df], axis = 1)
print(df.head())

#encoding 'housing'

print(df['housing'].unique())

df['housing'] = df['housing'].apply(lambda x: 1 if x == 'yes' else 0)

#encoding 'loan'

print(df['loan'].unique())

df['loan'] = df['loan'].apply(lambda x: 1 if x == 'yes' else 0)

#4. Fitting Decision Trees

features = [
    'age',
    'balance',
    'campaign',
    'previous',
    'housing',
] + list(jobs_encoded_df.columns) + list(marital_encoded_df.columns)

response_var = 'conversion'

print(features)

from sklearn import tree

dt_model = tree.DecisionTreeClassifier(max_depth=4)

print(dt_model.fit(df[features], df[response_var]))

print(dt_model.classes_)

# 決策樹可視化

import graphviz

dot_data = tree.export_graphviz(
    dt_model, 
    out_file=None, 
    feature_names=features,  
    class_names=['0', '1'],  
    filled=True, 
    rounded=True,  
    special_characters=True
)

graph = graphviz.Source(dot_data)

from IPython.display import display
from IPython.core.display import HTML

display(HTML("<style>text {font-size: 10px;}</style>"))

print(graph)

#或許可以存.dot檔

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
sys.exit()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
