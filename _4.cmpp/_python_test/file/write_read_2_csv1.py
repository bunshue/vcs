#各種檔案寫讀範例 csv 1

#csv檔 逗號分隔值(comma-seperated values)


import csv

print("python寫資料到CSV檔 1")

filename_w = "__temp\TestCSVFileW.csv"

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
with open('data/test1.csv', newline='') as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row)


import csv
# 開啟 csv 檔案
with open('data/test1.csv', newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)   
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row['姓名'],row['身高'],row['體重'])
        
import csv
with open('__temp/test3.csv', 'w', newline='') as csvfile:
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
with open('__temp/test1.csv', 'w', newline='') as csvfile:
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
with open('__temp/test2.csv', 'w', newline='') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入二維串列資料
  writer.writerows(csvtable)
        

