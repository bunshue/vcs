# ch6_12.py
import csv

infn = 'AQI_20190814010150.csv'                     # 來源檔案
outfn = 'out6_12.csv'                               # 目的檔案
with open(infn) as csvRFile:                        # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)                # 讀檔案建立Reader物件
    listReport = list(csvReader)                    # 將資料轉成串列 

newListReport = []                                  # 空串列
tmpList = []
for row in listReport:                              # 使用迴圈取新的欄位
    tmpList = [row[1],row[23],row[11],row[0]]
    newListReport.append(tmpList)

with open(outfn, 'w', newline = '') as csvOFile:    # 開啟csv檔案供寫入
    csvWriter = csv.writer(csvOFile)                # 建立Writer物件   
    for row in newListReport:                       # 將串列寫入和列印
        csvWriter.writerow(row)                     # 寫入檔案
        if row[0] != 'County':                      # 不是標題
            print('城市名稱 =%4s  站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
                  (row[0], row[1], row[2], row[3]))
        


