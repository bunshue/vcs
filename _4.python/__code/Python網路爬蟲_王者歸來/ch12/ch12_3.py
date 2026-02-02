# ch12_3.py
import csv

fn = 'MI_5MINS.csv'                             # 台灣證劵交易所資料
out = 'MI_30MINS.csv'                           # 每30分鐘資料
with open(out, 'w', newline='') as csvOut:
    csvWriter = csv.writer(csvOut)
    csvWriter.writerow(["時間", "累積成交數"])
    with open(fn) as csvFile:
        csvReader = csv.reader(csvFile)
        listCsv = list(csvReader)               # 轉成串列
        csvData = listCsv[2:-8]                 # 切片刪除非成交資訊
        for row in csvData:
            xmin = row[0][3:5]                  # 分
            xsec = row[0][6:]                   # 秒
            if xmin == '00' or xmin == '30':    # 每30分鐘
                if xsec == '00':                # True時寫入時間和累積成交數
                    csvWriter.writerow([row[0], row[6]]) 

                    
            
       


