# ch22_10.py
import csv

fn = 'out22_10.csv'
with open(fn, 'w', newline = '') as csvFile:                    # 開啟csv檔案
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)     # 建立Writer物件

    dictWriter.writeheader()                                    # 寫入標題
    dictWriter.writerow({'Name':'Hung', 'Age':'35', 'City':'Taipei'})
    dictWriter.writerow({'Name':'James', 'Age':'40', 'City':'Chicago'})




