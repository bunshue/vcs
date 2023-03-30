import csv
# 開啟 csv 檔案
with open('test.csv', newline='') as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row)