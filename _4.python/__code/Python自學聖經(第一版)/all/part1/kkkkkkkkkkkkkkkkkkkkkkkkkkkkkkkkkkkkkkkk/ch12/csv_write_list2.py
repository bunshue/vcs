import csv
# 建立csv二維串列資料
csvtable = [
        ['姓名', '身高', '體重'],
        ['Chiou', 170, 65],
        ['David', 183, 78],
]
# 開啟輸出的 csv 檔案
with open('test2.csv', 'w', newline='') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入二維串列資料
  writer.writerows(csvtable)