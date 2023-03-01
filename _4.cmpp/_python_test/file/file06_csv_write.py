print("python寫資料到CSV檔")

import csv

#寫資料到TestCSVFileW.csv中
filename_w = "TestCSVFileW.csv"

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
finally:
#關閉文件
    csvFile.close()


