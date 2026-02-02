# ch6_13.py
import csv

infn = 'out6_12.csv'                                # 來源檔案
with open(infn) as csvRFile:                        # 開啟csv檔案供讀取
    csvReader = csv.reader(csvRFile)                # 讀檔案建立Reader物件
    listReport = list(csvReader)                    # 將資料轉成串列 

for row in listReport:                              # 使用迴圈取新的欄位
    if row[0] == '臺北市':                         
        print('站台ID =%3s  PM2.5值 =%3s  站台名稱 = %s ' %
              (row[1], row[2], row[3]))
        


