import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import pandas as pd

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


