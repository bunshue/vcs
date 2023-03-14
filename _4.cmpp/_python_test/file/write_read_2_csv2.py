#各種檔案寫讀範例 csv 2

from urllib.request import urlopen
from io import StringIO
import csv

#遠端檔案
filename_r1 = "http://pythonscraping.com/files/MontyPythonAlbums.csv"
print("讀取一個遠端csv檔案 : "+filename_r1)

#本地檔案
filename_r2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/MontyPythonAlbums.local.csv'

print("讀取一個本地csv檔案 : "+filename_r2)

#讀取遠端檔案
#data = urlopen(filename_r1).read().decode('ascii', 'ignore')

#讀取本地檔案
data = open(filename_r2).read()

dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
	print("The album \""+row[0]+"\" was released in "+str(row[1]))
