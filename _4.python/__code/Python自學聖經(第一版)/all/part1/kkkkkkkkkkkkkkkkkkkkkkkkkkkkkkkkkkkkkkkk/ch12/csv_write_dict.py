import csv
with open('test3.csv', 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'Chiou', '身高': 170, '體重': 65})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})