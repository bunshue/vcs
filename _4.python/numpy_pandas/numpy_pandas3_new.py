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

broken_df = pd.read_csv('data/bikes.csv', encoding = "ISO-8859-1")

# Look at the first 3 rows
print(broken_df[:3])

print('------------------------------------------------------------')	#60個

fixed_df = pd.read_csv('data/bikes.csv', sep = ';', encoding = 'latin1', parse_dates = ['Date'], dayfirst=True, index_col='Date')
print(fixed_df[:3])

print(fixed_df['Berri 1'])

fixed_df['Berri 1'].plot()

plt.show()


fixed_df.plot(figsize=(15, 10))

plt.show()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
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
complaints = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

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
complaints = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

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


bikes = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
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

bikes = pd.read_csv('data/bikes.csv', 
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


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

#Canada's weather data for 2012, and saved it to a CSV.
#Here's the temperature every hour for 2012!

weather_2012_final = pd.read_csv('data/weather_2012.csv', index_col='Date/Time')
weather_2012_final['Temp (C)'].plot(figsize=(15, 6))

plt.show()

print('------------------------------------------------------------')	#60個

#Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

#To get the data for March 2013, we need to format it with month=3, year=2012.
#url = url_template.format(month=3, year=2012)
#weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

# because the url is broken, we use our saved dataframe for now
weather_mar2012 = pd.read_csv('data/weather_2012.csv')

print(weather_mar2012)


weather_mar2012[u"Temp (C)"].plot(figsize=(15, 5))
plt.show()


# '\xb0' for that degree character °
""" fail
weather_mar2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)', 
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag', 
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag', 
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill', 
    u'Wind Chill Flag', u'Weather']
"""

weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
print(weather_mar2012[:5])

print('------------------------------------------------------------')	#60個

#fail
#weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
#print(weather_mar2012[:5])

print('------------------------------------------------------------')	#60個


#Plotting the temperature by hour of day

"""fail
temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()

plt.show()
"""

print('------------------------------------------------------------')	#60個

""" fail in reading csv data
#5.3 Getting the whole year of data

def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = 'weather_2012.csv'
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


cc = download_weather_month(2012, 1)[:5]
print(cc)

data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

weather_2012 = pd.concat(data_by_month)
print(weather_2012)

#save to csv file
weather_2012.to_csv('tmp_weather_2012.csv')
"""

print('------------------------------------------------------------')	#60個

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



