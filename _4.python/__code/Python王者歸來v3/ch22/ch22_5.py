# ch22_5.py
import csv

fn = 'out22_5.csv'
with open(fn,'w',newline='',encoding="utf-8") as csvFile: # 開啟csv檔案
    csvWriter = csv.writer(csvFile)                     # 建立Writer物件   
    csvWriter.writerow(['姓名', '年齡', '城市'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


