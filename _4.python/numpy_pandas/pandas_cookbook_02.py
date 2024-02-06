import os
import sys
import time
import random

import pandas as pd
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
print(weather_2012[:5])

weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

# Not super useful
print(is_snowing[:5])

# More useful!
is_snowing=is_snowing.astype(float)
is_snowing.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#Use resampling to find the snowiest month

#If we wanted the median temperature each month, we could use the resample() method like this:

weather_2012['Temp (C)'].resample('M').apply(np.median).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個


print(is_snowing.astype(float)[:10])





print('------------------------------------------------------------')	#60個

print(is_snowing.astype(float).resample('M').apply(np.mean))

is_snowing.astype(float).resample('M').apply(np.mean).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

#Plotting temperature and snowiness stats together

temperature = weather_2012['Temp (C)'].resample('M').apply(np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M').apply(np.mean)

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"

#We'll use concat again to combine the two statistics into a single dataframe.
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

stats.plot(kind='bar')
plt.show()

#Uh, that didn't work so well because the scale was wrong. We can do better by plotting them on two separate graphs:

stats.plot(kind='bar', subplots=True, figsize=(15, 10))
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

print('------------------------------------------------------------')	#60個


#NYC 311 service request dataset
requests = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

cc = requests['Incident Zip'].unique()
print(cc)


print('------------------------------------------------------------')	#60個

#Fixing the nan values and string/float confusion

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

cc = requests['Incident Zip'].unique()
print(cc)


#What's up with the dashes?

rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
cc = len(requests[rows_with_dashes])
print(cc)

print(requests[rows_with_dashes])

#But then my friend Dave pointed out that 9-digit zip codes are normal.
#Let's look at all the zip codes with more than 5 digits, make sure they're okay, and then truncate them.
long_zip_codes = requests['Incident Zip'].str.len() > 5
cc = requests['Incident Zip'][long_zip_codes].unique()
print(cc)


requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

#Earlier I thought 00083 was a broken zip code, but turns out Central Park's zip code 00083!
#Shows what I know. I'm still concerned about the 00000 zip codes, though: let's look at that.
cc = requests[requests['Incident Zip'] == '00000']
print(cc)


zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

""" fail
unique_zips = requests['Incident Zip'].unique()
unique_zips.sort()
cc = unique_zips
print(cc)
"""
zips = requests['Incident Zip']
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse, and why?)
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~(is_close) & zips.notnull()

cc = zips[is_far]
print(cc)

cc = requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip')
print(cc)

cc = requests['City'].str.upper().value_counts()
print(cc)

print('------------------------------------------------------------')	#60個

#Putting it together

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv', 
                       na_values=na_values, 
                       dtype={'Incident Zip': str})

def fix_zip_codes(zips):
    # Truncate everything to length 5 
    zips = zips.str.slice(0, 5)
    
    # Set 00000 zip codes to nan
    zero_zips = zips == '00000'
    zips[zero_zips] = np.nan
    
    return zips

requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])

cc = requests['Incident Zip'].unique()
print(cc)





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#Parsing Unix timestamps

# Read it, and remove the last row
popcon = pd.read_csv('data/popularity-contest', sep=' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print(popcon[:5])

popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

print(popcon['atime'].dtype)


print(popcon[:5])

print('------------------------------------------------------------')	#60個

popcon = popcon[popcon['atime'] > '1970-01-01']

#不包含lib的
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

cc = nonlibraries.sort_values('ctime', ascending=False)[:10]
print(cc)



print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

#Reading data from SQL databases
import pandas as pd
import sqlite3

con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

print('------------------------------------------------------------')	#60個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col='id')
print(df)

print('------------------------------------------------------------')	#60個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, 
                 index_col=['id', 'date_time'])
print(df)

print('--------ddd----------------------------------------------------')	#60個

#Writing to a SQLite database

weather_df = pd.read_csv('data/weather_2012.csv')
con = sqlite3.connect("tmp_test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)


con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

print('------------------------------------------------------------')	#60個

"""
#Connecting to other kinds of database

#MySQL / PostgreSQL
import MySQLdb
con = MySQLdb.connect(host="localhost", db="test")

#To connect to a PostgreSQL database:
import psycopg2
con = psycopg2.connect(host="localhost")

"""






print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

