import csv
# 開啟 csv 檔案
with open('school.csv', newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)   
    # 以迴圈顯示每一列
    for row in rows:
        print(row['座號'],row['姓名'],row['國文'],row['英文'],row['數學'])