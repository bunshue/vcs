'''
檔案讀寫 暫存1

'''
import sys

print('------------------------------------------------------------')	#60個


import csv

csvfile = "tmp_Example2.csv"
list1 = [[10,33,45], [5, 25, 56]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["Data1","Data2","Data3"])
    for row in list1:
        writer.writerow(row)

print("------------------------------------------------------------")  # 60個

print('讀取csv檔')
import csv

csvfile = "data/pl.csv"
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

csvfile = "tmp_pl2.csv"
lst1 = [["Python","Cuido van Rossum",1991,".py"],
        ["Java","James Gosling",1995,".java"],
        ["C++","Bjarne Stroustrup",1983,".cpp"]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["程式語言","開發者","上市年","副檔名"])
    for row in lst1:
        writer.writerow(row)
print('------------------------------------------------------------')	#60個

