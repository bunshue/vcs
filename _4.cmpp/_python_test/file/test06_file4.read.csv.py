#python讀取CSV檔

from urllib.request import urlopen
from io import StringIO
import csv

#讀取遠端的檔案
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')

#讀取當地的檔案
#data = open("MontyPythonAlbums.local.csv").read()

dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
	print("The album \""+row[0]+"\" was released in "+str(row[1]))

