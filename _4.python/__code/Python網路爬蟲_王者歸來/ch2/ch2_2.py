# ch2_2.py
import csv

fn = 'csvReport.csv'
with open(fn) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件csvReader
    for row in csvReader:               # 用迴圈列出csvReader物件內容
        print("Row %s = " % csvReader.line_num, row)
