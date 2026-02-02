# ch2_8.py
import csv

infn = 'csvReport.csv'                              # 來源檔案
outfn = 'out2_8.csv'                                # 目的檔案
with open(infn) as csvRFile:                        # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)                # 讀檔案建立Reader物件
    listReport = list(csvReader)                    # 將資料轉成串列 

with open(outfn, 'w', newline = '') as csvOFile:    # 開啟csv檔案供寫入
    csvWriter = csv.writer(csvOFile)                # 建立Writer物件   
    for row in listReport:                          # 將串列寫入
        csvWriter.writerow(row)


