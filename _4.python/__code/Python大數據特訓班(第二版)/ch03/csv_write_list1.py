import csv
with open('test1.csv', 'w', newline='') as f:
    # 建立 csv 檔寫入物件
    writer = csv.writer(f)
    # 寫入欄位及資料
    writer.writerow(['座號', '姓名', '國文', '英文', '數學'])
    writer.writerow([1, '葉大雄', 65, 62, 40])
    writer.writerow([2, '陳靜香', 85, 90, 87])
    writer.writerow([3, '王聰明', 92, 90, 95])