import csv
# 開啟輸出的 csv 檔案
with open('test.csv', 'w', newline='') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入欄位名稱
  writer.writerow(['姓名', '身高', '體重'])
  # 寫入資料
  writer.writerow(['chiou', 170, 65])
  writer.writerow(['David', 183, 78])


import csv
with open('test.csv', 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'chiou', '身高': 17, '體重': 6})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})
