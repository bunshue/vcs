import csv
with open('test3.csv', 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['座號', '姓名', '國文', '英文', '數學']
    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'座號': 1, '姓名': '葉大雄', '國文': 65, '英文': 62, '數學': 40})
    writer.writerow({'座號': 2, '姓名': '陳靜香', '國文': 85, '英文': 90, '數學': 87})
    writer.writerow({'座號': 3, '姓名': '王聰明', '國文': 92, '英文': 90, '數學': 95})