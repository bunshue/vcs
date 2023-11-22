import sys

print('------------------------------------------------------------')	#60個

print('讀取csv檔')
import csv

csvfile = "pl.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print()
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

print('------------------------------------------------------------')	#60個

print('寫入csv檔')

import csv

csvfile = "pl2.csv"
lst1 = [["Python","Cuido van Rossum",1991,".py"],
        ["Java","James Gosling",1995,".java"],
        ["C++","Bjarne Stroustrup",1983,".cpp"]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["程式語言","開發者","上市年","副檔名"])
    for row in lst1:
        writer.writerow(row)
print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse

o = urlparse("http://www.example.com:80/test/index.php?user=joe")

print('使用urlparse()方法剖析URL網址成為組成的元素')
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

