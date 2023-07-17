import csv
# 建立csv二維串列資料
csvtable = [
        ['座號', '姓名', '國文', '英文', '數學'],
        [1, '葉大雄', 65, 62, 40],
        [2, '陳靜香', 85, 90, 87],
        [3, '王聰明', 92, 90, 95]
        ]
# 寫入csv檔案
with open('test2.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(csvtable)