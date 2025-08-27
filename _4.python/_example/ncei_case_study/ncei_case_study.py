"""
美國國家環境資訊中心
National Centers for Environmental Information，簡稱：NCEI


"""

import sys
import os
import requests
import matplotlib.pyplot as plt
import numpy as np

r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt')
readme = r.text
print(readme)

filename1 = 'inventory.txt'
filename2 = 'stations.txt'

if os.path.exists(filename1):
    print('檔案存在')
    with open(filename1, "r", encoding = 'UTF-8') as inventory_file:
        inventory_txt = inventory_file.read()
else:
    print('檔案不存在')
    r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt')
    inventory_txt = r.text
    with open("inventory.txt", "w", encoding = 'UTF-8') as inventory_file:
        inventory_file.write(inventory_txt)

if os.path.exists(filename2):
    print('檔案存在')
    with open(filename2, "r", encoding = 'UTF-8') as stations_file:
        stations_txt = stations_file.read()
else:
    print('檔案不存在')
    r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt')
    stations_txt = r.text
    with open("stations.txt", "w", encoding = 'UTF-8') as stations_file:
        stations_file.write(stations_txt)

print(inventory_txt[:137])

# parse to named tuples
# use namedtuple to create a custom Inventory class
from collections import namedtuple
Inventory = namedtuple("Inventory", ['station', 'latitude', 'longitude', 'element', 'start', 'end'])

# parse inventory lines and convert some values to floats and ints
inventory = [Inventory(x[0:11], float(x[12:20]), float(x[21:30]), x[31:35], int(x[36:40]), int(x[41:45]))
             for x in inventory_txt.split("\n") if x.startswith("US")]

for line in inventory[:5]:
    print(line)

#Selecting a station based on latitude and longitude
inventory_temps = [x for x in inventory if x.element in ['TMIN', 'TMAX'] 
                   and x.end >= 2015 and x.start < 1920]
inventory_temps[:5]

# Downtown Chicago, obtained via online map
latitude, longitude = 41.882, -87.629

inventory_temps.sort(key=lambda x:  abs(latitude-x.latitude) + abs(longitude-x.longitude))

print(inventory_temps[:20])

#Selecting a station and getting the station metadata

station_id = 'USC00110338'

# parse stations
Station = namedtuple("Station", ['station_id', 'latitude', 'longitude', 'elevation', 'state', 'name', 'start', 'end'])

stations = [(x[0:11], float(x[12:20]), float(x[21:30]), float(x[31:37]), x[38:40].strip(), x[41:71].strip())
            for x in stations_txt.split("\n") if x.startswith(station_id)]

station = Station(*stations[0] + (inventory_temps[0].start, inventory_temps[0].end))
print(station)


# Fetching and parsing the actual weather data

# fetch daily records for selected station
r = requests.get('https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/all/{}.dly'.format(station.station_id))
weather = r.text

# save into a text file, so we won't need to fetch again
with open('weather_{}.txt'.format(station), "w") as weather_file:
    weather_file.write(weather)

# read from saved daily file if needed (only used if we want to start the process over without downloadng the file)
with open('weather_{}.txt'.format(station)) as weather_file:
    weather = weather_file.read()

print(weather[:540])

#Parsing the weather data

def parse_line(line):
    """ parses line of weather data
        removes values of -9999 (missing value)
    """
    
    # return None if line is empty
    if not line:
        return None
    
    # split out first 4 fields and string containing temperature values
    record, temperature_string = (line[:11], int(line[11:15]), int(line[15:17]), line[17:21]), line[21:] 
    
    # raise exception if the temperature string is too short
    if len(temperature_string) < 248:
        raise ValueError("String not long enough - {} {}".format(temperature_string, str(line)))
        
    # use a list comprehension on the temperature_string to extract and convert the 
    values = [float(temperature_string[i:i + 5])/10 for i in range(0, 248, 8)
              if not temperature_string[i:i + 5].startswith("-9999")]
    
    # get the number of values, the max and min, and calculate average
    count = len(values)
    tmax = round(max(values), 1)
    tmin = round(min(values), 1)
    mean = round(sum(values)/count, 1)

    # add the temperature summary values to the record fields extracted earlier and return
    return record + (tmax, tmin, mean, count)

# If we test this function with the first line of our raw weather data, we get the following result:

print(parse_line(weather[:270]))


# So it looks like we have a function that will work to parse our data.
# If that works then we can parse the weather data and either store it or continue on with our processing.

# process all weather data

# list comprehension, will not parse empty lines
weather_data = [parse_line(x) for x in weather.split("\n") if x]

len(weather_data)

print(weather_data[:10])


# We now have all the weather records, not just the temperature records, parsed and in our list. 



# ### Saving the weather data in a database (Optional)
# 
# At this point we can save all of the weather records (and the station records and inventory records as well, if we want) into a database.
# This would let us come back in later sessions and use the same data without having to go the hassle of fetching and parsing the data again. 
# 
# As an example, the code below would be how we could save the weather data into a SQLite3 database.


import time
#db_filename = 'D:/_git/vcs/_1.data/______test_files2/weather_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';
db_filename = 'weather_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.sqlite';

import sqlite3

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# create weather table
create_weather = """CREATE TABLE "weather" (
    "id" text NOT NULL,
    "year" integer NOT NULL,
    "month" integer NOT NULL,
    "element" text NOT NULL,
    "max" real,
    "min" real,
    "mean" real,
    "count" integer)"""
cursor.execute(create_weather)
conn.commit()

# store parsed weather data in database
for record in weather_data:
    cursor.execute("""insert into weather (id, year, month, element, max, min, mean, count) values (?,?,?,?,?,?,?,?) """, record)

conn.commit()

# Once we have the data stored we could retreive it from the database with code like the below, which fetches only the TMAX records.
cursor.execute("""select * from weather where element='TMAX' order by year, month""")
tmax_data = cursor.fetchall()
print(tmax_data[:5])

# ### Selecting and graphing data
# 
# Since we're only concerned with temperature we need to select just the temperature records.
# We can do that quickly enough by just usign a couple of list comprehensions to pick out a list for TMAX and one for TMIN.
# Or we could use the features of pandas, which we'll be using for graphing the date, to filter out the records we don't want.
#Since were more concerned with pure Python than pandas, we'll take the first approach.

tmax_data = [x for x in weather_data if x[3] == 'TMAX']
tmin_data = [x for x in weather_data if x[3] == 'TMIN']
print(tmin_data[:5])

# #### Using pandas to graph our data
# At this point we have our data cleaned and ready to graph.
# To make the graphing easier we can use pandas and matplotlib as described in chapter 24.
# In order to do this we need to have a Jupyter server running and have pandas and matplotlib installed.
# We can make sure that they are installed from within our Jupyter notebook by using the following command:

import pandas as pd

# Once pandas and matplotlib are installed we can load pandas and create data frames for our TMAX and TMIN data.

tmax_df = pd.DataFrame(tmax_data, columns=['Station', 'Year', 'Month', 'Element', 'Max', 'Min', 'Mean', 'Days'])
tmin_df = pd.DataFrame(tmin_data, columns=['Station', 'Year', 'Month', 'Element', 'Max', 'Min', 'Mean', 'Days'])


# We could plot the monthly values, but the 123 years times 12 months of data is almost 1500 data points,
# and the cycle of seasons also makes picking out patterns difficult. 
# Instead, it would probably make more sense to average the high, low, and mean monthly values into yearly values and plot those.
# We could do this in python, but since we already have our data loaded in a pandas data frame we can use that to group by year
# and give us the mean values.

# select Year, Min, Max, Mean columns, group by year, average and line plot
tmin_df[['Year','Min', 'Mean', 'Max']].groupby('Year').mean().plot( kind='line', figsize=(16, 4))
plt.show()


# The result above has a fair amount of variation, but does seem to indicate that the minimum temperature, at least,
# has been on the rise the past 20 years. 
# Note that if you wanted to get the same graph without using Jupyter notebook and matplotlib,
# you could use still use pandas, but write to a csv or excel file using the data frame's `to_csv` or `to_excel` methods.
# Then you could load the resulting file into a spreadsheet and graph from there. 

print('作業完成')
