import csv
f=open('writerProduct.csv','w', newline='') # 開啟writerProduct.csv檔案
csvWriter=csv.writer(f) # 建立writer物件，物件名稱為csvWriter
# 建立listProduct二維串列有兩筆產品
listProduct=[
              ['B01','小林煎餅','78'],
              ['B02','五香豆干','90']
            ]
# 寫入一維串列當做標題
csvWriter.writerow(['編號','品名','單價'])
csvWriter.writerows(listProduct) # 將二維串列的兩筆產品寫入csv內
f.close() # 關閉檔案
