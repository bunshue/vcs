# ch2_7_1.py
import csv

fn = 'out2_7_1.csv'
with open(fn, 'w') as csvFile:                  # 開啟csv檔案
    csvWriter = csv.writer(csvFile)             # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


