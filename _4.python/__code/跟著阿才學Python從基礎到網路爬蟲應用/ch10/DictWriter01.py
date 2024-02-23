import csv
f=open('dictWriterProduct.csv', 'w', newline='')
# 建立writer物件，同時指定欄位名稱
csvWriter = csv.DictWriter(f, fieldnames=['產品編號','品名','單價'])
csvWriter.writeheader()     # 寫入欄位名稱
csvWriter.writerow({'產品編號':'A02','品名':'黑松沙士','單價':90})
# 寫入兩筆產品記錄到csv檔中
csvWriter.writerow({'產品編號':'A02','品名':'草苺蛋糕','單價':120})
f.close()
