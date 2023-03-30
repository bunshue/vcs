import csv
# 開啟 csv 檔案
with open('test.csv', newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)   
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row['姓名'],row['身高'],row['體重'])