#各種檔案寫讀範例 csv 1

#csv檔 逗號分隔值(comma-seperated values)


import csv

print("python寫資料到CSV檔 1")

filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/TestCSVFileW.csv'

print("打開一個csv檔案 : "+filename_w)
csvFile = open(filename_w, 'w+', newline='')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('column1', 'column2', 'column3'))
    writer.writerow((1,2,3))
    writer.writerow(('','','',4,5,6))   #前幾欄是空的
    writer.writerow((7,8,'',9))         #空一欄
    writer.writerow((7,8,9))
    writer.writerow(('a','b','c'))
    writer.writerow(('lion','mouse','cat','dog'))
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()

print("寫入檔案 " + filename_w + " 完成")



#各種檔案寫讀範例 csv 3

import csv

# 開啟 csv 檔案
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test1.csv'
with open(filename, newline='') as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row)


import csv
# 開啟 csv 檔案
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/test1.csv'
with open(filename, newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)   
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row['姓名'],row['身高'],row['體重'])
        
import csv
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/test3.csv'
with open(filename_w, 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'Chiou', '身高': 170, '體重': 65})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})
    
    
import csv
# 開啟輸出的 csv 檔案
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/test1.csv'
with open(filename_w, 'w', newline='') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入欄位名稱
  writer.writerow(['姓名', '身高', '體重'])
  # 寫入資料
  writer.writerow(['Chiou', 170, 65])
  writer.writerow(['David', 183, 78])
  
  
import csv
# 建立csv二維串列資料
csvtable = [
        ['姓名', '身高', '體重'],
        ['Chiou', 170, 65],
        ['David', 183, 78],
]

# 開啟輸出的 csv 檔案
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/test2.csv'
with open(filename_w, 'w', newline='') as csvfile:
    # 建立 csv 檔寫入物件
    writer = csv.writer(csvfile)

    # 寫入二維串列資料
    writer.writerows(csvtable)

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


#各種檔案寫讀範例 csv 4

import pandas as pd

scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)

print("另存新檔");
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/score_this.csv'
df.to_csv(filename, encoding='utf-8-sig')
print("寫入完成")


#各種檔案寫讀範例 csv 5

import numpy as np

print("讀取 .csv 檔 1")
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/scores.csv'
na = np.genfromtxt(filename, delimiter=',', skip_header=1)
print("資料寬高")
print(na.shape)

print('國文最高分數：', na[:,1].max())
print('英文最低分數：', na[:,2].min())
print('數學平均分數：', na[:,3].mean())
total1 = na[:,1] + na[:,2] + na[:,3]
print(total1)
print('全班最高總分：',total1.max())

total2 = na[:,1:4].sum(axis=1)
print(total2)
print('全班最高總分：',total2.max())


print("讀取 .csv 檔 2")
import pandas as pd
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/scores2.csv'
data = pd.read_csv(filename, header=0, index_col=0)
print('打印資料')
print(data)
#print('打印資料型態')
#print(type(data))




import csv

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/zipcode.csv'

with open(filename, 'r', encoding='utf-8') as f:
    datas = csv.reader(f)
    for data in datas:
        if data != "":
            sqlstr = "insert into zipcode (Zip5, City, Area, Road, Scope) values ('{}', '{}', '{}', '{}', '{}')".format(data[0], data[1], data[2], data[3], data[4])
            print(sqlstr)
            #cursor.execute(sqlstr)









