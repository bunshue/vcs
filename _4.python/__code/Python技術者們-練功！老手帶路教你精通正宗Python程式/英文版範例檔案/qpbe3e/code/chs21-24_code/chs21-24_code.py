import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個



21.2.1 Text encoding – ASCII, Unicode, and others

>>> open('test.txt', 'wb').write(bytes([65, 66, 67, 255, 192,193]))
6

>>> x = open('test.txt').read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.6/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte


>>> open('test.txt', errors='ignore').read()
'ABC'
>>> open('test.txt', errors='replace').read()
'ABC���'
>>> open('test.txt', errors='surrogateescape').read()
'ABC\udcff\udcc0\udcc1'
>>> open('test.txt', errors='backslashreplace').read()
'ABC\\xff\\xc0\\xc1'
>>>

21.2.2 Unstructured text

>>> moby_text = open("moby_01.txt").read()          #A reads all of file as a single string
>>> moby_paragraphs = moby_text.split("\n\n")       #B Splits on two newlines together
>>> print(moby_paragraphs[1])
There now is your insular city of the Manhattoes, belted round by wharves
as Indian isles by coral reefs--commerce surrounds it with her surf.
Right and left, the streets take you waterward.  Its extreme downtown
is the battery, where that noble mole is washed by waves, and cooled
by breezes, which a few hours previous were out of sight of land.
Look at the crowds of water-gazers there.



>>> moby_text = open("moby_01.txt").read()          #A reads all of file as a single string
>>> moby_paragraphs = moby_text.split("\n\n")       
>>> moby = moby_paragraphs[1].lower()                   #B Makes everything lower case
>>> moby = moby.replace(".", "")          #C Removes periods
>>> moby = moby.replace(",", "") 
>>> moby_words = moby.split()
>>> print(moby_words)
['there', 'now', 'is', 'your', 'insular', 'city', 'of', 'the', 'manhattoes,', 'belted', 'round', 'by', 'wharves', 'as', 'indian', 'isles', 'by', 'coral', 'reefs--commerce', 'surrounds', 'it', 'with', 'her', 'surf', 'right', 'and', 'left,', 'the', 'streets', 'take', 'you', 'waterward', 'its', 'extreme', 'downtown', 'is', 'the', 'battery,', 'where', 'that', 'noble', 'mole', 'is', 'washed', 'by', 'waves,', 'and', 'cooled', 'by', 'breezes,', 'which', 'a', 'few', 'hours', 'previous', 'were', 'out', 'of', 'sight', 'of', 'land', 'look', 'at', 'the', 'crowds', 'of', 'water-gazers', 'there']

21.2.4 The csv module

>>> results = []
>>> for line in open("temp_data_pipes_00a.txt"):
...     fields = line.strip().split("|")
...     results.append(fields)
... 
>>> results
[['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)'], ['Illinois', '1979/01/01', '17.48', '994'], ['Illinois', '1979/01/02', '4.64', '994'], ['Illinois', '1979/01/03', '11.05', '994'], ['Illinois', '1979/01/04', '9.51', '994'], ['Illinois', '1979/05/15', '68.42', '994'], ['Illinois', '1979/05/16', '70.29', '994'], ['Illinois', '1979/05/17', '75.34', '994'], ['Illinois', '1979/05/18', '79.13', '994'], ['Illinois', '1979/05/19', '74.94', '994']]


>>> import csv
>>> results = [fields for fields in csv.reader(open("temp_data_pipes_00a.txt"), delimiter="|")]
>>> results
[['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)'], ['Illinois', '1979/01/01', '17.48', '994'], ['Illinois', '1979/01/02', '4.64', '994'], ['Illinois', '1979/01/03', '11.05', '994'], ['Illinois', '1979/01/04', '9.51', '994'], ['Illinois', '1979/05/15', '68.42', '994'], ['Illinois', '1979/05/16', '70.29', '994'], ['Illinois', '1979/05/17', '75.34', '994'], ['Illinois', '1979/05/18', '79.13', '994'], ['Illinois', '1979/05/19', '74.94', '994']]


>>> results2 = [fields for fields in csv.reader(open("temp_data_01.csv", newline=''))]
>>> results2
[['Notes', 'State', 'State Code', 'Month Day, Year', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)', 'Min Temp for Daily Max Air Temp (F)', 'Max Temp for Daily Max Air Temp (F)', 'Avg Daily Min Air Temperature (F)', 'Record Count for Daily Min Air Temp (F)', 'Min Temp for Daily Min Air Temp (F)', 'Max Temp for Daily Min Air Temp (F)', 'Avg Daily Max Heat Index (F)', 'Record Count for Daily Max Heat Index (F)', 'Min for Daily Max Heat Index (F)', 'Max for Daily Max Heat Index (F)', 'Daily Max Heat Index (F) % Coverage'], ['', 'Illinois', '17', 'Jan 01, 1979', '1979/01/01', '17.48', '994', '6.00', '30.50', '2.89', '994', '-13.60', '15.80', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'Jan 02, 1979', '1979/01/02', '4.64', '994', '-6.40', '15.80', '-9.03', '994', '-23.60', '6.60', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'Jan 03, 1979', '1979/01/03', '11.05', '994', '-0.70', '24.70', '-2.17', '994', '-18.30', '12.90', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'Jan 04, 1979', '1979/01/04', '9.51', '994', '0.20', '27.60', '-0.43', '994', '-16.30', '16.30', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'May 15, 1979', '1979/05/15', '68.42', '994', '61.00', '75.10', '51.30', '994', '43.30', '57.00', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'May 16, 1979', '1979/05/16', '70.29', '994', '63.40', '73.50', '48.09', '994', '41.10', '53.00', 'Missing', '0', 'Missing', 'Missing', '0.00%'], ['', 'Illinois', '17', 'May 17, 1979', '1979/05/17', '75.34', '994', '64.00', '80.50', '50.84', '994', '44.30', '55.70', '82.60', '2', '82.40', '82.80', '0.20%'], ['', 'Illinois', '17', 'May 18, 1979', '1979/05/18', '79.13', '994', '75.50', '82.10', '55.68', '994', '50.00', '61.10', '81.42', '349', '80.20', '83.40', '35.11%'], ['', 'Illinois', '17', 'May 19, 1979', '1979/05/19', '74.94', '994', '66.90', '83.10', '58.59', '994', '50.90', '63.20', '82.87', '78', '81.60', '85.20', '7.85%']]

21.2.5 Reading a csv file as a list of dictionaries

import csv

>>> results = [fields for fields in csv.DictReader(open("temp_data_01.csv", newline=''))]
>>> results[0]
OrderedDict([('Notes', ''), ('State', 'Illinois'), ('State Code', '17'), ('Month Day, Year', 'Jan 01, 1979'), ('Month Day, Year Code', '1979/01/01'), ('Avg Daily Max Air Temperature (F)', '17.48'), ('Record Count for Daily Max Air Temp (F)', '994'), ('Min Temp for Daily Max Air Temp (F)', '6.00'), ('Max Temp for Daily Max Air Temp (F)', '30.50'), ('Avg Daily Max Heat Index (F)', 'Missing'), ('Record Count for Daily Max Heat Index (F)', '0'), ('Min for Daily Max Heat Index (F)', 'Missing'), ('Max for Daily Max Heat Index (F)', 'Missing'), ('Daily Max Heat Index (F) % Coverage', '0.00%')])


>>> results[0]['State']
'Illinois'

21.3 Excel files

>>> from openpyxl import load_workbook
>>> wb = load_workbook('temp_data_01.xlsx')
>>> results = []
>>> ws = wb.worksheets[0]
>>> for row in ws.iter_rows():
...     results.append([cell.value for cell in row])
...  
>>> print(results)
[['Notes', 'State', 'State Code', 'Month Day, Year', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)', 'Min Temp for Daily Max Air Temp (F)', 'Max Temp for Daily Max Air Temp (F)', 'Avg Daily Max Heat Index (F)', 'Record Count for Daily Max Heat Index (F)', 'Min for Daily Max Heat Index (F)', 'Max for Daily Max Heat Index (F)', 'Daily Max Heat Index (F) % Coverage'], [None, 'Illinois', 17, 'Jan 01, 1979', '1979/01/01', 17.48, 994, 6, 30.5, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 02, 1979', '1979/01/02', 4.64, 994, -6.4, 15.8, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 03, 1979', '1979/01/03', 11.05, 994, -0.7, 24.7, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'Jan 04, 1979', '1979/01/04', 9.51, 994, 0.2, 27.6, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 15, 1979', '1979/05/15', 68.42, 994, 61, 75.1, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 16, 1979', '1979/05/16', 70.29, 994, 63.4, 73.5, 'Missing', 0, 'Missing', 'Missing', '0.00%'], [None, 'Illinois', 17, 'May 17, 1979', '1979/05/17', 75.34, 994, 64, 80.5, 82.6, 2, 82.4, 82.8, '0.20%'], [None, 'Illinois', 17, 'May 18, 1979', '1979/05/18', 79.13, 994, 75.5, 82.1, 81.42, 349, 80.2, 83.4, '35.11%'], [None, 'Illinois', 17, 'May 19, 1979', '1979/05/19', 74.94, 994, 66.9, 83.1, 82.87, 78, 81.6, 85.2, '7.85%']]


21.5.1 CSV and other delimited files

>>> temperature_data = [['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)'], ['Illinois', '1979/01/01', '17.48', '994'], ['Illinois', '1979/01/02', '4.64', '994'], ['Illinois', '1979/01/03', '11.05', '994'], ['Illinois', '1979/01/04', '9.51', '994'], ['Illinois', '1979/05/15', '68.42', '994'], ['Illinois', '1979/05/16', '70.29', '994'], ['Illinois', '1979/05/17', '75.34', '994'], ['Illinois', '1979/05/18', '79.13', '994'], ['Illinois', '1979/05/19', '74.94', '994']]
>>> csv.writer(open("temp_data_03.csv", "w", newline='')).writerows(temperature_data)


>>> fields = ['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)']
>>> dict_writer = csv.DictWriter(open("temp_data_04.csv", "w"), fieldnames=fields)
>>> dict_writer.writeheader()
>>> dict_writer.writerows(fie)
>>> del dict_writer

21.5.2 Writing Excel files

>>> import csv
>>> from openpyxl import Workbook
>>> data_rows = [fields for fields in csv.reader(open("temp_data_01.csv"))]
>>> wb = Workbook()
>>> ws = wb.active
>>> ws.title = "temperature data"
>>> for row in data_rows:
...     ws.append(row)
... 
>>> wb.save("temp_data_02.xlsx")



22.1.1 Using Python to fetch files from an FTP server

>>> import ftplib
>>> ftp = ftplib.FTP('tgftp.nws.noaa.gov')
>>> ftp.login()
'230 Login successful.'

>>> ftp.cwd('data')
'250 Directory successfully changed.'
>>> ftp.nlst()
['climate', 'fnmoc', 'forecasts', 'hurricane_products', 'ls_SS_services', 'marine', 'nsd_bbsss.txt', 'nsd_cccc.txt', 'observations', 'products', 'public_statement', 'raw', 'records', 'summaries', 'tampa', 'watches_warnings', 'zonecatalog.curr', 'zonecatalog.curr.tar']


>>> x = ftp.retrbinary('RETR observations/metar/decoded/KORD.TXT', open('KORD.TXT', 'wb').write)
'226 Transfer complete.'

22.1.2 Fetching files with SFTP

>>> import paramiko
>>> t = paramiko.Transport((hostname, port))
>>> t.connect(username, password)
>>> sftp = paramiko.SFTPClient.from_transport(t)

22.1.3 Retrieving files over HTTP/HTTPS

>>> import requests 
>>> response = requests.get("http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt")


>>> print(response.text)
Heathrow (London Airport)
Location 507800E 176700N, Lat 51.479 Lon -0.449, 25m amsl
Estimated data is marked with a * after the value.
Missing data (more than 2 days missing in month) is marked by  ---.
Sunshine data taken from an automatic Kipp & Zonen sensor marked with a #, otherwise sunshine data taken from a Campbell Stokes recorder.
   yyyy  mm   tmax    tmin      af    rain     sun
              degC    degC    days      mm   hours
   1948   1    8.9     3.3    ---     85.0    ---
   1948   2    7.9     2.2    ---     26.0    ---
   1948   3   14.2     3.8    ---     14.0    ---
   1948   4   15.4     5.1    ---     35.0    ---
   1948   5   18.1     6.9    ---     57.0    ---

22.2 Fetching data via an API

>>> import requests
>>> response = requests.get("http://marsweather.ingenology.com/v1/latest/?format=json")
>>> response.text
'{"report": {"terrestrial_date": "2017-01-08", "sol": 1573, "ls": 295.0, "min_temp": -74.0, "min_temp_fahrenheit": -101.2, "max_temp": -2.0, "max_temp_fahrenheit": 28.4, "pressure": 872.0, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": null, "wind_direction": "--", "atmo_opacity": "Sunny", "season": "Month 10", "sunrise": "2017-01-08T12:29:00Z", "sunset": "2017-01-09T00:45:00Z"}}'
>>> response = requests.get("http://marsweather.ingenology.com/v1/archive/?sol=155&format=json")
>>> response.text
'{"count": 1, "next": null, "previous": null, "results": [{"terrestrial_date": "2013-01-18", "sol": 155, "ls": 243.7, "min_temp": -64.45, "min_temp_fahrenheit": -84.01, "max_temp": 2.15, "max_temp_fahrenheit": 35.87, "pressure": 9.175, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": 2.0, "wind_direction": null, "atmo_opacity": null, "season": "Month 9", "sunrise": null, "sunset": null}]}'

22.3.1 JSON data

>>> import json
>>> import requests
>>> response = requests.get("http://marsweather.ingenology.com/v1/latest/?format=json")
>>> weather = json.loads(response.text)
>>> weather
{'report': {'terrestrial_date': '2017-01-10', 'sol': 1575, 'ls': 296.0, 'min_temp': -58.0, 'min_temp_fahrenheit': -72.4, 'max_temp': 0.0, 'max_temp_fahrenheit': None, 'pressure': 860.0, 'pressure_string': 'Higher', 'abs_humidity': None, 'wind_speed': None, 'wind_direction': '--', 'atmo_opacity': 'Sunny', 'season': 'Month 10', 'sunrise': '2017-01-10T12:30:00Z', 'sunset': '2017-01-11T00:46:00Z'}}
>>> weather['report']['sol']
1575

>>> from pprint import pprint as pp
>>> pp(weather)
{'report': {'abs_humidity': None,
            'atmo_opacity': 'Sunny',
            'ls': 296.0,
            'max_temp': 0.0,
            'max_temp_fahrenheit': None,
            'min_temp': -58.0,
            'min_temp_fahrenheit': -72.4,
            'pressure': 860.0,
            'pressure_string': 'Higher',
            'season': 'Month 10',
            'sol': 1575,
            'sunrise': '2017-01-10T12:30:00Z',
            'sunset': '2017-01-11T00:46:00Z',
            'terrestrial_date': '2017-01-10',
            'wind_direction': '--',
            'wind_speed': None}}

>>> outfile = open("mars_data_01.json", "w")
>>> json.dump(weather, outfile)
>>> outfile.close()
>>> json.dumps(weather)
'{"report": {"terrestrial_date": "2017-01-11", "sol": 1576, "ls": 296.0, "min_temp": -72.0, "min_temp_fahrenheit": -97.6, "max_temp": -1.0, "max_temp_fahrenheit": 30.2, "pressure": 869.0, "pressure_string": "Higher", "abs_humidity": null, "wind_speed": null, "wind_direction": "--", "atmo_opacity": "Sunny", "season": "Month 10", "sunrise": "2017-01-11T12:31:00Z", "sunset": "2017-01-12T00:46:00Z"}}'



>>> print(json.dumps(weather, indent=2))
{
  "report": {
    "terrestrial_date": "2017-01-10",
    "sol": 1575,
    "ls": 296.0,
    "min_temp": -58.0,
    "min_temp_fahrenheit": -72.4,
    "max_temp": 0.0,
    "max_temp_fahrenheit": null,
    "pressure": 860.0,
    "pressure_string": "Higher",
    "abs_humidity": null,
    "wind_speed": null,
    "wind_direction": "--",
    "atmo_opacity": "Sunny",
    "season": "Month 10",
    "sunrise": "2017-01-10T12:30:00Z",
    "sunset": "2017-01-11T00:46:00Z"
  }
}

>>> outfile = open("mars_data.json", "w")
>>> for report in weather_list:
...     json.dump(weather, outfile) 
>>> outfile.close()


>>> for line in open("mars_data.json"):
...     weather_list.append(json.loads(line))


>>> outfile = open("mars_data.json", "w")
>>> weather_obj = {"reports": weather_list, "count": 2} 
>>> json.dump(weather, outfile)
>>> outfile.close()


>>> with open("mars_data.json") as infile:
>>> weather_obj = json.load(infile)

22.3.2 XML data

>>> import xmltodict
>>> data = xmltodict.parse(open("observations_01.xml").read())

22.4 Scraping web data

>>> import bs4
>>> html = open("test.html").read()
>>> bs = bs4.BeautifulSoup(html, "html.parser")


>>> a_list = bs("a")
>>> print(a_list)
[<a href="http://bitbucket.dev.null">link</a>]


>>> a_item = a_list[0]
>>> a_item.text
'link'
>>> a_item["href"]
'http://bitbucket.dev.null'


>>> special_list = bs.select(".special")
>>> print(special_list)
[<span class="special">this is special</span>]
>>> special_item = special_list[0]
>>> special_item.text
'this is special'
>>> special_item["class"]
['special']



23.2 SQLite - using the sqlite3 database

>>> import sqlite3
>>> conn = sqlite3.connect("datafile.db")


>>> cursor = conn.cursor()
>>> cursor
<sqlite3.Cursor object at 0xb7a12980>


>>> cursor.execute("create table people (id integer primary key, name text, count integer)")
<sqlite3.Cursor object at 0x7fef111031f0>
>>> cursor.execute("insert into people (name, count) values ('Bob', 1)")
>>> cursor.execute("insert into people (name, count) values (?, ?)", 
...                ("Jill", 15))
<sqlite3.Cursor object at 0x7fef111031f0>
>>> conn.commit()


>>> cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount": 10})


>>> result = cursor.execute("select * from people")
>>> print(result.fetchall())
[(1, 'Bob', 1), (2, 'Jill', 15), (3, 'Joe', 10)]
>>> result = cursor.execute("select * from people where name like :name", 
...                         {"name": "bob"})
>>> print(result.fetchall())
[(1, 'Bob', 1)]
>>> cursor.execute("update people set count=? where name=?", (20, "Jill"))
>>> result = cursor.execute("select * from people")
>>> print(result.fetchall())
[(1, 'Bob', 1), (2, 'Jill', 20), (3, 'Joe', 10)]


>>> result = cursor.execute("select * from people")
>>> for row in result:
...     print(row)
... 
(1, 'Bob', 1)
(2, 'Jill', 20)
(3, 'Joe', 10)


>>> cursor.execute("update people set count=? where name=?", (20, "Jill"))
>>> conn.commit()
>>> conn.close()

23.4.1 SQLAlchemy

>>> from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
>>> from sqlalchemy.orm import sessionmaker


>>> dbPath = 'datafile2.db'
>>> engine = create_engine('sqlite:///%s' % dbPath)
>>> metadata = MetaData(engine)
>>> people  = Table('people', metadata, 
...                 Column('id', Integer, primary_key=True),
...                 Column('name', String),
...                 Column('count', Integer),
...                )
>>> Session = sessionmaker(bind=engine)
>>> session = Session()
>>> metadata.create_all(engine)


>>> people_ins = people.insert().values(name='Bob', count=1)
>>> str(people_ins)
'INSERT INTO people (name, count) VALUES (?, ?)'
>>> session.execute(people_ins)
<sqlalchemy.engine.result.ResultProxy object at 0x7f126c6dd438>
>>> session.commit()


>>> session.execute(people_ins, [
...     {'name': 'Jill', 'count':15},
...     {'name': 'Joe', 'count':10}
... ])
<sqlalchemy.engine.result.ResultProxy object at 0x7f126c6dd908>
>>> session.commit()
>>> result = session.execute(select([people]))
>>> for row in result:
...     print(row)
... 
(1, 'Bob', 1)
(2, 'Jill', 15)
(3, 'Joe', 10)


>>> result = session.execute(select([people]).where(people.c.name == 'Jill'))
>>> for row in result:
...     print(row)
... 
(2, 'Jill', 15)


>>> result = session.execute(people.update().values(count=20).where(people.c.name == 'Jill'))
>>> session.commit()
>>> result = session.execute(select([people]).where(people.c.name == 'Jill'))
>>> for row in result:
...     print(row)
... 
(2, 'Jill', 20)
>>> 


>>> from sqlalchemy.ext.declarative import declarative_base
>>> Base = declarative_base()
>>> class People(Base):
...     __tablename__ = "people"
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     count = Column(Integer)
...
>>> results = session.query(People).filter_by(name='Jill')
>>> for person in results:
...     print(person.id, person.name, person.count)
... 
2 Jill 20


>>> new_person = People(name='Jane', count=5)
>>> session.add(new_person)
>>> session.commit()
>>> 
>>> results = session.query(People).all()
>>> for person in results:
...     print(person.id, person.name, person.count)
... 
1 Bob 1
2 Jill 20
3 Joe 10
4 Jane 5


>>> jill = session.query(People).filter_by(name='Jill').first()
>>> jill.name
'Jill'
>>> jill.count = 22
>>> session.add(jill)
>>> session.commit()
>>> results = session.query(People).all()
>>> for person in results:
...     print(person.id, person.name, person.count)
... 
1 Bob 1
2 Jill 22
3 Joe 10
4 Jane 5


>>> jane = session.query(People).filter_by(name='Jane').first()
>>> session.delete(jane)
>>> session.commit()
>>> jane = session.query(People).filter_by(name='Jane').first()
>>> print(jane)
None

23.6 Key:value stores with Redis

>>> import redis
>>> r = redis.Redis(host='localhost', port=6379)


>>> r.keys()
[]
>>> r.set('a_key', 'my value')
True
>>> r.keys()
[b'a_key']
>>> v = r.get('a_key')
>>> v
b'my value'
>>> r.incr('counter')
1
>>> r.get('counter')
b'1'
>>> r.incr('counter')
2
>>> r.get('counter')
b'2'


>>> r.rpush("words", "one")
1
>>> r.rpush("words", "two")
2
>>> r.lrange("words", 0, -1)
[b'one', b'two']
>>> r.rpush("words", "three")
3
>>> r.lrange("words", 0, -1)
[b'one', b'two', b'three']
>>> r.llen("words")
3
>>> r.lpush("words", "zero")
4
>>> r.lrange("words", 0, -1)
[b'zero', b'one', b'two', b'three']
>>> r.lrange("words", 2, 2)
[b'two']
>>> r.lindex("words", 1)
b'one'
>>> r.lindex("words", 2)
b'two'


>>> r.setex("timed", "10 seconds", 10)
True
>>> r.pttl("timed")
7165
>>> r.pttl("timed")
5208
>>> r.pttl("timed")
1542
>>> r.pttl("timed")
>>>

23.7 Documents in MongoDB

>>> from pymongo import MongoClient
>>> mongo = MongoClient(host='localhost', port=27017)   #A


>>> import datetime
>>> a_document = {'name': 'Jane',
...               'age': 34,
...               'interests': ['Python', 'databases', 'statistics'],
...               'date_added': datetime.datetime.now()
... }
>>> db = mongo.my_data     #A
>>> collection = db.docs   #B 
>>> collection.find_one()  #C 
>>> db.collection_names()
[]


>>> collection.insert(a_document)
ObjectId('59701cc4f5ef0516e1da0dec')    #A
>>> db.collection_names()
['docs']


>>> collection.find_one()   #A
{'_id': ObjectId('59701cc4f5ef0516e1da0dec'), 'name': 'Jane', 'age': 34, 'interests': ['Python', 'databases', 'statistics'], 'date_added': datetime.datetime(2017, 7, 19, 21, 59, 32, 752000)}
>>> from bson.objectid import ObjectId
>>> collection.find_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')}) #B
{'_id': ObjectId('59701cc4f5ef0516e1da0dec'), 'name': 'Jane', 'age': 34, 'interests': ['Python', 'databases', 'statistics'], 'date_added': datetime.datetime(2017, 7, 19, 21, 59, 32, 752000)}
>>> collection.update_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')}, {"$set": {"name":"Ann"}}) #C
<pymongo.results.UpdateResult object at 0x7f4ebd601d38>
>>> collection.find_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')})
{'_id': ObjectId('59701cc4f5ef0516e1da0dec'), 'name': 'Ann', 'age': 34, 'interests': ['Python', 'databases', 'statistics'], 'date_added': datetime.datetime(2017, 7, 19, 21, 59, 32, 752000)}
>>> collection.replace_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')}, {"name":"Ann"})   #D
<pymongo.results.UpdateResult object at 0x7f4ebd601750>
>>> collection.find_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')})
{'_id': ObjectId('59701cc4f5ef0516e1da0dec'), 'name': 'Ann'}
>>> collection.delete_one({"_id":ObjectId('59701cc4f5ef0516e1da0dec')})     #E
<pymongo.results.DeleteResult object at 0x7f4ebd601d80>
>>> collection.find_one()


>>> db.collection_names()
['docs']
>>> collection.drop()
>>> db.collection_names()
[]





# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas matplotlib numpy')


# In[2]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np


# In[3]:


grid = [[1,2,3], [4,5,6], [7,8,9]]
print(grid)

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[4]:


import pandas as pd
df = pd.DataFrame(grid)
print(df)


# In[5]:


df = pd.DataFrame(grid, columns=["one", "two", "three"] )
print(df)


# In[6]:


print(df["two"])


# In[7]:


print([x[1] for x in grid])
[2, 5, 8]


# In[8]:


for x in df["two"]:
    print(x)


# In[9]:


edges = df[["one", "three"]]
print(edges)


# In[10]:


print(edges.add(2))


# In[11]:


df['two'].value_counts()


# In[18]:


mars = pd.read_json("mars_data_01.json")
print(mars)


# In[27]:


temp = pd.read_csv("temp_data_01.csv", header=0, names=range(18), usecols=range(4,18))


# In[28]:


print(temp)


# In[26]:


temp = pd.read_csv("temp_data_01.csv", na_values=['Missing'], header=0, names=range(18), usecols=range(4,18))
print(temp)


# In[29]:


temp[17][0]


# In[31]:


temp[17]=temp[17].str.strip("%")
temp[17][0]


# In[34]:


temp[17][0]


# In[32]:


temp[17] = pd.to_numeric(temp[17])
temp[17][0]


# In[33]:


temp[17] = temp[17].div(100)
temp[17]


# In[34]:


calls = pd.read_csv("sales_calls.csv")
print(calls)


# In[35]:


revenue = pd.read_csv("sales_revenue.csv")
print(revenue)


# In[37]:


calls_revenue = pd.merge(calls, revenue, on=['Territory', 'Month'])
print(calls_revenue)


# In[38]:


print(calls_revenue[calls_revenue.Territory==3])


# In[39]:


print(calls_revenue[calls_revenue.Amount/calls_revenue.Calls>500])


# In[40]:


calls_revenue['Call_Amount'] = calls_revenue.Amount/calls_revenue.Calls
print(calls_revenue)


# In[42]:


print(calls_revenue.Calls.sum())
print(calls_revenue.Calls.mean())
print(calls_revenue.Calls.median())
print(calls_revenue.Calls.max())
print(calls_revenue.Calls.min())


# In[43]:


print(calls_revenue[calls_revenue.Call_Amount >= calls_revenue.Call_Amount.median()])
print(calls_revenue.Call_Amount.median())


# In[45]:


print(calls_revenue[['Month', 'Calls', 'Amount']].groupby(['Month']).sum())


# In[46]:


print(calls_revenue[['Territory', 'Calls', 'Amount']].groupby(['Territory']).sum())


# In[47]:


calls_revenue[['Territory', 'Calls']].groupby(['Territory']).sum().plot.bar()


# In[152]:


calls_revenue[['Month', 'Call_Amount']].groupby(['Month']).mean().plot()


# In[ ]:






print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



