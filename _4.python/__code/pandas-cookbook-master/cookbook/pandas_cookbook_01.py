import os
import sys
import time
import random

import pandas as pd
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

print('------------------------------------------------------------')	#60個

broken_df = pd.read_csv('../data/bikes.csv', encoding = "ISO-8859-1")

# Look at the first 3 rows
print(broken_df[:3])

print('------------------------------------------------------------')	#60個

fixed_df = pd.read_csv('../data/bikes.csv', sep = ';', encoding = 'latin1', parse_dates = ['Date'], dayfirst=True, index_col='Date')
print(fixed_df[:3])

print(fixed_df['Berri 1'])

fixed_df['Berri 1'].plot()

plt.show()


fixed_df.plot(figsize=(15, 10))

plt.show()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
df['Berri 1'].plot()

plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

# because of mixed types we specify dtype to prevent any errors
complaints = pd.read_csv('../data/311-service-requests.csv', dtype='unicode')

print(complaints)
complaints['Complaint Type']

complaints['Complaint Type'].value_counts()

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

complaint_counts[:10].plot(kind='bar')
plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)


# because of mixed types we specify dtype to prevent any errors
complaints = pd.read_csv('../data/311-service-requests.csv', dtype='unicode')

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

noise_complaint_counts / complaint_counts

noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)


bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
bikes['Berri 1'].plot()
plt.show()


berri_bikes = bikes[['Berri 1']].copy()


berri_bikes[:5]



berri_bikes.index


berri_bikes.index.day

berri_bikes.index.weekday

berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
berri_bikes[:5]


weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts


weekday_counts.plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

bikes = pd.read_csv('../data/bikes.csv', 
                    sep=';', encoding='latin1', 
                    parse_dates=['Date'], dayfirst=True, 
                    index_col='Date')
# Add the weekday column
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')


plt.show()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





