# ch2_11.py
import csv

dictList = [{'Name':'Hung', 'Age':'35', 'City':'Taipei'},       # 定義串列,元素是字典
          {'Name':'James', 'Age':'40', 'City':'Chicago'}]
          
fn = 'out2_11.csv'
with open(fn, 'w', newline = '') as csvFile:                    # 開啟csv檔案
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)     # 建立Writer物件

    dictWriter.writeheader()                                    # 寫入標題
    for row in dictList:                                        # 寫入內容
        dictWriter.writerow(row)




