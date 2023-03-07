#建立一個csv檔 逗號分隔值(comma-seperated values)

print("python寫資料到CSV檔")

import csv

#寫資料到TestCSVFileW.csv中
filename_w = "__temp\TestCSVFileW.csv"

print("打開一個csv檔案 : "+filename_w)
csvFile = open(filename_w, 'w+', newline='')

try:
#寫資料
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
#關閉文件
    csvFile.close()

print("寫入檔案 " + filename_w + " 完成")
