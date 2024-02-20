import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import pandas as pd

print('------------------------------------------------------------')	#60個
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

dt_model = tree.DecisionTreeClassifier(
    max_depth=4
)

print(dt_model.fit(df[features], df[response_var]))

print(dt_model.classes_)

#5. Interpreting Decision Tree Model

# pip install graphviz

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

from IPython.core.display import display, HTML
display(HTML("<style>text {font-size: 10px;}</style>"))

print(graph)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

